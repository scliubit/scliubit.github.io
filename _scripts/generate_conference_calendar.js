const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const root = path.resolve(__dirname, '..');
const sourcePath = path.join(root, 'conf-timeline.html');
const outputPath = path.join(root, 'conference-calendar.ics');
const html = fs.readFileSync(sourcePath, 'utf8');
const match = html.match(/const DATA = (\{[\s\S]*?\n\});/);

if (!match) {
  throw new Error('Could not find DATA in conf-timeline.html');
}

const data = vm.runInNewContext(`(${match[1]})`, Object.create(null), { timeout: 1000 });
const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d{3}Z$/, 'Z');
const deadlines = new Map();
const conferences = new Map();
let impreciseDeadlines = 0;
let impreciseConferences = 0;

function escapeText(value) {
  return String(value)
    .replace(/\\/g, '\\\\')
    .replace(/\r?\n/g, '\\n')
    .replace(/;/g, '\\;')
    .replace(/,/g, '\\,');
}

function foldLine(line) {
  const chunks = [];
  let chunk = '';
  let limit = 75;

  for (const char of line) {
    if (Buffer.byteLength(chunk + char, 'utf8') > limit) {
      chunks.push(chunk);
      chunk = char;
      limit = 74;
    } else {
      chunk += char;
    }
  }

  chunks.push(chunk);
  return chunks.join('\r\n ');
}

function utcDate(year, month, day) {
  const date = new Date(Date.UTC(year, month - 1, day));
  if (
    date.getUTCFullYear() !== year
    || date.getUTCMonth() !== month - 1
    || date.getUTCDate() !== day
  ) {
    throw new Error(`Invalid date: ${year}-${month}-${day}`);
  }
  return date;
}

function formatDate(date) {
  return date.toISOString().slice(0, 10).replace(/-/g, '');
}

function addDays(date, days) {
  return new Date(date.getTime() + days * 86400000);
}

function slug(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function eventLines({ uid, start, end, summary, description, location, url }) {
  const lines = [
    'BEGIN:VEVENT',
    `UID:${uid}`,
    `DTSTAMP:${stamp}`,
    `LAST-MODIFIED:${stamp}`,
    `DTSTART;VALUE=DATE:${formatDate(start)}`,
    `DTEND;VALUE=DATE:${formatDate(end)}`,
    `SUMMARY:${escapeText(summary)}`,
    `DESCRIPTION:${escapeText(description)}`,
  ];

  if (location && location !== 'TBD') lines.push(`LOCATION:${escapeText(location)}`);
  if (url) lines.push(`URL:${url}`);
  lines.push('TRANSP:TRANSPARENT', 'END:VEVENT');
  return lines;
}

for (const [yearValue, entries] of Object.entries(data)) {
  const year = Number(yearValue);

  for (const conference of entries) {
    if (conference.ddlDay) {
      const start = utcDate(year, conference.ddl, conference.ddlDay);
      const uid = `ddl-${formatDate(start)}-${slug(conference.name)}@scliubit.github.io`;
      deadlines.set(uid, eventLines({
        uid,
        start,
        end: addDays(start, 1),
        summary: `${conference.name} Submission Deadline`,
        description: `Submission deadline for ${conference.name}. The timeline only specifies the date; check the official website for the exact time and timezone. Source: https://scliubit.github.io/conf-timeline.html`,
        url: conference.url,
      }));
    } else {
      impreciseDeadlines += 1;
    }

    if (conference.cs && conference.ce) {
      const conferenceYear = conference.next ? year + 1 : year;
      const start = utcDate(conferenceYear, conference.cs[0], conference.cs[1]);
      const end = addDays(utcDate(conferenceYear, conference.ce[0], conference.ce[1]), 1);
      if (end <= start) throw new Error(`Invalid conference date range for ${conference.name}`);

      const uid = `conf-${formatDate(start)}-${slug(conference.name)}@scliubit.github.io`;
      if (!conferences.has(uid)) {
        conferences.set(uid, eventLines({
          uid,
          start,
          end,
          summary: conference.name,
          description: `Conference dates: ${conference.dates}. Check the official website for the latest information. Source: https://scliubit.github.io/conf-timeline.html`,
          location: conference.loc,
          url: conference.url,
        }));
      }
    } else {
      impreciseConferences += 1;
    }
  }
}

const lines = [
  'BEGIN:VCALENDAR',
  'VERSION:2.0',
  'PRODID:-//Shicong LIU//Conference Deadline Timeline//EN',
  'CALSCALE:GREGORIAN',
  'METHOD:PUBLISH',
  'NAME:Conference Deadlines & Events',
  'X-WR-CALNAME:Conference Deadlines & Events',
  'X-WR-CALDESC:Exact-day submission deadlines and conference dates from https://scliubit.github.io/conf-timeline.html',
  'REFRESH-INTERVAL;VALUE=DURATION:P1D',
  'X-PUBLISHED-TTL:P1D',
  'X-APPLE-CALENDAR-COLOR:#3498DB',
  ...[...deadlines.values()].flat(),
  ...[...conferences.values()].flat(),
  'END:VCALENDAR',
];

fs.writeFileSync(outputPath, `${lines.map(foldLine).join('\r\n')}\r\n`);
console.log(
  `Generated ${path.relative(root, outputPath)}: ${deadlines.size} deadlines, `
  + `${conferences.size} conference events. Skipped ${impreciseDeadlines} imprecise deadlines `
  + `and ${impreciseConferences} imprecise conference dates.`,
);

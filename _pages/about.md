---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style type="text/css">
    h1 {text-align: center}
	h2 {text-align: left}
</style>

<style type="text/css">
		.content-container {
	      display: flex;
	      align-items: center;
      gap: 10px; 
      flex-wrap: wrap; 
    }

    .button-container {
      position: relative;
      display: inline-block;
    }

	/* Tooltip styling */
    .tooltip {
      visibility: hidden;
      background-color: var(--global-text-color);
      color: var(--global-bg-color);
      text-align: center;
      border-radius: 5px;
      padding: 5px;
      position: absolute;
      z-index: 1;
      bottom: 125%; /* Position above the button */
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      font-size: 14px;
      opacity: 0;
      transition: opacity 0.3s;
    }

    /* Tooltip arrow */
    .tooltip::after {
      content: "";
      position: absolute;
      top: 100%; /* Position below the tooltip */
      left: 50%;
      transform: translateX(-50%);
      border-width: 5px;
      border-style: solid;
      border-color: var(--global-text-color) transparent transparent transparent;
    }

    /* Show tooltip on hover */
    .button-container:hover .tooltip {
      visibility: visible;
      opacity: 1;
    }

    .theme-select {
      background-color: var(--global-bg-color);
      color: var(--global-text-color);
      border: 1px solid var(--global-border-color);
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 1em;
      cursor: pointer;
      outline: none;
      /* height: 24px; */
    }
    .theme-select:hover {
      border-color: var(--global-link-color);
    }
    .theme-select-wrapper {
      margin-left: auto;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 6px;
      white-space: nowrap;
    }
    .theme-select-label {
      color: var(--global-text-color);
    }
    @media (max-width: 430px) {
      .theme-select-wrapper {
        width: 100%;
      }
    }
	</style>

<style>
	    html {
	      scroll-padding-top: 5rem;
	    }
	    p {
	        text-align: justify;
	        text-justify: inter-word;
	    }
	    .accent { color: var(--global-footnote-color); }
	    .muted  { color: var(--global-text-color-light); }
	    .research-grid {
	      display: flex;
	      flex-direction: column;
	      gap: 0;
	      margin: 1.5rem 0 4rem;
	    }
	    #news {
	      padding-top: 5rem;
	      margin-top: -5rem;
	      scroll-margin-top: 5rem;
	    }
	    #research,
	    #publications,
	    #stats {
	      padding-top: 7rem;
	      margin-top: -4rem;
	      scroll-margin-top: 6rem;
	    }
	    .page__content a.research-card,
	    .page__content a.research-card:hover {
	      text-decoration: none;
	    }
	    .research-card {
	      display: grid;
	      grid-template-columns: 204px minmax(0, 1fr);
	      gap: 18px;
	      align-items: start;
	      min-height: 0;
	      padding: 16px 0;
	      border: 0;
	      border-top: 1px solid var(--global-border-color);
	      border-radius: 0;
	      background: transparent;
	      color: var(--global-text-color);
	      text-decoration: none;
	      box-shadow: none;
	    }
	    .research-card:first-child {
	      padding-top: 2px;
	      border-top: 0;
	    }
	    .research-card:hover {
	      transform: none;
	      box-shadow: none;
	    }
	    .research-card__image {
	      display: block;
	      width: 204px;
	      height: 142px;
	      min-height: 0;
	      object-fit: contain;
	      box-sizing: border-box;
	      padding: 6px;
	      border: 1px solid var(--global-border-color);
	      border-radius: 6px;
	      background: var(--global-code-background-color);
	      transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
	    }
	    .research-card:hover .research-card__image {
	      transform: translateY(-2px);
	      border-color: var(--global-link-color);
	      box-shadow: 0 16px 40px rgba(41, 52, 61, 0.08);
	    }
	    .research-card__body {
	      display: flex;
	      flex-direction: column;
	      justify-content: flex-start;
	      min-width: 0;
	      padding: 0;
	    }
	    .research-card__title {
	      margin: 0 0 0.3rem;
	      color: var(--global-text-color);
	      font-size: 1rem;
	      font-weight: 600;
	      line-height: 1.42;
	      transition: color 0.15s ease;
	    }
	    .research-card:hover .research-card__title {
	      color: var(--global-link-color);
	    }
	    .research-card__summary {
	      margin: 0;
	      color: var(--global-text-color-light);
	      font-size: 0.86rem;
	      line-height: 1.5;
	      text-align: left;
	    }
	    .research-card__tags {
	      display: flex;
	      flex-wrap: wrap;
	      gap: 6px;
	      margin-top: 0.7rem;
	    }
	    .research-card__tags span {
	      border: 1px solid var(--global-border-color);
	      border-radius: 4px;
	      padding: 2px 8px;
	      background: var(--global-code-background-color);
	      color: var(--global-text-color-light);
	      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
	      font-size: 0.68rem;
	      line-height: 1.45;
	    }
	    @media (max-width: 700px) {
	      .research-card {
	        grid-template-columns: 1fr;
	        gap: 10px;
	        padding: 17px 0;
	      }
	      .research-card__image {
	        width: 100%;
	        height: auto;
	        min-height: 0;
	        aspect-ratio: 16 / 9;
	      }
	      .research-card__body {
	        justify-content: flex-start;
	      }
	    }

	    .news-section ul {
	      list-style: none;
      padding-left: 5.5em;
      margin-left: 0;
    }
    .news-section li {
      text-indent: -5.05em;
      margin-bottom: 0.4em;
    }
    .news-section li > b:first-child {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 0.9em;
      margin-right: 0.4em;
    }
    ol.publications {
      list-style: none;
      padding-left: 0;
    }
    ol.publications p {
      padding-left: 2.5em;
      text-indent: -2.2em;
    }
    .publications-number {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 0.9em;
      margin-right: 0.3em;
    }

	</style>

<script>
function refreshPage() {
      location.reload();
    }
</script>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<div class="content-container" style="font-size:0.8em;">
<!-- <img src="https://img.shields.io/github/actions/workflow/status/scliubit/scliubit.github.io/google_citation.yml?branch=main&logo=github" height="50px"> -->
<img src="https://img.shields.io/github/last-commit/scliubit/scliubit.github.io?logo=github" height="50px">
<div class="button-container" style="position: relative;">
      <button class="refresh-btn" onclick="refreshPage()">Refresh</button>
      <div class="tooltip">Refresh for Updates</div>
</div>
	<div class="theme-select-wrapper">
		<span class="theme-select-label">Color Theme:</span>
	    <select id="theme-selector" class="theme-select">
	      <option value="default">Default</option>
		  <option value="sunrise">Sunrise</option>
		  <option value="solarized">Solarized</option>
		  <option value="one-dark-pro">One Dark Pro</option>
		  <option value="tidal">Tidal (CVD: R/G)</option>
	    </select>
	  </div>
</div>
<br>

Hello :-)

I received my B.S. and M.S. degree in Electrical Engineering from Beijing Institute of Technology, Beijing, China, in 2020 and 2023, respectively, under the supervision of <a href="https://gaozhen16.github.io" target="_blank">Prof. Zhen GAO</a>. I am currently a Ph.D. candidate at the City University of Hong Kong, Hong Kong SAR, under the supervision of <a href="https://www.ee.cityu.edu.hk/~alexyu/" target="_blank">Prof. Xianghao YU</a>. My research interest includes signal processing and wireless communication. I have published some papers at IEEE ComSoc/SPS/VTS conferences and journals with total google scholar citations ~900.

<b><a href="/files/CV_Shicong.pdf"><span class="accent">Download Full CV</span></a></b>

# News

<div class="news-section">
<ul>
<li><b><span class="accent">[2026.06]</span></b> Released a <b>Conference Deadline Timeline</b> tracking Communications &amp; Signal Processing deadlines. Check it out <a href="./conf-timeline.html">here</a>.</li>
<li><b><span class="accent">[2026.06]</span></b> New article on <b>bending beam (caustic beamforming)</b> for next-generation wireless systems available on <a href="https://arxiv.org/abs/2606.12321">arXiv</a>.</li>
<li><b><span class="accent">[2026.05]</span></b> Manuscript on near-field <b>secure communication</b> via <b>bending beams</b> accepted by IEEE WCL, available on <a href="https://arxiv.org/abs/2603.24077">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11505880">IEEE</a>.</li>
<li><b><span class="accent">[2026.04]</span></b> Awarded Student Travel Grant for ICC 2026. Will chair oral Symposium sessions </li>
<li><b><span class="accent">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></b> <b>WC-11 (Near-Field, ELAA & Holographic MIMO)</b> and</li>
<li><b><span class="accent">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></b> <b>CQRM-13 (Wireless Networks II)</b>.</li>
<li><b><span class="accent">[2026.04]</span></b> Manuscript on <b>near-field optimal movable antenna placement</b> (discrete) accepted by IEEE TWC, available on <a href="https://arxiv.org/abs/2512.21660">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11501185">IEEE</a>. Toy demo available <a href="./demo.html">here</a>.</li>
<li><b><span class="accent">[2026.03]</span></b> Manuscript on <b>near-field optimal movable antenna placement</b> (continuous) accepted by IEEE TWC, available on <a href="https://arxiv.org/abs/2508.01201">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11466358">IEEE</a>.</li>
<li><b><span class="accent">[2026.03]</span></b> Awarded Outstanding Master's Thesis of 2025 by the Chinese Institute of Electronics (CIE).</li>
<li><b><span class="accent">[2026.02]</span></b> Nominated as 2025 <a href="https://www.comsoc.org/publications/journals/ieee-wcl/reviewer-appreciation" target="_blank">Exemplary Reviewer</a> of <span style="font-variant-caps: small-caps;">IEEE Wireless Communications Letters</span></li>
<!-- <li><b><span class="accent">[2026.01]</span></b> New paper submitted to IEEE WCL, available on <a href="https://arxiv.org/abs/2603.24077">arXiv</a>.</li> -->
<li><b><span class="accent">[2026.01]</span></b> Two conference papers accepted by ICASSP'26 and ICC'26. Available online: <a href="https://ieeexplore.ieee.org/document/11463842">ICASSP'26</a>, <a href="/files/icc26.pdf">ICC'26</a>.</li>
<!-- <li><b><span class="accent">[2025.12]</span></b> New paper submitted to IEEE TWC, available on <a href="https://arxiv.org/abs/2512.21660">arXiv</a>. Toy demo available <a href="./demo.html">here</a>.</li> -->
<!-- <li><b><span class="accent">[2025.12]</span></b> Comments and discussions for TWC'25 are released. See <a href="/posts/TWC25COMMENTS/">here</a> for more info.</li> -->
<li><b><span class="accent">[2025.10]</span></b> New paper submitted to IEEE ICC. Journal Version available on <a href="https://arxiv.org/abs/2512.21660">arXiv</a>.</li>

</ul>

<details><summary>More News</summary>
<ul>
<li><b><span class="accent">[2026.02]</span></b> Themes and Dark Modes (beta) are now available! Select the theme you like from the dropdown menu above, or click the top-right button to toggle between light and dark modes.</li>
<li><b><span class="muted">[2025.05]</span></b> An errata for JSAC'25 was released. See <a href="/posts/JSAC25ERRATA/">here</a> for more info.</li>
<li><b><span class="accent">[2024.12]</span></b> Nominated as 2024 <a href="https://www.comsoc.org/publications/journals/ieee-comml/reviewer-and-editor-appreciation" target="_blank">Exemplary Reviewer</a> of <span style="font-variant-caps: small-caps;">IEEE Communications Letters</span></li>
<li><b><span class="accent">[2024.11]</span></b> One coauthored <a href="https://www.nature.com/articles/s41467-024-54168-3" target="_blank">article</a> was accepted by <b>Nature Communications</b></li>
<li><b><span class="muted">[2024.11]</span></b> Albums and Posts now support multiple languages :-P</li>
<li><b><span class="accent">[2024.11]</span></b> One <a href="https://arxiv.org/abs/2403.11809" target="_blank">journal paper</a> was accepted by IEEE JSAC</li>
<li><b><span class="accent">[2024.08]</span></b> I was awarded the CityU Academic Excellence and QE Award</li>
<li><b><span class="accent">[2024.07]</span></b> One <a href="https://arxiv.org/abs/2405.01000" target="_blank">conference paper</a> was accepted by IEEE Globecom'24</li>
<li><b><span class="accent">[2023.10]</span></b> One <a href="https://arxiv.org/abs/2310.18180" target="_blank">conference paper</a> was accepted by IEEE ICC'24</li>
</ul>
</details>
</div>


# Research
<br>
<div class="research-grid">
  <a class="research-card" href="/posts/WCL26COMMENTS/">
    <img class="research-card__image" src="/images/in-post/caustic26/beamvis.png" alt="Bending Beam Visualization">
    <div class="research-card__body">
      <h2 class="research-card__title">Bending Beams For Secure Links</h2>
      <p class="research-card__summary">Caustic beamforming shapes bending beams that follow curved trajectories, creating controllable non-line-of-sight secure regions and suppressing unintended receivers in the near field.</p>
      <div class="research-card__tags"><span>Near-Field</span><span>Security</span><span>Caustics</span><span>Beamforming</span></div>
    </div>
  </a>

  <a class="research-card" href="/posts/ICC_TWC26/">
    <img class="research-card__image" src="/images/in-post/icc26/sysmod.png" alt="Movable Antenna System Model">
    <div class="research-card__body">
      <h2 class="research-card__title">Movable Antenna Placement</h2>
      <p class="research-card__summary">Movable antennas are placed through electrostatic-equilibrium-inspired updates, turning discrete near-field placement into a structured optimization problem with low-complexity geometry.</p>
      <div class="research-card__tags"><span>Movable Antenna</span><span>Optimization</span><span>Near-Field</span><span>Geometry</span></div>
    </div>
  </a>

  <a class="research-card" href="/posts/TWC25COMMENTS/">
    <img class="research-card__image" src="/images/in-post/twc25/fig2.png" alt="Optimal Antenna Density Illustration">
    <div class="research-card__body">
      <h2 class="research-card__title">Optimal Antenna Density</h2>
      <p class="research-card__summary">Continuous antenna density design is treated as a functional optimization problem, revealing how aperture resources should concentrate across massive movable antenna systems.</p>
      <div class="research-card__tags"><span>Functional Analysis</span><span>Density Design</span><span>Aperture</span><span>MIMO</span></div>
    </div>
  </a>

  <a class="research-card" href="/posts/ICC24/">
    <img class="research-card__image" src="/images/in-post/dpss/alg.png" alt="DPSS Channel Estimation Algorithm">
    <div class="research-card__body">
      <h2 class="research-card__title">Near-Field Channel Estimation</h2>
      <p class="research-card__summary">Discrete prolate spheroidal sequences provide compact sparse dictionaries for near-field channels, reducing training overhead while preserving the dominant spatial structure.</p>
      <div class="research-card__tags"><span>DPSS</span><span>Channel Estimation</span><span>Sparse Dictionary</span><span>Near-Field</span></div>
    </div>
  </a>
</div>


# Publications

Selected publications. <a href="/publications/">More Details</a>

## Journals

<ol class="publications">
{% assign sorted_pubs = site.publications | where: "type", "Journal" | sort: 'date' | reverse %}
{% for pub in sorted_pubs %}
	{% if pub.type == "Journal" %}
	<p>
	<span class="publications-number">[{{ sorted_pubs.size | minus: forloop.index | plus: 1  }}]</span>
	{% assign authors = pub.authors | split: ", " %}
	{% for author in authors %}
		{% if author == "S. Liu" %}
			<strong>{{ author }}</strong>{% if forloop.last == false %}, {% endif %}
		{% elsif author == "X. Yu" %}
			<i>{{ author }}*</i>{% if forloop.last == false %}, {% endif %}
		{% else %}
		  	{{ author }}{% if forloop.last == false %}, {% endif %}
		{% endif %}
	{% endfor %}
	, "{{ pub.title }}", <i>{{ pub.venue }}</i>, 
	{% if pub.vol %}
		vol. {{ pub.vol }},
	{% endif %}
	{% if pub.issue %}
		no. {{ pub.issue }},
	{% endif %}
	{% if pub.pp %}
		pp. {{ pub.pp }},
	{% endif %}
	{{ pub.date | date: "%b. %Y" }}{% if pub.notes %}, <b><span class="accent">{{ pub.notes }}</span></b>{% endif %}.
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.errata %}
		[<a href="{{ pub.errata }}" target="_blank">Erratum</a>]
	{% endif %}
	{% if pub.demo %}
		[<a href="{{ pub.demo }}" target="_blank"><span class="accent">Demo</span></a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank"><span class="accent">Codes</span></a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.DOI %}
		<a href="https://doi.org/{{ pub.DOI }}" target="_blank"><img src="https://zenodo.org/badge/DOI/{{ pub.DOI }}.svg" height="60px"></a>
		<img src="https://api.juleskreuer.eu/citation-badge.php?doi={{ pub.DOI }}" height="60px">
	{% endif %}
	<br>
  	</p>
	{% endif %}
{% endfor %}
</ol>

## Articles


<ol class="publications">
{% assign sorted_pubs = site.publications | where: "type", 'Article' | sort: 'date' | reverse %}
{% for pub in sorted_pubs %}
	{% if pub.type == "Article" %}
	<p>
	<span class="publications-number">[{{ sorted_pubs.size | minus: forloop.index | plus: 1  }}]</span>
	{% assign authors = pub.authors | split: ", " %}
	{% for author in authors %}
		{% if author == "S. Liu" %}
			<strong>{{ author }}</strong>{% if forloop.last == false %}, {% endif %}
		{% elsif author == "X. Yu" %}
			<i>{{ author }}*</i>{% if forloop.last == false %}, {% endif %}
		{% else %}
		  	{{ author }}{% if forloop.last == false %}, {% endif %}
		{% endif %}
	{% endfor %}
	, "{{ pub.title }}", <i>{{ pub.venue }}</i>, 
	{% if pub.vol %}
		vol. {{ pub.vol }},
	{% endif %}
	{% if pub.issue %}
		no. {{ pub.issue }},
	{% endif %}
	{% if pub.pp %}
		pp. {{ pub.pp }},
	{% endif %}
	{{ pub.date | date: "%b. %Y" }}{% if pub.notes %}, <b><span class="accent">{{ pub.notes }}</span></b>{% endif %}.
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.errata %}
		[<a href="{{ pub.errata }}" target="_blank">Erratum</a>]
	{% endif %}
	{% if pub.demo %}
		[<a href="{{ pub.demo }}" target="_blank"><span class="accent">Demo</span></a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank"><span class="accent">Codes</span></a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.DOI %}
		<a href="https://doi.org/{{ pub.DOI }}" target="_blank"><img src="https://zenodo.org/badge/DOI/{{ pub.DOI }}.svg" height="60px"></a>
		<img src="https://api.juleskreuer.eu/citation-badge.php?doi={{ pub.DOI }}" height="60px">
	{% endif %}
	<br>
  	</p>
	{% endif %}
{% endfor %}
</ol>

## Conferences

<ol class="publications">
{% assign sorted_pubs = site.publications | where: "type", "Conference" | sort: 'date' | reverse %}
{% for pub in sorted_pubs %}
	{% if pub.type == "Conference" %}
	<p>
    <span class="publications-number">[{{ sorted_pubs.size | minus: forloop.index | plus: 1  }}]</span>
    {% assign authors = pub.authors | split: ", " %}
    {% for author in authors %}
        {% if author == "S. Liu" %}
        	<strong>{{ author }}</strong>{% if forloop.last == false %}, {% endif %}
		{% elsif author == "X. Yu" %}
			<i>{{ author }}*</i>{% if forloop.last == false %}, {% endif %}
        {% else %}
          	{{ author }}{% if forloop.last == false %}, {% endif %}
        {% endif %}
    {% endfor %}
    , "{{ pub.title }}",
		in <i>{{ pub.venue }}</i>, {{ pub.location }}, {{ pub.date | date: "%b. %Y" }}{% if pub.notes %}, <b><span class="accent">{{ pub.notes }}</span></b>{% endif %}.
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.errata %}
		[<a href="{{ pub.errata }}" target="_blank">Erratum</a>]
	{% endif %}
	{% if pub.demo %}
		[<a href="{{ pub.demo }}" target="_blank"><span class="accent">Demo</span></a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank"><span class="accent">Codes</span></a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.DOI %}
		<a href="https://doi.org/{{ pub.DOI }}" target="_blank"><img src="https://zenodo.org/badge/DOI/{{ pub.DOI }}.svg" height="60px"></a>
		<img src="https://api.juleskreuer.eu/citation-badge.php?doi={{ pub.DOI }}" height="60px">
	{% endif %}
	<br>
  	</p>
	{% endif %}
{% endfor %}
</ol>



# Stats
<br>
<!-- <hr> -->
<style>
    .center {
        text-align: center;
		width: 300px;
		margin: 0 auto;
    }
    hr {
        width: 200px; /* Adjust width as needed */
        margin: 0 auto; /* Center the hr */
    }
</style>

<div class='center'>
<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=300&t=tt&d=dmVatQT8g0590arpll0thgjnbjngqp0QqLSiLkH5KuU'></script>
</div>

<div class='center'>
<a href="https://info.flagcounter.com/4GAt"><img src="https://s01.flagcounter.com/count2/4GAt/bg_FFFFFF/txt_000000/border_CCCCCC/columns_4/maxflags_8/viewers_Countries+and+Regions/labels_0/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
</div>

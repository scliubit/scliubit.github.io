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
	.someClass {
		display: flex;
		justify-content: space-between;
	}
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}



<img src="https://img.shields.io/github/actions/workflow/status/scliubit/scliubit.github.io/google_citation.yml?branch=main&logo=github" height="50px">
<img src="https://img.shields.io/github/last-commit/scliubit/scliubit.github.io?logo=github" height="50px">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fscliubit.github.io&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=false" height="50px"/>
<br>

Hello :-)

I am a Ph.D. candidate at City University of Hong Kong currently in Hong Kong SAR. My research interest includes signal processing and system design in wireless communication. I have published some papers at IEEE ComSoc conferences and journals with total google scholar citations ~500.

<b><a href="/files/CV_Shicong.pdf" ><font color="#FF0000">Download Full CV</font></a></b>

# News

- <b><font color="#000000">[2024.11]</font></b> Albums and Posts now support multiple languages :-P
- <b><font color="#FF0000">[2024.11]</font></b> One coauthored <a href="https://www.nature.com/articles/s41467-024-54168-3" target="_blank">article</a> was accepted by <b>Nature Communications</b>
- <b><font color="#FF0000">[2024.11]</font></b> One <a href="https://arxiv.org/abs/2403.11809" target="_blank">journal paper</a> was accepted by IEEE JSAC
- <b><font color="#FF0000">[2024.08]</font></b> I was awarded the CityU Academic Excellence and QE Award
- <b><font color="#FF0000">[2024.07]</font></b> One <a href="https://arxiv.org/abs/2405.01000" target="_blank">conference paper</a> was accepted by IEEE Globecom'24

<details><summary>More News</summary>
<ul>
<li><b>[2023.10]</b> One <a href="https://arxiv.org/abs/2310.18180" target="_blank">conference paper</a> was accepted by IEEE ICC'23</li>
</ul>
</details>


# Education

- <div class="someClass"><div>Ph.D. in Electronic Engineering, City University of Hong Kong</div><div>2023-2027(est.)</div></div>
- <div class="someClass"><div>M.S. in Electronic Engineering, Beijing Institute of Technology</div><div>2020-2023</div></div>
- <div class="someClass"><div>B.S. in Electrical Engineering, Beijing Institute of Technology</div><div>2016-2020</div></div>


# Publications

Selected publications. <a href="/publications/">More Details</a>

## Journals

<ol class="publications">
{% assign sorted_pubs = site.publications | where: "type", "Journal" | sort: 'date' | reverse %}
{% for pub in sorted_pubs %}
	{% if pub.type == "Journal" %}
	<p style="text-indent: -1.5rem;margin-left: 0rem;">
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
	, "{{ pub.title }}", <i>{{ pub.venue }}</i>, vol. {{ pub.vol }}, no. {{ pub.issue }}, pp. {{ pub.pp }}, {{ pub.date | date: "%b. %Y" }}.
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank">Codes</a>]
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
	<p style="text-indent: -1.5rem;margin-left: 0rem;">
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
	, "{{ pub.title }}", <i>{{ pub.venue }}</i>, vol. {{ pub.vol }}, no. {{ pub.issue }}, pp. {{ pub.pp }}, {{ pub.date | date: "%b. %Y" }}.
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank">Codes</a>]
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
	<p style="text-indent: -1.5rem;margin-left: 0rem;">
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
	{% if pub.type == "Conference" %}
		in <i>{{ pub.venue }}</i>, {{ pub.location }}, {{ pub.date | date: "%b. %Y" }}.
	{% endif %}
	{% if pub.arxiv %}
		[<a href="{{ pub.arxiv }}" target="_blank">arXiv</a>]
	{% endif %}
	{% if pub.slidesurl %}
		[<a href="{{ pub.slidesurl }}" target="_blank">Slides</a>]
	{% endif %}
	{% if pub.paperurl %}
		[<a href="{{ pub.paperurl }}" target="_blank">Paper</a>]
	{% endif %}
	{% if pub.codes %}
		[<a href="{{ pub.codes }}" target="_blank">Codes</a>]
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

# Services


## Academics

- **Session Chair**, <i>Antenna and Smart Antenna</i>, IEEE Globecom'23, Cape Town, South Africa.
- **Session Chair**, <i>Mobile and Wireless Networks</i>, IEEE/CIC ICCC'23, Dalian, China.
- **Peer Reviewer**, IEEE ComSoc Journals and Conferences.

## Teaching

- **Teaching Assistant**
	- <div class="someClass"><div>EE3008: Principles of Communications, City University of Hong Kong</div><div>2024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fall</div></div>
	- <div class="someClass"><div>EE3008: Principles of Communications, City University of Hong Kong</div><div>2024 Spring</div></div>
	- <div class="someClass"><div>EE3008: Principles of Communications, City University of Hong Kong</div><div>2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fall</div></div>
	- <div class="someClass"><div>Innovation and Entrepreneurship, Beijing Institute of Technology</div><div>2023 Spring</div></div>
	- <div class="someClass"><div>Frontiers of Communication Technology, Beijing Institute of Technology</div><div>2022 Spring</div></div>

# Awards and Honors

- <div class="someClass"><div>1st place in National Undergraduate Algorithmic Game Theory Championship</div><div>2018</div></div>
- <div class="someClass"><div>Meritorious Winner (~7%) in Mathematical Contest in Modeling (MCM)</div><div>2019</div></div>
- <div class=someClass><div>2020 National Scholarship (~2.5%) for Graduate Students</div><div>2020</div></div>
- <div class=someClass><div>2021 National Scholarship (~2.5%) for Graduate Students</div><div>2021</div></div>
- <div class=someClass><div>2021 Outstanding Student</div><div>2021</div></div>
- <div class=someClass><div>Hong Kong Ph.D. Fellowship Scheme (HKPFS) Awardee</div><div>2023</div></div>
- <div class=someClass><div>Beijing Municipal Outstanding Master Graduate</div><div>2023</div></div>
- <div class=someClass><div>Entrance Fellowship of CityU Graduate School</div><div>2023</div></div>
- <div class=someClass><div>CityU Academic Excellence and QE Award</div><div>2024</div></div>



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
<!-- <div class='center'>
<h5>STAT</h5>
<script type="text/javascript"
    src="//rf.revolvermaps.com/0/0/8.js?i=5sp8fsqa9x1&amp;m=7&amp;c=ff0000&amp;cr1=ffffff&amp;f=georgia&amp;l=33&amp;s=200"
    async="async">
</script> -->
<!-- </div> -->
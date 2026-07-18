---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="home-page" markdown="1">

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<div class="home-top-bar">
  <img src="https://img.shields.io/github/last-commit/scliubit/scliubit.github.io?logo=github&label=last%20update" height="20px">
  <!--
  <div class="button-container" style="position: relative;">
    <button class="refresh-btn" onclick="refreshPage()">Refresh</button>
    <div class="tooltip">Refresh for Updates</div>
  </div>
  -->
  <div class="theme-select-wrapper">
    <span class="theme-select-label">Color Theme:</span>
    <select id="theme-selector" class="theme-select" aria-label="Color theme">
	  <option value="claude">Claude</option>
      <option value="sunrise">Sunrise</option>
      <option value="one-dark-pro">One Dark Pro</option>
      <option value="tidal">Tidal (CVD: R/G)</option>
	  <option value="default">Default</option>
    </select>
  </div>
</div>

<br>

Hello :-)

I am a Ph.D. candidate at the City University of Hong Kong, supervised by <a href="https://www.ee.cityu.edu.hk/~alexyu/" target="_blank">Prof. Xianghao YU</a>. I received my B.S. and M.S. degrees in Electrical Engineering from Beijing Institute of Technology, supervised by <a href="https://gaozhen16.github.io" target="_blank">Prof. Zhen GAO</a>. My research lies at the intersection of signal processing and wireless communications, with a recent focus on <b>near-field communications</b>, <b>movable antenna systems</b>, and <b>bending caustic beams</b>. I have published some papers at IEEE ComSoc/SPS/VTS conferences and journals with total google scholar citations ~900, and have been nominated as an Exemplary Reviewer by <i>IEEE Commun. Lett.</i> and <i>IEEE Wireless Commun. Lett.</i>

<!-- I received my B.S. and M.S. degree in Electrical Engineering from Beijing Institute of Technology, Beijing, China, in 2020 and 2023, respectively, under the supervision of <a href="https://gaozhen16.github.io" target="_blank">Prof. Zhen GAO</a>. I am currently a Ph.D. candidate at the City University of Hong Kong, Hong Kong SAR, under the supervision of <a href="https://www.ee.cityu.edu.hk/~alexyu/" target="_blank">Prof. Xianghao YU</a>. My research interest includes signal processing and wireless communication. I have published some papers at IEEE ComSoc/SPS/VTS conferences and journals with total google scholar citations ~900. -->

<b><a href="/files/CV_Shicong.pdf"><span class="accent"><i class="fa-solid fa-file-pdf" aria-hidden="true"></i> Download Full CV</span></a></b>

# News

<div class="news-section">
<ul>
<li><b><span class="accent">[2026.06]</span></b> Released a <b>Conference Deadline Timeline</b> tracking Communications & Signal Processing deadlines. Check it out <a href="./conf-timeline.html">here</a>.</li>
<li><b><span class="accent">[2026.06]</span></b> New article on <b>bending beam (caustic beamforming)</b> for next-generation wireless systems available on <a href="https://arxiv.org/abs/2606.12321">arXiv</a>.</li>
<li><b><span class="accent">[2026.05]</span></b> Manuscript on near-field <b>secure communication</b> via <b>bending beams</b> accepted by IEEE WCL, available on <a href="https://arxiv.org/abs/2603.24077">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11505880">IEEE</a>.</li>
<li><b><span class="accent">[2026.04]</span></b> Awarded Student Travel Grant for ICC 2026. Will chair oral Symposium sessions </li>
<li><b><span class="accent">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></b> <b>WC-11 (Near-Field, ELAA & Holographic MIMO)</b> and</li>
<li><b><span class="accent">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></b> <b>CQRM-13 (Wireless Networks II)</b>.</li>
<li><b><span class="accent">[2026.04]</span></b> Manuscript on <b>near-field optimal movable antenna placement</b> (discrete) accepted by IEEE TWC, available on <a href="https://arxiv.org/abs/2512.21660">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11501185">IEEE</a>. Toy demo available <a href="./demo.html">here</a>.</li>
<li><b><span class="accent">[2026.03]</span></b> Manuscript on <b>near-field optimal movable antenna placement</b> (continuous) accepted by IEEE TWC, available on <a href="https://arxiv.org/abs/2508.01201">arXiv</a> and <a href="https://ieeexplore.ieee.org/document/11466358">IEEE</a>.</li>
<li><b><span class="accent">[2026.03]</span></b> Awarded Outstanding Master's Thesis of 2025 by the Chinese Institute of Electronics (CIE).</li>
<li><b><span class="accent">[2026.02]</span></b> Nominated as 2025 <a href="https://www.comsoc.org/publications/journals/ieee-wcl/reviewer-appreciation" target="_blank">Exemplary Reviewer</a> of <span style="font-variant-caps: small-caps;">IEEE Wireless Communications Letters</span></li>
<li><b><span class="accent">[2026.01]</span></b> Two conference papers accepted by ICASSP'26 and ICC'26. Available online: <a href="https://ieeexplore.ieee.org/document/11463842">ICASSP'26</a>, <a href="/files/icc26.pdf">ICC'26</a>.</li>
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

<div class="research-grid">
{% assign researches = site.researches | sort: 'order' %}
{% for r in researches %}
  <a class="research-card" href="{{ r.link }}">
    <img class="research-card__image" src="{{ r.image }}" alt="{{ r.image_alt | default: r.title | escape }}">
    <div class="research-card__body">
      <h2 class="research-card__title">{{ r.title }}</h2>
      <p class="research-card__summary">{{ r.summary }}</p>
      <div class="research-card__tags">
        {% for tag in r.tags %}
        <span>{{ tag }}</span>
        {% endfor %}
      </div>
    </div>
  </a>
{% endfor %}
</div>

<div class="center">
<p class="research-more" style="margin-top: 1cm;">
<a href="/year-archive/"><span class="accent">Find Out More →</span></a>
</p>
</div>

# Publications

Selected publications. <a href="/publications/">More Details</a>

## Journals

{% include publication-list.html type="Journal" %}

## Articles

{% include publication-list.html type="Article" %}

## Conferences

{% include publication-list.html type="Conference" %}



# Stats
<br>
<div class="center">
<!-- Clustermaps widget disabled; kept for reference.
<script type="text/javascript" id="clustrmaps" src="//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=300&t=tt&d=dmVatQT8g0590arpll0thgjnbjngqp0QqLSiLkH5KuU"></script>
-->
</div>

<div class="center">
<a href="https://info.flagcounter.com/4GAt"><img src="https://s01.flagcounter.com/count2/4GAt/bg_FFFFFF/txt_000000/border_CCCCCC/columns_5/maxflags_5/viewers_Countries+and+Regions/labels_0/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
</div>

</div>

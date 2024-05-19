---
layout:     post
title:      "🌍 增加双语支持 | Bilingual Support"
subtitle:   "Finally..."
date:       2024-05-21 12:00:00
author:     "Shicong Liu"
header-img: "img/home-dark.jpg"
catalog: true
mathjax: true
comment: true
multilingual: true
tags:
    - test
---

很久前就该做的事情直到今天才终于想起来......无论如何，坑总算是填上了。

`The task that should have been done a long time ago was only remembered today... anyway, the pit is finally filled.`

这里就用早期的ICC'24统计信息的post来做第一期双语支持的测试了

`The first test of bilingual support falls on the ICC'24 statistic post on Mar. 16`

---

<!-- Chinese Version -->
<div class="zh post-container">
    {% capture about_zh %}{% include_relative bilin/zh/test1.md %}{% endcapture %}
    {{ about_zh | markdownify }}
</div>

<!-- English Version -->
<div class="en post-container">
    {% capture about_en %}{% include_relative bilin/en/test1.md %}{% endcapture %}
    {{ about_en | markdownify }}
</div>
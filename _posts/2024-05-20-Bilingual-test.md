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

⬆️ Please push the button to select your language. Chinese by default.

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
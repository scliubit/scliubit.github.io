---
layout:     post
title:      "🪪 香港身份证预约指南"
subtitle:   "👩‍💼 什么？我自己还没约到"
date:       2023-08-26 23:59:00
author:     "Shicong Liu"
header-img: "img/home-dark.jpg"
catalog: true
mathjax: true
comment: true
hide-in-nav: true
tags:
    - 学习
    - feed
---



自从香港政府允许持有HKID的人自助通关后，许多没有办理香港身份证的人也逐渐开始预约办理。目前时间八月，[官网](https://www.gov.hk/tc/residents/immigration/idcard/hkic/bookregidcard.htm)的预约却早已经排到了十二月。目前网络上充斥着语焉不详的预约经验，这里我们用实际数据来测试一下身份证预约配额的情况。

官方给了一个快速查询平台，每15分钟更新一次，该网站的返回信息结构为`json`，典型示例为

```json
{'date': '08/25/2023', 'quotaR': 'quota-r', 'officeId': 'RHK', 'quotaK': 'quota-y'}
{'date': '08/25/2023', 'quotaR': 'quota-r', 'officeId': 'RKT', 'quotaK': 'quota-y'}
{'date': '08/25/2023', 'quotaR': 'quota-r', 'officeId': 'TMO', 'quotaK': 'quota-y'}
{'date': '08/26/2023', 'quotaR': 'quota-r', 'officeId': 'RHK', 'quotaK': 'quota-y'}
{'date': '08/26/2023', 'quotaR': 'quota-r', 'officeId': 'RKO', 'quotaK': 'quota-y'}
```

其中`quotaR`表示一般配额，`quotaK`表示延长时间配额。这些配额的flag有四种取值，分别为

- `quota-r`：无配额
- `quota-y`：少量配额
- `quota-g`：大量配额
- `quota-non`：（延期配额）不可用

根据上述信息，我们为`quota-g`配置的参考数值为`20`，为`quota-y`配置的参考数值为`1`，可以根据轮询结果绘制配额曲线。感谢作者[@josephwww](https://github.com/josephwww)提供的[查询代码](https://github.com/josephwww/HongKongIdReservationCheck/blob/main/hkid.py)，此处进行少许改动后接入云服务器轮询。五天内的参考结果如下

<div>
<img src="/img/quota/quota.svg" alt="QUOTA" style="zoom:45%;"/>
</div>

那么答案就是，每天下午两点、五点以及晚上十点准时在网页中排队开抢！

---

\*\*\*\*\*\*\*\*UPDATE\*\*\*\*\*\*\*\*

经过若干次的尝试，HKID的机制已经基本探明。不过现在HKID的办理需求已经很低了，因此预约难度并不高，在此话题更新则颇有马后炮的意味（）。具体而言，在图示时间段内的第$12$分钟，网站会集中释放一批名额，已经预约的人则可以通过修改预约的方式逐步将预约时间提前。

# 扩展阅读

~~今天没有扩展阅读了~~


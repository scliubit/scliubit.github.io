---
layout:     post
title:      "无线通信领域审稿与回复套话一览<br>Review and Rebuttal Cliches"
subtitle:   "如果你懒得审稿，抄这里会让你看起来不像AI"
date:       2026-01-01
author:     "Shicong Liu"
permalink:  /posts/REVIEWNREBUTTAL/
excerpt:    "贺岁巨制，震撼首发！<br>Shocking Release for the New Year!"
catalog: true
mathjax: true
comment: true
multilingual: true
hide-in-nav: true
tags:
    - research
    - publication
    - comments
    - feed
---

本文总结常见无线通信领域审稿意见与回复套话，均为本人所见的整理，旨在为入门科研工作者提供便利，为资深科研工作者节省时间。如有雷同，纯属巧合。

# 通用型

<mark>创新性不足 (Lack of novelty; Limited Contribution; Incremental Improvement)</mark>

必备性：★★★★★

攻击性：★★☆☆☆

总的来说，这是一句几乎不会踩雷的审稿套话。现在全球科研处于全面没活的状态，所有领域都在做“屎上雕花”，创新性不足确实是大量科研工作本身存在的问题。再加上学术圈内每个人的品味天差地别，对于novelty、contribution都有自己的见解，不认同送审论文的创新点也实属常见。

回复建议：不直接反驳。清晰（例如分条陈述）、详细地列出论文与现有工作的区别。

<br>

<mark>需要补充Baseline/对比实验 (More Baseline/Comparison Experiments Needed)</mark>

必备性：★★★★★

攻击性：★★☆☆☆

这句更是典中典。补充实验这种行为目前已经被CS领域的一些会议rebuttal禁止，不过在期刊中，增加补充实验这种事仍是一个可接受的操作。对比实验能够提高论文的说服力，但对于已经充分对比的工作，很难不让人认为审稿人想要通过这句话让作者提高工作量，并暗示作者引用自己的工作。不过这句话有暴露自己身份的风险，建议谨慎使用。

2026年的ICLR中，一位（或多位）眼光独到的审稿人曾在多篇论文[^iclr1]${}^{,}$[^iclr2]的审稿意见中给出长达40条问题的审稿意见，其中多条意见均为补充对比/消融实验。这种行为对原文提升的意义不大，AC应该也不会考虑这种意见。

> 在最近的论文投稿中，我的两篇期刊均被要求补充实验，其中第一篇要求补充的实验复杂度很高，且原作者没有公开代码，另一篇要求补充的实验则和文章关联较低。在revision阶段我均没有补充这些实验，其中第一篇最终被接受，第二篇还在二轮审稿中。

回复建议：如果建议合理，可以补充实验；如果建议不合理，给出不补充实验的充分理由。

<br>

<mark>理想化假设/没有实际价值/实验报告 (Idealized Assumptions, Experimental Report)</mark>

必备性：★★★★☆

攻击性：★★★☆☆

常见于理论性较强的论文，通过指出理想化假设否认实际价值，从而否认论文的贡献。理论分析中理想化假设往往是不可或缺的，就像经典的`真空中的球形鸡`笑话。当然，理论人也会觉得工程人的工作像是工地打灰。这句话的精神伤害比较高，容易让作者陷入自我怀疑。我在审稿时既遇到过一点应用价值没有的纯理论分析，也遇到过纯实验报告。

回复建议：理论性工作遇到此类意见可以增加一个简单的非理想参数的仿真，证明工作的鲁棒性；或者增加一个简单的非理想参数的影响的分析，例如假设参数误差服从高斯分布等容易处理的分布。审稿人一般没有必要针对这个问题穷追不舍。

<br>

<mark>综述不足/缺少新论文的引用 (Lack of Recent Papers in Literature Review)</mark>

必备性：★★★☆☆

攻击性：★☆☆☆☆

这算是套话审稿中攻击性比较低的了。给出这样的意见时，大部分情况下审稿人只是希望你帮他刷几个引用，否则既暴露了身份又拒了稿，直接变成双输。

回复意见：我们要相信负责的审稿人还是广泛存在的（~~比如我~~），如果审稿人给出的建议合理，建议采纳。

<mark>写作质量差/语言问题 (Poor Writing Quality/Language Issues)</mark>

必备性：★★☆☆☆
攻击性：★☆☆☆☆

现在是AI时代了，提交的稿件如果还有明显的语法或者表达问题，只能证明作者本人是个老实人。事实上我们现在已经很难找到完全没有AI痕迹的论文了，大到论文idea，小到语法润色，AI已经在逐渐杀死学术职业。我建议这个时代不要再写这么招笑的审稿意见了，除非真的很烂。

回复建议：在AI开天辟地之前，对于虽然写的一般但是也能满足表达要求的论文，我们常常拉一个native speaker做coauthor，然后无论改没改都回复“我们已经润色了”；对于现在这个时代，建议还是AI跑一遍，然后手动调整一下让论文看起来像人写的。


# 其他常见套话 Lookup Table

<mark>仿真参数不合理 (Unrealistic Simulation Parameters)</mark>

无线通信仿真往往涉及SNR（发射功率与噪声）、用户数、天线配置等参数。作为审稿人可以重点关注一些容易被忽略的参数设置，例如路径损耗模型、噪声模型、OFDM子载波间隔（15kHz）与带宽，OFDM的循环前缀长度/导频与场景是否符合，etc。目前我审稿的大部分论文中都会有参数不合理的现象。这种问题可以显著填充审稿意见长度，且大部分容易解决。

回复建议：提供参数选择的依据（如基于3GPP标准或真实数据集），如方便可以补充敏感性/鲁棒性分析（如不同参数下的性能曲线）。如果参数确实不切实际，承认并调整。

<mark>缺少复杂度分析 (Lack of Complexity Analysis)</mark>

根据当代论文的八股风格，复杂度分析是必不可少的。不过其实很多论文在复杂度这一块都写得比较随意，有的人衡量模型参数量，有的人衡量乘加次数，有的人比较实际运行时间。这部分内容一般只会占用一个图表和一小段文字。

回复建议：补充复杂度分析，最好是乘法次数/模型参数量这样的指标，并对比运行时间。

<mark>复杂度分析无法反映端到端延迟 (Complexity Analysis Does Not Reflect End-to-End Latency)</mark>

对于已经提供了复杂度但是没提供运行时间的论文可以写这句话。复杂度分析往往无法反映实际运行时间，尤其是对于AI模型而言，硬件加速、并行计算算法等因素会显著影响实际运行时间。

回复建议：补充运行时间。

<mark>未考虑实际硬件 (Unrealistic Hardware Consideration)</mark>

常见于涉及硬件实现的论文，例如混合波束赋形、低分辨率ADC、可移动天线、超大MIMO/RIS。如果你恰好是一个研究硬件约束的人，可以用这个理由为自己刷几个引用。

回复建议：引用相关论文论证合理性。

<mark>缺少收敛性分析 (Lack of Convergence Analysis)</mark>

对于迭代算法类的论文，收敛性分析可以提高论文的说服力。考虑到数值仿真有时候已经能够体现收敛性，该意见的优先级不高。

<mark>信道模型太简单 (Overly Simplified Channel Model)</mark>

个人认为理论工作可以适当简化信道模型以便于分析。如果是比较工程/实际的工作，最好配合3GPP等标准信道模型进行仿真，否则容易overestimate算法性能。

回复建议：解释模型选择的合理性。如有必要，添加复杂模型的补充仿真。

<mark>(凸优化, 贝叶斯等算法)复杂度过高 (Complexity is too High)</mark>

车轱辘话。

回复建议：可以说明focus点在算法设计/问题建模上，并不在复杂度上，文章只是数值验证有效性等。如果能够提供更低复杂度的近似算法，可以补充。

<mark>模型的近似误差 (Approximation Error of the Model)</mark>

多次近似会积累误差，导致结果不准确。例如近场工作中常使用近轴近似这类方法，但是大部分场景不太近轴，误差较高。

回复建议：一般来说投出去的论文结果已经是近似误差影响后的，如果数值结果已经体现了优越性，说明近似误差的影响有限。做合理解释即可。

<mark>(物理层安全)假设窃听者的CSI完美是不现实的 (Perfect CSI of Eavesdropper is Unrealistic)</mark>

常见假设，窃听者CSI完美已知，此时可以严格推导闭式解。这个假设确实不够合理。

<mark>(物理层安全)只考虑了保密速率 (Only Considered Secrecy Rate)</mark>

车轱辘话。

回复建议：解释保密速率的重要性。篇幅合适的情况下补充其他合理指标，例如能量效率、复杂度等。

<mark>(物理层安全)窃听/攻击模型太简单 (Eavesdropping/Attacking Model is Too Simple)</mark>

<mark>(OFDM) Frequency-flat假设PAPR过高 (High Peak-to-Average Power Ratio)</mark>

当论文提到OFDM时可以打出此牌。

回复建议：如果frequency-flat假设在此场景下不必要，可以将原本flat的假设换成selective的；如果frequency-flat假设是必要的，自己想想办法。

<mark>(MIMO) 单用户/单天线不是MIMO (Single User/Single Antenna is not MIMO)</mark>

属于术语纠正类套话。

<mark>(信道估计) 未考虑多用户 (Multi-User Not Considered)</mark>

常见套话。

回复建议：用正交接入等话术化解。

<mark>(信道估计) 未考虑移动性/多普勒效应 (Doppler Effect Not Considered)</mark>

<mark>(信道估计) 导频开销过高 (Excessive Pilot Overhead)</mark>

<mark>(波束赋形) 移相器相位精度 (Phase-Shifter Accuracy)</mark>

<mark>(含ZF/LS算法) 矩阵条件数 (Poor Matrix Condition Number)</mark>

<mark>未展示AI模型泛化能力 (Generalization Ability)</mark>

<mark>可解释性差 (Interpretability)</mark>

<mark>训练数据集不合理/与实际采集数据失配 (Unrealistic Training Dataset)</mark>

<mark>缺少复杂度分析 (Lack of Complexity Analysis)</mark>

<mark>与传统方法对比不足 (Insufficient Comparison with Traditional Methods)</mark>



# 个人总结

经过套路的对轰，论文原本想要表达的意思可能会隐藏在这许多套话中。有时一篇非常精巧的paper，在几个审稿意见之后就会变得贴满狗皮膏药。希望新的一年里大家审稿都能peace一点。

一点微小的人生经验

 - 写论文introduction部分时，尤其是在写related work时，尽量引用近期的工作。由于编辑有时会在参考论文中寻找审稿人，巧妙地调整引用可以降低被部分同行攻击的风险。
 - 可以适当地留几个比较显然的漏洞，例如仿真中少仿了一个参数的影响，少对比了某种知名的方案，论文综述少写了一些内容，推导过程的某一步骤没有详细说明。审稿人在捕捉到这些漏洞后，往往会认为自己的review过程已经找出了论文的不足，会放松一些对其他部分的苛刻程度。当然，这个度要自己把握，要防止漏的太多被审稿人分类为垃圾文章。（本条针对人类审稿人）
 - 拿到审稿意见后，建议先放一两天再开始回复，避免情绪化的回复。（经过尝试，对我无效）
 - 根据编辑对审稿人意见的总结，以及最终的判决结果，可以大概了解编辑的看法。编辑的意见比审稿人更重要。
 - 不要拒稿自己能够看懂的论文。



# 扩展阅读

[^iclr1]: [VGR: Visual Grounded Reasoning](https://openreview.net/forum?id=kDhAiaGzrn)

[^iclr2]: [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](https://openreview.net/forum?id=8qk6eUnvbH)
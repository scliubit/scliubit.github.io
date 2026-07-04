---
layout:     post
title:      "WCL'26: 弯曲波束物理层安全<br>WCL'26: Robust and Secure Communication with Bending Beams"
# subtitle:   "Caustic Beams for Secure Communication"
date:       2026-03-29
author:     "Shicong Liu"
permalink:  /posts/WCL26COMMENTS/
excerpt:    "内容补充说明<br>COMMENTS"
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

<style>
    p {
        text-align: justify;
        text-justify: inter-word;
    }
</style>


我于2024年末在globecom南非偶然听说一些人最近在做<mark>可弯曲波束</mark>，且效果甚佳。彼时的相关工作已经发表准子刊`NC`[^NC]或者孙刊`Comm. Eng.`[^CE]，风光无两。当时我没有深入了解技术细节，当反应过来时已经看到了一些工作出版，因此决定浅蹭一下热度。

本文目前已经被`IEEE Wireless Commun. Lett.`接收，可以通过[arXiv](https://arxiv.org/abs/2603.24077)免费获取。以下简要介绍一下本文的核心思路和方法。




# 前言



实话说，寻找可弯曲波束的应用场景是一个难题。在现代beamforming技术中，ZF和EVD都是常见的方案。通过对信道矩阵做ZF或者EVD，波束能够在所需的用户位置汇聚，且能够尽可能降低干扰、提高频谱效率。近年来一些基于毫米波甚至THz的方案中，由于高频元器件的成本与能耗都很高，因此才引入了分层处理的方案。最典型的就是数模混合的方案，其中模拟部分需要进行波束对准，数字部分消去近似误差。



在这种经验惯性下，设计一个波束的形状似乎不是很重要。一个满足各种要求的波束形状，几乎可以肯定它不是优化问题的最优解，而经过合适的处理能够被优化求解的问题，优化结果一般都会更好，无论形状是怎样的[^quote]。



经过一段时间的慎重考虑，我们采纳了物理层安全场景。该场景比较能够有效利用波束形状。由于大部分弯曲波束的形成原理，其单侧辐射图样总呈现出显著低于另一侧的特性。我们将利用这个性质和弯曲的形状，提升传输的安全性。



# Motivation

近场波束聚焦（beamfocusing）利用XL-MIMO的大孔径，可以将能量集中到特定位置，从而在物理层安全通信中有效降低窃听者的接收信号强度。然而在实际场景中，窃听者的位置估计往往存在误差，即便很小的定位误差也可能导致焦点偏移，进而使得保密速率严重下降。

现有的鲁棒设计方案主要有两方面的问题：
1. 大部分方案假设窃听者CSI完美已知，或者依赖迭代优化求解，计算复杂度较高，不适合XL-MIMO系统；
2. 近场中的CSI不确定性主要来源于<mark>定位误差</mark>而非信道估计误差，传统远场鲁棒优化方法（如松弛约束并做S-procedure）无法直接处理。

为此，我们提出了一种基于电磁焦散（`EM caustic`）效应的物理启发式鲁棒波束成形方案，通过设计弯曲的焦散波束轨迹绕过潜在的窃听区域，实现安全的通信。

# 系统模型

<div>
    <img class="postimg" src="/images/in-post/caustic26/sysmodel.png" width="500px" />
    <div class="caption">系统模型与符号定义</div>
</div>

考虑一个近场安全通信场景，BS配备$M$个无源超表面（metasurface）阵元[^meta]，服务一个单天线（实际上天线数没有严格约束，阵列尺寸较小即可）合法用户（UE），同时一个窃听者处于BS的近场区域。

我们采用球面波模型来描述近场信道：
<div>
$$
\begin{equation}
	h\left( {\bf r}_{\rm T},  {\bf r}_{\rm R}\right) = \frac{e^{\jmath \kappa \Vert {\bf r}_{\rm T} - {\bf r}_{\rm R} \Vert} }{\Vert {\bf r}_{\rm T} - {\bf r}_{\rm R} \Vert},
\end{equation}
$$
</div>

由于窃听者通常不会配合BS进行定位，其位置被建模为 $$\mathbf{r}_{\rm E}=\hat{\mathbf{r} }_{\rm E}+\Delta\mathbf{r}$$，定位误差 $$\Delta\mathbf{r}$$ 约束在半径为 $$\varepsilon$$ 的圆形区域 $$\Omega_\varepsilon$$ 内。由于我们采用无源超表面进行模拟波束成形，优化变量为相移向量 $${\bf f}$$，满足恒模约束 $$\vert f_m\vert = 1$$。

设计目标是最大化窃听区域上的<mark>最差(worst-case)保密速率</mark>：
<div>
$$
\begin{equation}
\underset{ {\bf f} }{\rm max} ~~ \underset{\Delta{\bf r}\in \Omega_{\varepsilon} }{\rm min}~{R}_{\rm S},\quad\mathrm{s.t.}~~\vert {\bf f} [m]\vert = {1}/{\sqrt{M} }.
\end{equation}
$$
</div>

# 相位梯度与波束方向控制

本文的核心思想是通过控制阵列上的<mark>相位梯度</mark>来操纵EM波的出射方向。丰俭由人，这里提供一个比较容易理解的推导过程，如果想直接看结论也可以跳过，看本段最后。

考虑满足Helmholtz方程的单色EM波 $$U(x,y)$$，令试探解为

<div>
$$
\begin{equation}
	U(x,y) = A(x,y)e^{\jmath\kappa D(x,y)},
\end{equation}
$$
</div>
代入Helmholtz方程后得到

<div>
    $$
    \nabla^2 A + 2\jmath \kappa \nabla A\cdot \nabla D + \jmath\kappa A\nabla^2 D-A\kappa^2\vert \nabla D \vert^2 + \kappa^2 A = 0
    $$
</div>

整理得到

<div>
    $$
    \frac{\nabla^2 A}{\kappa^2} + \frac{2\jmath \nabla A\cdot \nabla D + \jmath A\nabla^2 D}{\kappa} + A\left(1 - \vert \nabla D \vert^2\right) = 0.
    $$
</div>

在高频率造成的大波数 $$\kappa = 2\pi/\lambda$$ 的近似下，我们得到如下Eikonal方程：

<div>
$$
\begin{equation}
	\Vert \nabla D (x,y) \Vert = 1.
\end{equation}
$$
</div>
这意味着距离函数 $D(x,y)$ 的梯度长度是固定的（若不考虑折射率归一化的情况，此处等式右侧为折射率$$n$$）。由于距离函数的梯度始终垂直于波前面，因此，**如果我们能控制发射界面上的相位梯度 $$x$$ 分量（或者任意方向的分量），就可以控制发射孔径上每个位置的EM波的出射方向**。具体而言，对于期望的出射角 $\theta$：

<div>
$$
\begin{equation}
	\left.\frac{\partial \phi(x,y)}{\partial x}\right\vert_{y=0} =\kappa\cos \theta.
\end{equation}
$$
</div>
<div>
    <img class="postimg" src="/images/in-post/caustic26/illustrate.png" width="720px" />
    <div class="caption">(a) 波束指向、(b) 波束聚焦、(c) 焦散波束，及对应的相位分布 (d)-(f)</div>
</div>



这个关系本质上是广义Snell定律[^generalizedsnell]。利用它可以推导出不同的波束成形方案：
- **波束指向**：固定出射角 $$\theta$$，相位分布为线性函数 $$\phi(x) = \kappa\cos\theta \cdot x + C$$；

- **波束聚焦**：出射角随 $$x$$ 变化以使所有射线汇聚于UE位置，相位分布 $$\phi(x) = -\kappa\Vert {\bf r}_{\rm UE} - (x,0) \Vert + C$$。

- **任意波束轨迹**：直接求解微分方程。例如，对于**抛物线**轨迹（产生特定方向的抛物线轨迹的波束有时也被称为Airy波束），若在$$f(x) = (x/a)^2$$时求解

  <div>
      $$
      \left.\frac{\partial \phi(x)}{\partial x}\right\vert_{x=x_\xi} =\kappa\cos\theta = \frac{\kappa}{\sqrt{1\!+\!\left( f^\prime(\xi) \right)^2}},
      $$
  </div>

  则有

  <div>
      $$
      \phi_{\rm Quad}(x) = \frac{\kappa a^2}{4}{\rm asinh}\left( \frac{4x}{a^2} \right).
      $$
  </div>
  
  
  
  

# 焦散波束轨迹设计

有了上述的波束设计方法，我们可以想办法设计一个波束来绕过窃听区域。

## 分段轨迹设计

为了兼顾安全性和能量效率，我们将BS阵列划分为<mark>焦散子阵</mark>和<mark>聚焦子阵</mark>两部分：

<div>
    <img class="postimg" src="/images/in-post/caustic26/proposed.png" width="250px" />
    <div class="caption">分段轨迹设计示意图</div>
</div>


- **焦散子阵** $$\mathcal{A}_{\rm C}$$：直射路径被窃听区域遮挡的阵元，其出射波束沿焦散轨迹绕开 $$\Omega_\varepsilon$$；
- **聚焦子阵** $$\mathcal{A}_{\rm F}$$：直射路径不经过窃听区域的阵元，直接将能量聚焦到UE。

分段焦散轨迹由三段组成：切线段 $$\overline{TP}$$ + 圆弧 $$\widehat{PQ}$$ + 切线段 $$\overline{QR}$$。

## 闭式相位分布

对于焦散子阵，以出射角 $$\theta$$ 为参数求解，最终得到闭式相位分布：
<div>
$$
\begin{equation}
	\phi(x)=\kappa\left( 2\varepsilon{\rm atan}\left( \frac{x-x_{\rm E}+S(x)}{\varepsilon+y_{\rm E} } \right)-S(x) \right),
\end{equation}
$$
</div>
其中
<div>
$$
\begin{equation}
	S(x) = \sqrt{\left( x-x_{\rm E} \right)^2+y_{\rm E}^2 -\varepsilon^2}.
\end{equation}
$$
</div>

对于聚焦子阵，相位分布即为经典的聚焦相位。整体相位分布为分段函数，确保连续性即可。

值得注意的是，该闭式解<mark>不需要任何迭代优化</mark>，可以直接由几何参数计算得到。



# 仿真结果

## 波束可视化

<div>
    <img class="postimg" src="/images/in-post/caustic26/beamvis.png" width="640px" />
    <div class="caption">不同方案的空间波束可视化及窃听区域局部放大</div>
</div>



上图展示了不同相位设计方案下的归一化辐射强度。可以看到：
- 波束指向方案 (a) 在窃听区域内有大量能量泄漏；
- 基准方案 (b)(c) 只能在窃听区域内很小的范围抑制泄漏；
- 本文提出的焦散波束 (d) 成功绕过了整个窃听区域，实现了接近绝对安全的通信。

## 保密速率

<div>
    <img class="postimg" src="/images/in-post/caustic26/sr_pt.png" width="600px" />
    <div class="caption">保密速率随发射功率变化</div>
</div>


在不同发射功率下，本文方案在均值和最差情况保密速率上均显著优于对比方案。特别是在高SNR区域，传统方案的保密速率趋于饱和，而焦散波束方案由于有效抑制了窃听区域的能量泄漏，保密速率持续增长。

## 计算复杂度

本文方案的执行时间在 $$M=256$$ 时仅约 $$9.64\times 10^{-4}$$ 秒，远低于基线方案（Norm-Bounded: $$27.4$$s, ADMM: $$0.104$$s），且随阵元数增长的时间开销增加极小，展现了良好的可扩展性。

# 引用格式



```bibtex
@ARTICLE{11505880,
  author={Liu, Shicong and Yu, Xianghao and Schober, Robert},
  journal={IEEE Wireless Commun. Lett.}, 
  title={Robust and Secure Near-Field Communication via Curved Caustic Beams}, 
  year={2026},
  volume={15},
  number={},
  pages={3069-3073},
  keywords={Antennas;Apertures;Feeds;Antennas and propagation;Phased arrays;Radio broadcasting;Frequency modulation;Phase noise;Phase shifters;System-on-chip;Caustic;near field;robust design;secrecy rate;secure communication},
  doi={10.1109/LWC.2026.3690036}}
```

```plaintext
S. Liu, X. Yu and R. Schober, "Robust and Secure Near-Field Communication via Curved Caustic Beams," IEEE Wireless Commun. Lett., vol. 15, pp. 3069-3073, 2026.
```

---

<br>
<br>
<br>

~~更多内容待续~~

~~To Be Continued~~

---

# 拓展阅读

[^NC]: [Chen, H., Kludze, A. & Ghasempour, Y. A physics-informed Airy beam learning framework for blockage avoidance in sub-terahertz wireless networks. Nat Commun 16, 7387 (2025)](https://www.nature.com/articles/s41467-025-62443-0)

[^CE]: [Guerboukha, H., Zhao, B., Fang, Z. et al. Curving THz wireless data links around obstacles. Commun Eng 3, 58 (2024).](https://www.nature.com/articles/s44172-024-00206-3)

[^quote]: 尽管我本人并不了解优化相关内容，但已经在电子年会、ICC'26等多处听人提及这个观点。此处仅为引述。

[^meta]: metasurface是一种低成本高精度的相位调制方案，本方案也可以用在其他硬件上。

[^generalizedsnell]: [N. Yu, P. Genevet, M. A. Kats, F. Aieta, J.-P. Tetienne, F. Capasso, and Z. Gaburro, "Light Propagation with Phase Discontinuities: Generalized Laws of Reflection and Refraction," *Science*, vol. 334, no. 6054, pp. 333-337, 2011.](https://www.science.org/doi/10.1126/science.1210713)

[^causticopt]: [J. Froehly, F. Courvoisier, A. Mathis, M. Jacquot, L. Furfaro, R. Giust, P. A. Lacourt, and J. M. Dudley, "Arbitrary accelerating micron-scale caustic beams in two and three dimensions," *Opt. Express*, vol. 19, no. 17, pp. 16455-16465, 2011.](https://opg.optica.org/oe/fulltext.cfm?uri=oe-19-17-16455)

Expectation-Maximization (EM)算法是一种广泛应用于参数估计/分类等问题的算法[^1]。和名字所指出的一样，该算法通过在`E步骤`和`M步骤`之间的迭代过程实现参数估计，其最重要的特点是可以应对概率分布中存在隐变量的场景，通过引入替代函数并优化上界的方式实现原似然函数的优化。在通信问题中，该类算法通常被用于估计参数变量的分布，但经常被用于算法迭代中的一个步骤[^2]或者为贝叶斯推断方案提供初始化参数[^3]。

对于一个最普遍的场景，问题往往是如下形式：

我们通过某种采样方式获取了观测数据$\bf y$, 并已知被观测的数据分布被$\boldsymbol{\theta}$参数化。

> 实际场景中我们或许对数据的实际分布没有先验知识，因此该参数$\boldsymbol{\theta}$可以是我们建模数据分布后假定的待估计参数。

一个非常实际的情况是，原数据可能存在一个或若干未被观测到的隐变量$\bf z$，例如，原始数据存在多个聚类中心点，或者原始数据由多个高斯分布叠加而成，则被采样的数据来自不同的高斯分布，etc，此时我们需要估计的参数$\boldsymbol{\theta}$则是来自不同“类别”$\bf z$。

> 这里的隐变量大部分情况下是为了简化问题建模而引入的。例如进行概率密度估计时，可以采用混合高斯分布来近似多峰的分布谱，可以让原本难以描述的概率密度被几个简单的参数描述。

我们先不考虑隐变量时，估计过程可以是简单的最大似然法，即

<div>
    \begin{equation}
\begin{aligned}
\ell(\boldsymbol{\theta} \mid {\bf y} ) & =\log P({\bf y} \mid \boldsymbol{\theta} ) \\
& =\log \left(\prod_{i=1}^n P\left({\bf y}_i \mid \boldsymbol{\theta} \right)\right) \\
& =\sum_{i=1}^n \log P\left({\bf y}_i \mid \boldsymbol{\theta} \right)
\end{aligned}
\end{equation}
</div>

此时的参数$\boldsymbol{\theta}$可以通过最大似然的方式求得，或者说，在解空间范围内穷搜。不过由于我们对数据的分布做了假设，即真实分布中存在隐变量，此时的对数似然函数将被改写为

<div>
    \begin{equation}
\begin{aligned}
\log P({\bf y} \mid \boldsymbol{\theta}) & =\log \sum_{\bf z} P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) \\
& =\log \left(\sum_{\bf z} P({\bf y} \mid \boldsymbol{\theta}, {\bf z}) P({\bf z} \mid \boldsymbol{\theta} )\right)
\end{aligned}
\label{eq2}
\end{equation}
</div>

实际上最大似然估计(Maximum Likelihood Estimation, MLE)大部分情况下是参数空间穷搜，因此复杂度本身较高。如果引入额外的隐变量，该过程的复杂度将成倍提升。

为了以能够接受的复杂度进行求解，一个很直观的操作是构造一个代理函数，使得其上界能够在指定位置与最大似然函数对齐。那么我们通过不断迭代优化代理函数，就能实现似然函数的优化过程。

首先，假设隐变量存在分布$P({\bf z})$，且有

<div>
    \begin{equation}
\begin{aligned}
P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) = P({\bf z}\mid {\bf y}, \boldsymbol{\theta} ) P({\bf y}\mid \boldsymbol{\theta})
\end{aligned}
\end{equation}
</div>
那么原对数似然函数$\eqref{eq2}$可以表示为

<div>
    \begin{equation}
\begin{aligned}
\log P({\bf y}\mid \boldsymbol{\theta}) = \log \frac{P({\bf y}, {\bf z} \mid \boldsymbol{\theta})}{P({\bf z}\mid {\bf y}, \boldsymbol{\theta} )}  
\end{aligned}
\end{equation}
</div>

显然左侧与$\bf z$无关，对左侧关于$\bf z$求和仍不变，对右侧关于$\bf z$求和可以得到

<div>
    \begin{equation}
\begin{aligned}
    \underset{\bf z}{\mathbb{E}}[ \log \frac{P({\bf y}, {\bf z} \mid \boldsymbol{\theta})}{P({\bf z}\mid {\bf y}, \boldsymbol{\theta} )}   ] &= \underset{\bf z}{\mathbb{E}}[ \log \frac{ P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) }{P({\bf z})} -\log \frac{P({\bf z}\mid {\bf y}, \boldsymbol{\theta} )}{P({\bf z})}  ]\\
    &=\sum_{\bf z} P({\bf z})\log \frac{ P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) }{P({\bf z})} + {\rm KL}(P({\bf z}) \| P({\bf z}\mid {\bf y}, \boldsymbol{\theta} ) )\\
    &\geq \sum_{\bf z} P({\bf z})\log \frac{ P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) }{P({\bf z})}
\end{aligned}
\end{equation}
</div>

> 这里其实和[变分](../../../../2023/08/13/VAE-TUT/)的推导差不多，就这点东西来回倒。该过程也可以采用Jensen不等式直接给出。

由于KL散度是一个大于$0$的指标，因此最后的大于号成立，等于号的成立当且仅当KL散度内的两个分布完全相同。注意到隐变量$\bf z$的分布无法被观测，这里不加证明地指出可以用$\bf z$的估计后验分布$\hat{P}({\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)})$作为$P({\bf z})$的替代。这个操作直接消去了上述公式中KL散度项（即，让似然函数与指定上界函数之间等号成立），并进一步得到

<div>
\begin{equation}
\begin{aligned}
\log P({\bf y}\mid \boldsymbol{\theta}) = \sum_{\bf z} \hat{P}({\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)}) \log \frac{ P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) }{\hat{P}({\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)})}
\end{aligned}
\end{equation}
</div>

那么$\boldsymbol{\theta}$的MLE就可以表示为

<div>
\begin{equation}
\begin{aligned}
\hat{\boldsymbol{\theta}} &= {\underset{\theta}{\rm argmax}}\log P({\bf y}\mid \boldsymbol{\theta})\\ 
    &= {\underset{\theta}{\rm argmax}} \sum_{\bf z} \hat{P}({\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)}) \log { P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) }\\
    &={\underset{\theta}{\rm argmax}} \underset{ {\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)} }{\mathbb{E}}[ \log { P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) } ]
\end{aligned}
\end{equation}
</div>

至此EM的基本原理实际上已经结束。E步骤执行的操作正是

<div>
\begin{equation}
\begin{aligned}
Q(\boldsymbol{\theta},\boldsymbol{\theta}^{(t)}) = \underset{ {\bf z}\mid {\bf y},\boldsymbol{\theta}^{(t)} }{\mathbb{E}}[ \log { P({\bf y}, {\bf z} \mid \boldsymbol{\theta}) } ]
\end{aligned}
\end{equation}
</div>

M过程则对$\theta$进行MLE运算。

> 和许多类似算法相似，EM算法的效果实际上很依赖初始值。







---

关于EM算法的更多实现细节可以参考论文[^4]及其对应演示文稿[^5]。

# 扩展阅读

[^1]:[Do, C., Batzoglou, S. What is the expectation maximization algorithm?. *Nat Biotechnol* **26**, 897–899 (2008).](https://doi.org/10.1038/nbt1406)
[^2]:[X. Meng, S. Wu, L. Kuang, D. Huang, and J. Lu, "Approximate Message Passing with Nearest Neighbor Sparsity Pattern Learning"](https://arxiv.org/abs/1601.00543)
[^3]:[C. -K. Wen, S. Jin, K. -K. Wong, J. -C. Chen and P. Ting, "Channel Estimation for Massive MIMO Using Gaussian-Mixture Bayesian Learning," in *IEEE Transactions on Wireless Communications*, vol. 14, no. 3, pp. 1356-1368, March 2015]()
[^4]:[A View of the EM Algorithm that Justifies Incremental, Sparse, and other Variants](https://www.cs.toronto.edu/~hinton/absps/emk.pdf)
[^5]:[Slides for Paper `A View of the EM Algorithm that Justifies Incremental, Sparse, and other Variants`](https://cs.brown.edu/courses/csci2950-p/spring2010/lectures/2010-02-24_zuffi.pdf)
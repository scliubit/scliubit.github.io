---
layout:     post
title:      "Hello World"
subtitle:   " \"Hello World, Again\""
date:       2022-01-27 12:00:00
author:     "Shicong Liu"
header-img: "img/home.jpg"
catalog: true
mathjax: true
tags:
    - 生活
    - Meta
    - 测试
---

# 样式测试

## 代码块

`Python 3`

```python
import os
import math
import time

print(time.time())

@tf_utils.shape_type_conversion
def build(self, input_shape):
    if context.executing_eagerly() and tf_config.list_logical_devices('GPU'):
      with ops.device('cpu:0'):
        self.embeddings = self.add_weight(
            shape=(self.input_dim, self.output_dim),
            initializer=self.embeddings_initializer,
            name='embeddings',
            regularizer=self.embeddings_regularizer,
            constraint=self.embeddings_constraint,
            experimental_autocast=False)
    else:
      self.embeddings = self.add_weight(
          shape=(self.input_dim, self.output_dim),
          initializer=self.embeddings_initializer,
          name='embeddings',
          regularizer=self.embeddings_regularizer,
          constraint=self.embeddings_constraint,
          experimental_autocast=False)
    self.built = True

  def compute_mask(self, inputs, mask=None):
    if not self.mask_zero:
      return None
    return math_ops.not_equal(inputs, 0)

```

## 站内图像

![](/img/num/matlab.bmp){:height="90%" width="90%"}

## LaTeX 公式

一句话

<div>
$$
\begin{align}
\tilde{r}(t)&=\sum_{\ell=0}^{L-1}\sqrt{\alpha_\ell}\tilde{s}(t-\tau_\ell)\notag\\
&=\sum_{\ell=0}^{L-1}\sqrt{\alpha_\ell}\mathfrak{R}\{s(t-\tau_\ell)e^{2\pi f(t-\tau_\ell)}\}\notag\\
&=\mathfrak{R}\{\sum_{\ell=0}^{L-1}\sqrt{\alpha_\ell} s(t-\tau_\ell)e^{2\pi f(t-\tau_\ell)}\}
\end{align}
$$
</div>

一句话

## 引用

然而目前遇到的问题是图像该如何进行embedding。ViT给我们的答案是将图像crop成不同的patch，然后将不同的patch进行展平，获得一个向量。原文[^1]中作者将一个图像切分成$16\times 16$的块，若是RGB图像，我们就会得到$256\times 3=768$的矢量。则原来的$224\times 224$的图像就可以被切割为$196$个patch，从而作为$196$个序列被处理。



> 超链接

[^1]: AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE [URL](https://openreview.net/pdf?id=YicbFdNTTy)
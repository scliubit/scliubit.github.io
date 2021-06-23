---
layout:     post
title:      "Transformer基础学习"
subtitle:   " 只代表作者个人观点 "
date:       2021-06-21 12:00:00
author:     "Shicong Liu"
header-img: "img/home.jpg"
catalog: true
mathjax: false
tags:
    - 学习
---


# Transformer 与个人想法乱写

`只代表个人观点`

## Word Embedding

`embedding`本意为嵌入，是一种用低维向量代表一个高维语义的工具。

曾经的词袋模型CBOW，skip-gram，glove之类的方案会根据语料库信息分析一个单次的出现与前后文出现单词的关系，从而通过对词频pdf等因素进行统计，生成一个具有语义信息的定长稠密词向量。与这些传统方法相似，现在的词嵌入研究手段也是利用语料库和任务目标进行联合训练调整。`Keras`中的实现为

```python
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

其中不难看出，embedding就是通过随机矩阵生成的初始权重，这里的初始化方式默认是`uniform`，即均匀分布，也容易验证权重均值确实为0。

在进行调用时，embedding层根据前一层的词token进行查表，得到

```python
def call(self, inputs):
    dtype = backend.dtype(inputs)
    if dtype != 'int32' and dtype != 'int64':
      inputs = math_ops.cast(inputs, 'int32')
    out = embedding_ops.embedding_lookup_v2(self.embeddings, inputs)
    if self._dtype_policy.compute_dtype != self._dtype_policy.variable_dtype:
      out = math_ops.cast(out, self._dtype_policy.compute_dtype)
    return out
```

关键操作即为`out = embedding_ops.embedding_lookup_v2(self.embeddings, inputs)`查表操作。

语言模型为了解决输入难以处理的问题不得不采用词嵌入手段，但是词嵌入又由于其附加的语义信息帮助语言模型的处理。Transformer模型利用词嵌入方法和完全由注意力构成的网络实现了各种功能，这也让我想将其转移到竞赛题目上使用。单纯采用卷积的网络已经开始出现明显的过拟合现象，不知道能否采用Transformer来combat。

然而目前遇到的问题是图像该如何进行embedding。ViT给我们的答案是将图像crop成不同的patch，然后将不同的patch进行展平，获得一个向量。原文[^1]中作者将一个图像切分成$16\times 16$的块，若是RGB图像，我们就会得到$256\times 3=768$的矢量。则原来的$224\times 224$的图像就可以被切割为$196$个patch，从而作为$196$个序列被处理。

如果并非分类处理，实际上每一层Encoder的输出维度都是相同的。将输入转化为固定维度$d$之后，每一层Encoder就会输出固定维度，并重新输入Decoder。

## Positional Encoding

除了输入词嵌入之外，Transformer还采用位置编码的方式来利用序列的前后顺序。

> ..., we must inject some information about the relative or absolute position of the tokens in the sequence.[^2]

经过词嵌入得到的输入已经是一个${\rm seq\_length}\times {\rm dimension}$维度的矩阵，其中${\rm dimension}$维度为自定义的维度。其实${\rm dimension}$是对原来文本的一种升维表示，也是词嵌入的维度。${\rm seq\_length}$维度为输入序列长度，其中每一个矢量长度均为${\rm dimension}$，都对应原序列中的一个字符。这个处理将原来的序列升维了${\rm dimension}$倍。对于这样一个升维表示，我们采用每一个维度不同的编码才有利于对特征的处理，因此对于每一个位置的字符，我们做一个位置编码。原文的编码方式为奇数和偶数对应的${\rm dimension}$维度采用$\sin$或者$\cos$编码，这样的目的是另不同维度包含的信息更为丰富。

实际操作中，我们会将嵌入词向量信息直接加在位置编码上，不采用乘法是为了防止出现迫零小值令信息失真。

## Encoder Layer

实际编码层只有两个主要部分，一个是线性映射前馈网络（2层），一个是并行注意力。注意力机制是Transformer的核心，也将在后面具体研究。一般Encoder Layer是被复用的部分，常见的写法都会将ffn和attn两部分写在enc layer中，以便直接叠层。

需要注意的是，对于输入而言，如果序列长度不统一，则在输入之前会统一padding到统一的长度（某最大长度约束），

## Layer Norm

LN与BN不同在于，BN是对一个mini-batch内的所有数据计算归一化，也被称为横向归一化，而LN相比之下不对batch内做归一化。在语言模型中不同batch之间的差距较大，如果对batch维度做归一化可能导致梯度的不稳定，而做layer norm的时候则可以有效避免这个问题

> Normalize the activations of the previous layer for each given example in a batch independently, rather than across a batch like Batch Normalization.[^3]
>
> *对batch内每一项输入单独做归一化*



[^1]: AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE [URL](https://openreview.net/pdf?id=YicbFdNTTy)
[^2]: Attention Is All You Need [URL](https://arxiv.org/abs/1706.03762)
[^3]: tf.keras.layers.LayerNormalization [URL](https://tensorflow.google.cn/versions/r2.1/api_docs/python/tf/keras/layers/LayerNormalization)


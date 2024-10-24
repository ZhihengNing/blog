---
title: '多元正态分布极大似然估计'
date: 2023-10-14T17:33:09+08:00
draft:  false
summary:  "模式识别第一次作业——多元正态分布的极大似然估计"
tags: ["数学","机器学习"]
---

{{< katex >}}

## 前言

此为研究生课程模式识别的第一次作业，求多元正态分布下关于\\(\boldsymbol{\mu},\boldsymbol{\Sigma}\\)的极大似然估计值。本文用于记录相关公式及推导过程，内容涉及极大似然估计、矩阵求导等。

## 正态分布

众所周知，正态分布的概率密度函数为\\(f(x)=\frac{1}{\sqrt{2\pi \sigma^2}} \exp[-\frac{(x-\mu)^2}{2}]\\)。令\\(x_i \sim N(\mu,\sigma^2)\\)，\\(\mathcal{D}=\set{x_1,x_2,\cdots,x_n}\\)，则极大似然函数为
$$
L(\mu,\sigma^2)=\prod_{i=1}^n f(x_i)=\frac{1}{(2\pi \sigma^2)^{\frac{n}{2}}}\exp [-\frac{1}{2} \sum_{i=1}^n (x_i-\mu)^2 ]
$$
对极大似然取对数，再求导并令\\(\frac{\partial{\ln L(\mu,\sigma^2)}}{\partial \mu}=0,\frac{\partial{\ln L(\mu,\sigma^2)}}{\partial \sigma^2}=0\\)，解得\\(\hat{\mu}=\bar{x},\sigma^2=\frac{1}{n}\sum_{i=0}^n (x-\bar{x})^2=\frac{1}{n}\sum_{i=0}^n (x-\hat{\mu})^2\\)

## 多元正态分布

假设\\( \boldsymbol{x}\_i \in \mathbb{R}^p, \boldsymbol{u} \in \mathbb{R}^p,\boldsymbol{\Sigma} \in \mathcal{S}\_{+}^p \\) ，且\\(\boldsymbol{x}_i \sim \mathcal{N}_p(\boldsymbol{\mu},\boldsymbol{\Sigma})\\)，令\\(\mathcal{D}=\set{\boldsymbol{x}_1,\boldsymbol{x}_2,\cdots,\boldsymbol{x}_n}\\)，则多元形式下的正态分布概率密度函数为：

$$
f(\boldsymbol{x})= \frac{1}{(2\pi)^\frac{p}{2} | \boldsymbol{\Sigma}|^\frac{1}{2}} 
\exp[{-\frac{1}{2}} (\boldsymbol{x-u})^T\boldsymbol{\Sigma}^{-1}(\boldsymbol{x-u})]
$$
对其取对数，并进行化简：
$$
\ln{L(\boldsymbol{u},\boldsymbol{\Sigma})}=-\frac{pn}{2}\ln(2\pi) -\frac{n}{2}\ln|\boldsymbol{\Sigma}|-\frac{1}{2}\sum\_{i=1}^n {(\boldsymbol{x_i-u})^T\boldsymbol{\Sigma}^{-1}(\boldsymbol{x_i-u})}
$$

## 矩阵求导公式

下面给出几个后续证明推导要用到的公式，由于不是本文重点，此处不对其进行证明


$$
\frac{\partial{\ln{|\boldsymbol{X}|}}}{\partial{\boldsymbol {X}}}=\boldsymbol{X^{-T}} \tag{1}
$$

$$
\frac{\partial{\ln(\boldsymbol{\lambda^T X^{-1}\lambda})}}{\partial{\boldsymbol{X}}}=-(\boldsymbol{X^{-1} \lambda \lambda^T X^{-1}})^T \tag{2}
$$

$$
\frac{\partial{(\boldsymbol{\lambda-x})^T \boldsymbol{\Sigma^{-1}} (\boldsymbol{\lambda-x})}}{\partial{\boldsymbol{x}}}=[\boldsymbol{(\lambda-x)^T (\Sigma^{-T}+\Sigma^{-1})}]^T \tag{3}
$$

记\\( \frac{\partial{f(\boldsymbol{X})}}{\partial{\boldsymbol{X}}}=\boldsymbol{A} \\)，其中\\(\boldsymbol{X} \in \mathbb{R}^{n \times n} ,f:\mathbb{R}^{n \times n} \rightarrow \mathbb{R}\\)。因此对于\\(\boldsymbol{X} \in S^n\\)，有：
$$
\frac{\partial{f(\boldsymbol{X})}}{\partial{\boldsymbol{X}}}=\boldsymbol{A^T +A - A\circ E} \tag{4}
$$
其中\\(\circ\\)为Hadamard product。这表明了对称矩阵在求导过程中的特殊性。

由于\\(\boldsymbol{X} \in \mathcal{S}^n\\)，则式\\((1),(2)\\)可转换为\\((5),(6)\\)：


$$
\frac{\partial{\ln{|\boldsymbol{X}|}}}{\partial{\boldsymbol {X}}}
=\boldsymbol{X^{-1}}+\boldsymbol{X^{-T}}-\boldsymbol{X^{-T}}\circ \boldsymbol{E} \tag{5}
$$

$$
\begin{aligned}
\frac{\partial{\ln(\boldsymbol{\lambda^T X^{-1}\lambda})}}{\partial{\boldsymbol{X}}} 
=&-(\boldsymbol{X^{-1} \lambda \lambda^T X^{-1}}) 
-(\boldsymbol{X^{-1} \lambda \lambda^T X^{-1}})^T \newline
&+(\boldsymbol{X^{-1} \lambda \lambda^T X^{-1}})^T \circ \boldsymbol{E} \tag{6}
\end{aligned}
$$



由式\\((3)\\)可得：


$$
\begin{aligned}
\frac{\partial{\ln{L(\boldsymbol{u},\boldsymbol{\Sigma})}}}{\partial{\boldsymbol{u}}}
&=-\frac{1}{2} \sum_{i=0}^n \frac{\partial{(\boldsymbol{x_i-u})^T\boldsymbol{\Sigma}^{-1}(\boldsymbol{x_i-u})}}{\partial{\boldsymbol{u}}} \newline
&=\sum_{i=1}^n \boldsymbol{\Sigma^{-1}(x_i-u)} \newline
&=\boldsymbol{\Sigma^{-1} \sum_{i=1}^n (x_i-u)} \tag{7}
\end{aligned}
$$


由式\\((5),(6)\\)可得：


$$
\begin{aligned}
\frac{\partial{\ln{L(\boldsymbol{u},\boldsymbol{\Sigma})}}}{\partial{\boldsymbol{\Sigma}}}
    &=-\frac{n}{2} \frac{\partial{\ln|\boldsymbol{\Sigma}|}}{\partial{\boldsymbol{\Sigma}}}-\frac{1}{2} \sum_{i=0}^n \frac{\partial{(\boldsymbol{x_i-u})^T\boldsymbol{\Sigma}^{-1}(\boldsymbol{x_i-u})}}{\partial{\boldsymbol{\Sigma}}} \newline
    &=\frac{1}{2} [\boldsymbol{\sum_{i=0}^n (\Sigma^{-1}(x_i-u)(x_i-u)^T \Sigma^{-1}} -n\boldsymbol{\Sigma^{-1}})^T \newline
    &+ \boldsymbol{\sum_{i=0}^n (\Sigma^{-1}(x_i-u)(x_i-u)^T \Sigma^{-1}} -n\boldsymbol{\Sigma^{-1}}) \newline
    &-\boldsymbol{\sum_{i=0}^n (\Sigma^{-1}(x_i-u)(x_i-u)^T \Sigma^{-1}} -n \boldsymbol{\Sigma^{-1}) \circ E }] \newline
    &=\boldsymbol{\sum_{i=0}^n (\Sigma^{-1}(x_i-u)(x_i-u)^T \Sigma^{-1}} -n \boldsymbol{\Sigma^{-1})}
    -\frac{1}{2} \boldsymbol{\sum_{i=0}^n (\Sigma^{-1}(x_i-u)(x_i-u)^T \Sigma^{-1}} -n \boldsymbol{\Sigma^{-1}) \circ E } \tag{8}
    \end{aligned}
$$

令式\\((7)\\)等于\\(0\\)，左右两边同乘\\(\boldsymbol{\Sigma}^{-1}\\)，得\\(\hat{\boldsymbol{\mu}}=\sum_{i=0}^n x_i=\bar{x}\\)，令式\\((8)\\)等于\\(\boldsymbol{0}\\)，并把\\(\hat{\boldsymbol{\mu}}\\)带入式\\((8)\\)，得\\(\boldsymbol{\hat{\Sigma}} =\frac{1}{n} \sum\_{i=1}^n (\boldsymbol{x}\_i-\boldsymbol{\bar{x}})(\boldsymbol{x}\_i-\boldsymbol{\bar{x}})^T=\frac{1}{n} \sum\_{i=1}^n (x\_i-\hat{\boldsymbol{\mu}})(x\_i-\hat{\boldsymbol{\mu}})^T\\)。综上，多元正态分布的极大似然估计值\\(\hat{\boldsymbol{\mu}}\\)为样本的矩阵，而\\(\boldsymbol{\hat{\Sigma}}\\)为样本的协方差矩阵。




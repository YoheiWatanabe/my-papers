# テスト中心主義(2)

[:contents]

## 概要

この記事では、テスト中心主義(Test-centrism)を圏論的に形式化する。テスト列を対象とする圏を構成し、対象の振る舞いは反変関手

$$
F_T : \mathcal{X}^{op} \to \mathbf{Set}
$$

として表される。このとき対象の意味はpresheafとして与えられ、Test-Centrism圏

$$
\mathbf{TC} = \mathbf{Set}^{\mathcal{X}^{op}}
$$

はpresheafトポスとなる。

このトポスの内部論理は直観主義論理であり、さらにKripke意味論として解釈できる。そこではテスト列が世界に対応し、真理はテスト拡張に対して安定な性質として理解される。

本稿の枠組みにより、

- 概念(実践的意味)
- プログラム(計算的対象)
- 科学理論(予測体系)

がすべて同一の構造、すなわち「テストに対する応答」として統一的に記述できることを示す。

## 1. 圏論での定式化

### 公理1. テスト圏

テスト圏

$$
\mathcal{X}
$$

を次のように定義する。

- 対象

```text
finite test sequences
```

$$
\mathbb{X} = ((i_1,o_1),\dots,(i_n,o_n))
$$

ここで、$i_k \in I$ であり、$o_k \in O \cup \{\bot\}$ である。

- 射

$$
\mathbb{X} \to \mathbb{Y}
$$

は

```text
prefix extension
```

つまり

$$
\mathbb{X} \preceq \mathbb{Y}
$$

である($\mathbb{X}$ が $\mathbb{Y}$ の前半部分列)。

これは

```text
テストが順序付きで増える
```

ことを意味する。

### 公理2. 振る舞い関手

対象 $T \in\mathcal{T}$ に対して振る舞い関手

$$
F_T : \mathcal{X}^{op} \to \mathbf{Set}
$$

を定義する。

$$
F_T(\mathbb{X})= \{ f: inputs(\mathbb{X}) \to O\mid f(i) = \text{behavior}_T(i) \}
$$

これはテスト列上での振る舞いのグラフである。

- 射に対する作用

$$
\mathbb{X} \preceq \mathbb{Y}
$$

に対して

```text
restriction(制限写像)
```

これは

```text
テストが増えるほど観測される振る舞いが増える
```

ことを意味する。

### 公理3. 意味

対象 $T \in \mathcal{T}$ の圏論的意味は

$$
\text{Meaning}(T)=F_T
$$

である。

つまり

```text
meaning = behavior presheaf
```

### 公理4. 識別同値

対象 $T,S \in \mathcal{T}$ が識別同値であるとは

$$
F_T = F_S
$$

であることをいう。

つまり

$$
\forall i \in I,\quad
\text{behavior}_T(i) = \text{behavior}_S(i)
$$

これは

```text
すべてのテストに対して区別できない
```

ことを意味する。

### 公理5. 検証

対象 $T \in \mathcal{T}$ がテスト列 $\mathbb{X}$ を満たすとは

$$
T \vDash \mathbb{X}
$$

と書き、

$$
o_k \neq \bot \Rightarrow
\text{behavior}_T(i_k) = o_k
$$

を満たすこととする。

これは

```text
観測があるテストのみ一致を要求する
```

ことを意味する。

### 公理6. Test-Centrism圏

Test-Centrism圏を

$$
\mathbf{TC} = \mathbf{Set}^{\mathcal{X}^{op}}
$$

と定義する。

これは

```text
presheaf topos
```

である。

### 7. Test-CentrismでのYonedaの定理

Yonedaの補題より

$$
\text{Nat}(y(\mathbb{X}), F_T) \cong F_T(\mathbb{X})
$$

が成り立つ。

ここで、$y(\mathbb{X}) = \text{Hom}(-,\mathbb{X})$ であり、$\text{Nat}$ は自然変換の集合である。

#### 定理

対象 $T$ はその振る舞い関手 $F_T$ によって完全に決定される。すなわち

$$
F_T = F_S
\iff
T \sim S
\iff
\forall i \in I,\quad
\text{behavior}_T(i) = \text{behavior}_S(i)
$$

これは

```text
対象 = テスト応答の総体
```

であることを意味する。

### 8. 理解の圏論的解釈

対象 $T \in \mathcal{T}$ をテスト列 $\mathbb{X}$ に関して理解するとは、

$$
F_T(\mathbb{X})
$$

を与えることである。これは

```text
テスト列に対する応答を決定できる
```

ことを意味する。

## 2. トポスの内部論理

Test-Centrism圏
$$
\mathbf{TC} = \mathbf{Set}^{\mathcal{X}^{op}}
$$
はpresheafトポスである。したがって内部論理は**直観主義論理**である。

### 2.1 真理値対象

真理値対象
$$
\Omega
$$
はsubobject classifierである。

presheafトポスでは

$$
\Omega(\mathbb{X})
$$
は

```text
𝕏上のsieve
```

である。

### 2.2 sieveの意味

ここで sieve とは

```text
𝕏に入る射の集合
```

であり、ここでは

```text
𝕏のprefix(部分テスト列)の集合
```

に対応する。さらにsieveは

```text
prefixに関して閉じている
(sieve = future-closed)
```

すなわち

```text
あるテスト列で成り立つなら
それ以前のテストでも成り立つ
```

### 2.3 命題の意味

命題 $P$ の真理値は

$$
\Omega(\mathbb{X})
$$

の元、すなわちsieveである。

これは

```text
Pが成立するだけでなく
その後のすべての拡張でも成立する集合
```

を意味する。

ただし重要なのは

```text
テストの拡張に対して安定
```

であることである。

### 2.4 真理の意味

命題 $P$ がテスト列 $\mathbb{X}$ において真であるとは

```text
𝕏を含むsieveに属する
```

ことである。

これは

```text
Pは𝕏で成立し
かつその後のテスト拡張でも崩れない
```

ことを意味する。

### 2.5 論理結合子

#### 2.5.1 AND(論理積)

$$
P \wedge Q
$$

```text
両方の条件を満たすテスト列の共通部分
```

#### 2.5.2 OR(論理和)

$$
P \vee Q
$$

```text
P ∨ Q は、現在のテスト列において
P または Q が成立すること
```

ここでは単なる「どちらかが成り立つ」ではなく、拡張で保証される必要がある。

#### 2.5.3 含意

$$
P \Rightarrow Q
$$

```text
任意のテスト拡張において
Pが成り立つならQも成り立つ
```

これは非常に重要で

```text
安定な推論
```

を意味する。

#### 2.5.4 否定

$$
\neg P
$$

とは

$$
P \Rightarrow \bot
$$

であり

```text
どのテスト拡張においても
Pが成立しない
```

ことを意味する。

### 2.6 排中律が成立しない理由

一般に

$$
P \vee \neg P
$$

は成立しない。

理由:

```text
まだ十分なテストが行われていない状態
```

が存在するためである。

つまり

```text
Pも¬Pも確定していない
```

これは

```text
科学的探究の途中状態
```

に対応する。

### 2.7 哲学的解釈

テスト中心主義の内部論理は

```text
テスト依存的直観主義論理
```

である。

ここでは

- 真理 = すべての将来のテストにおいても崩れない成立
- 命題 = テスト列に依存する性質

となる。

### 2.8 科学哲学との対応

この構造は

- Karl Popperの反証主義
- Charles Sanders Peirceのプラグマティズム

と一致する。

特に

```text
否定 = 反証可能性
```

という解釈が成立する。

- テスト列 = 知識の蓄積
- 拡張 = 実験の追加
- 安定性 = 反証されない

## 3. Kripke意味論

Test-centrismの内部論理は、**Kripke意味論**としても解釈できる。

### 3.1 Kripkeフレーム

Kripkeフレームを

$$
(\mathcal{X}, \preceq)
$$

とする。

- 世界：テスト列 $\mathbb{X}$
- 到達関係：prefix関係 $\preceq$

```text
テストが拡張されるほど未来へ進む
```

### 3.2 強制関係(forcing)

命題 $P$ に対して

$$
\mathbb{X} \Vdash P
$$

を「$\mathbb{X}$ において $P$ が成立する」と定義する。

このとき重要な条件は

```text
単調性(monotonicity)
```

である。

$$
\mathbb{X} \preceq \mathbb{Y},\quad
\mathbb{X} \Vdash P
\Rightarrow
\mathbb{Y} \Vdash P
$$

つまり

```text
一度成立した命題は
テストが増えても崩れない
```

### 3.3 論理結合子

Kripke意味論では論理は次のように解釈される。

#### 3.3.1 AND(論理積)

$$
\mathbb{X} \Vdash P \wedge Q
\iff
\mathbb{X} \Vdash P \,\,\text{and}\,\, \mathbb{X} \Vdash Q
$$

#### 3.3.2 OR(論理和)

$$
\mathbb{X} \Vdash P \vee Q
$$

とは

```text
P ∨ Q は、現在のテスト列において
P または Q が成立する
```

ただし成立性は将来に対して安定である必要がある。

#### 3.3.3 含意

$$
\mathbb{X} \Vdash P \Rightarrow Q
$$

とは

$$
\forall \mathbb{Y} \succeq \mathbb{X},\quad
\mathbb{Y} \Vdash P \Rightarrow \mathbb{Y} \Vdash Q
$$

#### 3.3.4 否定

$$
\mathbb{X} \Vdash \neg P
$$

とは

$$
\forall \mathbb{Y} \succeq \mathbb{X},\quad
\mathbb{Y} \not\Vdash P
$$

### 3.4 トポスとの一致

このKripke意味論は、前節のトポス内部論理と一致する。

対応は次の通り

| トポス | Kripke |
| ----- | --------- |
| sieve | 上に閉じた真理集合 |
| 安定性 | 単調性 |
| 真理 | すべての拡張で成立 |

したがって

```text
Test-centrismは
presheafトポスとして定式化され
その内部論理はKripke意味論として解釈できる
```

である。

### 3.5 哲学的意味

この構造の意味は明確である。

```text
世界 = テストの進行状態
知識 = テストの蓄積
真理 = 将来のテストでも崩れない命題
```

これは

- 概念(実践的帰結)
- プログラム(テストの安定性)
- 科学理論(反証可能性)

を統一的に説明する。

## 結論

この記事では、テスト中心主義(Test-centrism)を圏論的に形式化した。圏論的には、テスト列の圏に対するpresheafとして対象の意味が与えられ、Test-Centrism圏はトポス構造を持つ。この内部論理は直観主義論理であり、Kripke意味論と一致する。そこでは

```text
真理 = テスト拡張に対して安定な成立
```

として理解される。

この視点から、従来異なる領域とされてきた次の対象が統一される:

- 概念: 状況に対する実践的効果
- ソフトウェア: テストに対する振る舞い
- 科学理論: 実験に対する予測

さらにこの理論は、

- Peirceのプラグマティズム
- Popperの反証主義

を共通の形式のもとに統合する。

最終的に、テスト中心主義は次の原理に要約される:

```text
意味 = テストへの応答
真理 = テストに対して安定な成立
理解 = テストに応答できる能力
```

したがってテストとは、単なるソフトウェア開発の技法ではなく、対象を理解し、意味を与え、理論を評価するための**一般的な認識の枠組み**である。

## おわりに

- 今回はテスト中心主義の圏論の定式化をおこなった。
- 圏論の定式化はまだ理解できるが、トポス理論に関してはほとんどわからず、したがってAIの指示するままに書いた。この内容が正しいのかほとんど判断できない。改めてトポス理論を勉強しなければならない。前回の記事と今回の記事を1つの英語の論文にして、それを教授にメールしてみる。

<!-- markdownlint-disable MD033 -->
<br><br><br><br><br>
僕から以上
<!-- markdownlint-enable MD033 -->

## 改訂記録

### 1

- 2026/03/23 (Mon)
- 新規作成
- [この記事のリンク](https://github.com/YoheiWatanabe/my-papers/blob/main/philosophy/test-centrism/02/paper/jp/paper.md)

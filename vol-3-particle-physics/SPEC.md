# SPEC — 第三卷 · 粒子物理 单篇文章规范

> 复用规范, 用法同第一卷的 SPEC.md.
> **风格、读者假设、口气都与第一卷一致** — 从一个能观察到的现象或一个具体问题出发, 第一性原理推到一个具体的数字或公式. 但本卷新增一条要求: 每篇必须把一个被频繁引用却很少被认真讲清楚的 *cliché 概念* 严格地推一遍 — 例如路径积分 $\int\!\mathcal D\phi\,e^{iS/\hbar}$ 怎么从 Schrödinger 方程出来, Noether 定理的真正证明, 重整化"吸收发散"在做什么事, Higgs 机制破的是哪个对称, 5σ 显著性凭什么是 5...

---

## 1 · 风格 (与第一卷一致)

### 1.1 结构

1. **标题** — 一个具体问题 + `?`
2. **副标题** — `—— ` + 本节用的物理 / 数学
3. **摘要 (.abstract)** — 一段路径描述
4. **开场** — 接日常观察 / 上一节 / 一个具体问题, 把问题摆在读者面前
5. **编号小节** (`一、` `二、` `三、` `四、`) — 描述性题目
6. **deepdive 小节** — 至少有一节把一个 *cliché 概念*严格地展开
7. **小结** — 与更大物理图景的连结

### 1.2 腔调 (与第一卷同)

- 第一性原理, 不挥手
- 自问自答
- 常识与方程并置
- 代入真实数字 (能标、寿命、截面、耦合)
- 公开讲方法论
- 结尾点连结 (BSM, GUT, 早期宇宙学, 凝聚态对偶...)

### 1.3 每篇必含

- [ ] 标题带问号, 副标题两个破折号
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号公式**
- [ ] **≥ 2 数字代入** (能标、寿命、截面、耦合)
- [ ] **专门 deepdive 一个 cliché 概念** — 严格推
- [ ] **≥ 1 极限/类比/特殊情况检验**
- [ ] **≥ 1 历史人物或里程碑** (Dirac, Feynman, Schwinger, Tomonaga, Yang-Mills, Glashow, Salam, Weinberg, 't Hooft, Wilson, Higgs, Anderson, Englert, Kobayashi-Maskawa...)
- [ ] **恰好 1 个图占位符** (Feynman 图、能谱、衰变图、对称破缺势...)
- [ ] 顶部和底部导航
- [ ] 不 inline CSS

### 1.4 长度

- 简体中文, MathJax 公式
- **3000-4000 中文字** (与第一卷同; 偏理论或带完整推导的可到 4500)

---

## 2 · HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 第三卷·粒子物理</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: {inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams'}, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>  <!-- 首篇 disabled -->
  <span class="chapter-title">第 {N} 节 / 30 · {PART_NAME} · 第三卷·粒子物理</span>
  <a href="{NEXT_FILE}">下一节 →</a>  <!-- 末篇 disabled -->
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要}</div>
  <p>{开场}</p>

  <h2>一、{...}</h2>
  ...

  <!-- 唯一图占位符 -->

  <h2>二、{通常这里 deepdive 一个 cliché 概念}</h2>
  ...

  <h2>三、{...}</h2>
  ...

  <h2>四、{数字代入 / 历史 / 极限}</h2>
  ...

  <div class="small-summary">
  <h4>小结</h4>
  <p>{连到 BSM 或更大图景}</p>
  <p style="text-align:right; color:#8b2f1a; margin-top:1em;">▲</p>
  </div>
</article>

<nav class="chapter-nav bottom">
  <a href="{PREV_FILE}">← 上一节</a>
  <span class="chapter-title"><a href="index.html">目录</a></span>
  <a href="{NEXT_FILE}">下一节 →</a>
</nav>

</body>
</html>
```

---

## 3 · 图占位符

同第一卷格式. Feynman 图建议用 `\usetikzlibrary{decorations.pathmorphing,decorations.markings,arrows.meta}` 配合 `snake` / `coil` / `wave` 装饰画粒子线.

---

## 4 · 命名与路径

- 目录: `vol-3-particle-physics/`
- 文件: `{NN}-{slug}.html` (NN = 01-30)
- 共享样式: `style.css`
- 编译产物: `build/`

---

## 5 · Topic Brief

```
=== 文件 ===
{绝对路径}

=== 位置 ===
N=N/30, PART=..., PREV=..., NEXT=...
BOOK_NAME = 第三卷·粒子物理

=== 标题 ===
TITLE: ... ?
SUBTITLE: —— ...

=== 物理 brief ===
- 核心论断 / 问题 / 观察
- 关键 Lagrangian / 对称 / 群论结构
- 关键计算或实验数字
- 极限 / 类比 / 历史

=== Cliché 概念 (必须严格 deepdive) ===
...

=== 图示 brief ===
...
```

---

## 6 · 禁止

- 不糊弄 cliché — 必须严格地推
- 不 inline CSS
- 字数不在 2800–4800 之间均不行
- 图占位符不要变成真图
- 一次只写一个文件

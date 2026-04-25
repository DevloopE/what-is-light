# SPEC — 第四卷 · 物理学的数学基础 单篇文章规范

> 复用规范, 与第一卷的写作口气保持一致 — 从一个具体的物理 (或日常) 问题出发, 第一性原理推导, 落到一个具体的公式或可计算的结果. 但本卷的主角不是物理而是它后面的数学.
>
> **不假设读者熟悉抽象代数、泛函分析等专业数学**. 每一节都从一个具体物理问题或简单几何例子起步, 自下而上地建立这门数学 — 同时也指出这门数学在第一/二/三卷里被怎么用.

---

## 1 · 风格 (与第一卷一致)

### 1.1 结构
1. **标题** — 一个具体问题 + `?` (e.g. "极限究竟是什么?", "Hilbert 空间凭什么是 QM 的舞台?")
2. **副标题** — `——` + 本节会用到的关键概念
3. **摘要 (.abstract)** — 一段路径描述: 本节从 X (物理观察 / 几何例子) 出发, 引入数学概念 Y, 严格定义并推一些性质 Z, 落回到一个具体例子或物理应用
4. **开场** — 接日常 / 上一节 / 一个具体的物理问题
5. **编号小节** (`一、` `二、` `三、` `四、`) — 描述性题目
6. **小结** — 这门数学在第一/二/三卷哪里出现, 以及它打开的更深一层

### 1.2 腔调
- **第一性原理, 不挥手**: 先给清晰定义, 再推性质, 再举例
- **从具体到抽象**: 先看一个例子 (e.g., 平面旋转), 再抽象化 (e.g., SO(2))
- **不假设专业背景**: 即使是常见名词 (Hilbert 空间、群、流形) 也在第一次出现时用具体例子带读者建立直觉
- **公开讲方法**: "我们先看 SO(2) 是因为它最简单 —— SO(3) 加上一维就复杂了"
- **代入具体数字 / 例子**: 至少一处具体计算 (积分、矩阵本征值、群元素验证)
- **历史**: 至少一位数学家 / 物理学家 (Cauchy, Riemann, Cartan, Hilbert, von Neumann, Dirac, ...) 与他们的动机

### 1.3 每篇必含 (checklist)
- [ ] 标题带问号, 副标题两个破折号起头
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号定义 / 公式 / 定理** (用 `(1)` `(2)` `(3)` 编号)
- [ ] **≥ 1 处具体计算或例子代入** (e.g., 计算一个具体积分, 求矩阵本征值, 验证群运算, 估算尺度)
- [ ] **≥ 1 处与物理的连结** — 这门数学在 vol-1/2/3 里是怎么用的
- [ ] **≥ 1 历史人物** (数学家或物理学家)
- [ ] **恰好 1 个图占位符** (TikZ 待渲染)
- [ ] 顶部和底部两条导航栏齐全, 首篇禁 PREV, 末篇禁 NEXT
- [ ] 不在 HTML 内 inline CSS, 只引 `style.css`

### 1.4 语言与长度
- 简体中文, 数学符号 LaTeX
- MathJax 行内 `$...$`, 行间 `$$...$$`
- **3000-4000 中文字** (与 Vol 1 一致; 偏概念多的篇可到 4500)

---

## 2 · HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 第四卷·物理学的数学基础</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: { inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams', macros: { slashed: ['{\\not{#1}}', 1], slash: ['{\\not{#1}}', 1], bra: ['\\langle{#1}|', 1], ket: ['|{#1}\\rangle', 1], braket: ['\\langle{#1}|{#2}\\rangle', 2], abs: ['\\left|{#1}\\right|', 1], norm: ['\\left\\|{#1}\\right\\|', 1], Tr: ['\\operatorname{Tr}', 0], Im: ['\\operatorname{Im}', 0], Re: ['\\operatorname{Re}', 0] } }, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>  <!-- 首篇 disabled -->
  <span class="chapter-title">第 {N} 节 / 30 · {PART_NAME} · 第四卷·物理学的数学基础</span>
  <a href="{NEXT_FILE}">下一节 →</a>  <!-- 末篇 disabled -->
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要}</div>
  <p>{开场: 物理动机或几何观察}</p>

  <h2>一、{...}</h2>
  ...
  <p>$$ \text{编号定义/公式 (1)} $$</p>

  <!-- 唯一图占位符 -->

  <h2>二、{...}</h2>
  ...

  <h2>三、{具体例子 / 计算}</h2>
  ...

  <h2>四、{物理回响 / 历史 / 极限}</h2>
  ...

  <div class="small-summary">
  <h4>小结</h4>
  <p>{小结: 这门数学打开了 vol-1/2/3 的什么}</p>
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

## 3 · 图占位符 (与第一卷同)

```html
<figure class="diagram-placeholder">
<div class="placeholder-box">
  <span class="tag">TikZ 待渲染</span>
  <h4>图 1 · {图题}</h4>
  <dl class="tikz-req">
    <dt>主题</dt><dd>...</dd>
    <dt>必含元素</dt><dd>...</dd>
    <dt>几何/示意精度</dt><dd>...</dd>
    <dt>标签与公式</dt><dd>...</dd>
    <dt>风格建议</dt><dd>...</dd>
  </dl>
</div>
<figcaption>图 1  ...</figcaption>
</figure>
```

---

## 4 · 命名与路径
- 目录: `vol-4-math-foundations/`
- 文件: `{NN}-{slug}.html` (NN = 01-30)
- 共享样式: `style.css`
- 编译产物: `build/`

---

## 5 · Topic Brief 格式

```
=== 文件 ===
{绝对路径}

=== 位置 ===
N=N/30, PART=..., PREV=..., NEXT=...
BOOK_NAME = 第四卷·物理学的数学基础

=== 标题 ===
TITLE: ... ?
SUBTITLE: —— ...

=== 物理动机 ===
{从一个具体物理 (或几何) 问题出发, 解释为什么需要这门数学}

=== 数学内容 ===
- 关键定义 / 定理 / 公式 (会编号)
- 推导路径
- 具体例子 / 数值代入

=== 物理回响 ===
{这门数学在 vol-1/2/3 里被怎么用 — 引用具体的章节标题或公式}

=== 历史 ===
{至少一位数学家或物理学家 + 年份}

=== 图示 brief ===
- 主题; 必含元素; 几何精度; 标签与公式; 风格建议
```

---

## 6 · 禁止
- 不假设读者已会抽象代数 / 泛函分析 / 微分几何 — 每个新概念都用具体例子建立直觉
- 不在 HTML inline CSS
- 字数不在 2800–4500 之间均不行
- 图占位符不要变成真图
- 一次只写一个文件

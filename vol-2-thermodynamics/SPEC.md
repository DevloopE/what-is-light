# SPEC — 第二卷 · 热力学与统计力学 单篇文章规范

> 复用规范, 用法同第一卷的 SPEC.md.
> **风格、读者假设、口气都与第一卷一致** — 从一个能观察到的现象或一个具体问题出发, 第一性原理推到一个具体的数字或公式. 但本卷新增一条要求: 每篇必须把一个被滥用却很少被认真讲清楚的 *cliché 概念* 严格地推一遍 — 例如熵的多种定义凭什么等价、配分函数 $\log Z$ 凭什么是热力学的全部、Legendre 变换究竟在做什么、临界指数为什么 universal、重整化群究竟做了什么事.

---

## 1 · 风格 (与第一卷一致)

### 1.1 结构

1. **标题** — 一个具体问题 + `?` (与第一卷同)
2. **副标题** — `—— ` + 本节用到的物理 / 数学
3. **摘要 (.abstract)** — 一段路径描述 ("本节从 X 出发, 推导 Y, 最终得到 Z")
4. **开场** — 接日常观察 / 上一节, 把问题摆在读者面前 (与第一卷同)
5. **编号小节** (`一、` `二、` `三、` `四、`) — 每节描述性题目
6. **deepdive 小节** — 至少有一节专门把一个 *cliché 概念*严格地展开 (从清晰定义/导出推到底, 不挥手)
7. **小结** — 与更大物理图景的连结

### 1.2 腔调 (与第一卷同)

- 第一性原理, 不挥手
- 自问自答: "为什么 X? 这是因为..."
- 常识与方程并置
- 代入真实数字
- 公开讲方法论
- 结尾点普适性

### 1.3 每篇必含

- [ ] 标题带问号, 副标题两个破折号
- [ ] 摘要不超过一段
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号公式** (`(1)` `(2)`)
- [ ] **≥ 2 数字代入或量级估算**
- [ ] **专门 deepdive 一个 cliché 概念** (从定义到关键性质严格推, 不糊弄)
- [ ] **≥ 1 极限/类比/特殊情况检验**
- [ ] **≥ 1 历史人物或里程碑** (Boltzmann, Gibbs, Onsager, Wilson, Jaynes, Bekenstein, Landauer...)
- [ ] **恰好 1 个图占位符** (TikZ 待渲染)
- [ ] 顶部和底部两条导航, 首篇禁 PREV, 末篇禁 NEXT
- [ ] 不在 HTML 内 inline CSS

### 1.4 长度

- 简体中文, MathJax 行内 `$...$` 行间 `$$...$$`
- **3000-4000 中文字** (与第一卷同; 偏数学的可到 4500)

---

## 2 · HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 第二卷·热力学与统计力学</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: {inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams'}, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>  <!-- 首篇 disabled -->
  <span class="chapter-title">第 {N} 节 / 30 · {PART_NAME} · 第二卷·热力学与统计力学</span>
  <a href="{NEXT_FILE}">下一节 →</a>  <!-- 末篇 disabled -->
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要}</div>
  <p>{开场: 日常观察 / 上一节承接}</p>

  <h2>一、{...}</h2>
  ...
  <p>$$ \text{公式 (1)} $$</p>

  <!-- 唯一图占位符 -->

  <h2>二、{通常这里 deepdive 一个 cliché 概念}</h2>
  ...

  <h2>三、{...}</h2>
  ...

  <h2>四、{数字代入 / 历史 / 极限}</h2>
  ...

  <div class="small-summary">
  <h4>小结</h4>
  <p>{连到大图景}</p>
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
    <dt>几何/数学精度</dt><dd>...</dd>
    <dt>标签与公式</dt><dd>...</dd>
    <dt>风格建议</dt><dd>...</dd>
  </dl>
</div>
<figcaption>图 1  ...</figcaption>
</figure>
```

---

## 4 · 命名与路径

- 目录: `vol-2-thermodynamics/`
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
BOOK_NAME = 第二卷·热力学与统计力学

=== 标题 ===
TITLE: ... ?
SUBTITLE: —— ...

=== 物理 brief ===
- 问题/观察
- 关键工具/公式
- 关键数字
- 极限/类比/历史

=== Cliché 概念 (必须严格 deepdive) ===
{一段, 描述本节要展开的核心概念}

=== 图示 brief ===
- 主题; 必含元素; 几何精度; 标签; 风格
```

---

## 6 · 禁止

- 不糊弄 cliché 概念 — 必须严格地推
- 不 inline CSS
- 字数不在 2800–4800 之间均不行
- 图占位符不要变成真图
- 一次只写一个文件

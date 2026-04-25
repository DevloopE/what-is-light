# SPEC — 第六卷 · 量子是什么? 单篇文章规范

> 与前 5 卷一致的写作口气. 从一个具体物理现象 (光电效应、Stern-Gerlach 分裂、Bell 不等式数据) 出发, 第一性原理, 落到一个能算出来的数字或公式. 本卷主角: 量子力学.
>
> **不假设读者懂量子力学**. 假设读者完成了 vol 1-5 (或同等水平) — 会基础 SR/GR、知道 Hilbert 空间名义、听过 Schrödinger 方程. 第四卷里 Hilbert 空间 / 自伴算符 / 谱定理 / Fourier 那几节是这一卷的数学根 (引用即可).

---

## 1 · 风格 (与前几卷一致)

### 1.1 结构
1. 标题 + `?`; 副标题 `——` + 关键概念
2. 摘要 (.abstract) — 一段路径
3. 开场 — 接日常或一个具体实验数据
4. 编号小节 (`一、` `二、` ...) — 描述性题目
5. 小结 — 在 QM / 量子信息 / 凝聚态 / 量子引力 更大图景中的位置

### 1.2 腔调
- 第一性原理, 不挥手
- 写下波函数, 写出算符, 代具体数字
- 例: 氢原子基态 -13.6 eV, Bell 关联 |⟨XY⟩| ≤ 2 (经典) vs 2√2 (量子), 退相干时间 ~10⁻²³ s for 1 cm⁻³ 空气分子
- 历史: Planck, Bohr, Schrödinger, Heisenberg, Dirac, Born, Pauli, Bell, Aspect, Feynman, Wheeler

### 1.3 每篇必含 (checklist)
- [ ] 标题带问号 (除非主题不适合疑问句)
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号公式 / 定理** (`(1)` `(2)` ...)
- [ ] **≥ 1 处具体计算或数字代入** (能级, 概率幅, 期望值, 散射截面...)
- [ ] **≥ 1 处与实验的连结** (Stern-Gerlach, 双缝, Aspect 1982 Bell, GHZ, 量子隐形传态, ...)
- [ ] **≥ 1 历史人物**
- [ ] **恰好 1 个图占位** — 见 §2.3
- [ ] 顶部和底部两条导航栏齐全 (首篇禁 PREV, 末篇禁 NEXT, 用 `<a class="disabled" href="#">`)
- [ ] 不在 HTML 内 inline CSS, 只引 `style.css`

### 1.4 长度
- 简体中文; LaTeX 数学; MathJax `$...$` 与 `$$...$$`
- **3000-4000 中文字** (概念多的可到 4500)

---

## 2 · HTML 骨架与图占位规则

### 2.1 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 第六卷·量子是什么?</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: { inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams', macros: { slashed: ['{\\not{#1}}', 1], slash: ['{\\not{#1}}', 1], bra: ['\\langle{#1}|', 1], ket: ['|{#1}\\rangle', 1], braket: ['\\langle{#1}|{#2}\\rangle', 2], abs: ['\\left|{#1}\\right|', 1], norm: ['\\left\\|{#1}\\right\\|', 1], Tr: ['\\operatorname{Tr}', 0], Im: ['\\operatorname{Im}', 0], Re: ['\\operatorname{Re}', 0] } }, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>
  <span class="chapter-title">第 {N} 节 / 30 · {PART_NAME} · 第六卷·量子是什么?</span>
  <a href="{NEXT_FILE}">下一节 →</a>
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要}</div>
  <p>{开场}</p>
  <h2>一、{...}</h2>
  ...
  <p>$$ \text{编号公式 (1)} $$</p>

  <!-- 图占位 — 不画图, 只留位置 + 简短描述 -->
  <figure class="diagram-stub">
    <div class="stub-box">[此处应有一张图: 简短描述图想表达什么]</div>
  </figure>

  <h2>二、...</h2> <h2>三、...</h2> <h2>四、...</h2>

  <div class="small-summary">
  <h4>小结</h4>
  <p>{...}</p>
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

### 2.2 图占位规则 (本卷专用)

**本卷只交付正文, 不渲染 TikZ.** 在最自然的位置放一个 `<figure class="diagram-stub">`, 内含一行说明 "[此处应有一张图: <短描述>]". 描述要具体到可以让后来者 (人或 agent) 直接照着画.

例:
```html
<figure class="diagram-stub">
  <div class="stub-box">[此处应有一张图: 双缝干涉图样 — 两个相干光源, 屏幕上呈条纹强度 cos²(πd sin θ/λ); 标注 d, λ, 第 0/±1/±2 级峰]</div>
</figure>
```

**不要写 .tex, 不要 tectonic, 不要 SVG**. SVG 会在另一轮统一补.

### 2.3 命名与路径
- 目录: `vol-6-quantum/`
- 文件: `{NN}-{slug}.html`
- 共享样式: `style.css`
- `build/` 留空 (留给后续渲染)

---

## 3 · Topic Brief (调度 agent 时使用)

```
=== 文件 ===
HTML: C:\...\vol-6-quantum\NN-slug.html

=== 位置 ===
N=N/30, PART=第 X 部分 · 名称, PREV=..., NEXT=..., BOOK_NAME=第六卷·量子是什么?

=== 标题 ===
TITLE: ...?
SUBTITLE: ——...

=== 物理 brief ===
- 现象 / 问题
- 关键机制 / 公式 (会编号)
- 关键数字
- 极限 / 历史

=== 图占位 brief ===
- 图想说的是什么 (一两句, 直接进 [此处应有一张图: ...])
```

---

## 4 · 禁止
- 不假设读者会 QM
- 不在 HTML inline CSS
- 字数 2800-4500 之外不行
- 本卷绝对不写 TikZ / 不调 tectonic
- 一次只写一篇

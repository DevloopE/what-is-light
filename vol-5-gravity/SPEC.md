# SPEC — 第五卷 · 引力是什么? 单篇文章规范

> 与前四卷一致的写作口气. 从一个具体的物理 (或日常) 现象出发, 第一性原理推导, 落到一个具体公式或可计算的数字. 本卷主角: 引力 / 弯曲时空 / 黑洞 / 宇宙学.
>
> **不假设读者懂广义相对论**. 假设读者具备本科物理水平 (会基础牛顿力学, 听过 SR, 模糊认得几个张量符号). 必要时回顾一下第四卷里的微积分 / 流形 / 度规 / 协变导数 (引用 vol-4 第 16–20 节即可).

---

## 1 · 风格

### 1.1 结构
1. **标题** — 一个具体问题 + `?` (e.g. "引力为什么不是一种力?", "时间真的会变快慢吗?")
2. **副标题** — `——` + 关键概念
3. **摘要 (.abstract)** — 一段路径描述: 本节从 X 出发, 引入概念 Y, 推到具体数字或公式 Z, 落回到一个测量或观测
4. **开场** — 接日常 / 上一节 / 一个具体物理问题
5. **编号小节** (`一、` `二、` `三、` `四、`) — 描述性题目
6. **小结** — 这件事在 GR / 黑洞 / 宇宙学 / 量子引力的更大图景中的位置

### 1.2 腔调
- **第一性原理, 不挥手**: 写下度规 / 写下方程 / 代具体数字
- **从具体到抽象**: 先看一个例子 (Pound-Rebka 落塔, GPS 误差, Mercury 进动), 再写出一般理论
- **公开讲方法**: "我们先看 Schwarzschild — 它最简单, Kerr 比它多一个旋转参数"
- **代入具体数字**: Sun 的 Schwarzschild 半径 ≈ 3 km, 地面引力红移 ≈ 1.09×10⁻¹⁶/m, GPS 修正 ≈ 38 μs/day, GW150914 应变 ≈ 10⁻²¹, M87* 阴影 ≈ 40 μas
- **历史**: 至少一位人物 (Einstein, Schwarzschild, Hilbert, Kerr, Hawking, Penrose, Eddington, Bondi, Misner, Wheeler...) 与他们的动机

### 1.3 每篇必含 (checklist)
- [ ] 标题带问号 (除非主题不适合疑问句), 副标题两个破折号起头
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号公式 / 定理** (用 `(1)` `(2)` `(3)` 编号)
- [ ] **≥ 1 处具体计算或数字代入** (估算 r_s, 算 Δν/ν, 计算 Mercury 进动, 求 Hawking 温度...)
- [ ] **≥ 1 处与实验 / 观测的连结** (Pound-Rebka, GPS, 1919 日食, LIGO, EHT, COBE, Planck...)
- [ ] **≥ 1 历史人物**
- [ ] **恰好 1 张图** — **直接渲染为 SVG**, 不留占位符 (见 §2.3 "图的规则")
- [ ] 顶部和底部两条导航栏齐全, 首篇禁 PREV (`<a class="disabled" href="#">`), 末篇禁 NEXT
- [ ] 不在 HTML 内 inline CSS, 只引 `style.css`

### 1.4 语言与长度
- 简体中文, 数学符号 LaTeX
- MathJax 行内 `$...$`, 行间 `$$...$$`
- **3000-4000 中文字** (偏概念多的篇可到 4500)

---

## 2 · HTML 骨架与图的规则

### 2.1 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 第五卷·引力是什么?</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: { inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams', macros: { slashed: ['{\\not{#1}}', 1], slash: ['{\\not{#1}}', 1], bra: ['\\langle{#1}|', 1], ket: ['|{#1}\\rangle', 1], braket: ['\\langle{#1}|{#2}\\rangle', 2], abs: ['\\left|{#1}\\right|', 1], norm: ['\\left\\|{#1}\\right\\|', 1], Tr: ['\\operatorname{Tr}', 0], Im: ['\\operatorname{Im}', 0], Re: ['\\operatorname{Re}', 0] } }, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>  <!-- 首篇 → <a class="disabled" href="#">← 上一节</a> -->
  <span class="chapter-title">第 {N} 节 / 30 · {PART_NAME} · 第五卷·引力是什么?</span>
  <a href="{NEXT_FILE}">下一节 →</a>  <!-- 末篇 → <a class="disabled" href="#">下一节 →</a> -->
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要}</div>
  <p>{开场}</p>

  <h2>一、{...}</h2>
  ...
  <p>$$ \text{编号公式 (1)} $$</p>

  <!-- 图: 真实 <img>, 不留占位符 -->
  <figure class="diagram">
    <img src="build/{NN}.svg" alt="..." style="max-width:100%;height:auto;background:#fff;border:1px solid #c9c3b5;padding:8px;border-radius:4px;">
    <figcaption>图 1  ...</figcaption>
  </figure>

  <h2>二、...</h2>  <h2>三、...</h2>  <h2>四、...</h2>

  <div class="small-summary">
  <h4>小结</h4>
  <p>{小结}</p>
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

### 2.2 图的规则 — **不留占位符 (硬性)**

**每篇文章交付时, 图必须已经渲染为 SVG, HTML 里直接是 `<figure class="diagram"><img src="build/NN.svg" ...></figure>`. 禁止 `<figure class="diagram-placeholder">` 占位符块.** 流程见 §2.3.

### 2.3 写文章 + 渲染图的端到端流程

每篇文章一个 agent 闭环完成:

1. 写 HTML 正文 (按 §2.1 骨架).
2. 写 `build/NN.tex`:
   ```latex
   \documentclass[tikz,border=8pt]{standalone}
   \usepackage{amsmath,amssymb}
   \usetikzlibrary{arrows.meta,calc,decorations.markings,decorations.pathmorphing,patterns,shapes.geometric,positioning}
   \begin{document}
   \begin{tikzpicture}[>=Latex]
     ...  % 英文+LaTeX 数学标签, 不用中文 (避免 xeCJK)
   \end{tikzpicture}
   \end{document}
   ```
3. 编译: `"C:/Users/Devlo/bin/tectonic.exe" -X compile build/NN.tex --outdir build/`. 失败 → 读 stderr, 修语法重试.
4. PDF → SVG: `python "C:/Users/Devlo/Desktop/book/pdf_to_svg.py" build/NN.pdf build/NN.svg`.
5. 验收: 确认 `build/NN.svg` 存在, HTML 里 `<img src="build/NN.svg">` 已就位.

### 2.4 已知 TikZ 坑
- `step` / `vstep` 不可作 TikZ style 名 (与 `grid` 的 `step=...` 关键字冲突), 改 `rung` / 类似.
- 中文字符不要写进 .tex (会触发 xeCJK 依赖).
- `\slashed{...}` 在 amsmath 下需 slashed 宏包, 避免使用; 用 `\not{...}` 代替.
- `\pgfmathsetmacro` 算术超 16383pt → 拆成小步.

---

## 3 · 命名与路径
- 目录: `vol-5-gravity/`
- 文件: `{NN}-{slug}.html`, NN = 01-30
- 共享样式: `style.css`
- 编译产物: `build/NN.tex`, `build/NN.pdf`, `build/NN.svg`

---

## 4 · Topic Brief 格式 (调度 agent 时使用)

```
=== 文件 ===
HTML: C:\Users\Devlo\Desktop\book\light-book\vol-5-gravity\NN-slug.html
TeX : C:\Users\Devlo\Desktop\book\light-book\vol-5-gravity\build\NN.tex
PDF/SVG: 同 build/

=== 位置 ===
N=N/30, PART=第 X 部分 · 名称
PREV=PP-prev.html / NEXT=MM-next.html (首末篇用 disabled)
BOOK_NAME = 第五卷·引力是什么?

=== 标题 ===
TITLE: 一个具体问题 ?
SUBTITLE: —— 用到的物理

=== 物理 brief ===
- 现象 / 问题
- 关键机制 (2–4 条)
- 关键公式 (会编号)
- 关键数字
- 极限 / 类比 / 历史

=== 图示 brief ===
- 主题: ...
- 必含元素: ...
- 几何精度: ...
- 标签 (英文 + LaTeX 数学): ...
- 风格建议: ...
```

---

## 5 · 禁止
- 不假设读者已会 GR — 每个新概念都用具体例子建立直觉
- 不在 HTML inline CSS
- 字数不在 2800–4500 之间均不行
- **绝对禁止 `<figure class="diagram-placeholder">` 占位符** — 必须当场渲染
- 一次只写一篇文章

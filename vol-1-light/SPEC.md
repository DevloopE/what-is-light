# SPEC — 《光是什么?》单篇文章规范 (reusable)

> Reusable spec for writing a single article in this book's style. When dispatched, you receive only a topic brief. Everything about style, structure, HTML skeleton, CSS, and diagram-placeholder format lives here. Read this first, then follow the brief.

---

## 1 · 风格

### 1.1 结构模板
1. **标题** = 一个具体问题 + "?"
2. **副标题** = `—— ` + 本节用到的物理
3. **摘要 (.abstract)** = 一段"本节从 X 出发, 推导 Y, 最终得到 Z"的路径
4. **开场** = 接上一节 / 引日常观察 / 把问题摆在读者面前
5. **编号小节** = `一、` `二、` `三、` `四、` 编号, 每节带描述性题目
6. **小结 (.small-summary)** = 点出与更大物理图景的连结
7. **结束符** = 居右红色 `▲`

### 1.2 腔调
- **第一性原理, 不挥手**: 从基本定律一步步推
- **自问自答**: "为什么 X? 这是因为..."
- **常识与方程并置**
- **代入真实数字**: 每篇至少做一次具体估算到一个数
- **公开讲方法论**: "这里我们选择 X, 因为..."
- **结尾点普适性**: 把当前结果连到更深的物理

### 1.3 每篇必含 (checklist)
- [ ] 标题带问号, 副标题两个破折号起头
- [ ] 摘要不超过一段, 描述推导路径
- [ ] **≥ 4 个编号小节** (扩展后的篇幅需要更充实的展开: 一、二、三、四)
- [ ] **≥ 2 个编号公式** (`(1)` `(2)` `(3)`)
- [ ] **≥ 2 处代入真实数字**到具体答案
- [ ] **≥ 1 处极限/类比/特殊情况检验**
- [ ] **恰好 1 个图示占位符** (见第 3 节, 不渲染真图)
- [ ] **历史/名人典故至少一处** (Fermat, Huygens, Maxwell, Einstein, ...)
- [ ] **小结点出本节在"光是什么"这一大问题上的贡献**, 并暗示下一节
- [ ] 顶部和底部两条导航栏, 首篇禁 PREV 末篇禁 NEXT
- [ ] 不在 HTML 内复写 CSS, 只引 `style.css`

### 1.4 语言与长度
- 简体中文
- 公式用 MathJax: 行内 `$...$`, 行间 `$$...$$`
- **篇幅: 约 3000-4000 中文字** (比短章节的 1800-2200 扩展 50-100%; 深度话题可到 4200 字)

---

## 2 · HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · 光是什么?</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: {inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams'}, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>  <!-- 首篇改 <a class="disabled" href="#">← 上一节</a> -->
  <span class="chapter-title">第 {N} 节 / 20 · {PART_NAME} · 光是什么?</span>
  <a href="{NEXT_FILE}">下一节 →</a>  <!-- 末篇改 disabled 同上 -->
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>

  <div class="abstract">{摘要 — 推导路径一段}</div>

  <p>{开场: 日常观察 / 上一节承接 / 问题提出}</p>
  <!-- 可再接 1-2 段引入 -->

  <h2>一、{第一节}</h2>
  <p>{推导 / 说明}</p>
  <p>$$ \text{编号公式 (1)} $$</p>
  <!-- 唯一的图示占位符, 放在最合适的节中 -->

  <h2>二、{第二节}</h2>
  ...

  <h2>三、{第三节}</h2>
  ...

  <h2>四、{第四节 — 数值代入 / 极限检验 / 历史连接}</h2>
  ...

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

---

## 3 · 图示占位符格式

```html
<figure class="diagram-placeholder">
<div class="placeholder-box">
  <span class="tag">TikZ 待渲染</span>
  <h4>图 1 · {图题}</h4>
  <dl class="tikz-req">
    <dt>主题</dt><dd>{what the diagram shows}</dd>
    <dt>必含元素</dt><dd>{elements, each enumerated clearly}</dd>
    <dt>几何精度</dt><dd>{angles, ratios, alignments}</dd>
    <dt>标签与公式</dt><dd>{text labels, LaTeX formulas}</dd>
    <dt>风格建议</dt><dd>{color, line weight, typography}</dd>
  </dl>
</div>
<figcaption>图 1  {full caption}</figcaption>
</figure>
```

**只放占位符, 不渲染真图.**

---

## 4 · 可用 CSS 类 (见 `style.css`)

`.chapter-nav.top/.bottom`, `.chapter-nav a.disabled`, `h1 + .sub`, `.abstract`, `<h2>` (带边框), `<h3>`, `.small-summary h4`, `.placeholder-box`, `.tag`, `.tikz-req dt/dd`, `blockquote`, `table`, `hr`, `ol/ul`.

不在 HTML 里 inline 写 CSS.

---

## 5 · 命名与路径
- 目录: `C:\Users\Devlo\Desktop\book\light-book\`
- 文件名: `{NN}-{slug}.html` (`NN` = 01..20)
- 目录页: `index.html`, 使用 `.toc` class
- 共享样式: `style.css`

---

## 6 · Topic Brief 格式

Agent 调用时会收到以下结构的 topic brief:
```
=== 文件 ===
输出: {absolute path}

=== 位置 ===
N / 20, PART={part name}, PREV_FILE, NEXT_FILE (或 "disabled")
BOOK_NAME = 光是什么?

=== 标题 ===
TITLE (带 ?)
SUBTITLE (—— 本节用的物理)

=== 物理 brief ===
- 问题 / 观察
- 关键机制 (2-4 条)
- 推导路径 / 关键公式
- 关键数字 → 目标结果
- 极限/类比/历史检验

=== 图示 brief ===
- 主题; 必含元素; 几何精度; 标签与公式; 风格建议
```

---

## 7 · 禁止事项

- 不要渲染真图 — 只占位符
- 不要在 HTML 中 inline CSS
- 不要漏: 编号公式、数字代入、极限检验、历史典故、小结
- 不要输出多个文件 — 一次调用一个
- 不要短于 2700 中文字, 也不要超过 4500 字

---

## 8 · 自校

落盘前对着 1.3 checklist 逐条确认, 尤其:
1. ≥ 4 节, ≥ 2 公式, ≥ 2 数字估算
2. 1 个图示占位符, 不含真 SVG
3. 1 处极限检验
4. 1 处历史/名人典故
5. 小结明确联系"光是什么"这个大问题

—— end —

# PIPELINE — DevCollection 写作与渲染流水线

> 给接手的 agent 看的"操作手册". 描述本仓库完整的写作 → 编译 → 部署链路, 并列出常见踩坑与对应修复脚本. 读完就能直接动手.

---

## 0 · 仓库结构

```
DevCollection/                       (GitHub repo, 部署在 GitHub Pages)
├── README.md                        (collection-level overview)
├── PIPELINE.md                      (this file)
├── index.html                       (collection TOC, 列出 vols)
├── fix_math.py                      (utility: escape <,>,<= in math)
├── add_macros.py                    (utility: register MathJax macros)
├── pdf_to_svg.py                    (utility: PyMuPDF wrapper)
└── vol-N-{slug}/                    (each volume)
    ├── SPEC.md                      (per-volume writing spec)
    ├── style.css                    (shared per-volume styles)
    ├── index.html                   (volume TOC)
    ├── NN-slug.html                 (articles, NN = 01..N)
    └── build/                       (TikZ outputs)
        ├── NN.tex                   (sources)
        ├── NN.pdf                   (compiled)
        └── NN.svg                   (browser-embeddable)
```

**One volume = one folder.** Each volume's `SPEC.md` defines its writing style; reusing the SPEC keeps voice consistent across articles.

---

## 1 · 三种最常见的任务

### Task A — 新增一卷 (Volume N)

1. `mkdir vol-N-{slug}/build/`
2. `cp vol-1-light/style.css vol-N-{slug}/style.css`
3. Write `vol-N-{slug}/SPEC.md` — adapt from existing SPEC, change BOOK_NAME and topic flavor. Keep the structure / checklist / HTML skeleton sections intact.
4. Write `vol-N-{slug}/index.html` — TOC with parts and N article links (clone from an existing volume's index, edit titles).
5. Update root `index.html` and `README.md` to list the new volume.
6. Pick **all article topics + cliché concept + diagram brief** in one go (Vol-1 used 40, Vols 2/3 used 30 — 5 articles per part is a clean unit).
7. Dispatch agents (see Task B).

### Task B — 写文章 (single agent dispatch)

Each agent gets a **topic brief**. Keep prompts thin (~600-1000 chars) by referencing the SPEC.md. Template:

```
Read C:\...\vol-N-{slug}\SPEC.md, then write ONE article per spec.

=== 文件 ===
输出: C:\...\vol-N-{slug}\NN-slug.html

=== 位置 ===
N=N/TOTAL, PART=第 X 部分 · 名称
PREV=PP-prev.html (or "disabled" for 首篇 — use <a class="disabled" href="#">)
NEXT=MM-next.html (or "disabled" for 末篇)
BOOK_NAME = 第 N 卷 · 名称

=== 标题 ===
TITLE: 一个具体问题 + ?
SUBTITLE: —— 本节用的物理

=== 物理 brief ===
- 现象 / 问题
- 关键机制 (2-4 条)
- 关键公式 (会编号)
- 关键数字 → 目标答案
- 极限 / 类比 / 历史检验

=== Cliché 概念 (必须严格 deepdive, 仅 Vol 2+) ===
{被滥用却很少讲清的那个概念, 例如 entropy from microstates / Legendre / RG / Noether / renormalization}

=== 图示 brief ===
- 主题: ...
- 必含元素: (逐条)
- 几何精度: ...
- 标签与公式: ...
- 风格建议: ...

写 3000-4000 字, 4+ 节, ≥2 编号公式, ≥2 数字估算, ≥1 极限, ≥1 历史, 恰 1 占位符. 报 < 30 字.
```

**Dispatch in parallel.** 30 in one message has been tested and works. 40 also works. 60 in one message is risky; split if possible.

### Task C — 渲染 TikZ 图 (single agent dispatch)

Each article comes with a `<figure class="diagram-placeholder">` block listing TikZ requirements. To turn it into a real diagram:

```
Render TikZ diagram for article NN-slug.

1. Read C:\...\vol-N-{slug}\NN-slug.html; extract <figure class="diagram-placeholder"> tikz-req fields, H4 title, figcaption.
2. Write C:\...\vol-N-{slug}\build\NN.tex:
   \documentclass[tikz,border=8pt]{standalone}
   \usepackage{amsmath,amssymb}
   \usetikzlibrary{arrows.meta,calc,decorations.pathreplacing,patterns,shapes.geometric,positioning,shadings,plotmarks,decorations.markings,decorations.pathmorphing}
   English+math labels only (NO Chinese — avoids xeCJK).
3. Compile: "C:/Users/Devlo/bin/tectonic.exe" -X compile "...build/NN.tex" --outdir "...build". Retry on errors (read tectonic log, fix syntax).
4. Convert PDF→SVG: python "C:/Users/Devlo/Desktop/book/pdf_to_svg.py" "...build/NN.pdf" "...build/NN.svg"
5. Edit article: replace ENTIRE <figure class="diagram-placeholder">...</figure> verbatim with:
<figure class="diagram"><img src="build/NN.svg" alt="[H4 TITLE]" style="max-width:100%;height:auto;background:#fff;border:1px solid #c9c3b5;padding:8px;border-radius:4px;"><figcaption>[ORIG FIGCAPTION]</figcaption></figure>

Report < 30 words.
```

Dispatch all article rendering agents in parallel. Each takes 1-3 min (first compile per machine pulls the TeX bundle).

---

## 2 · 工具与依赖

| 工具 | 用途 | 安装 |
|---|---|---|
| **tectonic** | LaTeX → PDF (单文件二进制, 自动拉包) | `winget install --id ...` 或下载 GitHub release; 路径 `C:/Users/Devlo/bin/tectonic.exe` |
| **PyMuPDF (fitz)** | PDF → SVG | `pip install pymupdf` |
| **gh CLI** | GitHub repo + Pages 操作 | `winget install GitHub.cli` |
| **Python 3.x** | 修复脚本 + PDF→SVG 包装 | 系统已装 |

PDF→SVG 脚本: `pdf_to_svg.py` (在 `C:/Users/Devlo/Desktop/book/`). 简单, 调用 `fitz.open(pdf).load_page(0).get_svg_image(text_as_path=True)`.

---

## 3 · HTML 骨架 (每篇文章必须长这样)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} · {BOOK_NAME}</title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: { inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams', macros: {
    slashed: ['{\\not{#1}}', 1], slash: ['{\\not{#1}}', 1],
    bra: ['\\langle{#1}|', 1], ket: ['|{#1}\\rangle', 1],
    braket: ['\\langle{#1}|{#2}\\rangle', 2],
    abs: ['\\left|{#1}\\right|', 1], norm: ['\\left\\|{#1}\\right\\|', 1],
    Tr: ['\\operatorname{Tr}', 0], Im: ['\\operatorname{Im}', 0], Re: ['\\operatorname{Re}', 0]
  } }, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="{PREV_FILE}">← 上一节</a>
  <span class="chapter-title">第 {N} 节 / {TOTAL} · {PART_NAME} · {BOOK_NAME}</span>
  <a href="{NEXT_FILE}">下一节 →</a>
</nav>

<article>
  <h1>{TITLE}</h1>
  <div class="sub">—— {SUBTITLE}</div>
  <div class="abstract">{摘要 一段路径}</div>
  <p>{开场}</p>

  <h2>一、...</h2>
  <p>...</p>
  <p>$$ \text{编号公式 (1)} $$</p>

  <!-- 图占位符放最自然的位置 -->
  <figure class="diagram-placeholder">
    <div class="placeholder-box">
      <span class="tag">TikZ 待渲染</span>
      <h4>图 1 · ...</h4>
      <dl class="tikz-req">
        <dt>主题</dt><dd>...</dd>
        <dt>必含元素</dt><dd>...</dd>
        <dt>几何精度</dt><dd>...</dd>
        <dt>标签与公式</dt><dd>...</dd>
        <dt>风格建议</dt><dd>...</dd>
      </dl>
    </div>
    <figcaption>图 1  ...</figcaption>
  </figure>

  <h2>二、...</h2>  <h2>三、...</h2>  <h2>四、...</h2>

  <div class="small-summary">
  <h4>小结</h4>
  <p>...</p>
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

**首篇:** PREV 改成 `<a class="disabled" href="#">← 上一节</a>`. **末篇:** NEXT 同样 disabled.

**volume `index.html` 也要加 MathJax** (否则 TOC 里的 `$...$` 显示成原文). 以及顶栏 BOOK_NAME 要带本卷名.

---

## 4 · 已知坑与修复脚本

### 坑 4.1 — `<` 和 `>` 在 `$...$` 里被 HTML 解析器吃掉

**症状**: 屏幕上出现 `$T0` (本应是 `$T<T_c$`) 之类残文; 后续 `$...$` 配对错乱.

**原因**: HTML 解析器看到 `<T_c$` 视作不规范 tag, 吃掉后续直到找到 `>` 或文本边界.

**修复**: 用 `\lt`, `\gt`, `\le`, `\ge`, `\ll`, `\gg` 替换 `<`, `>`, `<=`, `>=`, `<<`, `>>` (仅在 math 内).

```bash
python C:/Users/Devlo/Desktop/book/fix_math.py \
  C:/Users/Devlo/Desktop/book/light-book/vol-2-thermodynamics \
  C:/Users/Devlo/Desktop/book/light-book/vol-3-particle-physics
```

(`fix_math.py` 已在仓库内.)

### 坑 4.2 — `\slashed` 等 LaTeX 包命令在 MathJax 里没定义

**症状**: 红字显示 `\slashedk` 而非 Feynman 斜杠.

**修复**: 在 MathJax 配置里注册 macros (见上面 HTML 骨架). 用 `add_macros.py` 一次性更新所有文章的 config.

如发现新的未定义命令 (`\bra`, `\Tr`, ...), 直接在 macros 里加一项, 重跑 `add_macros.py`.

### 坑 4.3 — Volume `index.html` 没加 MathJax 导致标题里的 `$...$` 显示原文

**修复**: 在每个 volume 的 `index.html` `<head>` 中, `<link>` 后追加同样的 MathJax `<script>` 块 (见骨架). 已对所有现有 volume 修过.

### 坑 4.4 — Tectonic 首次编译网络不稳

**症状**: `failure fetching ... default_bundle_v33.tar`.

**修复**: 重试. 大部分包已在前一次部分下载到本地缓存, 第二次很快就能拿到剩下那个文件. 如多次失败检查 `https://relay.fullyjustified.net` 是否可访问.

### 坑 4.5 — TikZ 编译失败常见原因

- `\slashed` / `\boldmath` 等 — 改 `\not{}` / `\boldsymbol{}`
- 未声明 library — 把所有需要的塞进 `\usetikzlibrary{...}`: `arrows.meta, calc, decorations.pathreplacing, decorations.markings, decorations.pathmorphing, patterns, shapes.geometric, positioning, shadings, plotmarks`
- `\pgfmath` 算术超 16383pt — 把表达式拆小或先存到 `\pgfmathsetmacro`
- `\node at (a*b, c*d)` 直接写算术 — 改用括号 `(\x, {a*b})` 或 `\pgfmathsetmacro{\xv}{a*b}` 后用 `\xv`
- 中文字符 — 不要在 .tex 里写中文 (避免 xeCJK 依赖). 标签全用英文 + LaTeX 数学.

### 坑 4.6 — Windows 行尾警告 (无害)

`warning: in the working copy of '...html', LF will be replaced by CRLF` — git autocrlf 的常规警告, 文件正常工作, 忽略即可.

---

## 5 · Git / GitHub Pages 工作流

```bash
cd C:/Users/Devlo/Desktop/book/light-book
git add -A
git commit -m "..."
git push                            # 推到 main, GitHub Pages 自动重建
```

URL: `https://devloope.github.io/DevCollection/`. Pages CDN 缓存约 1-2 分钟. 强制刷新 `Ctrl+F5`.

如果 token 过期: `gh auth login -h github.com -p https -w` (interactive, 需要浏览器).

---

## 6 · 风格 (vol-1 一致, vol-2+ 加深)

详见每卷 `SPEC.md`. 核心要点重述:

- **标题** = 一个具体问题 + `?`
- **副标题** = `—— ` + 用到的物理
- **摘要** = 一段路径描述, 不是简介
- **开场** = 接日常观察 / 上一节 / 把问题摆在读者面前
- **小节** ≥ 4, 带描述性题目
- **小结** = 点出与更大物理图景的连结
- **每篇**: ≥ 2 编号公式 / ≥ 2 数字估算 / ≥ 1 极限检验 / ≥ 1 历史人物 / 1 个图占位符
- **vol-2+ 额外**: 严格 deepdive 一个 cliché 概念 (entropy / Legendre / RG / Noether / renormalization / Higgs SSB / ...)
- **不在 HTML inline CSS** — 只引 `style.css`

---

## 7 · 一次完整 cycle 的时序示意

```
T+0      mkdir vol-N + 写 SPEC.md + index.html
T+0:01   parallel dispatch N agents (每篇文章一个)
T+0:05   agents 陆续返回 (1-3 min/篇)
T+0:10   git add + commit + push (文章版)
T+0:11   parallel dispatch N agents (每幅图一个)
T+0:15   agents 陆续返回 (TeX 编译 + SVG)
T+0:25   git add + commit + push (图版)
T+0:27   GitHub Pages 重建完成, 访问 vol-N TOC 链接验收
```

如果某篇/某图编译失败, 单独修, 单 agent 重跑.

---

## 8 · 后续计划提示 (留给后来者参考)

可能的下一卷主题 (保持"一卷一个具体问题/领域"风格):

- 第四卷: 经典力学 / Lagrangian / Hamilton / 最小作用量
- 第五卷: 广义相对论 / 黑洞 / 宇宙学
- 第六卷: 凝聚态物理 / 拓扑相 / 超导
- 第七卷: 量子信息 / 量子计算
- 第八卷: 流体 / 非线性物理 / 混沌

每一卷重复 Task A → B → C 三步即可.

—— end of pipeline doc —

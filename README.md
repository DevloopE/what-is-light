# DevCollection

A collection of first-principles physics books. Each volume circles a single concrete question, and answers it from many angles — starting from an observable phenomenon, derived first-principles, landing on a specific number or formula.

## Volumes

| 卷 | 标题 | 主题 | 状态 |
|---|---|---|---|
| 第一卷 | [光是什么?](vol-1-light/) | 四十个角度的追问 (8 部分 × 5 节) | ✓ |
| 第二卷 | 运动是什么? | (规划中) | — |

## 阅读

直接打开 `vol-1-light/index.html` 进入第一卷, 或访问 GitHub Pages 部署:

- Collection: https://devloope.github.io/DevCollection/
- Volume 1: https://devloope.github.io/DevCollection/vol-1-light/

## 卷内结构 (示范, 适用于每一卷)

- `index.html` — 卷的目录
- `NN-slug.html` — 各节正文 (HTML + MathJax for LaTeX)
- `style.css` — 共享样式
- `SPEC.md` — 单篇文章的可复用规范 (口气、结构、HTML 骨架、图占位符格式)
- `build/` — TikZ 源 + 编译产物 (.tex / .pdf / .svg)

## 写作流程

每卷的写作遵循同一套 SPEC. 给定主题和图占位符, 一次只写/渲染一节:

1. 写正文 HTML (按 SPEC 中的口气与骨架)
2. 在文章中放入图占位符 (`<figure class="diagram-placeholder">` + 详细 TikZ 需求)
3. 渲染图: TikZ → tectonic 编译为 PDF → PyMuPDF 转 SVG → 用 `<img>` 替换占位符

每一步都可以独立 dispatch 给 agent 并行执行.

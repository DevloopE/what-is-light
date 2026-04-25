# DevCollection

A collection of first-principles physics books. Each volume circles a single concrete question, and answers it from many angles — starting from an observable phenomenon, derived first-principles, landing on a specific number or formula.

## Volumes

| 卷 | 标题 | 主题 | 节数 |
|---|---|---|---|
| 第一卷 | [光是什么?](vol-1-light/) | 几何 → 波动 → 能动量 → 量子 → 物质 → 信息 → 宇宙 → 生命 | 40 |
| 第二卷 | [热力学与统计力学](vol-2-thermodynamics/) | 热力学根基 → 统计力学核心 → 相变 → 量子统计 → 非平衡 → 信息与黑洞热力学 | 30 |
| 第三卷 | [粒子物理](vol-3-particle-physics/) | QFT 脚手架 → 对称与守恒 → 标准模型 → 计算与发散 → 实验与统计 → BSM | 30 |
| 第四卷 | [物理学的数学基础](vol-4-math-foundations/) | 微积分与向量分析 → 线性代数 → 群论 → 流形 → 函数空间 → 概率/复分析/路径积分 | 30 |
| 第五卷 | [引力是什么?](vol-5-gravity/) | 等效原理 → 弯曲时空 → Einstein 场方程 → 黑洞 → 宇宙学 → 检验与前沿 | 30 |
| 第六卷 | [量子是什么?](vol-6-quantum/) | 量子起源 → 量子力学语言 → 解谱 → 测量与诠释 → 多体与场 → 量子信息与前沿 | 30 |
| 第七卷 | [物质是什么?](vol-7-matter/) | 晶体与对称 → 电子在固体 → 强关联与磁性 → 超导与超流 → 拓扑相 → 软物质与涌现 | 30 |

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

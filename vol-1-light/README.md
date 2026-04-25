# 光是什么? — 四十个角度的追问 (第一卷)

一本围绕 "光是什么?" 的第一性原理物理书,共 40 节,分 8 部分. 每节从一个可观察的现象出发, 推到一个具体的数字或公式, 并附 TikZ 渲染的技术插图.

## 阅读

直接打开 `index.html` 即可 (或访问部署的 GitHub Pages 链接).

## 目录

- **第 1 部分 · 光线** (01-05): Fermat, Snell, rainbow, gravitational bending, Fresnel
- **第 2 部分 · 光波** (06-10): double-slit, single-slit, diffraction limit, polarization, laser
- **第 3 部分 · 速度/能量/动量** (11-15): c measurement, Maxwell c, phase vs group, radiation pressure, solar constant
- **第 4 部分 · 量子与热辐射** (16-20): photon random walk, blackbody, photoelectric, wave-particle duality, vacuum zero-point
- **第 5 部分 · 光与物质** (21-25): glass/metal, thin-film, grating, Compton, laser cooling
- **第 6 部分 · 光与信息** (26-30): fiber, WDM, LIDAR, holography, QKD
- **第 7 部分 · 光与宇宙** (31-35): redshift, lensing, gravitational redshift, CMB peaks, pulsars
- **第 8 部分 · 光与生命** (36-40): photosynthesis, single-photon eye, bee UV vision, bioluminescence, eye resolution

## 构成

- `index.html` — 目录
- `NN-slug.html` — 40 节正文 (MathJax for LaTeX, links to `style.css`)
- `style.css` — 共享样式
- `SPEC.md` — 单篇文章的可复用规范
- `build/` — TikZ 源文件 (.tex)、PDF 输出、SVG 插图

## 技术栈

- 文章: HTML + MathJax v3 (CDN)
- 插图: TikZ 源 → tectonic 编译为 PDF → PyMuPDF 转 SVG → HTML `<img>` 引用

# DevCollection

A collection of first-principles physics books. Each volume circles a concrete question, starts from observable phenomena, and works toward formulas, numbers, and experiments.

## Volumes

| 卷 | 标题 | English | 主题 | 节数 |
|---|---|---|---|---|
| 第一卷 | [光是什么?](vol-1-light/) | Light | 几何光学 → 波动 → 能量与动量 → 量子与热辐射 → 光与物质 → 光与信息 → 光与宇宙 → 光与生命 | 40 |
| 第二卷 | [热力学与统计力学](vol-2-thermodynamics/) | Thermodynamics | 热力学根基 → 统计力学核心 → 相变 → 量子统计 → 非平衡 → 信息与黑洞热力学 | 30 |
| 第三卷 | [粒子物理](vol-3-particle-physics/) | Particle Physics | QFT 脚手架 → 对称与守恒 → 标准模型 → 计算与发散 → 实验与统计 → BSM | 30 |
| 第四卷 | [物理学的数学基础](vol-4-math-foundations/) | Mathematical Foundations | 微积分与向量分析 → 线性代数 → 群论 → 流形与微分几何 → 函数空间 → 概率/复分析/路径积分 | 30 |
| 第五卷 | [引力是什么?](vol-5-gravity/) | Gravity | 等效原理 → 弯曲时空 → Einstein 场方程 → 黑洞 → 宇宙学 → 检验与前沿 | 30 |
| 第六卷 | [量子是什么?](vol-6-quantum/) | Quantum | 量子起源 → 量子力学语言 → 解释 → 测量与诡异 → 多体与场 → 量子信息与前沿 | 30 |
| 第七卷 | [物质是什么?](vol-7-matter/) | Matter | 晶体与对称性 → 电子在固体里 → 强关联与磁性 → 超导与超流 → 拓扑相 → 软物质与涌现 | 30 |
| 第八卷 | [流体是什么?](vol-8-fluids/) | Fluids | Reynolds 数 → Navier-Stokes → Bernoulli → 涡与不稳定 → 冲击波 → 湍流和天气 | 30 |
| 第九卷 | [声音是什么?](vol-9-sound/) | Sound | 声波方程 → 频谱与音色 → 共鸣与房间 → 超声/声呐 → Doppler → 回声消除 | 30 |
| 第十卷 | [颜色是什么?](vol-10-color/) | Color | 光谱 → 散射 → 色觉 → RGB/CMYK → 结构色/金属 → 荧光和植物 | 30 |
| 第十一卷 | [生命的物理](vol-11-physics-of-life/) | Physics of Life | 细胞尺度 → 扩散与低 Re → ATP 和分子机器 → 生物力学 → 神经与信息 → 标度律 | 30 |
| 第十二卷 | [看见是什么?](vol-12-seeing/) | Seeing | 眼球光学 → 视网膜与知觉 → 深度 → 显微镜极限 → 望远镜 → 成像与全息 | 30 |
| 第十三卷 | [运动是什么?](vol-13-motion/) | Motion | 运动学 → Newton 定律 → 能量/动量 → 转动/振动 → 轨道 → 作用量与混沌 | 30 |
| 第十四卷 | [天气是什么?](vol-14-weather/) | Weather | 辐射收支 → 对流与云 → Coriolis → Hadley 环流 → 风暴 → 气候和预报 | 30 |
| 第十五卷 | [音乐与数学](vol-15-music-math/) | Music and Math | 泛音列 → 音程与调律 → Fourier 与音色 → 乐器耦合 → 节奏/群 → 压缩与信号处理 | 30 |
| 第十六卷 | [能量是什么?](vol-16-energy/) | Energy | 功与守恒 → 热力学第一/第二定律 → 发动机/冰箱 → 电池与电网 → 生命能量 → 永动机失败 | 30 |
| 第十七卷 | [测量是什么?](vol-17-measurement/) | Measurement | SI 标准 → 时间和频率 → 长度/质量/电学 → 传感器 → 误差和噪声 → GPS/宇宙尺度 | 30 |

## Reading

Open `index.html` locally, or visit the GitHub Pages deployment:

- Collection: https://devloope.github.io/DevCollection/
- Volume 1: https://devloope.github.io/DevCollection/vol-1-light/

## Volume Structure

- `index.html` — collection or volume table of contents
- `NN-slug.html` — article body, with MathJax for LaTeX
- `style.css` — shared reading style with per-volume accent colors
- `SPEC.md` — reusable article specification
- `build/` — rendered diagram artifacts when a volume enters the TikZ/SVG pass

## Writing Workflow

Newer volumes currently ship with one detailed diagram placeholder per article, matching volumes 6-7. During a later rendering pass, replace each `<figure class="diagram-stub">` with a real SVG figure under `build/`.

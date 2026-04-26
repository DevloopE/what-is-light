# Vol 11 · 生命的物理 — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-11-physics-of-life/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

生命是一种远离平衡的稳态. 30 节按 6 部分:

1. 尺度与扩散: 细胞 1-10 μm 不是巧合; 扩散时间; 拥挤; 热涨落
2. 低 Reynolds 世界: 细菌怎么游, 鞭毛, 纤毛, 毛细血管, 黏液
3. 分子机器: ATP, 肌动蛋白, 离子泵, 光合作用, 酶, 蛋白折叠
4. 从单细胞到器官: 细胞骨架, 骨头标度, 鸟 V 队, 鱼群
5. 信号与神经: 动作电位, 突触, 视网膜, 听毛细胞, 大脑能量
6. 进化与起源: Kleiber, 体温, 形态发生, 鲁棒性, 生命起源

每节落到一个具体生物 (E. coli, 大肠杆菌, 蓝鲸, 神经元, 萤火虫) + 一个具体数 (μm, ms, ATP/s, mV) + 一位有名字的实验家.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "E. coli 长 2 μm, 鞭毛旋转 100 Hz, 在水里以 30 μm/s 游, $Re \sim 10^{-4}$ — 这跟人在沥青里走是一回事. 心脏一拍泵 70 mL 血, 一辈子拍 25 亿次. 一个突触在 1 ms 内放掉 10000 个神经递质分子. 蓝鲸 100 t, BMR 1500 W, 单位质量代谢比小鼠低 100 倍, 几乎完美贴合 Kleiber 1932 给的 $P \propto M^{3/4}$. 这一卷把生命的物理底线立起来: 为什么细胞要这么小, 为什么大象不能跳, 为什么 ATP 是 30.5 kJ/mol, 为什么动作电位 +40 mV. 终点是 Schrödinger 1944 *What is Life?* 那条暗线 — 生命是从环境取低熵以维持局部秩序."

---

## 30 节具体 brief

### 第 1 部分 · 尺度与扩散

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | cell-size | 哺乳动物细胞 10 μm, 细菌 1 μm; 神经元轴突最长 1 m | 扩散时间 $\tau = L^2/D$; $D \sim 10^{-9}$ m²/s 蛋白; 1 μm 用 1 ms, 1 mm 用 1000 s | Hooke 1665 cell 一词; Anton van Leeuwenhoek 1676 第一次看到细菌 | $\tau = L^2/(2D)$ 设上限 | 细胞尺寸 vs 扩散时间双对数图, 标神经元长度做对比 |
| 02 | diffusion | 红细胞内血红蛋白每秒 collide $10^{12}$ 次 | $D = k_B T/(6\pi \eta r)$; 蛋白 $r=2$ nm, $\eta = 10^{-3}$ Pa·s, $T = 310$ K → $D \approx 10^{-10}$ m²/s | Robert Brown 1827, Einstein 1905 (布朗运动 paper) | $\langle x^2 \rangle = 2 D t$ | 蛋白质在细胞质里的随机轨迹 + MSD ∝ t |
| 03 | membrane | 细胞膜双层磷脂厚度 ~5 nm | 介电常数 ~2 (类油), 电阻 $10^9\,\Omega\!\cdot\!\mathrm{cm^2}$, 电容 $1\,\mu\mathrm{F/cm^2}$ | Gorter & Grendel 1925 双层假说; Singer-Nicolson 1972 流体镶嵌模型 | 两性分子 self-assembly; lipid Langmuir trough | 双层结构 + 镶嵌蛋白 + 电学等效模型 |
| 04 | crowding | 细胞质蛋白浓度 200-400 mg/mL, 占体积 30-40% | macromolecular crowding 把扩散减慢 10× ; 反应速率提高 (excluded volume) | Fulton 1982 (cytoplasm crowding 概念) | excluded volume free energy → activity coeff > 1 | 拥挤 vs 稀释的细胞质对比 + 蛋白扩散迹 |
| 05 | thermal-noise-life | 离子通道单分子电流 ~1 pA, 信噪比与 $\sqrt N$ | $k_B T = 4.1 \times 10^{-21}\,\mathrm{J}$ at 310 K; ATP 水解 $\Delta G = 30.5$ kJ/mol = $\sim 12 k_B T$ | Berg 1977 鞭毛 SNR 论文 | $\sigma_{\rm thermal}^2 = 4 k_B T R \Delta f$ | $k_B T$ 对照 ATP, 光子能量, 共价键 |

### 第 2 部分 · 低 Reynolds 世界

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | low-re | E. coli 2 μm, 30 μm/s 游, Re = $6\times 10^{-5}$ | $\eta_{\rm water}/\rho \sim 10^{-6}$ m²/s; cell scale 完全 viscous-dominated | Edward M. Purcell 1977 *Life at Low Reynolds Number* (经典演讲) | scallop theorem: 时间反演对称下不能游 | 大鱼 vs 细菌 Re 对比 + 鞭毛轨迹 |
| 07 | bacterial-flagella | E. coli flagellum 直径 20 nm 长 10 μm, 100 Hz 螺旋旋转 | rotation 100 Hz × 2π → 600 rad/s; 螺距 2.5 μm | Howard Berg 1973 第一次记录 flagellar rotation; Berg & Brown 1972 chemotaxis | 螺旋 propulsion: $F = -A v$ 各向异性阻力 | 鞭毛旋转 + run-and-tumble 轨迹 |
| 08 | cilia | 气管纤毛 6 μm 长, 12 Hz 摆动, metachronal wave 沿气管 | clearance 速度 ~ 5 mm/min mucus; 哮喘患者降到 1 mm/min | Sleigh 1962 *Biology of Cilia and Flagella* | 9+2 微管轴丝 + dynein arm 步进 | cilia 摆动相位差 + 黏液流向 |
| 09 | blood-capillary | 毛细血管直径 6-8 μm, 红细胞 7-8 μm, 必须形变挤过 | 血流速度 ~ 0.5 mm/s 在 capillary; 单红细胞过 capillary 用 ~1 s | Marcello Malpighi 1661 (毛细血管发现) | Hagen-Poiseuille + 红细胞变形 (parachute / slipper shape) | 毛细血管 + 红细胞变形顺序图 |
| 10 | mucus | 呼吸道 mucus 60% 水, 凝胶 mesh ~100 nm | 双层结构: 上 gel 5 μm + 下 sol 5 μm; nano 颗粒被 trap | Lai 2009 (mucin polymer 网研究) | 网状分子 → 选择性通透 | mucus 双层 + cilia 摆动 + 颗粒被 trap |

### 第 3 部分 · 分子机器

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | atp | 一个体内一天合成 ~50 kg ATP (重复利用 1000 次) | $\Delta G_{\rm hyd} = -30.5$ kJ/mol $= -7.3$ kcal/mol $\approx 12 k_B T$; 浓度 ~5 mM | Lipmann 1941 提出 ATP 中央地位; Boyer & Walker Nobel 1997 (ATP synthase 旋转机制) | ATP synthase: F0 旋子 + F1 三个 αβ 对 | ATP synthase 结构 + 一个完整旋转周期 |
| 12 | molecular-motor | myosin II 每步 8 nm, 5-10 步/s on actin; kinesin 8 nm 每步 100 步/s | 单步力 ~5 pN (myosin), ~7 pN (kinesin); ATP/step = 1 | Andrew Huxley 1957 (sliding filament); Sheetz/Spudich 1980 single motor | 步态 = 化学能 → 力学功; Brownian ratchet 嵌入 | myosin 步态 + ATP cycle |
| 13 | ion-pump | Na/K ATPase 每秒泵 ~150 Na/K; 占脑能量 50% | 3 Na+ 出 / 2 K+ 入, 1 ATP; 静息电位 -70 mV | Jens Skou 1957 发现 (Nobel 1997) | 离子梯度建立 + ATP 周期 | Na/K pump 状态循环 4 步 |
| 14 | photosynthesis-life | 光合作用 PSII excite, charge separate < 1 ps | 量子效率 ~ 100% per excitation in lab; 整株植物 ~2% solar-to-chemical | Engelmann 1882 找出光合波长依赖; Calvin 1950 暗反应 | Z scheme: PSII (P680) → PSI (P700) → NADPH | Z 形电子流 + 两个反应中心 |
| 15 | enzyme | catalase 把 H₂O₂ 分解 5×10⁶ 次/s | $k_{\rm cat}/K_M$ ~ $10^8$ M⁻¹s⁻¹ near diffusion limit | Michaelis-Menten 1913; Pauling 1948 transition-state stabilization | $v = k_{\rm cat}[E][S]/(K_M + [S])$ | 反应坐标图 + transition state + ΔG‡ |

### 第 4 部分 · 单细胞到器官

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | protein-folding | RNase A 124 残基折叠 ms - s; AlphaFold 2 (2020) 革命 | Levinthal 1968 paradox: 60 残基随机 search 用 10⁵⁹ 年; 实际 ms | Anfinsen 1961 (Nobel 1972 RNase A 折叠), DeepMind AlphaFold 2 2020 | 能量漏斗 (Wolynes); evolutionary covariation | 漏斗 free energy 表面 + 折叠路径 |
| 17 | cytoskeleton | 微管直径 25 nm, persistence length 5 mm (大于细胞!); actin 直径 7 nm $L_p \approx 17$ μm | 动态不稳定: 微管 $v_+ \approx 1$ μm/s; rescue rate | Tilney & Porter 1965; Mitchison & Kirschner 1984 dynamic instability | filament polymerize / depolymerize | 微管 + actin + 中间纤维三种丝 + 长度尺度 |
| 18 | bone-scaling | 大象不能跳; 骨横截面 $\propto m^{2/3}$ 但体重 $\propto m$ → 应力 $\propto m^{1/3}$ | 老虎跳 5 m, 大象不能跳; 骨断裂应力 ~150 MPa | Galileo 1638 *Two New Sciences*: 第一次提 square-cube law | 弹性 / 强度标度 → 体型上限 | 跳跃高度 vs 体重 + Galileo 巨人骨架草图 |
| 19 | bird-v | 鹅 V 队飞节省 12-20% 能量 | 翼尖涡 induced upwash; V 队最佳间距 ~翼展 | Lissaman & Shollenberger 1970 飞行队节能计算 | 涡诱导升力 + drag reduction | V 队示意 + 翼尖涡 + 节能曲线 |
| 20 | fish-school | 沙丁鱼群同步, 邻间距 ~一个体长 | 群体决策 reaction time ~50 ms | Couzin 2002 三规则: 排斥 + 对齐 + 吸引 | local 规则 → 全局有序 (Vicsek) | 三同心圈区域: repel / align / attract |

### 第 5 部分 · 信号与神经

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | action-potential | 鱿鱼巨轴突直径 1 mm, 第一次记录动作电位; -70 mV 静息, +40 mV 峰值 | $V_{\rm Na} = +60$ mV, $V_K = -90$ mV; 持续 1-2 ms; 速度 1-100 m/s | Hodgkin & Huxley 1952 (Nobel 1963); Cole 1949 voltage clamp | $C_m \dot V = -I_{\rm Na} - I_K - I_L$, gating $m^3 h$ vs $n^4$ | 电压变化时序 + Na/K 电流分解 |
| 22 | synapse | NMJ 终板 200 nm cleft; 一次释放 ~10⁴ ACh | 神经递质 release latency ~0.5 ms; 突触强度变化 = LTP | Bernard Katz 1952 quantal release (Nobel 1970) | $P_{\rm release} = 0.1$-$0.5$; vesicle fusion SNARE | 突触前 / 后膜 + vesicle 释放 |
| 23 | retina | 视杆 30000 个/mm² 中央凹外; 视锥峰密度 200000/mm² 中央凹 | 视杆 1 photon 探测; 视锥 100 photons | Hecht 1942 (单光子探测); Wald (锥谱) | rhodopsin photoisomerization; phototransduction G 蛋白级联 | 眼底 + 视杆 / 视锥分布 |
| 24 | hearing-hair-cell | 耳蜗 ~ 16000 内毛细胞, sensitivity ~ atomic-scale displacement | 阈值膜位移 ~0.3 nm (亚原子级!); 音频 100-4000 Hz phase locking | Hudspeth 1985 mechanotransduction; Békésy 1928 (Nobel 1961) | tip link 张开 ion channel 在 ~10 μs 内 | hair cell + stereocilia + tip link |
| 25 | brain-energy | 人脑 1.4 kg 占 BMR 的 20%; 100 W BMR 中脑用 ~20 W | 神经元发放 ~5 Hz mean; cortex 200 W/kg | Magistretti & Pellerin 1990s neurometabolic coupling | astrocyte-neuron lactate shuttle | 脑代谢 + 灰质 / 白质能耗 |

### 第 6 部分 · 进化与起源

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | kleiber | $P_{\rm BMR} \propto M^{3/4}$; 鼠 $\rightarrow$ 蓝鲸 跨 6 数量级仍贴 | West-Brown-Enquist 1997 fractal vascular network 给 3/4 | Max Kleiber 1932 牛饲料数据 | $P = a M^{b}, b \approx 0.75$ | log-log $P$ vs $M$ + WBE 模型 |
| 27 | temperature-life | 哺乳动物 37°C; 极地鱼活到 -2°C; 嗜热菌 113°C (Pyrolobus) | 蛋白质失活 > 60°C 多数; 抗冻蛋白阻止冰晶 | Stewart 1972 (psychrophile/thermophile/hyperthermophile 分类) | Arrhenius 反应速率与温度 | 生物可活温度区间图 + 不同物种例 |
| 28 | morphogenesis | Turing 1952 反应扩散 → stripe / spot 模式 | $D_a/D_i \gtrsim 10$ for 模式形成; 鱼斑纹波长 mm | Alan Turing 1952 *The Chemical Basis of Morphogenesis*; Murray 鱼斑纹模型 | 反应扩散方程 + Turing 不稳定 | Turing 模式数值仿真 + 真实斑马鱼 |
| 29 | robustness | E. coli chemotaxis 对酶浓度 100× 变化仍精准趋化 | adaptation accuracy ~99% | Barkai & Leibler 1997 robust adaptation 论文 | integral feedback control | chemotaxis 网络 + 适应曲线 |
| 30 | origin-life | RNA world; Miller-Urey 1953 合成 amino acid 实验 | 早期地球: NH3, CH4, H2 + spark → glycine, alanine | Stanley Miller 1953 (Urey 实验室); 1980 Cech / Altman ribozyme | RNA 既能复制又能催化 | Miller 装置 + 火花 + 产物分析 |

---

## 本卷易踩的坑

- 这一卷不是生物书. 每节落到一个数 / 一个公式 / 一个有名字的实验家, 而不是 lengthy 的生物术语堆.
- 第 6 节 (low-Re) 必须 mention Purcell 1977 演讲与 scallop theorem, 那是这个领域的入口.
- 第 11 节 (ATP) 必须给 30.5 kJ/mol $\approx 12 k_B T$ 这个对照, 让读者把 ATP 与 thermal noise 放一个标尺上.
- 第 21 节 (action potential) 必须给 -70 mV / +40 mV 与 1-2 ms 持续时间, Hodgkin-Huxley 方程的 $m^3 h, n^4$ 至少 mention 一次.
- 第 30 节 (origin-life) 不是 speculation. 给 Miller-Urey 的具体合成产物, 给 RNA world 的具体 ribozyme.

---

## 颜色

`vol-11-physics-of-life/style.css` 已设. 卷色: 春绿 (生命色, 不是 vol-7 的 forest).

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 尺度与扩散 | 01-cell-size.html ... 05-thermal-noise-life.html |
| 第 2 部分 · 低 Reynolds | 06-low-re.html ... 10-mucus.html |
| 第 3 部分 · 分子机器 | 11-atp.html ... 15-enzyme.html |
| 第 4 部分 · 单细胞到器官 | 16-protein-folding.html ... 20-fish-school.html |
| 第 5 部分 · 信号与神经 | 21-action-potential.html ... 25-brain-energy.html |
| 第 6 部分 · 进化与起源 | 26-kleiber.html ... 30-origin-life.html |

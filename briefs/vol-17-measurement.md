# Vol 17 · 测量是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-17-measurement/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

测量 = 从巴黎一根铂铱棒到 Cs 跃迁到 Planck 常数. 30 节按 6 部分:

1. SI 标准: 米、秒、千克、SI 单位、定义重塑
2. 日常测量: 尺、秤、温度计、气压计、光度
3. 误差与不确定: error bars, 随机 / 系统, SNR, 分辨率, 三角法
4. 现代仪器: GPS, 相对论 GPS, 加速度计, 激光雷达
5. 微观: 原子尺寸, 质子半径, 电子电荷, 量子极限
6. 大尺度: 宇宙距离, 视差, 标准蜡烛, 红移, 测量哲学

每节落到一个具体仪器 / 标定 / 实验 + 一个具体不确定度数 + 一位有名字的人.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "1799 年法国大革命用赤道到北极弧的 1/10⁷ 定义了'米' (实际偏 0.2 mm). 1875 年签 *Convention du Mètre*, 巴黎国际度量衡局保管那根铂铱国际原器. 1983 年米被改成 '光在真空中走 1/299,792,458 s 的距离', 完全摆脱了那根棒. 2019/05/20 千克跟随, 不再是法国保险柜里的 Le Grand K, 而是用 Planck 常数 $h = 6.62607015 \times 10^{-34}$ J·s 反推. 这一卷把'测量'从一根尺一直走到 Hubble 常数 $H_0$ 那个 67 vs 73 km/s/Mpc 的 5σ tension. 终点是 Heisenberg 测量极限 + Bell 实验告诉我们: 不只是测精度, 测量本身改变物理."

---

## 30 节具体 brief

### 第 1 部分 · SI 标准

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | standards | 从国王脚到 Cs 钟 — 4 千年标准化史 | 1875 *Convention du Mètre*; 17 个国家原始签约 | Mèchain & Delambre 1792-99 (法国测地大圆); 1875 BIPM | 标准 = 高复制性的物理过程 | 标准化时间线 |
| 02 | meter | 从 1/10⁷ 子午线到 1960 Kr 86 谱线到 1983 c 定义 | 1 m = $c \times 1/299792458$ s | Mèchain-Delambre 1799; CGPM 1983 c-defined | $c$ 是定义, 米是导出 | 米的定义演变三阶段 |
| 03 | second | 从 86400 / 自转日 到 1967 Cs 钟 | $1\,\mathrm{s} = 9192631770$ Cs 跃迁周期; uncertainty $10^{-16}$ at NIST F1 | Essen & Parry 1955 first Cs clock NPL | hyperfine transition $^{133}$Cs $F=3 \to F=4$ | Cs 喷泉钟原理图 |
| 04 | kilogram | 2019/05/20 之前 Le Grand K (法国铂铱); 之后 Planck 常数 | $h = 6.62607015 \times 10^{-34}$ J·s 严格定义; Kibble 平衡 $10^{-8}$ | NIST Kibble balance 2017; 26th CGPM 2018 | $mg = BIL \cdot v$ (Watt balance) → $h$ | Kibble 平衡装置示意 |
| 05 | si-units | 7 base units (m, s, kg, A, K, mol, cd) 全部定义自常数 (2019 后) | $c, h, e, k_B, N_A, \Delta\nu_{\rm Cs}, K_{cd}$ 七基本常数 | 26th CGPM 2018 SI redefinition | 物理常数 → 单位 (反向) | 7 基本常数 → 7 单位映射 |

### 第 2 部分 · 日常测量

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | ruler | 钢卷尺 0.1 mm 精度; 游标卡尺 0.02 mm; 千分尺 1 μm | 测量精度 ↔ 物体表面粗糙度 | Pierre Vernier 1631 游标尺 | 直接对照 | 各类尺 + 精度对比 |
| 07 | scale | 弹簧秤 ~ 1% accuracy; 电子秤 0.01 g; 化学天平 1 μg | 杠杆平衡; 应变片秤; balance 灵敏度 ~$\mu$g | Joseph von Fraunhofer 1820 化学天平 | $F = mg$ vs balance | 各类秤原理 |
| 08 | thermometer | 水银 -39 to 357°C; Pt 电阻 -260 to 962°C; 红外辐射 -100 to 3000°C | resistor $R(T) = R_0(1 + \alpha T)$; Pt α = 0.00385 /K | Fahrenheit 1714 (mercury); Pt RTD 1932 | 测温物理: 物质性质 = T 函数 | 温度计种类 + 工作范围 |
| 09 | pressure-gauge | 气压计 1013 hPa = 760 mmHg; 微压传感器 0.1 Pa | Torricelli 1643 第一个气压计 (水银) | Torricelli 1643; piezoelectric 现代 | 压力 → 位移 / 应变 | 水银柱 + 压力传感器 |
| 10 | camera-meter | 相机测光 ISO 100 + f/2.8 + 1/125 = EV 11 | 18% 灰参考反射率 | Weston 1932 first electric meter | 光强 = 物体反射 × 入射 | 测光表 + EV 系统 |

### 第 3 部分 · 误差与不确定度

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | error-bars | 1 σ 68%, 2 σ 95%, 5 σ < 1/3.5×10⁶ | 误差棒 = 1σ 标准 | Gauss 1809 *Theoria motus* | $\sigma = \sqrt{\sum (x_i - \bar x)^2/(N-1)}$ | 数据点 + error bar + 拟合 |
| 12 | random-error | $N$ 次平均 → $\sigma/\sqrt N$ | $\sigma_{\bar x} = \sigma/\sqrt N$; 100 次平均误差 1/10 | Bessel correction 1838 | 中心极限定理 | $\sigma$ vs $N^{-1/2}$ |
| 13 | systematic-error | LIGO 镜面 systematic 比 random 难; tritium decay rate 长期 ~10⁻⁵ stability | 系统不可被平均消除 | 工程实践积累 | 校准 + 重复测量 + cross-check | 系统 vs 随机误差 |
| 14 | signal-noise | LIGO 应变灵敏度 $10^{-23}/\sqrt{\rm Hz}$ | SNR = 信号 / 噪声 dB; matched filter 把高斯噪声里 SNR 提高 √(BT) | Matched filter optimal; LIGO 2015 first GW detection | $S/N$ in different bandwidth | 时序 + 频谱 + matched filter |
| 15 | resolution-precision | 5 mm 尺刻线 vs 0.1 mm 显微刻 vs 1 nm STM | resolution = 最小分辨; precision = 重复性 | classical Rayleigh resolution | 区别 resolution / precision / accuracy | 三种概念图解 |

### 第 4 部分 · 现代仪器

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | triangulation | Eratosthenes 公元前 240 年测地球周长 250000 stadia ≈ 40000 km | Aswan 太阳顶点正午 + Alexandria 7° → 圆周 | Eratosthenes 公元前 240 (Library of Alexandria) | 几何三角法 | 地球 + 两城 + 太阳角度 |
| 17 | gps | 24 颗 ~20000 km 高轨; 民用 5 m 精度 | $\Delta t \times c = $ 距离; 4 颗解 (x, y, z, $\Delta t$) | Bradford Parkinson 1973 (GPS architect); operational 1995 | trilateration with time | GPS 卫星 + 地面 + 4 颗解 |
| 18 | relativity-gps | GPS 必修相对论: SR -7 μs/day, GR +45 μs/day → 净 +38 μs/day | 不修正一天 ~10 km 漂移 | Bradford Parkinson + Hafele-Keating 1971 飞行实验 | $\Delta t/t = -v^2/2c^2 + gh/c^2$ | 卫星 + 两个相对论修正 + 错误累积 |
| 19 | accelerometer | iPhone MEMS accel ~50 μg 噪声; 1 mm³ 芯片 | $a = F/m$; 微悬臂梁 + 容性 / 压阻 | Charles Kuffel 1968 first MEMS; 现代 STMicro / Bosch | 微悬臂梁 + 电容感测 | MEMS accel 截面 |
| 20 | lidar-measure | iPhone LiDAR 5 m range ±1 cm; 自动驾驶 100 m | $d = c \times t/2$; 飞秒激光 + APD | Hughes Aircraft 1961 first LiDAR | pulse time of flight | LiDAR 点云 + ToF |

### 第 5 部分 · 微观

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | atom-size | 氢 Bohr 半径 0.529 Å; 重原子 ~3 Å | $a_0 = \hbar^2/(m_e e^2/(4\pi\epsilon_0)) = 0.5292$ Å | Bohr 1913 氢原子 | $a_0 = 4\pi\epsilon_0 \hbar^2/(m_e e^2)$ | Bohr radius + 原子大小光谱 |
| 22 | proton-size | μH 实验 0.840 fm vs eH 0.875 fm 之争 (proton radius puzzle) | $r_p$ 由 Lamb shift 与 elastic scattering 测; 4σ 矛盾 | Pohl 2010 muonic H, Bezginov 2019 H Lamb 重测 | electromagnetic form factor | μH vs eH 测值 + 误差棒 |
| 23 | electron-charge | Millikan 油滴 1909-13: $e = 1.6 \times 10^{-19}$ C | 现代 SI 定义 $e = 1.602176634 \times 10^{-19}$ C 严格 | Robert Millikan 1909 (Nobel 1923) — 后被指数据选择性 | $eE = mg$ + Stokes drag | Millikan 油滴装置 |
| 24 | quantum-limit | LIGO 镜面 standard quantum limit ~ $10^{-19}$ m at 100 Hz | SQL: $\sigma_x \sigma_p = \hbar/2$; squeezed light 突破 | Caves 1981 quantum noise in interferometers; LIGO O3 squeezed light 2019 | Heisenberg + back action | LIGO + squeezed light Wigner |
| 25 | weak-signal | 微波背景 CMB 2.725 K, 各向异性 ~10⁻⁵; LIGO H1 strain 10⁻²¹ | matched filter; lock-in amplifier; bolometer | Penzias & Wilson 1965 CMB (Nobel 1978); Smoot/Mather COBE 1992 | 调制 + 锁相检测 + 平均 | 信号 + 噪声 + 解调 |

### 第 6 部分 · 大尺度

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | cosmic-distances | 距离阶梯: 视差 → Cepheid → SN Ia → CMB | parallax < 1 kpc; Cepheid < 30 Mpc; SN Ia < few Gpc | distance ladder Hubble | 三角法 → 标准烛光 → 宇宙学 | 距离阶梯 4 层 |
| 27 | parallax-stars | Bessel 1838 第一颗恒星视差 (61 Cyg, 0.314") | 1 pc = 3.086×10¹⁶ m = 3.26 ly; Gaia DR3 视差精度 25 μas | Friedrich Bessel 1838; Gaia 2013 | $d = 1/p_{\rm arcsec}$ pc | 视差几何 + Gaia 测得范围 |
| 28 | standard-candle | Cepheid period-luminosity (Leavitt 1908); Type Ia SN 1994 标准化 | Cepheid $\log L = a \log P + b$; SN Ia $M = -19.3$ | Henrietta Swan Leavitt 1908 (Harvard "computer"); Riess/Perlmutter SN 1998 (Nobel 2011) | $m - M = 5\log_{10}(d/10\,\mathrm{pc})$ | Leavitt 数据图 + SN Ia 光变 |
| 29 | redshift-distance | $z = \Delta\lambda/\lambda$; SDSS 数百万星系 z 测得 | Hubble constant $H_0$ tension: 67 (CMB) vs 73 (Cepheid+SN) km/s/Mpc, 5σ | Hubble 1929 first $v = H_0 d$; Riess 2018 SH0ES vs Planck 2018 | $v = H_0 d$, cosmic expansion | $H_0$ 测值时间线 + 两组矛盾 |
| 30 | measurement-philosophy | Heisenberg + Bell 实验告诉我们: 测量改变 system | $\Delta x \Delta p \ge \hbar/2$; Bell inequality 经典上限 vs 量子破坏 | Heisenberg 1927; Aspect 1982 第一 Bell 实验 (Nobel 2022 Aspect/Clauser/Zeilinger) | quantum + 信息论 lower limits | Heisenberg + Bell 实验关系 |

---

## 本卷易踩的坑

- 第 4 节 (千克) 必须给 2019/05/20 这个日期, 这是物理史时刻. Le Grand K 退休.
- 第 18 节 (GPS 相对论): 要给 SR 与 GR 反向 (-7, +45) μs/day → 净 +38 μs/day, 强调不修正一天漂 10 km.
- 第 22 节 (proton radius): 这是 ongoing 争议 (μH 0.840 vs eH 0.875 fm), 不要装作已 resolved.
- 第 23 节 (Millikan): Millikan 选择性数据是 history of science 经典 case, 必须 mention.
- 第 29 节 (Hubble tension): 67 vs 73 km/s/Mpc 5σ 是 2024 cosmology 最大 puzzle, 必须给具体数字.
- 第 30 节: Aspect 2022 Nobel — 给具体 1982 实验 + 2022 奖名.

---

## 颜色

`vol-17-measurement/style.css` 已设. 卷色: 测量精确灰 / 石墨.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · SI 标准 | 01-standards.html ... 05-si-units.html |
| 第 2 部分 · 日常测量 | 06-ruler.html ... 10-camera-meter.html |
| 第 3 部分 · 误差与不确定度 | 11-error-bars.html ... 15-resolution-precision.html |
| 第 4 部分 · 现代仪器 | 16-triangulation.html ... 20-lidar-measure.html |
| 第 5 部分 · 微观 | 21-atom-size.html ... 25-weak-signal.html |
| 第 6 部分 · 大尺度 | 26-cosmic-distances.html ... 30-measurement-philosophy.html |

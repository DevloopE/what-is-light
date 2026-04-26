# Vol 8 · 流体是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-8-fluids/`. 30 个 HTML 文件已经存在 (有低质量旧稿), **需要按下表逐节重写正文**, 文件名 / index.html / style.css 已经对好, 不要改.

## 卷主轴

水槽里的水、烟圈、浴缸涡、帆船、音爆与天气都共用同一套场方程. 30 节按 6 部分搭起来:

1. 日常流动与尺度: 水从 "一块" 变成 "无数层", 黏性怎么定义, Reynolds 数怎么压住所有现象
2. Navier-Stokes 直觉: NS 在每个网格上算什么, Bernoulli 与压力怎么从 NS 掉出来
3. 涡与不稳定: 涡度、烟环、Kármán 涡街、Kelvin-Helmholtz、Rayleigh-Taylor
4. 飞行与冲击: 升力、阻力、终端速度、激波、喷管
5. 湍流与计算: 转捩、Kolmogorov 5/3、对数律、湍流混合、CFD
6. 大尺度流体: 大气环流、洋流、血流、河曲、微流控

每节落到一个具体材料/对象 + 一个具体数 + 一个有名字的实验.

---

## 卷引子 (覆盖 `index.html` 的 `<p class="intro">`)

> "水龙头一拧, 水柱在 5 cm 落差里从透明的玻璃柱变成皱起的麻花; 厨房抽烟机上方一缕烟环可以稳稳飘 5 秒不散; 一架 A380 在 12 km 高度以 250 m/s 巡航, 机翼表面被一层只有几毫米厚的空气托住; 1883 年 Manchester 的 Reynolds 把染料注进玻璃管, 让全世界第一次看见层流变湍流的临界点. 这一卷把这些现象塞进一个统一的语言: 不可压缩或可压缩, 黏性或无黏, 整个图样常常被一个无量纲数控制. 我们从水槽里 0.5 mm/s 的薄层一路走到 $E(k) = C\varepsilon^{2/3} k^{-5/3}$ 的湍流谱, 终点是 NS 方程的存在唯一性 — Clay $1M 的题目."

---

## 30 节具体 brief

### 第 1 部分 · 日常流动与尺度

| NN | slug | 切入对象 / 现象 | 必含数字 | 必含人 + 年份 | 关键公式 / 机制 | 图占位 brief 提示 |
|---|---|---|---|---|---|---|
| 01 | sink-water | 厨房水槽不锈钢台面, 水以 ~10 cm/s 摊开, 在边界附近变薄到 1 mm 的剪切层 | $\nu_{\rm 水, 20°C}=1.0\times 10^{-6}\,\mathrm{m^2/s}$; 边界层 $\delta \approx \sqrt{\nu L/U} \approx 1\,\mathrm{mm}$ | Newton 1687 (黏性的最初定义), Stokes 1845 | $\tau = \mu \dfrac{\partial u}{\partial y}$; no-slip 条件 | 水槽截面剖面图, 水从无滑移壁面到自由表面的 $u(y)$ 抛物线 |
| 02 | reynolds-number | Manchester 实验室 1883 年那根玻璃管, 染料一注就能看见层流 → 转捩 → 湍流三阶段 | 管流临界 $Re_{\rm crit} \approx 2300$; 完全湍流 $Re \approx 4000$ | Osborne Reynolds 1883 (Phil Trans Roy Soc) | $Re = \rho U L / \mu = U L / \nu$ | 三幅小图: $Re=1000$ 直线染料 / $Re=2500$ 起伏 / $Re=5000$ 完全乱 |
| 03 | pipe-flow | 家用 1/2 英寸冷水管 (内径约 13 mm), 在 1 m 水头下流多少 | Hagen-Poiseuille; $Q = \pi r^4 \Delta P / (8 \mu L)$; 上述参数代入 $Q \approx 28\,\mathrm{mL/s}$ | Hagen 1839 (Berlin), Poiseuille 1840 (Paris, 用毛细血管度量水银) | $Q \propto r^4$ — 直径加倍流量 16 倍 | 圆管横截面 $u(r)$ 抛物线 + 标 $r,L,\Delta P$ |
| 04 | draining-vortex | 浴缸放水时的小漩涡, 几秒内从一团雾收紧到 5 mm | 角动量守恒 $\omega r^2 = \mathrm{const}$; Coriolis 在中纬度 $f = 2\Omega \sin 45° \approx 10^{-4}\,\mathrm{s^{-1}}$ — 比浴缸涡频率小 4 个量级 | Shapiro 1962 MIT 实验 (大盆静置 24 小时确认 Coriolis 效应) | 涡线拉伸: $\boldsymbol\omega \cdot \nabla \mathbf u$ 让涡度集中 | 浴缸 + 漩涡, 标进水角动量 $L_0$ 与排水时半径 $r(t)$ |
| 05 | boundary-layer | A380 巡航, 70 m 翼展, 表面那层空气 | $\delta \sim 5\sqrt{\nu x/U}$; 在 $\nu_{\rm air}=1.5\times 10^{-5}$, $U=250$ m/s, $x=10$ m 处 $\delta \approx 4$ mm 层流, 转捩后 $\delta \sim 50$ mm | Ludwig Prandtl 1904 Heidelberg 大会 (8 min 演讲就改了空气动力学整门学科) | Prandtl 边界层方程 (NS 在 $\delta/L \to 0$ 极限) | 翼前缘流线, 标 laminar / turbulent / wake; 标 $\delta(x)$ 上升曲线 |

### 第 2 部分 · Navier-Stokes 直觉

| NN | slug | 切入对象 / 现象 | 必含数字 | 必含人 + 年份 | 关键公式 / 机制 | 图占位 brief 提示 |
|---|---|---|---|---|---|---|
| 06 | continuity | 水龙头出水柱在 5 cm 落差里收细一半 | 自由落体 $v = v_0 + gt$, $A v = \mathrm{const}$ → $A(z)$ 收缩比 | Euler 1757 (流体力学第一篇 paper) | $\dfrac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf u) = 0$ | 水柱侧面图, 标 $A(z) v(z) = A_0 v_0$ |
| 07 | navier-stokes | NASA CFD 计算翼型, 每个网格每个 timestep 算 NS | 在 $10^9$ 网格 × $10^4$ steps 上, 一次 70 万核小时; Clay $1M 题目 (3D regularity) | Navier 1822 (法国, 加 viscous term), Stokes 1845 (再独立推一遍, 给现代写法) | $\rho\!\left(\dfrac{\partial \mathbf u}{\partial t} + \mathbf u \cdot \nabla \mathbf u\right) = -\nabla p + \mu \nabla^2 \mathbf u + \mathbf f$ | NS 各项的物理意义图: 时间导数 + 对流 = 压差 + 扩散 + 体力, 每项配一个微小流体元 |
| 08 | pressure | 潜水员每下 10 m 多 1 atm, 100 m 处听到耳膜被压 | $p = \rho g h$; 海水 $\rho = 1025$ kg/m³, 每 10.06 m 增加 1 atm | Pascal 1648 Le Puy de Dôme 实验 (姐夫 Périer 帮忙带气压计上山) | 静压力各向同性: 应力张量在静止流体里成 $-p\,\delta_{ij}$ | 海水柱 $h$ 与压力刻度, 同时给 $\rho g h$ 与 atm |
| 09 | bernoulli | B737 一只翼 $\approx 50\,\mathrm{m^2}$, 70 t lift at $U \approx 70$ m/s 起飞 | $\tfrac12 \rho v^2 + p + \rho g z = \mathrm{const}$; 升力系数 $C_L \approx 1.2$ 起飞构型, $L = \tfrac12 \rho v^2 C_L S$ | Daniel Bernoulli 1738 *Hydrodynamica* (Strasbourg 出版) | 沿流线 Bernoulli; Kutta-Joukowski $L = \rho U \Gamma$ | 翼型截面 + 流线, 上下流速差 $\Delta v$, 标压力差 $\Delta p$ |
| 10 | vorticity | 在水池里搅拌, 涡轴清晰可见; 提取局部"旋率" | $\boldsymbol\omega = \nabla \times \mathbf u$; 平均涡度数量级在生活流动中 $1$-$10\,\mathrm{s^{-1}}$ | Helmholtz 1858 *Über Integrale*, Kelvin 1869 (circulation theorem) | 涡度方程 $D\boldsymbol\omega/Dt = (\boldsymbol\omega \cdot \nabla)\mathbf u + \nu \nabla^2 \boldsymbol\omega$ | 一个涡管, 标涡线、Kelvin 圆环路 $\Gamma = \oint \mathbf u \cdot d\mathbf l$ |

### 第 3 部分 · 涡与不稳定

| NN | slug | 切入对象 | 必含数字 | 必含人 + 年份 | 公式 / 机制 | 图占位 brief |
|---|---|---|---|---|---|---|
| 11 | smoke-rings | 抽烟机或核试爆形成的烟环, 在 5-10 s 内自传 | 自感诱速 $U \approx \dfrac{\Gamma}{4\pi R} \ln\!\dfrac{8R}{a}$; 典型烟环 $R\approx 5$ cm, $\Gamma \sim 10^{-2}$ m²/s | Helmholtz 1858 (vortex theorems), Kelvin 1867 vortex atom 理论 (后被原子理论取代) | 涡环 = 闭合涡线圆; Kelvin 定理保 $\Gamma$ | 涡环侧面 + 截面 (双涡核), 自感速度箭头 |
| 12 | karman-vortices | 大西洋 Madeira 岛后方卫星图的 von Kármán 云街 | Strouhal $St = fD/U \approx 0.2$ 在 $Re = 10^2$-$10^5$; 涡间距比 $h/a \approx 0.281$ | Theodore von Kármán 1911 (Göttingen) | 一对圆柱后流的稳定排布: $\cosh^{-1}(h/a) = \pi/\sqrt 2$ | 圆柱后涡街棋盘式排列 + 标 $h, a, D, U, St$ |
| 13 | kelvin-helmholtz | 山顶背风云的鱼鳞波或杯壁油水分层 | 不稳定增长率 $\gamma = k\sqrt{U_1 U_2 - g(\rho_2-\rho_1)/k(\rho_1+\rho_2)}$ | Helmholtz 1868, Kelvin 1871 (in *Phil Mag*) | 剪切两侧 + 重力的色散关系 | 双层流体在剪切下边界振荡成卷状, 标 $U_1, U_2, k, \lambda$ |
| 14 | rayleigh-taylor | 冷战核试爆蘑菇云的"伞柄"; 实验里水上面盖一层硫酸铜 | Atwood 数 $A = (\rho_1 - \rho_2)/(\rho_1+\rho_2)$; 增长率 $\gamma = \sqrt{Agk}$ | Rayleigh 1883 (重力不稳定), G. I. Taylor 1950 (Manhattan Project 后开放发表) | 重流体在轻流体上方的指状下沉 | 蘑菇云截面 + 实验槽 (上 dye 下水), $\gamma(k)$ 曲线在右下 |
| 15 | mixing | 一勺奶倒进咖啡, 两秒变均匀 vs 静置一小时也不均匀 | 分子扩散 $D \sim 10^{-9}$ m²/s, 湍流扩散 $D_T \sim 10^{-3}$; 比值 $10^6$; Batchelor 尺度 $\ell_B = (\nu D^2/\varepsilon)^{1/4}$ | Welander 1955 (奶咖啡的混沌混合), Batchelor 1959 | 标量耗散方程: $D\theta/Dt = D\nabla^2\theta$, 拉伸+折叠 | 一杯咖啡顶视奶迹被搅成丝带, 长度随时间指数增长 |

### 第 4 部分 · 飞行与冲击

| NN | slug | 切入对象 | 必含数字 | 必含人 + 年份 | 公式 / 机制 | 图占位 brief |
|---|---|---|---|---|---|---|
| 16 | sail-lift | 美洲杯 AC75 帆船在 25 节风里以 50 节船速逆风 45° 跑 | VMG 最佳约 30°-40° to true wind; 升阻比 $L/D \sim 30$ | 中世纪 lateen sail; Bernoulli + Newton 第三 | 帆 = 翼, 升力垂直于 apparent wind; 矢量合成 | 帆船俯视图, 真风 / 表观风 / 升力 / 推力四矢量 |
| 17 | airfoil | NACA 0012 经典翼型, 厚度 12% 弦长 | 薄翼理论 $dC_L/d\alpha = 2\pi$ /rad; 失速角 $\alpha \approx 15°$ | Joukowski 1906 (Moscow), Kutta 1902, Prandtl 1918 (Lifting line) | $L = \rho U \Gamma$; 环量 $\Gamma$ 由 Kutta 条件决定 | 翼型截面, 上 / 下表面流线密度差, 后缘 Kutta 点 |
| 18 | drag | 雨滴 2 mm 直径, 终端速度 $\approx 6\,\mathrm{m/s}$ (不是 100 m/s) | $F_D = \tfrac12 \rho v^2 C_D A$; 球 $C_D \approx 0.5$ at $Re \approx 10^4$; $v_\infty = \sqrt{2mg/(\rho C_D A)}$ | Stokes 1851 (low-$Re$, $F = 6\pi \mu r v$); Newton drag 1687 | 高 $Re$ 阻力 $\propto v^2$, 低 $Re$ $\propto v$ | 球周围流线 $Re=1$ 与 $Re=10^4$ 对比, 后部尾涡显形 |
| 19 | shock-waves | F-18 跨音速 condensation cone; Concorde 落地前的双 boom | Mach 锥半角 $\sin\theta = 1/M$; Concorde Mach 2 时 cone $30°$ | Ernst Mach 1887 (Schlieren 第一张激波照片), Prandtl-Meyer 1908 | Rankine-Hugoniot 跨激波守恒: $[\rho v]=0, [p+\rho v^2]=0, [h+v^2/2]=0$ | 激波锥 + Schlieren 图, 标 Mach 锥角 |
| 20 | nozzles | F-1 火箭发动机喉部 1 m, 出口 3 m, $I_{sp} \approx 263$ s 海平面 | 喉道 $M=1$ choked; 面积比 $A/A^* = (1/M)\!\left[\!\dfrac{2 + (\gamma-1)M^2}{\gamma+1}\!\right]^{(\gamma+1)/[2(\gamma-1)]}$ | de Laval 1888 蒸汽涡轮; Goddard 1926 第一枚液体火箭 | 收敛-发散喷管: 亚音速 → 喉道 $M=1$ → 超音速 | 喷管侧剖, $A(x)$ + $M(x)$ + $p(x)$ 三条曲线 |

### 第 5 部分 · 湍流与计算

| NN | slug | 切入对象 | 必含数字 | 必含人 + 年份 | 公式 / 机制 | 图占位 brief |
|---|---|---|---|---|---|---|
| 21 | transition | Reynolds 1883 玻璃管 + 染料的转捩观测; 现代风洞用热线丝测速度脉动 | 管流 $Re_{\rm crit}\approx 2300$; 平板 $Re_x \approx 5\times 10^5$ | Reynolds 1883; Tollmien-Schlichting 波 1929/1933 (临界扰动) | 不稳定本征模, 二次失稳 | 染料管三幅图 + 速度时间序列 (laminar 平直, 转捩有 burst, 湍流连续脉动) |
| 22 | kolmogorov | 大气湍流 $E(k)$ 谱测出 $-5/3$ 斜率, 风洞 / 海洋 / 木星都对得上 | $E(k) = C \varepsilon^{2/3} k^{-5/3}$, $C \approx 1.5$; Kolmogorov 微尺度 $\eta = (\nu^3/\varepsilon)^{1/4}$ | Andrey N. Kolmogorov 1941 (莫斯科, 4 篇 Doklady) | 能量级联: 大涡 → 小涡 → 黏性耗散 | log-log 谱图, 标注 inertial range 5/3 直线, 上下接 large-scale 与耗散区 |
| 23 | wall-turbulence | 平板湍流 mean velocity profile (用激光多普勒测) | $U/u_\tau = (1/\kappa)\ln(y u_\tau/\nu) + B$; $\kappa \approx 0.41, B \approx 5.0$ | Prandtl 1925 (mixing length), von Kármán 1930 (log law) | 壁面单位 $u_\tau = \sqrt{\tau_w/\rho}$, 内层/对数层/外层 | $U^+(y^+)$ 半对数图, 标三段: viscous sublayer, buffer, log law |
| 24 | turbulent-mixing | 河里污染物从入河口往下游 1 km 内被湍流稀释 1000 倍 | 湍流扩散系数 $D_T \sim u' L \sim 1\,\mathrm{m^2/s}$, vs 分子 $10^{-9}$; Pe = $UL/D_T$ | Reynolds 1894 (Reynolds 应力概念) | Reynolds averaging, $-\overline{u'\theta'} = D_T \partial \overline\theta/\partial y$ | 河流俯视, 染料从一点扩散成扇形, 标 $L \propto t^{1/2}$ vs $L \propto t$ 对比 |
| 25 | cfd | ECMWF 9 km 全球网格做 10 天天气预报 | $\sim 10^9$ grid cells, $\sim 10^4$ steps; Lyapunov 时间 $\sim 7$-$10$ d | Lewis F. Richardson 1922 (手算 6 hr forecast 失败); von Neumann 1950 ENIAC 第一次成功数值预报 | Primitive equations 离散; CFL 条件 | 气象预报图层级架构, 网格 + 物理参数化模块 |

### 第 6 部分 · 大尺度流体

| NN | slug | 切入对象 | 必含数字 | 必含人 + 年份 | 公式 / 机制 | 图占位 brief |
|---|---|---|---|---|---|---|
| 26 | weather-flow | 卫星图: 哈德利、费雷尔、极地三胞云带 | Hadley 0°-30°, Ferrel 30°-60°, Polar 60°-90°; 信风 5-10 m/s | George Hadley 1735 (信风), William Ferrel 1856, Carl-Gustaf Rossby 1939 (Rossby 数) | 旋转参考系 NS, $Ro = U/(fL)$ | 地球三胞结构 + 表面风向 |
| 27 | ocean-currents | 湾流在 Florida 海峡 $\sim 30$ Sv, 向北扩到 New Foundland 150 Sv | 1 Sv = $10^6$ m³/s; 西边界强化 | Henry Stommel 1948 (西边界化论文), Walter Munk 1950 | $\beta$ 平面 + 涡度方程 | 大西洋俯视 + 湾流 + 风应力 + Sverdrup transport |
| 28 | blood-flow | 主动脉直径 25 mm, 血流峰值 1 m/s, 心率 1 Hz | $Re \approx 4000$ (临界); Womersley $\alpha = R\sqrt{\rho\omega/\mu} \approx 13$ | John R. Womersley 1955 (脉动血流) | Pulsatile flow Bessel 解 | 主动脉横截面速度剖面随相位变化 |
| 29 | river-meanders | 长江弯道; Mississippi 平原蜿蜒 | 弯道波长 $\lambda \approx 7$-$10$ × 河宽 (Leopold-Wolman 1957) | A. Einstein 1926 (河岸冲刷与茶叶) — 物理学家 | 二次螺旋流 + 冲刷外岸 + 沉积内岸 | 河弯道俯视 + 横截面螺旋流 |
| 30 | microfluidics | 芯片实验室 100 μm channel, PCR 集成片 | $Re \sim 0.01$; Pe = $UL/D$; 混合靠分子扩散 | George Whitesides 1990s (PDMS soft lithography) | Stokes regime, $\nabla p = \mu \nabla^2 \mathbf u$ | 芯片俯视 + 三个通道 T 型混合, 标 $Re$ 极低 |

---

## 本卷易踩的坑

- 不要把 NS 写成纯张量数学. 第 7 节要把 NS 还原成 "时间 + 对流 = 压力 + 黏性 + 体力", 给微小流体元的图.
- 不要在第 4 节 (浴缸涡) 把 Coriolis 当主因 — Shapiro 1962 已经证明 Coriolis 太弱, 浴缸涡的初始角动量才是主因, 必须明说.
- 不要在第 21 节 (转捩) 直接跳到 K-S 方程或现代理论. Reynolds 1883 那个染料管才是物理直觉.
- 第 25 节 (CFD) 必须 mention Richardson 1922 那次失败的手算 — 6 小时的天气他算了 6 周, 错得离谱, 这是数值天气史最有戏剧性的开端.
- 不要把 "湍流" 写成 "复杂", 写出可写的部分 (Kolmogorov 谱) 和不可写的部分 (regularity), 边界要清楚.

---

## 颜色

`vol-8-fluids/style.css` 已经设 `--accent`, 不要改. 卷色: 深水蓝/灰蓝 (像静水的蓝绿).

## slug → 文件 / 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 日常流动与尺度 | 01-sink-water.html ... 05-boundary-layer.html |
| 第 2 部分 · Navier-Stokes 直觉 | 06-continuity.html ... 10-vorticity.html |
| 第 3 部分 · 涡与不稳定 | 11-smoke-rings.html ... 15-mixing.html |
| 第 4 部分 · 飞行与冲击 | 16-sail-lift.html ... 20-nozzles.html |
| 第 5 部分 · 湍流与计算 | 21-transition.html ... 25-cfd.html |
| 第 6 部分 · 大尺度流体 | 26-weather-flow.html ... 30-microfluidics.html |

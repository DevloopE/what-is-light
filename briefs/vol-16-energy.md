# Vol 16 · 能量是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-16-energy/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

能量 = 守恒 + 不可逆 + 工程边界. 30 节按 6 部分:

1. 形式与守恒: KE / PE, 功, 功率, 守恒, 耗散
2. 热力学一二律: 1st 律, entropy, Carnot, refrigerator, heat pump
3. 储能: 电池, 燃料, 电容, 电网, 储能
4. 转换: 引擎, 涡轮, 制动 / 回收, 火箭, 效率
5. 自然界能量: 太阳, 水, 风, 光合, 地球能量预算
6. 边界: 100 W 人体, 食物 calorie, 永动机, exergy, 未来

每节落到一个具体设备 / 数值 (Wh, J, η) + 一位有名字的人.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "1 kg 汽油 ~46 MJ; 1 kg 锂电 ~1 MJ; 1 kg 浓缩铀 (3.5%) ~3 TJ — 三个能量密度量级. 一台 Carnot 热机在 800 K → 300 K 之间最大效率 62.5%, 真实热电厂 ~40%. 人体 BMR 100 W ≈ 一支白炽灯泡, 一天用 8.6 MJ ≈ 2000 kcal. SpaceX Raptor 引擎比冲 380 s, $\dot m = 800$ kg/s, 单台推力 2.3 MN. 这一卷把'能量'从 $\tfrac12 m v^2$ 一路走到 Landauer 的 $kT \ln 2$ 信息能量极限, 终点是为什么永动机 (一类 + 二类) 都不可能, 以及 exergy 的会计."

---

## 30 节具体 brief

### 第 1 部分 · 形式与守恒

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | kinetic-potential | 30 km/h 撞墙的车 = 4 m 高坠落 | $\tfrac12 mv^2 = mgh$; 50 km/h 7.9 m | Leibniz 1686 *vis viva*; Émilie du Châtelet 1740 ($\tfrac12 mv^2$) | KE / PE 守恒 | 摆 + 高度 / 速度互换 |
| 02 | work | 推 1 kg × 1 m × 1 m/s² = 1 J | $W = F \cdot d$; 单位 N·m = J | Coriolis 1829 (work 一词); Joule 1843 | $W = \int F \, dx$ | 力 - 位移图积分 |
| 03 | power | 100 W 灯 vs Tesla 350 kW; 1 hp = 745.7 W | $P = dW/dt$; 单位 W; 1 hp = 33000 ft·lb/min (Watt 1782) | James Watt 1782 (hp 一词); SI Watt 1889 命名 | average vs instant | 功率 vs 时间, 不同设备对比 |
| 04 | conservation | 摆守恒; 蒸汽机功 = 热的等价 | Joule 1843 paddle 实验, $1\,\mathrm{cal} = 4.184\,\mathrm{J}$ | James P. Joule 1843; Mayer 1842 | 第一律 $\Delta U = Q - W$ | Joule paddle 设备图 |
| 05 | dissipation | 滑动摩擦 → 热; 汽车 60 km/h 急刹热量 ~150 kJ | $W_{\rm fric} = \mu N d$; KE 全转化 | Rumford 1798 (boring cannon → 热) | 不可逆做功 → 内能 + 热 | 摩擦 + 热释放 + 不可逆 |

### 第 2 部分 · 热力学一二律

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | first-law | 焦耳 paddle 实验确立等价 | $\Delta U = Q + W$ (W on system convention) | Mayer 1842, Joule 1843, Helmholtz 1847 | 能量守恒 = 第一律 | 蒸汽机能量平衡 |
| 07 | entropy-energy | 1 mol 冰融化 $\Delta S = 22$ J/K at 273 K | $dS = \delta Q_{\rm rev}/T$; Boltzmann $S = k\ln W$ | Clausius 1865 entropy 一词; Boltzmann 1877 | 第二律 $\Delta S \ge 0$ | 冰融化温度 - 熵图 |
| 08 | carnot | Carnot 800 K → 300 K 上限 62.5%; 实际 ~40% | $\eta_C = 1 - T_c/T_h$ | Sadi Carnot 1824 *Réflexions sur la puissance motrice du feu* | 可逆 = 上限 | Carnot 循环 PV / TS 图 |
| 09 | refrigerator | 1 kW 用电搬 3 kW 热 | $\mathrm{COP} = Q_c/W$; ideal $\mathrm{COP}_{\rm ideal} = T_c/(T_h - T_c)$; 100 K 寒冷难做 | Carl von Linde 1876 ammonia compression | 反向 Carnot | 制冷循环 + COP 公式 |
| 10 | heat-pump | 1 kW 电搬 3-4 kW 热进屋 | $\mathrm{COP}_{\rm heat} = T_h/(T_h-T_c)$ | Lord Kelvin 1852 提议; 现代 Mitsubishi 1980s | 反向 Carnot 用于 heating | 热泵循环 + COP |

### 第 3 部分 · 储能

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | battery | Li-ion ~250 Wh/kg, $10^7$ J/kg = 1/30 汽油 | Li 半反应 -3.04 V vs SHE; 全电池 ~3.7 V | Volta 1800 first battery; Whittingham 1976 Li-S; Goodenough 1980 LiCoO2 (Nobel 2019) | 电化学 cell 自由能 → 电能 | Li-ion 充放电过程 |
| 12 | fuel | 汽油 46 MJ/kg, 氢 142 MJ/kg, 锂电 1 MJ/kg, 铀 80 TJ/kg | volumetric vs gravimetric energy density | Faraday 1831 EM induction → 燃料 vs 电池起源 | combustion ΔH | 各类燃料能量密度对比柱状 |
| 13 | capacitor | supercap 5 Wh/kg < battery 但功率密度高 | $E = \tfrac12 CV^2$; supercap 几秒充放 | Becker 1957 first 超级电容 | 物理过程, 双层电容 | supercap vs battery 能量 / 功率密度图 |
| 14 | grid | 中国 PEAK 1.4 TW; 美国 ~1 TW; transmission 765 kV | 长距离 HVDC 损 ~3% per 1000 km; AC 60 Hz / 50 Hz | Tesla AC 1888 vs Edison DC; HVDC 1954 Sweden-Gotland | $P = VI \cos\phi$ | 电网层级 + 频率同步 |
| 15 | storage | pumped hydro 90+%, 全球 96% storage 是 PSH; battery 现 < 5% | PSH ~150 GWh max; Li-ion 现 cumulative < 10 GWh | Bath County PSH (US) 24 GWh largest | 上下池 + 抽水 / 发电 | PSH 示意 + 能量平衡 |

### 第 4 部分 · 转换

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | engine | 内燃机 30%, diesel 40%, 涡轮 60%; Carnot 上限随 T | Otto cycle vs Diesel cycle | Otto 1876 4-stroke; Diesel 1893 | PV 图 + 循环面积 = work | Otto / Diesel PV 循环 |
| 17 | turbine | 燃气涡轮 turbine inlet 1500°C, η ~ 38%; combined cycle 60% | Brayton cycle | Frank Whittle 1937 jet engine | Brayton + Rankine 双循环 | 燃气涡轮 + 蒸汽涡轮 串联 |
| 18 | braking | Tesla regen 70 kW typical; 60 km/h to 0 回收 50% KE | $W_{\rm brake} = \tfrac12 m v^2$; battery 接收效率 ~90% | first regen 1900 Krieger 电动车 | KE → 电能 (反向 motor) | 加速 / 制动 / 再生能量流 |
| 19 | rocket-energy | Saturn V $\Delta v = 11.2$ km/s; LH2/LOX $I_{sp} = 450$ s | rocket eq $\Delta v = I_{sp} g_0 \ln(m_0/m_f)$ | Tsiolkovsky 1903 rocket eq | mass ratio + Isp | Saturn V 三级 + Δv 累加 |
| 20 | efficiency | 钨丝灯 ~ 5% to visible; LED ~30%; metabolism 25% | $\eta = $ useful out / energy in | Joule 1840s — efficiency 概念 | various device η | 各类设备效率柱状对比 |

### 第 5 部分 · 自然界能量

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | solar | Earth 接 1361 W/m² 太阳常数; 单晶硅 PV 22%, 多晶 16% | Shockley-Queisser 上限 33% single junction | Becquerel 1839 photovoltaic; Bell Labs 1954 first Si cell | semiconductor 带隙 + photon | spectrum + Si 吸收 |
| 22 | hydro | 三峡 22.5 GW, 750 m³/s × 80 m head; 全球 16% 电力 | $P = \rho g Q h \eta$; η > 90% | Nikola Tesla / Westinghouse 1895 Niagara | $P = \rho g Q h$ | 水电站 + 水头 |
| 23 | wind-energy | Vestas 15 MW turbine, blade 115 m | Betz 上限 16/27 = 59.3%; 实际 45% | Albert Betz 1919 power coefficient limit | $P = \tfrac12 \rho A v^3$ | turbine + power curve |
| 24 | photosynthesis-energy | 地球年 photosynthesis 输出 ~120 GtC, ~ 130 TW | 量子效率单光子 ~ 100%; 整株 ~1-2% solar | Engelmann 1882 (波长依赖); Calvin 1950 dark reaction | C 固定 + Z scheme + ATP | 全球光合产量 + 食物链 |
| 25 | earth-energy | Earth 内热 47 TW; 太阳辐射 174 PW (3700×) | tidal 3 TW + radiogenic + primordial | Lord Kelvin 1862 wrong age estimate; Holmes 1913 with radioactivity | radiogenic + primordial heat | 地球能量预算 pie |

### 第 6 部分 · 边界

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | body-100w | 人 BMR 100 W, daily 2000 kcal = 8.6 MJ | active 200-1000 W; 大脑 20 W | Atwater 1899 calorimetry | $E = $ basal + activity + thermic | 人体能量分配 pie |
| 27 | food-calorie | 1 g 脂肪 9 kcal, 蛋白 4, 碳水 4; 食品 calorie = kcal | Atwater 系数 | Atwater 1900 USDA | combustion calorimeter (bomb) | bomb calorimeter 设备 |
| 28 | perpetual-motion | 一类违反 1st 律, 二类违反 2nd 律, 美国专利局自 1911 拒收 | 历史 attempts; Maxwell demon Bennett 1982 反驳 | Bessler 1715 (出名骗子); USPTO ban 1911 | violation of laws | 几个永动机骗局 + 失败原因 |
| 29 | exergy | 100 J 高 T 热 vs 100 J 低 T 热不等价 | exergy = available work; cold reservoir 也有 | Rant 1956 exergy 一词; Szargut 1980s | $\Phi = (U - U_0) + p_0(V-V_0) - T_0(S-S_0)$ | 同 J 不同 T 热的 work potential |
| 30 | energy-future | 全球 ~18 TW 总能耗; 2050 30-50 TW; 100% solar 需 ~ 0.3% land area | $1.7\times 10^5$ TW 太阳达地; 0.01% 可解决 | IEA scenarios; David MacKay 2008 *Sustainable Energy* | sustainable budget | 能源消费 + 太阳预算 + 占比 |

---

## 本卷易踩的坑

- 第 1 节 (KE/PE): 必须 mention Émilie du Châtelet 1740 的 $\tfrac12 mv^2$ — 她比 Newton/Leibniz 都晚, 但她的版本直接对接现代 KE 定义.
- 第 8 节 (Carnot): Sadi Carnot 1824 *Réflexions* 写于 28 岁, 死于 1832 (霍乱) — 这本书几乎决定了热力学第二律走向. 必须给历史.
- 第 11 节 (battery): Goodenough Nobel 2019 时 97 岁, 是 Nobel 历史最年长得主. mention.
- 第 23 节 (wind): Betz 1919 给的 16/27 上限是流体力学结果, 不是热力学. 这个数字必须给.
- 第 28 节 (perpetual motion): USPTO 自 1911 起不收永动机申请. 历史 fact.

---

## 颜色

`vol-16-energy/style.css` 已设. 卷色: 能量金黄.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 形式与守恒 | 01-kinetic-potential.html ... 05-dissipation.html |
| 第 2 部分 · 热力学一二律 | 06-first-law.html ... 10-heat-pump.html |
| 第 3 部分 · 储能 | 11-battery.html ... 15-storage.html |
| 第 4 部分 · 转换 | 16-engine.html ... 20-efficiency.html |
| 第 5 部分 · 自然界能量 | 21-solar.html ... 25-earth-energy.html |
| 第 6 部分 · 边界 | 26-body-100w.html ... 30-energy-future.html |

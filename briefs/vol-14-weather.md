# Vol 14 · 天气是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-14-weather/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

天气 = 旋转流体 + 辐射 + 水循环, 不可预测窗口约 10 天. 30 节按 6 部分:

1. 大气结构: 气压, 辐射平衡, 递减率, 湿度, 云
2. 风的物理: 压差, Coriolis, geostrophic, 海陆风, jet stream
3. 大尺度环流: Hadley, 信风, 季风, Rossby, ENSO
4. 水循环: 对流, 雨, 雪, 闪电, 彩虹
5. 极端: 气旋, 飓风, 龙卷, 暴潮, 闪电
6. 预报与气候: 混沌可预测性, 数据同化, 气候 vs 天气, 强迫, 反馈

每节落到一个具体现象 (湾流、Hadley、龙卷) + 一个具体数 (m/s, hPa, K) + 一位有名字的实验家.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "中纬度站立 1 m² 上方有 10000 kg 的空气柱重 — 这是 1013 hPa 的气压. Earth 接 1361 W/m² 太阳常数, 反照率 0.3, 吸 240 W/m² 平衡到 -18°C 黑体温度; 实际表面 +15°C 是温室气体的 33 K 增量. 飓风 Katrina 2005 内 30 m/s 风, 中央眼 905 hPa, 释放每秒 ~10¹⁴ W 的潜热. 这一卷把'天气'从一杯水的 evaporation 一直带到 ECMWF 9 km 全球预报. 终点是 Lorenz 1963 的 butterfly attractor 与 Hasselmann 2021 Nobel — 气候 = 天气的统计极限."

---

## 30 节具体 brief

### 第 1 部分 · 大气结构

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | atmosphere-weight | 1 m² 上 10000 kg; 标准大气 1013.25 hPa | $p = \rho g h$; 气压随高度 $p(z) = p_0 e^{-z/H}$; $H \approx 8.4$ km | Torricelli 1643 (water + mercury 双管); Pascal 1648 Le Puy de Dôme | barometric formula | 高度 - 气压指数衰减曲线 |
| 02 | radiation-balance | Earth 接 1361 W/m², 反 30%, 吸 240 W/m² | 黑体 $T = (S/(4\sigma))^{1/4} = 254$ K = -19°C; 实际 +15°C, 温室增 33 K | Joseph Fourier 1824 (温室气体首次假说), Tyndall 1859 (CO2/H2O 红外吸收实验) | $\sigma T^4$ + 反照率 + 温室 | 入辐射 / 出辐射 / 反射 平衡盘 |
| 03 | lapse-rate | 干绝热 9.8°C/km; 湿绝热 ~6°C/km | $\Gamma_d = g/c_p = 9.8$ K/km; 实际平均 ~6.5 K/km | Hadley 1735 提及, Brunt 1934 (Brunt-Väisälä) | adiabatic 上升 + cooling | 干 / 湿 / 实际三条递减率曲线 |
| 04 | humidity | 30°C 饱和水汽 30 g/m³, 0°C 仅 5 g/m³ → 凝露 | Clausius-Clapeyron $de_s/dT = L_v e_s/(R_v T^2)$; 7%/K | Magnus 1844 saturated vapor formula | 蒸气压 + 露点 | $e_s(T)$ 曲线 + 露点示意 |
| 05 | cloud-white-weather | 云为何漂浮; 不是悬浮空中, 而是上升流支撑 | 云水滴 5-50 μm; 终端 v ~ 1-30 cm/s | Aitken 1880 (cloud condensation nuclei) | upward 0.1-1 m/s 流支撑下沉 | 云内上升流 + 水滴下沉 |

### 第 2 部分 · 风的物理

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | wind | 东京到悉尼 9000 km, 一万米高 jet stream 西到东 ~50 m/s | 表面风 $v \sim 5$-$15$ m/s; jet stream 30-100 m/s | Rossby 1939 风带分类 | 压差驱动: $\rho \dot u = -\nabla p$ | 全球地表风向气候图 |
| 07 | coriolis | 旋转参考系下水平运动右偏 (北半球) | $f = 2\Omega \sin\phi$; 中纬度 $\phi=45°$ → $f = 1.03\times 10^{-4}$ /s | Gaspard-Gustave Coriolis 1835 | $\mathbf F_C = -2 m \boldsymbol\Omega \times \mathbf v$ | 旋转盘上飞行轨迹 + Coriolis 偏转 |
| 08 | geostrophic | 大气大尺度: 压差与 Coriolis 平衡, 风沿等压线 | $u_g = -1/(\rho f) \partial p/\partial y$; 1 hPa/100 km × $f$ → 几 m/s | Buys-Ballot 1857 (背风站立, 低压在左, 北半球) | $f \mathbf k \times \mathbf u = -\nabla p/\rho$ | 等压线 + 风向沿线箭头 |
| 09 | sea-breeze | 白天海风; 夜间陆风; 反差 ~5°C 驱动 | 海陆 T 差驱动 5-10 m/s; 周期 24 hr | Halley 1686 trade wind 论文; sea breeze 1700s | 局地热对流 + 反向 | 白天 / 夜晚 海陆温差驱动两幅 |
| 10 | jet-stream | jet stream 9-12 km 高, 50-150 m/s 西风; 北极 + 副热带两支 | 北半球 polar jet ~60°N, subtropical ~30°N | Rossby 1939 (jet 一词); WWII 美军轰炸机首次发现 | 极地高低层温度梯度 + thermal wind | 全球大气 jet 高度 + 速度 |

### 第 3 部分 · 大尺度环流

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | hadley-cells | 赤道暖空气上升 → 30° 下沉 → 信风带; 中纬度 Ferrel cell; polar cell | Hadley cell 0-30°, ITCZ 上升; 信风 5-10 m/s 东北 (北) | George Hadley 1735 *Concerning the Cause of the General Trade-Winds* | 旋转流体 → 三胞 | 三胞 + 表面信风 + 高空 |
| 12 | trade-winds | 东北 / 东南 trade winds 是 Columbus 1492 横渡大西洋的发动机 | 5-15° N/S 持续 5-10 m/s | Halley 1686 第一张 trade wind 全球图 | Coriolis 偏转 上升后下沉空气 | trade wind 全球图 + 哥伦布航线 |
| 13 | monsoon | 印度季风夏 (SW) / 冬 (NE); 反转每年 6 月 / 10 月 | 6-9 月降雨 ~75% 全年; 反转有 1 周 |  Halley 1686 (海陆温差解释); Webster 1980s detailed dynamics | 季节海陆温差 → 巨型海陆风 | 印度夏 / 冬季风路径对比 |
| 14 | rossby-waves | 高空西风带的大尺度波动 + jet meander | 波长 ~6000 km, 周期 7-14 天 | Carl-Gustaf Rossby 1939 (β-plane theory) | $\beta = df/dy$; Rossby 波 phase speed $c = U - \beta/k^2$ | 北半球 500 hPa 高空波 |
| 15 | el-nino | ENSO 周期 2-7 年; 厄尔尼诺 ~0.5°C+ in Niño 3.4 区 | El Niño peak: 太平洋东部 +2°C; 全球温度回应 ~0.1°C | Bjerknes 1969 ENSO mechanism | Walker 循环 weakening + 温跃层 east-west tilt | 太平洋 normal vs El Niño SST + 风 |

### 第 4 部分 · 水循环

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | convection | 夏天午后雷阵雨; 强对流 plume rise 10 km in 30 min | CAPE > 1000 J/kg → 对流; updraft 20-50 m/s | Rayleigh 1916 (Rayleigh-Bénard); Bjerknes 1937 air mass | 浮力 + 上升凝结释能 | thunderstorm cell 三阶段 |
| 17 | rain | 雨滴形成: 凝结核 → 1 mm 雨滴需 collision-coalescence ~30 min | Bergeron-Findeisen ice + supercooled water; warm cloud collision | Wegener 1911 (ice mechanism), Bergeron 1933 | 雨滴形成两机制 | 雨滴大小分布 + 形成时间线 |
| 18 | snowflakes | 六瓣对称; 形态依赖 T 与饱和度 (Nakaya 1936 morphology diagram) | -15°C, 高饱和 → dendrite; -5°C 平面 prism; -20°C 柱状 | Wilson Bentley 1885 (5000 张照片); Ukichiro Nakaya 1936 实验合成 | 冰晶生长 各向异性 + Mullins-Sekerka 不稳定 | Nakaya morphology diagram |
| 19 | lightning | 闪电电压 ~10⁸ V, 电流 30 kA; T ~30000 K | 1 strike 5×10⁹ J; 全球 ~50 闪/s | Franklin 1752 (kite 实验); Charles Wilson 1908 (cloud 电荷分离) | 电荷分离 + breakdown 击穿 | 雷雨云电荷分布 + stepped leader |
| 20 | rainbow-weather | 双虹: 主虹 42°, 副虹 51°; 颜色顺序反转 | 滴 ~1 mm; 主虹 1 内反射, 副虹 2 内反射 | Descartes 1637 主虹几何; Newton 1704 *Opticks* 副虹 | 两次反射 → angle shift | 双虹形成几何 |

### 第 5 部分 · 极端天气

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | cyclone | 中纬度低压系统直径 ~2000 km, 寿命 ~5 天 | front 系统 + warm sector; 形成 ~3 km/s baroclinic | Bjerknes 1922 cyclone model (挪威派) | baroclinic instability | 中纬度气旋 cold/warm front 锋面 |
| 22 | hurricane-spin | Katrina 2005 直径 700 km, 中心 905 hPa | Coriolis 必需; 北半球逆时针; 形成于 SST > 26.5°C | Riehl 1948 hurricane theory; Emanuel 1986 max intensity | $f$ + 潜热释放 + 角动量守恒 | 飓风结构: 眼 / 眼壁 / 螺旋雨带 |
| 23 | hurricane-energy | 飓风每秒释放 6×10¹⁴ W ~ 200× 全球电力 | $\sim 10^{19}$ J 一次飓风; 主能源是凝结潜热 | Emanuel 1991 *The theory of hurricanes* | Carnot-like thermal engine: SST → tropopause | 飓风 Carnot 循环 |
| 24 | tornado | EF5 龙卷 200-300 mph (90-135 m/s); 中心 ~80 hPa lower | 直径 50-3000 m; 寿命数分钟 | Tornado Alley; Fujita 1971 scale | mesocyclone → 涡度集中 | 母 mesocyclone + 子 tornado 涡度集中 |
| 25 | storm-surge | Sandy 2012 NYC +3.4 m surge; Katrina 8.5 m | 气压低 1 hPa = 1 cm 海面升; 风 stress 主因 | Galveston 1900 hurricane (4000 死) | atmospheric pressure + wind stress + 波浪 | 飓风 + 海面升 + 海岸冲击 |

### 第 6 部分 · 预报与气候

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | forecast-chaos | 7-10 天可预测极限 (大尺度) | Lyapunov $\lambda \sim 0.4$/day → 误差倍增 ~1.7 day | Edward Lorenz 1963 (蝴蝶效应), Eady 1949 baroclinic | $\delta x(t) = \delta x(0) e^{\lambda t}$ | Lorenz 三方程 + 双吸引子 |
| 27 | data-assimilation | ECMWF 每 6 hr 用 100 万 satellite + radiosonde 观测同化 | 4D-Var, 集合 Kalman; analysis 误差 ~ 0.5 K | Lorenz 1965, Kalman 1960 | 模型 + 观测 → posterior state | 同化流程 + ensemble |
| 28 | climate-vs-weather | 天气 = 一次实现, 气候 = 30 年统计 | climatology 30 年 WMO 标准; 单年与气候 30+ 年偏离 | von Storch & Zwiers 1999 *Statistical Analysis in Climate Research* | 天气 trajectory vs 气候 distribution | 多年温度散点 + 统计分布 |
| 29 | climate-forcing | CO2 350 → 420 ppm, +1.1 K 全球 | radiative forcing $\Delta F = 5.35 \ln(C/C_0)$ W/m²; 2× CO2 → +3.7 W/m² | Arrhenius 1896 第一估算 +5°C, IPCC AR6 2021 | 强迫 → 平衡气候敏感度 (ECS 2-5 K) | CO2 上升 + 温度上升对照曲线 |
| 30 | feedbacks | 冰反照率, 水汽, 云三大反馈 | 水汽放大 ~2×; ice-albedo + ; 云反馈 ±不确定 | Manabe & Wetherald 1967, Hasselmann 1976 (Nobel 2021) | 反馈系数 $\Delta T = \lambda \Delta F$, $\lambda$ 含反馈 | 三反馈分解 + 总 climate sensitivity |

---

## 本卷易踩的坑

- 第 4 节 (humidity) 必须给 Clausius-Clapeyron 的 7%/K 经验律, 这是热浪 / 强降雨增多的物理根.
- 第 7 节 (Coriolis): Coriolis 不是 force, 是参考系效应. 写时要明说.
- 第 22 节 (hurricane): 飓风的能源是凝结潜热, 不是风, 不是太阳直接辐射. 必须明说 Carnot-like engine.
- 第 26 节 (chaos): Lorenz 1963 的 attractor 不是 metaphor, 是真实的天气方程截断后的解. 给三方程.
- 第 30 节 (feedbacks): Hasselmann 2021 Nobel 的工作就是把"天气噪声 + 气候慢驱动"分开. 必须 mention.

---

## 颜色

`vol-14-weather/style.css` 已设. 卷色: 天空蓝 / 云灰.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 大气结构 | 01-atmosphere-weight.html ... 05-cloud-white-weather.html |
| 第 2 部分 · 风的物理 | 06-wind.html ... 10-jet-stream.html |
| 第 3 部分 · 大尺度环流 | 11-hadley-cells.html ... 15-el-nino.html |
| 第 4 部分 · 水循环 | 16-convection.html ... 20-rainbow-weather.html |
| 第 5 部分 · 极端天气 | 21-cyclone.html ... 25-storm-surge.html |
| 第 6 部分 · 预报与气候 | 26-forecast-chaos.html ... 30-feedbacks.html |

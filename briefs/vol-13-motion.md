# Vol 13 · 运动是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-13-motion/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

经典力学的内核 = 守恒律 + 作用原理 + 混沌. 30 节按 6 部分:

1. 描述运动: 位移、速度、加速度、自由落体、抛体
2. 力与守恒: Newton 三律, 摩擦, 功-能, 动量, 质心
3. 旋转: 台球、弹跳、转动、角动量、陀螺
4. 振荡: 弹簧、单摆、阻尼、共振、本征模
5. 引力运动: 圆轨道、Kepler、逃逸、潮汐、岁差
6. 高级语言: 最小作用量, 相空间, 三体, 混沌, 实验感觉

每节落到一个具体物体 (台球、单摆、卫星、陀螺) + 一个具体数 (g=9.81, T=2π√(L/g), GM_⊕ ...) + 一位有名字的人.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "Galileo 在比萨斜塔上扔铁球与木球 (传说真伪不论, 他的斜面实验是真的), 第一次量出 $g \approx 9.81$ m/s² 的常数. 1687 年 Newton 把月球绕地球的 27.3 天周期与苹果落地连起来, 给出反平方律. 单摆的 $T = 2\pi\sqrt{L/g}$ 在 17 世纪 Huygens 给出, 一直用到 1967 才被铯钟接管. 三体问题在 1887 年被 Poincaré 证明无解析解 — 现代意义的混沌从此诞生. 这一卷把'运动'从一个抛物线一直带到 Lyapunov 指数, 终点是最小作用量原理 — Newton 表述只是 $\delta S = 0$ 的一面."

---

## 30 节具体 brief

### 第 1 部分 · 描述运动

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | position-time | 罢车上记录 GPS 轨迹: 每 1 s 一个 $(x,y)$ 点 | GPS 精度 ~ 5 m; 高速公路 30 m/s | Galileo 1638 *Two New Sciences* | $\mathbf r(t)$ 描述 + 速度位移图 | $x(t)$ 时序 + 速度斜率 |
| 02 | velocity | 100 m 跑 9.58 s = 平均 10.4 m/s; 峰值 12.4 m/s (Bolt) | km/h, m/s 换算; 平均 vs 瞬时 | Galileo 斜面实验 | $v = dx/dt$ | Bolt 100 m 速度曲线 |
| 03 | acceleration | F1 加速 0-100 km/h in 1.7 s ≈ 1.7 g | $a = dv/dt$; 9.81 m/s² 是地面常用单位 | Galileo $v \propto t, x \propto t^2$ | uniform vs nonuniform $a$ | F1 加速曲线 + 9.81 m/s² 标注 |
| 04 | free-fall | Apollo 15 月球上锤子 + 羽毛同时落 1.62 m | $g_{\rm Moon} = 1.62$ m/s²; 真空中 $a = g$ 不论质量 | Galileo (传说), Apollo 15 1971 (David Scott 实验) | $h = \tfrac12 g t^2$ | Apollo 15 真实视频 + 时序 |
| 05 | projectile | 球抛出 45° 距离最大; 体育里 30-35° 因为人体 launch 角不同 | $R = v^2 \sin 2\theta/g$; 45° 给最大 R | Tartaglia 1537 (军事炮弹), Galileo 抛物线证明 | 解耦水平 / 垂直 | 抛物线 + 45° vs 30° vs 60° 距离对比 |

### 第 2 部分 · 力与守恒

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | newton-laws | $F = ma$ 是定义还是定律? | 力的单位 $1\,\mathrm{N} = 1\,\mathrm{kg \cdot m/s^2}$ | Newton 1687 *Principia* | $\mathbf F = d\mathbf p/dt$ | 三律的图解: 静止 / F=ma / 反作用 |
| 07 | friction | 鞋底胶橡皮 $\mu_s \approx 0.7$, 冰 $\mu_s \approx 0.05$ | $F_f \le \mu_s N$; kinetic 通常稍小 | Coulomb 1781 friction law | $F_f = \mu N$, 与接触面无关 (粗略) | 滑块 + 法向 + 摩擦力 |
| 08 | work-energy | 1 J = 1 N·m; 推 1 kg 物 1 m 用 1 N → 1 J | $W = \int F \cdot dx$; KE $= \tfrac12 m v^2$ | Joule 1843 mechanical equivalent of heat | $W = \Delta KE$ | 力 - 位移积分 + KE 增量 |
| 09 | momentum | 1 kg 球 10 m/s 与 0.01 kg 球 1000 m/s 同动量 | $p = m v$; 子弹 7g × 850 m/s ≈ 6 kg·m/s | Descartes 1644 提出 (但用错), Newton 修正 | 守恒: 闭系 $\sum p =$ const | 弹性碰撞 + 非弹性碰撞 |
| 10 | center-of-mass | 高跳运动员的质心可以低于横杆 (Fosbury flop) | $R_{\rm cm} = \sum m_i r_i / \sum m_i$ | Archimedes 杠杆 + 重心; Fosbury 1968 Olympic | 质心运动遵守 Newton 不论物体形变 | Fosbury flop + 质心轨迹低于横杆 |

### 第 3 部分 · 旋转与碰撞

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | billiards | 母球击 8 球, 90° 分开 (理想弹性 + 等质量) | 弹性碰撞分析 + 切线 / 法线分量 | Coriolis 1835 *Théorie mathématique des effets du jeu de billard* | 等质量弹性 90° 分裂 | 母球击中 + 9 球散开角度 |
| 12 | bounce | 篮球弹性系数 e ≈ 0.75; 高尔夫球 e ≈ 0.78 | restitution $e = v_a'/v_a$; 弹回高度 $h' = e^2 h$ | Newton 1687 (Newton's experimental rule) | 能量损失 $1-e^2$ 比 | 球 bounce 高度衰减序列 |
| 13 | rotation | 地球赤道周长 4×10⁷ m, 自转一周 86400 s → 463 m/s | $\omega = 2\pi/T$; 切向 $v = \omega r$ | Galileo 自转地球的力学一致性 | $I, L, \omega$ | 地球赤道速度 + 不同纬度 cos 因子 |
| 14 | angular-momentum | 花样滑冰收手, 旋转加速 5x | $L = I\omega$ 守恒; 收手 $I$ 减小 5 倍 → $\omega$ 增 5 倍 | Newton (隐含); Euler 1758 rigid body | $\dot L = \tau$ | 滑冰开闭手对照 + I 与 ω |
| 15 | gyroscope | 陀螺仪在 cockpit 用作姿态参考 | 进动角速度 $\Omega = mgr/(I\omega)$; 100 g 旋转 100 Hz 下 mg 进动 ~rad/min | Foucault 1852 gyroscope (从摆推断地球自转) | $\dot L = \tau$ → 进动 | 陀螺 + 重力 + 进动方向 |

### 第 4 部分 · 振荡

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | spring | 1 kg 挂 1 N/m 弹簧, T = 6.28 s | $T = 2\pi\sqrt{m/k}$; F=-kx Hooke's law | Hooke 1660 "ut tensio sic vis" (anagram 1676) | SHO solution $x(t) = A\cos(\omega t)$ | 弹簧 + 振幅 + 周期 |
| 17 | pendulum | 1 m 单摆 T = 2.006 s; Foucault 摆 67 m 长 | $T = 2\pi\sqrt{L/g}$; large-amplitude correction $T(\theta_0) = T_0(1 + \theta_0^2/16 + ...)$ | Galileo (青年比萨教堂吊灯), Huygens 1656 第一台精确摆钟 | 小角近似 + 修正 | 单摆 + 周期公式 + 修正 |
| 18 | damping | 振动钟摆衰减时间常数 ~分钟; Q = 100 | $\ddot x + 2\gamma\dot x + \omega_0^2 x = 0$; underdamped/critical/overdamped | Stokes 1851 viscous damping | $Q = \omega_0/(2\gamma)$ | 三种衰减情形振幅 vs 时间 |
| 19 | resonance-motion | Tacoma Narrows 1940 桥 vortex shedding 共振倒塌 | frequency match → amplitude blow-up; Q × force amplification | Tacoma 1940; mechanical resonance Galileo 注意到 | 受迫 SHO + 共振峰 | 共振响应曲线 + Tacoma 桥摆动照片 |
| 20 | normal-modes | 双弹簧二球: 同相 + 反相两个本征模 | 模式频率 $\omega_\pm = \sqrt{k/m \pm k_{12}/m}$ | Lagrange 1762 small oscillations | 矩阵对角化 → 本征模 | 二球三弹簧 + 两个本征模动作 |

### 第 5 部分 · 引力运动

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | orbit | ISS 在 400 km 高轨, 速度 7.66 km/s, 周期 92 min | $v = \sqrt{GM/r}$; 圆轨道 | Newton 1687 月球验证反平方律 | 圆轨力 = 引力 | 圆轨示意 + 速度 / 半径 |
| 22 | kepler | 第三律 $T^2 \propto a^3$; 太阳系内行星全部对得上 | $a^3/T^2 = GM_\odot/(4\pi^2)$; 地球 1 AU/1 yr | Kepler 1609/1619 (用 Tycho 数据) | 三大律 | 椭圆轨道 + 焦点 + 等面积 |
| 23 | escape | 地球表面逃逸速度 11.2 km/s; 月球 2.4 km/s | $v_e = \sqrt{2GM/R}$; 与 $\sqrt 2$ × 圆轨速度 | Newton 1687 (Newton's cannon thought experiment) | 能量 KE = U | 速度从 圆轨 → 椭圆 → 抛物 → 双曲 |
| 24 | tides-motion | 月球潮汐 0.5 m, 太阳潮 0.2 m; 月地距离 3.84×10⁸ m | $\Delta g \propto M/d^3$; 月球虽小但近, tidal effect dominates | Newton 1687 潮汐解释 | tidal force ≠ gravity, 而是其梯度 | 地球椭圆 + 双 tidal bulge |
| 25 | precession-motion | 春分点岁差周期 26000 年; Earth 转轴进动 | $\Omega_{\rm prec} = (3GM/2\omega R^3) \cdot$ 系数 | Hipparchus 公元前 134 年发现; Newton 给出原因 | 转轴在引力场里 LSF (类陀螺) | 地球转轴在大圆上 26000 年 |

### 第 6 部分 · 高级语言

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | least-action | 光走最短光程; 粒子走 $S = \int L\,dt$ 极小 | $L = T - V$; Euler-Lagrange $\partial L/\partial q - d/dt(\partial L/\partial \dot q)= 0$ | Maupertuis 1744 提出 (有点神学), Euler 1744 严格化, Lagrange 1788 现代 | $\delta S = 0$ | 多条路径 + 真实路径 stationary |
| 27 | phase-space | 单摆相空间椭圆; 各能量层级一族椭圆 | Liouville: 相空间体积守恒; symplectic 结构 | Hamilton 1834, Liouville 1838 | $H(p,q)$, Hamilton 方程 | 单摆相轨迹 + saddle point at top |
| 28 | three-body | Apollo 自由返航轨道靠 Earth-Moon 三体平衡; Lagrange 点 5 个 | $L_4, L_5$ 稳定; 木星 Trojan asteroids | Lagrange 1772 5 点; Hill 1878 月球理论 | restricted three-body + Jacobi integral | 5 个 Lagrange 点 + 等势面 |
| 29 | chaos | Lorenz 1963 三方程蝴蝶 attractor; pendulum chaotic at large amplitude | Lyapunov exponent λ > 0 → chaos; sensitive to initial conditions | Henri Poincaré 1887 (3-body 大奖论文); Edward Lorenz 1963 | $\delta x(t) \sim \delta x(0) e^{\lambda t}$ | 双摆相图 + 蝴蝶 attractor |
| 30 | everyday-experiments | 厨房物理: 煎蛋翻面, 砸鸡蛋, 弹珠盘 | 11 个厨房经典: 喝水时杯里水转圈, 倒水的水流压扁等 | Pomeau / Berry 推动 amateur physics | 简单系统给非平凡现象 | 5 个厨房物理小实验拼图 |

---

## 本卷易踩的坑

- 第 6 节 (Newton's laws) 必须深究 $F = ma$ 是定义还是定律. Mach 1883 的批评至今仍 relevant — 别避开这个哲学问题.
- 第 17 节 (单摆) 给小角近似 $T = 2\pi\sqrt{L/g}$ 之外, 必须给大幅修正项 $1 + \theta_0^2/16 + ...$ — 否则 Foucault 摆精度不准.
- 第 19 节 (共振) Tacoma Narrows 真实原因不只是 vortex shedding, 是 aeroelastic flutter, 但教学里通常归共振. 写时要说明.
- 第 26 节 (least-action) Maupertuis 1744 提出时带神学色彩, Euler 1744 同年独立严格化 — 这是历史钩子.
- 第 29 节 (chaos): Poincaré 1887 是真正起点, Lorenz 1963 是现代发现 — 两人都要 mention.

---

## 颜色

`vol-13-motion/style.css` 已设. 卷色: 动感橙红 / kinetic orange.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 描述运动 | 01-position-time.html ... 05-projectile.html |
| 第 2 部分 · 力与守恒 | 06-newton-laws.html ... 10-center-of-mass.html |
| 第 3 部分 · 旋转与碰撞 | 11-billiards.html ... 15-gyroscope.html |
| 第 4 部分 · 振荡 | 16-spring.html ... 20-normal-modes.html |
| 第 5 部分 · 引力运动 | 21-orbit.html ... 25-precession-motion.html |
| 第 6 部分 · 高级语言 | 26-least-action.html ... 30-everyday-experiments.html |

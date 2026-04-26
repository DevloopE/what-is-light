# Vol 10 · 颜色是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-10-color/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名 / index.html / style.css 不要改.

## 卷主轴

颜色不是波长, 是波长在视网膜与大脑里的投影. 30 节按 6 部分:

1. 光谱与眼睛: 颜色 ≠ 波长, 锥细胞, 色盲, 白光, 颜色恒常
2. 大气光学: 彩虹, 蓝天, 落日, 云白, 偏振天
3. 显示与印刷: RGB / CMYK, 颜料, 印刷, 显示色域, 相机色彩
4. 金属与结构色: 金属反射, 黄金颜色, 蝴蝶 / 孔雀, 薄膜, 光子晶体
5. 发光机制: 荧光, 磷光, 黑体颜色, LED, 化学发光
6. 自然界与度量: 叶绿素, 动物色, 伪装, 虹彩, 颜色测量

每节落到一种具体物质 / 动物 / 设备 + 一个具体波长或 ΔE 数值 + 一位有名字的实验家.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "1666 年 Newton 把一束阳光放进三棱镜, 得到从红到紫的光谱; 但'颜色'其实不在那束光里, 而在你视网膜上三种锥细胞的相对兴奋度上. 同一波长的钠灯 589 nm 在 Tokyo 黄昏的街上看是橙黄, 拿一张白纸做参照后又被你的大脑校准回'白'. 孔雀的羽毛只有黑棕两种色素却闪出蓝绿, 因为里面是 1D 光子晶体, 周期 145 nm 像 X 射线衍射但反过来对可见光. 这一卷把'颜色'拆成五层: 谱、视、材、构、心 — 走过 380-780 nm 的可见波段, 走过 LMS 三色空间, 走过孔雀羽与黄金的色源, 终点是 ΔE = 2.3 这种'人眼能分辨的最小色差'."

---

## 30 节具体 brief

### 第 1 部分 · 光谱与眼睛

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | spectrum-color | Newton 1666 棱镜实验, 第一次证明白光由多颜色组成 | 可见光 380-780 nm; 钠 D 线 589.0/589.6 nm 双线 | Isaac Newton 1666 *Opticks* 公开 1704 | 折射 + 色散 $n(\lambda)$ | 棱镜分光路径 + 各色折射角 |
| 02 | cone-cells | 视网膜中央凹 6×10⁶ 锥细胞, S/M/L 比例约 1:5:10 | S 峰 ~420 nm, M ~534, L ~564; rod ~498 nm scotopic | George Wald 1955 (Nobel 1967), Gunnar Svaetichin 1956 锥反应曲线 | LMS 三激励空间, 颜色感知 = $(L,M,S)$ 矢量 | 三条响应曲线 + 一个钠 589 nm 点的激励向量 |
| 03 | color-blindness | 8% 男性 / 0.4% 女性 X 染色体上的 opsin 基因突变 | M 缺 (deuteranomaly): 红绿混淆; L 缺 (protanopia) | Dalton 1798 自述 (死后基因测出他是 deuteranope) | X-linked recessive opsin 基因 (OPN1MW, OPN1LW) | Ishihara 测试图 + 基因图 |
| 04 | white-light | 'D65 白': 6500 K 日光; 钨丝 2700 K 暖黄 | CIE Illuminant D65 spectrum; 色温 K 与黑体辐射对应 | CIE 1931 制定标准光源 | 颜色匹配函数 $\bar x(\lambda), \bar y(\lambda), \bar z(\lambda)$ | 三种光源谱 (D65, A 钨丝, F2 荧光) 对比 |
| 05 | color-constancy | 同一张白纸在黄灯下仍看成白; 但相机会拍成黄 | 大脑做"白平衡": 利用全局亮度调整 | Edwin Land 1971 retinex 理论 (Polaroid 创始人) | retinex algorithm | 同张白纸三种光源 + 大脑修正 + 相机不修正对比 |

### 第 2 部分 · 大气光学

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | rainbow | 雨后东方天空的 42° 主虹 + 副虹 | 主虹 42° red 外沿, 副虹 51°; 二次内反射使副虹颜色反转 | René Descartes 1637 *Discours de la Méthode* 附录 (用几何 + Snell 计算 42°) | $\theta_{\rm rainbow} = 4 \arcsin(\sin\theta_i/n) - 2\theta_i$ 极小 | 一滴水的光路 + 两次折射 + 一次内反射 |
| 07 | blue-sky | 中午天为何蓝; 1869 年 Lord Rayleigh 给出答案 | Rayleigh 散射截面 $\sigma \propto 1/\lambda^4$; 紫光 / 红光 ratio = $(700/400)^4 \approx 9.4$ | Lord Rayleigh 1871 *On the Scattering of Light* | $\sigma \propto \lambda^{-4}$, 大气分子尺度 $\ll \lambda$ | 太阳光 + 散射方位与波长依赖图 |
| 08 | sunset | 落日为何红; 沿 1000 km 大气路径 | 路径长度比中午 ~38×; 蓝光被散射掉, 红光透过 | Tyndall 1859 散射比 Rayleigh 早 | 短波被沿途多次散射移走, 长波相对保持 | 日落角度 + 大气路径长度 + 谱滤波示意 |
| 09 | cloud-white | 云为何白, 和 Rayleigh 不一样 | 水滴 5-50 μm $\gg \lambda$ → Mie 散射, 几乎无波长选择 | Gustav Mie 1908 (球散射全解析解) | Mie 散射 size parameter $x = 2\pi r/\lambda$ | Mie 散射相位函数 + 不同 $x$ 三条曲线 |
| 10 | polarized-sky | 蓝天 90° 离太阳处偏振度最高 (~75%) | $P = \sin^2\theta/(1+\cos^2\theta)$ for Rayleigh; 偏振墨镜利用此 | Arago 1809 polarimetry; Vikings 用方解石定位太阳 | Rayleigh 散射 induced dipole 偏振 | 太阳 - 观察者 - 散射点 + 90° 处偏振方向 |

### 第 3 部分 · 显示与印刷

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | rgb-cmyk | 屏幕 R 700, G 546, B 436 (sRGB primaries) | sRGB 色域三角形覆盖 ~35% CIE 1931, Rec.2020 ~ 76% | Maxwell 1861 三色摄影 (世界第一张彩色照片, 苏格兰格子带) | 加色 (RGB) vs 减色 (CMY); 颜色匹配 $C = R\bar r + G\bar g + B\bar b$ | CIE 1931 色度图 + sRGB / Rec.2020 / Pointer 色域 |
| 12 | pigments | 朱砂 HgS 红色 ~620 nm 反射, 蓝铜矿 azurite 蓝色 | 矿物颜料波段宽; 现代 phthalocyanine 蓝色更纯 | Romans 用 Egyptian Blue (CaCuSi₄O₁₀); 18 世纪合成 Prussian Blue 1706 | 价电子带间跃迁 + d-d 跃迁 (有色过渡金属) | 矿物切片 + 反射谱 + 跃迁 level scheme |
| 13 | printing | 报纸网点印刷; CMYK 4 色 + 抖动 | 网点 150-300 lpi; 4 色减色重叠近黑色 | Senefelder 1796 lithography; 20 世纪 4 色制版 | 减色: $\rm white - cyan = red$ 等 | 网点放大图 + CMYK 重叠区 |
| 14 | display-gamut | sRGB vs DCI-P3 vs Rec.2020 在彩色三角形里的覆盖 | sRGB ~ 35%, DCI-P3 ~ 53%, Rec.2020 ~ 76% of CIE 1931 | DCI-P3: SMPTE EG 432-1 (digital cinema 2005) | 色域顶点 = primary 颜色 chromaticity | CIE 1931 色域三角形对比 |
| 15 | camera-color | Bayer filter 50% G, 25% R, 25% B; 模仿人眼对绿敏感 | Bayer pattern 1976 Eastman Kodak | Bryce Bayer 1976 (Kodak) | demosaicking 算法 + 颜色矩阵 RGB → sRGB | Bayer filter 像素阵列 + demosaic 流程 |

### 第 4 部分 · 金属与结构色

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | metallic | 银白 Ag, 金黄 Au, 铜红 Cu — 自由电子 + 带间跃迁 | Ag plasma freq ~ 9 eV, Au ~ 5 eV; 黄金黄因 5d→6s 跃迁吸收 ~2.5 eV | Drude 1900 (free electron model) | $\epsilon(\omega) = 1 - \omega_p^2/\omega(\omega + i\gamma)$ | Ag/Au/Cu 反射率 vs 波长曲线 |
| 17 | gold-color | 黄金为何黄, 银为何白 — 相对论效应 | Au 5d 与 6s 间隔被相对论收缩, 吸收 480 nm 蓝光 | Pyykkö 1979 relativistic chemistry | $E_{5d \to 6s}$ 因 contraction 落入可见 | Au / Ag 能级图 + 反射光谱 |
| 18 | structural-color | 蓝色蝴蝶 (Morpho), 翅膀只有黑棕色素 | 翅膀脊上层片间距 ~70 nm + 折射率差 → bragg 470 nm | Hooke 1665 *Micrographia* 已观察孔雀羽 | thin film + multi-layer interference | Morpho 鳞片 SEM + 周期结构 + bragg |
| 19 | thin-film | 肥皂泡彩色; 油膜彩色 | $2 n d \cos\theta = (m + \tfrac12)\lambda$ for destructive of one polarization | Young 1801 干涉; Newton 1675 colors of thin plates | 薄膜干涉 | 肥皂泡 + 厚度变化的干涉色带 |
| 20 | photonic-crystal | 蛋白石 opal 是 SiO₂ 球的 fcc 堆积, 周期 200-300 nm | 周期 = $\lambda/(2n)$ 给可见反射; 蛋白石虹彩 | Yablonovitch 1987, John 1987 photonic bandgap | 1D / 2D / 3D 周期介电常数 → 光带隙 | opal SEM 球堆积 + 反射光谱 |

### 第 5 部分 · 发光机制

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | fluorescence | 绿色荧光蛋白 GFP excite 488 nm → emit 507 nm | Stokes shift ~19 nm; 寿命 ns | Stokes 1852 (萤石); Shimomura 1962 GFP 自水母 (Nobel 2008) | 激发 → 振动弛豫 → 发射, 总能量损失为 Stokes shift | Jablonski 图 + GFP 激发 / 发射谱 |
| 22 | phosphorescence | 夜光涂料 ZnS:Cu 持续发光数小时 | 寿命 ms - hours; 三重态禁戒跃迁 | Le Bel 1888 (long persistence luminescence) | 单重态 → 三重态 ISC → 慢辐射 | Jablonski 图含 ISC + 时间衰减曲线 |
| 23 | blackbody-color | 钨丝灯 2700 K 暖黄, 太阳 5800 K 白, 蓝巨星 30000 K 蓝 | Wien 位移 $\lambda_{\max} T = 2.898\times 10^{-3}$ m·K | Wien 1893, Planck 1900 | $B(\nu, T) = (2h\nu^3/c^2)/(e^{h\nu/kT}-1)$ | 不同 T 黑体谱 + 色温线在 CIE 图上 |
| 24 | led | 蓝 LED InGaN 芯片 1993 中村修二 | 蓝 460 nm + YAG:Ce 黄磷光 → 白 LED; 效率 > 100 lm/W | Shuji Nakamura 1993 (Nobel 2014) | 半导体直接带隙 → 电致发光 | InGaN 量子阱 + Y3Al5O12:Ce 磷光 + 复合谱 |
| 25 | chemiluminescence | 萤光棒 luminol + H2O2 + 催化剂 蓝 425 nm | 量子产率 ~1%; 持续 几小时 | Albrecht 1928 luminol; 萤火虫 luciferin/luciferase Harvey 1947 | 化学反应 → 激发态 → 发射 | luminol 反应路径 + 发射谱 |

### 第 6 部分 · 自然界与度量

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | green-leaf | 叶绿素 a 吸 430/662 nm, 反射 550 nm 绿 | photosynthesis 量子产率 ~100% per absorbed photon | Engelmann 1882 prism 实验 (光合作用波长依赖) | 叶绿素 a, b 吸收谱与 PSI/PSII 反应中心 | 叶绿素谱 + 太阳谱叠加 + "绿窗"反射 |
| 27 | animal-color | 鸟类四色觉; 紫外线视觉; 章鱼色盲却变色 | 鸟有 UV 锥 (~365 nm); 蜜蜂 UV-绿-蓝 三色 | Burkhardt 1989 鸟类 UV 视觉 | tetrachromacy 提升判别能力 | 鸟眼锥曲线 + 雄鸟羽毛在 UV 下的图样 |
| 28 | camouflage | 比目鱼皮肤 mottling 在 1 s 内匹配底色; 头足类不需借色觉 | 章鱼皮 chromatophore 1 mm² ~30 个; 颜色变化 < 100 ms | Hanlon & Messenger 1996 *Cephalopod Behaviour* | chromatophore + iridophore + leucophore 三层 | 章鱼皮显微 + 三层细胞 |
| 29 | iridescence | 钞票全息防伪; 蝴蝶翅膀; 孔雀羽角度色 | 角度变化 30° → 反射峰移 100 nm | 自然: Hooke 1665, Boyle 1664; 钞票 hologram 1980s | Bragg-mirror 角度依赖 $m\lambda = 2nd \cos\theta$ | 看角度变换的彩色变化连续序列 |
| 30 | color-measurement | 工业 CIELAB ΔE 阈值: ΔE < 1 几乎不可分辨, ΔE ≈ 2.3 是 just noticeable | ΔE 计算 (CIE76 / CIE94 / CIE2000); 印刷验收 ΔE < 4 | CIE 1976 LAB 色彩空间 | $L^*, a^*, b^*$ 与 perceptual uniformity | LAB 色立体 + ΔE 圆 |

---

## 本卷易踩的坑

- 第 1 节: 颜色 ≠ 波长. 这一点在第一句就要明白告诉读者. 不要让 Newton 棱镜实验给读者错觉.
- 第 17 节 (gold-color): 黄金黄是相对论效应, 这是物理课很少讲的有趣事实, 要 mention Pyykkö 1979.
- 第 18 节 (structural-color): Morpho 蝴蝶翅膀的色素只是黑棕, 蓝色完全来自结构. 这一点反直觉, 必须明说.
- 第 23 节 (blackbody-color): 色温 K 与黑体的对应不是 metaphor, 是物理上钨丝 2700 K 真的是黑体辐射. 要把 Planck 公式 + Wien 位移给出.
- 第 30 节 (measurement): ΔE = 2.3 是 just-noticeable 的工业标准, 给具体数才有用.

---

## 颜色

`vol-10-color/style.css` 已设 `--accent`. 不要改. 卷色: 鲜艳品红 / 玫红 (像晚霞 / Magenta).

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 光谱与眼睛 | 01-spectrum-color.html ... 05-color-constancy.html |
| 第 2 部分 · 大气光学 | 06-rainbow.html ... 10-polarized-sky.html |
| 第 3 部分 · 显示与印刷 | 11-rgb-cmyk.html ... 15-camera-color.html |
| 第 4 部分 · 金属与结构色 | 16-metallic.html ... 20-photonic-crystal.html |
| 第 5 部分 · 发光机制 | 21-fluorescence.html ... 25-chemiluminescence.html |
| 第 6 部分 · 自然界与度量 | 26-green-leaf.html ... 30-color-measurement.html |

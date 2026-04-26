# Vol 12 · 看见是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-12-seeing/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

"看见" = 光学 + 神经 + 推断. 30 节按 6 部分:

1. 眼的光学: 角膜 / 晶状体, 调节, 屈光不正, 像差, 瞳孔
2. 视网膜与神经: 感光细胞, 持续视觉, 颜色恒常, 边缘检测, 盲点
3. 深度与运动: 立体视, 视差, 焦距深度, 光流, 视错觉
4. 显微: 放大率, Abbe 极限, phase contrast, 荧光显微, 超分辨
5. 望远: 望远镜, 角分辨, 自适应光学, 干涉仪, 太空望远镜
6. 现代成像: CMOS sensor, 全息, CT, 反卷积, 信息看见

每节落到一种具体仪器 / 现象 + 一个具体光学/角度数 + 一位有名字的人.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "人眼瞳孔 2-8 mm, 视网膜中央凹 1.5 mm 直径, 但里面塞了 15 万个锥细胞. 一个清晨的晴朗天空里, 你能看到 6 等星 — 那是从 100 光年外射来的、已经稀释到每秒约 100 个光子打进瞳孔. Hubble 太空望远镜口径 2.4 m, 在 540 km 高轨道上仍受 Rayleigh 衍射极限约束, 不能分辨小于 0.05" 的细节. STED 显微镜 2014 年拿了 Nobel 化学奖, 因为它把 Abbe 1873 推出的 $d = \lambda/(2\mathrm{NA})$ 极限破到 30 nm. 这一卷把'看见'从角膜的 0.3 mm 厚到 Hubble 的 2.4 m 镜面摊开, 终点是 holography 与 phase retrieval — 我们看到的不只是光强, 还有相位."

---

## 30 节具体 brief

### 第 1 部分 · 眼的光学

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | eye-camera | 眼 vs 单反相机的物理对照 | 角膜 +43 D, 晶状体 +20 D, 总 +60 D ≈ 17 mm 焦距 | Christoph Scheiner 1619 (眼底成像首次描绘) | 复合透镜 + 像距固定 | 眼剖 + 主要光焦度贡献 |
| 02 | accommodation | 看远看近: 睫状肌使晶状体改形 | accommodation amplitude: 20 yr ~10 D, 50 yr ~2 D, 70 yr ~0.5 D | Helmholtz 1855 调节理论 | 改晶状体曲率 → 焦距 | 调节 vs 年龄曲线 + 晶体形变 |
| 03 | myopia | 近视: 眼轴过长; 屈光过强 | 眼轴 24 mm 正常, 27 mm = -3 D 近视; 全球患病率上升 | Donders 1864 屈光分类; 现代户外活动论 | 近视 = parallel rays focus 在视网膜前 | 三种眼 (正常 / 近视 / 远视) 光路 |
| 04 | aberration | 球差 / 色差 / 离焦; 角膜 K 值 | Zernike 多项式分解; 高阶像差 ~ 0.1 D RMS | Seidel 1856 五大像差 | $W(r,\theta) = \sum c_{nm} Z_n^m$ | Zernike 模式头几个 (defocus/astig/coma/spherical) |
| 05 | pupil | 瞳孔 2-8 mm; 衍射 + 像差权衡 | 最佳分辨在 ~3 mm pupil; Airy disk $\theta = 1.22\lambda/D$ | Helmholtz 1856 视觉光学 | bright/dark adaptation; sphincter / dilator muscle | 瞳孔在亮暗下尺寸 + 衍射极限 vs 像差曲线 |

### 第 2 部分 · 视网膜与神经

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | photoreceptor | 视杆 1.2×10⁸, 视锥 6×10⁶; 中央凹仅锥 | 视杆灵敏度 ~ 1 photon (阈值 ~ 5 photons / 100 ms 内 5 个杆) | Selig Hecht 1942 (单光子探测) | rhodopsin photo-isomerization 11-cis → all-trans | 视杆 / 视锥分布密度 + 中央凹 |
| 07 | persistence | 24 fps 电影, 60 Hz 灯不闪 | 临界融合频率 CFF ~ 50-60 Hz at high luminance, ~10 Hz at low | Plateau 1829 phenakistoscope; Nipkow 1884 disc | 视网膜响应 ~ 50 ms 整合 | 帧率 vs CFF + 持续视觉示意 |
| 08 | color-constancy-seeing | 黄路灯下白纸仍看白; Mondrian 实验 | 色度恒常: 全局光照减去, 物体反射保留 | Edwin Land 1971 retinex | retinex 算法; 大脑做局部相对计算 | 同张图三种光源下 + 大脑校正 |
| 09 | edge-detection | Mach bands; lateral inhibition | center-surround receptive field; ganglion cell 类型 ON/OFF | Hartline 1938 horseshoe crab eye (Nobel 1967) | DoG (difference of Gaussians) | 中心-旁侧抑制 + 边界处 firing rate 突起 |
| 10 | blind-spot | 视神经盘处无光感; 大脑填补 | 盲点 ~5° 大, 在中央凹偏 15° | Mariotte 1668 第一发现 | 大脑 fill-in 机制 | 一只眼测试图 + 盲点位置 |

### 第 3 部分 · 深度与运动

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | stereo | 双眼间距 65 mm 给立体视; 大脑做 disparity | 立体阈值 ~5 arcsec at 1 m → 深度阈值 ~1 mm | Wheatstone 1838 stereoscope | $\Delta = b f / d$ for far disparity | 两眼 + 同一目标 + 投影到两视网膜 |
| 12 | parallax | 移动头部, 近物相对远物移得快 | 月亮视差 ~57' (1 度 = 60'); 1 AU 视差 = 1 角秒 = 1 parsec | Friedrich Bessel 1838 (61 Cyg parallax 0.314") | 三角法 distance | 视差测量与距离反比 |
| 13 | focus-depth | 模糊圈 (CoC) 与景深; 单眼也有 focus-depth cue | f/2 lens 景深 短, f/22 景深 长; CoC 0.03 mm 标准 | Renaissance 画家 chiaroscuro | $DoF = 2NC/(f^2/u)$ | 不同光圈下景深图 |
| 14 | optical-flow | 走路时周围向后流; 飞鸟用此控制 landing | optical flow $\dot\theta = v/d$; landing 时 $\tau = \theta/\dot\theta$ 时间常数 | Gibson 1950 ecological perception | $\tau = $ time-to-contact | optical flow field + 中心 expansion + 边缘 outflow |
| 15 | illusions | Müller-Lyer; Café wall; Necker cube; 旋转蛇 | 错觉揭示视觉系统假设 | Müller-Lyer 1889 | 局部计算 vs 全局 + 假设违反 | 三个经典错觉图 |

### 第 4 部分 · 显微

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | magnification | 复合显微镜 = 物镜 × 目镜; 1665 Hooke *Micrographia* 第一次画出 cork cell | 物镜 100×, 目镜 10× → 1000× | Antonie van Leeuwenhoek 1670s 单透镜 270× 第一次看到细菌 | 透镜组合 magnification | 复合显微镜光路图 |
| 17 | abbe-limit | 1873 Abbe 推出 $d = \lambda/(2 \mathrm{NA})$; 20× NA 0.4 → 760 nm | NA = $n \sin\theta$, 油镜 NA 1.4 → 200 nm at 550 nm | Ernst Abbe 1873 (Zeiss 工厂理论部) | $d_{\min} = \lambda/(2\mathrm{NA})$ | 衍射极限示意 + 双点能否分辨 |
| 18 | phase-contrast | Zernike 1932 phase contrast 把透明细胞变可见 | 相位差 $\pi/2$ 偏移到 amplitude | Frits Zernike 1932 (Nobel 1953) | 相位环 + 检偏振 | 透明 → 相位环 → 可见对比 |
| 19 | fluorescence-microscope | GFP + 激光 488 nm + 滤色片 → 单蛋白可视 | 灵敏度: 单分子 detection (TIRF) | Shimomura 1962 GFP, Tsien 设计 mutant 1995, Chalfie 表达活体 (Nobel 2008) | 激发 / 发射光路分离 | 荧光显微光路 + 激发 / 发射 / 滤镜 |
| 20 | super-resolution | STED 30 nm; PALM/STORM 单分子定位 20 nm | 突破 Abbe 1873 极限 ~10×; 2014 Nobel 化学 | Hell (STED 1994), Betzig (PALM 2006), Moerner (single mol) (Nobel 2014) | 非线性 / 单分子定位 | STED 双激光 + donut 抑制 |

### 第 5 部分 · 望远

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | telescope | Galileo 1609 折射 30×; Newton 1668 反射 | 现代 KECK 10 m, ELT 39 m, JWST 6.5 m | Galileo 1609; Newton 1668 (Cambridge) | $M = f_o/f_e$ refractor | Galileo / Newton / Cassegrain 三种光路 |
| 22 | angular-resolution | Hubble 0.05" at 550 nm | $\theta = 1.22\lambda/D$ Rayleigh; D 越大越好 | Rayleigh 1879 criterion | 衍射限分辨 | Airy 模式 + 双星分辨 |
| 23 | adaptive-optics | 凯克 AO 校正大气湍流, ground-based 接近 diffraction-limited | wavefront sensor + DM 1 kHz feedback | Babcock 1953 提出, Beckers 1980s 实现 | wavefront sensing + deformable mirror | AO 闭环 + 校正前 / 后 PSF |
| 24 | interferometry | VLT 4 望远镜组合, 100 m 等效基线; Event Horizon Telescope 2019 拍到 M87* | 等效分辨 = $\lambda/B$, B = baseline; EHT 230 GHz × 10000 km baseline | Michelson 1920 first stellar interferometry (Betelgeuse 直径) | 干涉合成: aperture synthesis | 多镜阵列 + uv 平面采样 + 重建图 |
| 25 | space-telescope | Hubble 1990, JWST 2021/12, Roman 2027 | JWST L2 轨道, 6.5 m, 0.6-28 μm; HST 2.4 m, UV-NIR | Spitzer 2003 IR; Lyman Spitzer 1946 太空望远镜想法 | 无大气吸收 + 无散射光 + 稳定 | HST + JWST + Roman 比例对比 |

### 第 6 部分 · 现代成像

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | camera-sensor | iPhone CMOS 像素 1.7 μm; Bayer 50% G + 25% R + 25% B | 量子效率 ~ 80% peak; full well ~ 20000 e- per pixel | Boyle & Smith 1969 CCD (Nobel 2009) | photodiode → charge → ADC | 像素截面 + 微透镜 + Bayer + ADC |
| 27 | hologram | Gabor 1948 holography; 激光 → 1960s 实用 | 信用卡 hologram 表面浮雕 grating; 全息片记录振幅 + 相位 | Dennis Gabor 1948 (Nobel 1971); Leith & Upatnieks 1962 激光 | 物波 + 参考波 干涉 → 记录 | 记录 + 重现两幅光路图 |
| 28 | ct | CT 1971 Hounsfield; 1979 Nobel | 螺旋 CT 0.5 mm slice; 1 mGy ~ 1/100 自然剂量 | Cormack 1963 (math); Hounsfield 1971 (EMI 实物机) | Radon 变换 + filtered back-projection | X 射线 360° 扫描 + 逆 Radon |
| 29 | deconvolution | 望远镜 / 相机 模糊 = PSF 卷积; 反卷积恢复 | 维纳滤波 SNR 阈值; Lucy-Richardson 迭代 | Wiener 1942; Lucy 1974, Richardson 1972 | $g = h * f + n$ → 反演 | 模糊图 / PSF / 反卷积结果三幅 |
| 30 | seeing-information | "看见" = 光强 + 相位 + 推断; phase retrieval, light field | Lytro plenoptic camera; ptychography 60 nm at 1 nm wavelength | Gerchberg-Saxton 1972 phase retrieval | 物体 = 光场 + 推断 | "光场" 概念 + 相位 / 振幅分离 |

---

## 本卷易踩的坑

- 第 1 节 (eye-camera) 不要把眼写成 "完美相机". 眼有像差, color fringing, 有盲点, 视网膜还反着挂. 这些是关键差异.
- 第 17 节 (Abbe limit) 不要绕开 NA 定义 $n\sin\theta$, 给具体数字 200 nm at NA 1.4.
- 第 20 节 (super-res) 必须 mention 2014 Nobel 化学奖三位 (Hell, Betzig, Moerner) 与 STED + PALM 两路线.
- 第 24 节 (interferometry) 要 mention EHT 2019 拍到 M87 黑洞影 — 最具标志性的当代天文成果.
- 第 27 节 (hologram) 必须 mention Gabor 1948 与 Leith-Upatnieks 1962 激光出现后的实用化.

---

## 颜色

`vol-12-seeing/style.css` 已设. 卷色: 暮色紫蓝 / 视觉系冷调.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 眼的光学 | 01-eye-camera.html ... 05-pupil.html |
| 第 2 部分 · 视网膜与神经 | 06-photoreceptor.html ... 10-blind-spot.html |
| 第 3 部分 · 深度与运动 | 11-stereo.html ... 15-illusions.html |
| 第 4 部分 · 显微 | 16-magnification.html ... 20-super-resolution.html |
| 第 5 部分 · 望远 | 21-telescope.html ... 25-space-telescope.html |
| 第 6 部分 · 现代成像 | 26-camera-sensor.html ... 30-seeing-information.html |

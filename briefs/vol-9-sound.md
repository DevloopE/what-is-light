# Vol 9 · 声音是什么? — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-9-sound/`. 30 个 HTML 文件已经存在 (低质量旧稿), **逐节按下表重写正文**, 文件名 / index.html / style.css 不要改.

## 卷主轴

声音是介质里的纵波. 30 节按 6 部分:

1. 波的物理: 速度、强度、阻抗、拍频
2. 声源: 嗓音、弦、管、鼓、音色
3. 房间与心理: 房间模式、混响、音乐厅、回声、噪声控制
4. 运动 & 极端: Doppler、超声、声纳、激波声、蝙蝠
5. 信号与压缩: Fourier 在耳朵里, 采样, MP3, 回声 / 噪声消除
6. 边界: 非线性声、热噪声、听阈、次声、水下声

每节落到一个具体乐器/仪器/动物 + 一个具体频率或 dB 值 + 一位有名字的实验家.

---

## 卷引子 (覆盖 `index.html` 的 `<p class="intro">`)

> "1 m 外讲话耳膜被推动 $20\,\mu\mathrm{Pa}$ — 比一个大气压小八个量级, 比布朗噪声大两个量级, 这就是听阈. 一支长笛把 65 cm 空气柱按 264 Hz 的基频敲击, 一支单簧管同样长却给 132 Hz, 因为一端是闭管. Boston Symphony Hall 的 RT60 = 1.85 s 是 Wallace Sabine 1898 在 Harvard Fogg 美术馆里推出的方程的一个直接预测. 这一卷把声音从空气里的 $\Delta p$ 一路带到 1480 m/s 的水下、44.1 kHz 的 CD、20 kHz 的蝙蝠 chirp 与 0.01 Hz 的火山次声; 终点是耳蜗 32 mm 的 basilar membrane 上, 行波怎么把声压变成神经脉冲."

---

## 30 节具体 brief

### 第 1 部分 · 波的物理 (基础)

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | pressure-wave | 鼓面振动推动周围空气, 形成纵向疏密波 | $c_{\rm air, 20°C} = 343\,\mathrm{m/s}$; 经典阈值声压 $20\,\mu\mathrm{Pa}$ | Newton 1687 (估 $c \approx 290$ m/s 太低), Laplace 1816 (加 $\gamma$ 修正得正确值) | $c^2 = \gamma P/\rho = \gamma R T/M$; 一维波动 $\partial^2 p/\partial t^2 = c^2 \partial^2 p/\partial x^2$ | 鼓面位移 + 空气压缩稀疏带 + 一根波动方向上的 $p(x,t)$ |
| 02 | speed-of-sound | 钢轨贴耳听火车比空气先听见 | 钢 5100 m/s, 水 1480 m/s, 空气 343 m/s, 氦 1007 m/s (吸氦说话变高) | Biot 1809 (水中声速实验, 利用大炮在 Lake Geneva) | $c^2 = K/\rho$ (流体 bulk modulus), $c = \sqrt{E/\rho}$ (固体杨氏模量) | 三种介质中波速对比, 声波从一侧入到另一侧的 $c$ 变化 |
| 03 | loudness | 耳语 30 dB, 谈话 60 dB, 摇滚 110 dB, 喷气机 130 dB; 0 dB SPL = 阈值 | $\mathrm{dB} = 20\log_{10}(p/p_{\rm ref})$, $p_{\rm ref}= 20\,\mu\mathrm{Pa}$; 10 倍声压 = +20 dB | Bell Labs 1923 (定 dB), Fletcher-Munson 1933 等响曲线 | 声强 $I = p^2/(\rho c)$, $\mathrm{dB}_{\rm SIL} = 10\log_{10}(I/I_0)$ | 等响曲线网格 + 常见声源对应位置 |
| 04 | impedance | 在水下听岸上的人讲话几乎听不见 | 阻抗 $Z = \rho c$: 空气 415, 水 $1.5\times 10^6$ Pa·s/m; transmission $\approx -30\,\mathrm{dB}$ across air-water | Lord Rayleigh *Theory of Sound* 1877 (impedance concept) | $T = 4Z_1 Z_2/(Z_1+Z_2)^2$, 大失配几乎全反射 | 水/空气界面声波路径, 标反射 99.9%, 透射 0.1% |
| 05 | beats | 钢琴调音师用 beats: 两根弦失调 4 Hz 时一秒"颤"四下 | $f_{\rm beat} = \abs{f_1-f_2}$; 调音师常用 4-5 Hz beats for slightly stretched octave | Sauveur 1701 (acoustique 一词的发明者) | 两正弦叠加: $\cos\omega_1 t + \cos\omega_2 t = 2\cos\!\dfrac{\omega_1-\omega_2}{2}t \cos\!\dfrac{\omega_1+\omega_2}{2}t$ | 两正弦时序 + 包络 + 拍频频谱图 |

### 第 2 部分 · 声源

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | voice | 男声 F0 ~120 Hz, 女声 ~220 Hz; 声道 17 cm 的 quarter-wave resonance 决定 formant | 元音 /a/ F1 ~ 700 Hz, F2 ~ 1100 Hz; F1·F2 区分元音 | Helmholtz 1863, Gunnar Fant 1960 *Acoustic Theory of Speech Production* | source-filter 模型: 喉 source × 声道 filter | 声道侧剖 + 5 个元音的 F1-F2 散点图 |
| 07 | string | 小提琴 G 弦 196 Hz, 长 327 mm; 钢琴中央 C 261.63 Hz | $f = (1/2L)\sqrt{T/\mu}$; 钢琴 A4 弦 ~ 60-100 N tension | Marin Mersenne 1636 *Harmonie Universelle* (前现代乐律) | 一维弦驻波 $f_n = nf_1$; 谐波列 | 弦上 $n=1,2,3$ 驻波 + 五线谱里听到的谐波 |
| 08 | flute | 长笛 (两端开) vs 单簧管 (一端闭) 同长 65 cm 但单簧管低八度 | 开开 $f = nc/(2L)$, 闭开 $f = (2n-1)c/(4L)$; 开开 65 cm 中央 C ~ 264 Hz, 闭开 132 Hz | Bernoulli (Daniel) 1739 *Theoremata de oscillationibus*; Kundt 1866 用粉末测驻波 | 边界条件决定模式 | 两根管 + 内压力驻波: 长笛两端节, 单簧管一端腹一端节 |
| 09 | drum | timpani 可调音, snare 不能 — 圆膜本征频率比例非整数 | 圆膜 Bessel: $f_{01}:f_{11}:f_{21}:f_{02} = 1 : 1.59 : 2.14 : 2.30$; timpani 用 air loading 把比例修到接近 1:1.5:2 | Lord Rayleigh *Theory of Sound* vol.1 §200 (1877); Bessel 1824 | 二维波 Helmholtz $\nabla^2 \psi + k^2 \psi = 0$, Bessel $J_m$ | 鼓面 6 个本征模式云图 (几个节径 + 节圆) |
| 10 | timbre | 钢琴 A4 与小提琴 A4 同 440 Hz 听感不同 | 钢琴 ADSR: attack ~ 5 ms, sustain decay 数秒; 小提琴 attack 30-100 ms 持续可控 | Helmholtz 1863 (谐波分解 + Helmholtz 共鸣腔验证), Stumpf 1890 心理声学 | 频谱包络 = timbre; ADSR 包络 = 时序 timbre | 钢琴 / 小提琴 / 长笛 A4 的频谱叠加图 |

### 第 3 部分 · 房间与心理

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | room-modes | 卧室某个位置 60 Hz 低音突然很强 | $f_{lmn} = (c/2)\sqrt{(l/L_x)^2 + (m/L_y)^2 + (n/L_z)^2}$; 4×3×2.5 m 房间最低轴向模 43 Hz | Schroeder 1954 (Schroeder frequency 把模式与统计声学分开) | 三维 standing wave 本征频率 | 矩形房间内三个轴向模式压力云 |
| 12 | reverberation | Boston Symphony Hall RT60 = 1.85 s; 录音棚 0.3 s | Sabine: $T = 0.16 V/A$; 经典值: 演讲 0.5-1.0 s, 室内乐 1.4-1.7 s, 大型交响 1.8-2.2 s | Wallace Sabine 1898 Harvard Fogg 美术馆 (3 年实验, 把座椅往各厅搬) | $T_{60}$ 是声压 $-60$ dB 衰减时间 | 衰减包络 + Sabine 公式分解 (体积 / 吸声面积) |
| 13 | opera-hall | Vienna Musikverein 1870 鞋盒型, 保守认为最好的厅之一 | 侧反射 ITDG ~ 20 ms 最佳, IACC < 0.5 给空间感 | Beranek 1962 *Music, Acoustics and Architecture* (排名 50 厅) | 厅形 + 吸声 + 散射 = 听感 | 鞋盒厅平面图, 直达 + 一次侧反射路径 |
| 14 | echo | 山谷距 50 m, 喊声 0.3 s 后听到 | 整合时间 ~50 ms 是融合 / 回声分界 (Haas effect) | Helmut Haas 1949 *Über den Einfluss eines Einfachechos* | 优先效应 + 70 ms 后才听成两声 | 双声源时序图 + 听觉融合 / 分离的曲线 |
| 15 | noise-control | 工厂 90 dB 戴耳塞降到 60 dB | 多孔吸声 ($\lambda/4$ 规则): 1 kHz ~ 8.5 cm 吸声层最优 | Sabine 1898 早期吸声系数表; ISO 11654 现代标准 | 流阻、共振、多孔三机制 | 吸声材料三类 + 频率响应曲线 |

### 第 4 部分 · 运动 & 极端

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | doppler | 救护车 80 km/h pass, 2 kHz siren 升降 ~110 Hz | $\Delta f / f = v/c$; 80 km/h ÷ 343 m/s = 6.5%; 2 kHz × 0.065 = 130 Hz total swing | Christian Doppler 1842 (Prague), Buys-Ballot 1845 火车实验验证 | 静源动观或动源静观: $f' = f(c\pm v_o)/(c\mp v_s)$ | 救护车 + 等相波面 (前密后疏), 听者两位置 |
| 17 | ultrasound | 孕妇 B 超用 5 MHz 探头, 在组织里 $\lambda \approx 0.3$ mm | $c_{\rm tissue} \approx 1540$ m/s; 分辨率 $\sim \lambda/2 \approx 0.15$ mm; 透深 $\sim 100\lambda$ | Wild & Reid 1949 第一台医用 ultrasound; Donald 1958 GE 公司 | 脉冲-回声: 距离 $= ct/2$ | B 超机 + 探头 + 反射回波时序 |
| 18 | sonar | WWI 法国 Langevin 1917 第一台主动声纳; SOFAR 通道 1 km 深 | active sonar 5-100 kHz; SOFAR $c_{\min} \approx 1490$ m/s 在 1000 m 深 | Paul Langevin 1917, Maurice Ewing 1944 (SOFAR for downed pilots) | 距离 = $ct/2$; 海洋折射使声线弯进通道 | 海剖面 + 声速 $c(z)$ + 声线在 SOFAR 通道里来回反射 |
| 19 | shock-sound | M16 突击步枪 muzzle 165 dB at 1 m; AK-47 子弹 715 m/s 超音速 | N-波时长 ~ 1 ms; 子弹 Mach cone 半角 $\sin\theta = 1/M = 1/2.1$ → 28° | Mach 1887 第一张 Schlieren 激波相片 | 强非线性激波: Rankine-Hugoniot | 枪 + N-波时序 + Mach cone |
| 20 | bat-echolocation | 蝙蝠 chirp 50-100 kHz 下扫, 持续 5-20 ms; 时间分辨 50 μs | $\tau \sim 1/B$; 20 kHz 带宽 → 50 μs 时间分辨 → 8 mm 距离分辨 | Lazzaro Spallanzani 1793 (蒙住眼睛仍能避障); Donald Griffin 1944 (echolocation 一词) | matched filter | 蝙蝠 + chirp 频时谱 + 回波时序 |

### 第 5 部分 · 信号与压缩

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | fourier-ear | 耳蜗 32 mm 长, 沿膜分布频率 — tonotopy | 高 f 在 base, 低 f 在 apex; 频率分布 $\sim$ logarithmic, 5 mm/octave | Helmholtz 1863 共鸣理论, Georg von Békésy 1928 行波模型 (Nobel 1961) | basilar membrane 行波 envelope 在每个频率有对应位置 | 耳蜗展开图 + 三个频率的行波包络位置 |
| 22 | sampling | CD 1982 Sony-Philips Red Book 选 44.1 kHz | $f_s \ge 2 f_{\max}$ Nyquist; 22 kHz 听阈上限 + 余量; 44.1 = $4\times 11025$ 兼容 NTSC PCM 录像 | Harry Nyquist 1928 Bell Labs, Claude Shannon 1949 | sampling theorem: 带限信号可由 $\ge 2B$ 采样完整重建 | 连续信号 + 采样 + sinc interpolation 重建 |
| 23 | mp3-audio | CD 1411 → MP3 128 kbps, 11:1 压缩听感几乎无损 | 同时掩蔽: 强信号 ±0.5 critical band 内 ~20 dB 掩蔽; 时间掩蔽 ~50 ms forward | Karlheinz Brandenburg 1980s Fraunhofer; ISO MPEG-1 Layer 3 1993 | psychoacoustic model + MDCT + Huffman | 频谱图 + 掩蔽阈值 + 被去掉的 sub-band |
| 24 | echo-cancel | VoIP 通话能消去自己听筒漏到话筒的回声 | adaptive filter 100-200 taps; convergence ~ 200 ms | M.M. Sondhi 1967 Bell Labs 自适应回声消除 | LMS: $w_{n+1} = w_n + \mu e_n x_n$ | 回声路径 + 自适应滤波器 + 误差反馈 |
| 25 | noise-cancel | 飞机舱内噪声 80 dB, ANC 耳机降到 50-60 dB | 反相 latency < 0.5 ms; 主要消 < 1 kHz | Paul Lueg 1936 (德国专利); Bose 1989 first commercial | feedforward + feedback adaptive control | 耳机内麦克 / 外麦克 + 控制器 + 反相波 |

### 第 6 部分 · 边界

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | nonlinear-sound | parametric 阵列 (audio spotlight), 用两束高强度超声合成 narrow-beam audio | 差频出 1-10 kHz, beam 宽 ~3°, 比 conventional speaker 窄 10× | Peter Westervelt 1963 (Brown Univ); Yoneyama 1983 first commercial | 非线性 NS, $\partial^2 p/\partial t^2 - c^2 \nabla^2 p = (\beta/\rho c^2) \partial^2 p^2/\partial t^2$ | 两超声源 + 差频区 + 窄音束图 |
| 27 | thermal-noise | 半 anechoic 室在 1 kHz 测出 -9 dB SPL 背景, 接近热极限 | 空气热噪声 floor $\sim 6\times 10^{-13}\,\mathrm{Pa^2/Hz}$; 20-20k Hz 总功率 $\sim -23$ dB SPL | Kittel & Kroemer Thermal Physics; 1990s anechoic 测量 | $\langle p^2\rangle = 4 k_B T \rho c \,\mathrm{Hz}$ | 频谱 floor 比照 Microsoft anechoic chamber 测量数据 |
| 28 | hearing-range | 人 20 Hz - 20 kHz, 老化高频快速损失; 鸟 100 Hz - 20 kHz, 蝙蝠 20-200 kHz | 50 岁人均 16 kHz 上限; 内毛细胞 phase-lock 至 4 kHz | Wever-Bray 1930 (耳蜗电位); 老化听力 NHANES 数据 | 频率上下限源于机械共振范围 | 不同物种听力曲线对比, 标常见年龄层人耳上限 |
| 29 | infrasound | Tonga 火山 2022/01/15 喷发, 全球次声 $\sim 0.01$ Hz, 7 圈地球 | 1 Hz wavelength = 343 m; 0.01 Hz $\lambda = 34$ km; CTBT IMS 60 站 | Maurice Ewing 1957 大气次声; CTBT 1996 | 长波在大气波导内传播 | Tonga 喷发后大气压全球波形图 |
| 30 | sound-underwater | 蓝鲸 14 Hz call, 180 dB at source, 1000 km 可听 | 声速 1480-1540 m/s; SOFAR 1 km 深 c-min; 衰减 0.05-1 dB/km @ 100 Hz | Maurice Ewing 1944 SOFAR; Roger Payne 1971 鲸 song | 海洋声波导 ray bending | 海洋 c(z) 剖面 + 声波在 SOFAR channel 里 zigzag |

---

## 本卷易踩的坑

- 不要把 dB 写成 "声音的对数" 之类抽象描述. 一定要写出 $p_{\rm ref}=20\,\mu\mathrm{Pa}$ 这个具体起点, 并解释它接近健康年轻人的听阈.
- 第 7 节 (string) 要明说音色不只是基频, 钢琴 A4 含 1, 2, 3, ... 谐波且不严格整数 (inharmonicity), Mersenne 1636 没看到的细节.
- 第 8 节 (flute) 的"开闭管八度差"是单簧管低八度的物理根, 别绕开.
- 第 22 节 (sampling) 的 44.1 kHz 历史一定要写: 它是 NTSC 视频磁带兼容 hack, 不是 Nyquist 推导直接出来的好看数字.
- 第 30 节 (水下声) 必须 mention Ewing 1944 SOFAR 与 Roger Payne 1971 鲸歌, 这是有故事的两件事.

---

## 颜色

`vol-9-sound/style.css` 已设 `--accent`. 不要改. 卷色: 暖琥珀 / 黄铜色 (像铜管乐器的色调).

## slug → 部分对应

| 部分 | 文件范围 |
|---|---|
| 第 1 部分 · 波的物理 | 01-pressure-wave.html ... 05-beats.html |
| 第 2 部分 · 声源 | 06-voice.html ... 10-timbre.html |
| 第 3 部分 · 房间与心理 | 11-room-modes.html ... 15-noise-control.html |
| 第 4 部分 · 运动与极端 | 16-doppler.html ... 20-bat-echolocation.html |
| 第 5 部分 · 信号与压缩 | 21-fourier-ear.html ... 25-noise-cancel.html |
| 第 6 部分 · 边界 | 26-nonlinear-sound.html ... 30-sound-underwater.html |

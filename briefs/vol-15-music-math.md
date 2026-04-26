# Vol 15 · 音乐与数学 — Brief

> 必读: `briefs/00-tone-bible.md` 与 `vol-7-matter/01-crystals.html`. 没读完不要动笔.
> 目标目录: `vol-15-music-math/`. 30 个 HTML 文件已存在 (低质量旧稿), 文件名不要改.

## 卷主轴

音乐 = 数 + 共振 + 心理. 30 节按 6 部分:

1. 音高与基本: 频率 / 八度 / 谐波列 / cents / 拍音
2. 调律的数学: 毕达哥拉斯, comma, just intonation, 平均律, 移调
3. 音色与频谱: Fourier, timbre, ADSR, dissonance, missing fundamental
4. 乐器物理: 弦, 管, 簧, 钢琴, 合奏
5. 节奏与对称: 节拍, polyrhythm, 群论, 对称, 信息熵
6. 数字音频: 采样, 滤波, MP3, reverb, 空间声

每节落到一个具体乐器 / 调式 / 工程 + 一个具体数 (Hz, cents, ratio) + 一位有名字的人.

---

## 卷引子 (覆盖 `index.html` `<p class="intro">`)

> "钢琴中央 C 261.63 Hz, 上一八度 C 523.25 Hz — 频率严格 2:1, 可耳朵听成同一个音. 五度 C-G 频率比 3:2, 这是毕达哥拉斯公元前 6 世纪用一根单弦发现的; 12 个完美五度堆出来比 7 个八度多 23.5 cents (Pythagorean comma), 12 平均律就是把这个误差均匀分摊. CD 44.1 kHz, MP3 用心理声学掩蔽把 1411 kbps 压到 128. 这一卷把音乐的数学结构 — 频率、ratio、群、Fourier、心理声学 — 串起来; 终点是为什么 4'33" 在 1952 年首演时大厅里 35 dB 的环境噪声仍然 'is the music'."

---

## 30 节具体 brief

### 第 1 部分 · 音高与基本

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 01 | pitch-frequency | A4 标准 440 Hz, 钢琴最低 27.5 Hz, 最高 4186 Hz | 88 键覆盖 7+ 八度; pitch perception 对数 | Sauveur 1701 acoustique; ISO 1955 A=440 Hz | $f$ 与 pitch 对数关系 | 钢琴键 + 频率 / 名称表 |
| 02 | octave | 雌雄齐唱差一八度仍听成"一致"; 周期 2:1 | 八度 = 频率比 2:1 = 1200 cents | Pythagoras (公元前 6c.) — 单弦实验 | $f_2 = 2 f_1$ | 单弦实验图 + 整除位置 |
| 03 | overtone-series | 弦或空气柱基频 + 整数倍谐波 | n=1,2,3,4,...; 八度 (2), 五度 (3), 四度 (4 over 3) | Mersenne 1636 (overtone 列表) | 整数谐波 + 谱 | 谐波列 frequency comb + 名称对应 |
| 04 | cents | 半音 = 100 cents, 八度 = 1200 | $c = 1200 \log_2(f_2/f_1)$ | A. J. Ellis 1885 制定 cents | 对数频率单位 | cents vs 频率 + 调律差异 |
| 05 | beats-music | 钢琴调音用 4-5 Hz beat for stretched octave | $f_{\rm beat} = \abs{f_1-f_2}$ | Sauveur 1701, Helmholtz 1863 | 两正弦叠加 → 包络 | beat 时序 + 频率合并 |

### 第 2 部分 · 调律的数学

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 06 | pythagorean | Pythagorean tuning by stacking 3:2 fifths | 12 fifths $(3/2)^{12} = 129.7$, 7 octaves $2^7 = 128$ | Pythagoras (公元前 6c.); 中国先秦三分损益 | 3:2 链 + 误差 | 十二度循环 + Pythagorean comma |
| 07 | comma | Pythagorean comma = 23.46 cents; syntonic comma 21.51 cents | 12-tone close 12 fifths gap = 23.46 c | Boethius 6c. 学术化; Galilei 1581 实验测 | 不同 commas 名称与大小 | 几个 commas 大小条形图 |
| 08 | just-intonation | 大三和弦 4:5:6 ratio 完美协和 | C-E-G = 4:5:6, fundamental 整数倍 | Helmholtz 1863 *On the Sensations of Tone* | 整数比 → 简单波形 | 4:5:6 ratio 时域波形整齐 |
| 09 | equal-temperament | 12 平均律 $f = f_0 \cdot 2^{n/12}$ | 半音 100 cents; 五度 700 cents (vs JI 702) | Zhu Zaiyu 朱载堉 1584 (中国数学家); Stevin 1585; Bach 1722 *Well-tempered Clavier* | $2^{n/12}$ | 12 平均律 vs JI 偏差 |
| 10 | modulation | 调式转换 (modulation) 在 ET 里无缝, 在 JI 里需要重调 | comma drift in chains | Bach *Well-Tempered* 24 大小调 | tonal center shift | 转调路径 |

### 第 3 部分 · 音色与频谱

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 11 | fourier-music | 复杂周期信号 = sin 之和 | $f(t) = \sum a_n \cos(2\pi n f_0 t) + b_n \sin(...)$ | Fourier 1822 (热传导); Helmholtz 应用到音乐 | 频谱 = Fourier coefficients | 锯齿 / 方波 / 三角的谐波分解 |
| 12 | timbre-music | 钢琴 / 小提琴 / 长笛同 A4 听感不同 = 不同谐波分布 | sustained / decaying envelope; 谱包络 | Helmholtz 1863 | 谐波分布 + envelope | 三种乐器谱叠加 |
| 13 | attack-decay | ADSR envelope: attack 5-100 ms 决定 timbre | 钢琴 attack ~5 ms hammer 击; 小提琴 30-100 ms bow | Risset 1969 trumpet timbre study | ADSR 包络 | ADSR 四段 + 不同乐器形状 |
| 14 | dissonance | 大三 4:5:6 协和; 增四 5:7 不协和 | critical band ~1/3 octave; roughness 内 critical band | Helmholtz 1863, Plomp & Levelt 1965 roughness | beats within critical band → roughness | 协和 vs 不协和 dyad 频谱重叠 |
| 15 | missing-fundamental | 电话只传 300-3400 Hz, 仍听到 A1 = 110 Hz | 大脑从谐波列推出基频 | Schouten 1940 missing fundamental experiments | 大脑 pitch 提取 = pattern matching | 谐波列缺基频 + 仍感 pitch |

### 第 4 部分 · 乐器物理

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 16 | string-modes-music | 小提琴 G 弦, 长 327 mm, T=49 N, $\mu=0.7$ g/m → 196 Hz | $f_n = (n/2L)\sqrt{T/\mu}$ | Mersenne 1636 | 一维驻波本征模 | 弦上 4 模式 |
| 17 | wind-instrument | 长笛 + 单簧管 65 cm 同长但单簧管低八度 | 开开 vs 闭开 | Bernoulli 1738; Helmholtz | $f = nc/(2L)$ vs $(2n-1)c/(4L)$ | 两根管 + 模式 |
| 18 | reed | 单簧管 reed 自激振荡 ~ 双稳态系统 | reed beating against mouthpiece; 100-200 Hz fundamental | Helmholtz 1863 reed motion | 边界 nonlinear coupling | reed 振动 + 自激稳态 |
| 19 | piano | 钢琴 88 键, 低音弦缠绕 (变 μ); 高音 多弦同 pitch | inharmonicity by stiffness $f_n = nf_1\sqrt{1+Bn^2}$, $B \sim 10^{-4}$ | Steinway 1853 大三角钢琴 | string + sounding board + 锤击 | 钢琴内部 + inharmonicity 谱 |
| 20 | ensemble | 弦四重奏 ensemble: ~5 ms tempo coordination | 视觉 + 听觉 + 呼吸 同步 | Goebl & Palmer 2009 ensemble timing | mutual entrainment | 四重奏 cycle of mutual cue |

### 第 5 部分 · 节奏与对称

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 21 | rhythm | 4/4 拍最常见; 3/4 圆舞曲; 5/4 (Mission Impossible) | 大脑 prefer simple integer ratios | Fraisse 1982 rhythm psychology | tempo 60-180 BPM 是 'comfortable' | 不同节拍 grid 对比 |
| 22 | polyrhythm | 3 against 2 西非鼓; LCM 6 beats | 3:2, 4:3, 5:4 各种 polyrhythm | Arom 1991 *African Polyphony* | 整数 ratio 复合 | 3:2 grid + 重叠点 |
| 23 | scales-group | 12 个半音 = $\mathbb Z/12\mathbb Z$; 大调 = subset {0,2,4,5,7,9,11} | transposition = group action | Babbitt 1955 group theory in music | 12-tone group $\mathbb Z/12$ | 12 半音圆 + 大调 subset |
| 24 | symmetry-music | retrograde, inversion, transposition 4 个 symmetries | dihedral group D24 | Schoenberg 1923 12-tone, Webern 序列 | 反演 / 逆行 / 移调 | 一段 melody 4 transformations |
| 25 | information-music | 巴赫平均 entropy ~5 bits/note; pop ~ 3 bits | Shannon 1948 信息论 + Cohen 1962 music entropy | $H = -\sum p \log p$ | Bach vs pop entropy 对比 |

### 第 6 部分 · 数字音频

| NN | slug | 切入 | 必含数字 | 必含人 + 年 | 公式 / 机制 | 图占位 |
|---|---|---|---|---|---|---|
| 26 | sampling-music | CD 44.1 kHz × 16 bit = 1411 kbps; SACD 2.8 MHz DSD | Nyquist 2× listening upper 22 kHz | Nyquist 1928, Shannon 1949; Sony-Philips Red Book 1982 | sampling theorem | 模拟 → 采样 → 重建 |
| 27 | filtering | EQ low/high/band; 分子 reverb 用 IIR | digital biquad filter; cutoff 与 Q | Butterworth 1930; Chebyshev | $H(z)$ digital filter | EQ 谱 + IIR / FIR 区别 |
| 28 | mp3 | 1411 → 128 kbps, 11:1 几乎听不出 | psychoacoustic masking 20 dB ≈ -1 LSB | Brandenburg 1980s Fraunhofer | MDCT + 掩蔽阈 + Huffman | MP3 编码 pipeline |
| 29 | reverb-music | hall reverb 1-3 s; plate reverb 物理板; convolution reverb 用真实 IR | RT60 + early reflections + late tail | Schroeder 1962 数字 reverb 理论 | impulse response convolution | impulse + reverberant tail |
| 30 | spatial-audio | Dolby Atmos 64+ object channels; 头相关函数 HRTF | ITD ~600 μs at 90°; ILD up to 20 dB at high f | Blauert 1974 spatial hearing; Dolby Atmos 2012 | HRTF + binaural | 头部 + ITD / ILD 双耳定位 |

---

## 本卷易踩的坑

- 第 6 节 (Pythagorean): 朱载堉 1584 比 Stevin 1585 早一年, 这是中国音律史关键. 必须 mention.
- 第 9 节 (equal temperament): Bach 1722 *Well-tempered Clavier* 24 大小调全部演练, 是 ET 实验性宣言.
- 第 14 节 (dissonance): Helmholtz 1863 不只给"协和 = 简单 ratio", 还给了 critical band roughness 解释 — 需要两个层面都讲.
- 第 26 节 (sampling): 44.1 kHz 来自 NTSC PCM 兼容, 不是 Nyquist 直接给的好看数. 必须解释 history.
- 第 30 节 (spatial-audio): HRTF 是 1990 年代后大量数据驱动的 personalization, 现在 Apple AirPods 可以扫面.

---

## 颜色

`vol-15-music-math/style.css` 已设. 卷色: 酒红 / wine.

## slug → 部分对应

| 部分 | 文件 |
|---|---|
| 第 1 部分 · 音高与基本 | 01-pitch-frequency.html ... 05-beats-music.html |
| 第 2 部分 · 调律 | 06-pythagorean.html ... 10-modulation.html |
| 第 3 部分 · 音色与频谱 | 11-fourier-music.html ... 15-missing-fundamental.html |
| 第 4 部分 · 乐器物理 | 16-string-modes-music.html ... 20-ensemble.html |
| 第 5 部分 · 节奏与对称 | 21-rhythm.html ... 25-information-music.html |
| 第 6 部分 · 数字音频 | 26-sampling-music.html ... 30-spatial-audio.html |

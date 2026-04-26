# DevCollection 写作 Tone Bible (统一规范)

> 适用: 第 8-17 卷, 共 300 节. 任何为这十卷写文章的 agent (Codex / Claude / 人) 在动笔前必须先读完这一份, 然后才读对应的 vol-N 文档.

---

## 0 · 这份文件存在的原因

第 8-17 卷已经被一个 agent 自动产出过一遍 (commit `e439b3d`). 检查样本:

- `vol-8-fluids/01-sink-water.html`
- `vol-10-color/01-spectrum-color.html`
- `vol-13-motion/06-newton-laws.html`

三篇文章, 完全不同主题, 开头字面相同:

> "一个好问题通常先从日常经验里冒出来: <题目>. 如果只凭直觉, 我们很容易把它说成一句模糊的解释; 物理的做法更慢一点, 先问长度、时间、能量或通量的尺度, 再问哪一个无量纲比值真正控制图样. 本节保留这个路线: 从可观察现象开始, 写出最小方程, 代入一个数, 最后回到实验和历史."

> "任何测量都要先选变量. 对这一节, 最自然的变量不是越多越好, 而是刚好能描述「变化从哪里来、往哪里去」. 把空间尺度记作 $L$, 时间尺度记作 $\tau$, 典型速度或频率记作 $U$ 或 $f$..."

这套话适用于任何题目, 因此什么都没说. 重写就是要删掉这种万能模板, 换成只有那一节才能写得出来的具体内容.

---

## 1 · 黄金范例: `vol-7-matter/01-crystals.html`

任何写新一节之前先读这一篇. 它的开头:

> "把一块紫铜的劈面在显微镜下打磨抛光、再用稀硝酸腐蚀, 你会看到一种叫 "金相组织" 的图案: 大小不均的多边形格子拼在一起, 每个格子里又有规整的方向纹. 那些大格子是 "晶粒", 每个晶粒内部, 数以亿计的铜原子按一种几乎严格的周期方式排得齐齐整整..."

关键观察:
- 第一句是一个具体动作 (打磨 + 腐蚀), 不是 "我们将探讨"
- 90 个字之内已经 mention 了五个具体名词: 紫铜, 劈面, 金相, 多边形, 晶粒
- 第二段进数学时已经有数: $a = 3.615\,\mathrm{Å}$ for Cu, $a = 5.64\,\mathrm{Å}$ for NaCl
- 历史从 Hauy 1784 → Bravais 1850 → Schoenflies 1891 → Bragg 1914, 一条清晰的人物链
- 总长 3500+ 中文字, 5 个编号小节, 4 个 `\tag{N}` 公式, 1 个 diagram-stub, 末尾 `<div class="small-summary">` 带 ▲

每一节都要做到这种具体性. 没做到就是没做完.

---

## 2 · 反模板黑名单 (硬性禁止)

下列字符串及其变体不得在任何新写的章节里出现 (做语法变换、改个词都不行):

```
一个好问题通常先从日常经验里冒出来
如果只凭直觉, 我们很容易把它说成一句模糊的解释
物理的做法更慢一点
本节保留这个路线
从可观察现象开始, 写出最小方程, 代入一个数, 最后回到实验和历史
任何测量都要先选变量
最自然的变量不是越多越好
把空间尺度记作 $L$, 时间尺度记作 $\tau$
式 $(N)$ 的价值在于筛选主次
很多教材把这个步骤讲成"代公式"
[X] 不是口号
[X] 不是一个抽象名词
把……拆成三层: 什么量在守恒, 什么机制在传递, 什么尺度决定我们最终看到的结果
关键不是背下一个名字, 而是能把公式、数量级和可观察现象接起来
```

如果接到的稿子里有上面任何一行, 退稿重写.

---

## 3 · 每节的硬性指标

文长: **3000-4000 中文字** (不含 HTML 标签). 比 vol-6 / vol-7 略长是允许的, 短不行.

必须出现:

- [ ] 第一句话是具体的动作或具体的物体, 不是 meta 评论
- [ ] 第一段 (摘要 abstract 或开场) 内出现 **≥ 3 个具体名词** (材料名/仪器名/人名/年份/地点至少一种)
- [ ] **≥ 4 个编号小节**, 用 `<h2>一、...</h2>` 这种 (一、二、三、四、五)
- [ ] **≥ 2 个用 `\tag{N}` 的编号公式** (不只是 inline, 至少有 display 块)
- [ ] **≥ 2 处具体的数字代入**, 每处带单位 + 对象 (例: "Cu 在 20°C 电阻率 $1.7\times 10^{-8}\,\Omega\!\cdot\!\mathrm{m}$")
- [ ] **≥ 1 个有名字的人物 + 年份** (Helmholtz 1863, Reynolds 1883, Bragg 1914 这种)
- [ ] **≥ 1 处实验或具体材料的连结** (具体的仪器、具体的样品)
- [ ] **恰好 1 个** `<figure class="diagram-stub">`, 在最自然的位置 (不是在文末凑数), brief 描述能直接交给画师
- [ ] 末尾用 `<div class="small-summary">` 包一个小结段, 末行单独一个 `▲` 居右
- [ ] 顶部 + 底部 `<nav class="chapter-nav top/bottom">` 带 prev/next, 章节定位 ("第 N 节 / 30 · 第 X 部分 · ... · 第 Y 卷·...")

---

## 4 · HTML 骨架

精确按 `vol-7-matter/01-crystals.html` 的结构. 头部 MathJax 配置一字不改 (含所有 macros, 否则 vol-1 至 7 共享的若干公式渲染不出). 关键骨架:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><节题>? · <卷名></title>
<link rel="stylesheet" href="style.css">
<script>
  window.MathJax = { tex: { inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams', macros: { slashed: ['{\\not{#1}}', 1], slash: ['{\\not{#1}}', 1], bra: ['\\langle{#1}|', 1], ket: ['|{#1}\\rangle', 1], braket: ['\\langle{#1}|{#2}\\rangle', 2], abs: ['\\left|{#1}\\right|', 1], norm: ['\\left\\|{#1}\\right\\|', 1], Tr: ['\\operatorname{Tr}', 0], Im: ['\\operatorname{Im}', 0], Re: ['\\operatorname{Re}', 0] } }, svg: {fontCache:'global'} };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<nav class="chapter-nav top">
  <a href="<prev>.html">← 上一节</a>  <!-- 第一节: <a class="disabled" href="#"> -->
  <span class="chapter-title">第 N 节 / 30 · 第 X 部分 · 部分名 · 卷名</span>
  <a href="<next>.html">下一节 →</a>  <!-- 第 30 节: <a class="disabled" href="#"> -->
</nav>

<article>
  <h1><节题></h1>
  <div class="sub">—— 关键概念</div>

  <div class="abstract">
    <一段 200-350 字的"路线图". 头一句必须是具体动作或具体对象. 末尾交代本节会落到哪个数 / 哪个公式.>
  </div>

  <p><开场段, 接日常或具体材料, 给一个具体观察, 最后用一句问题钩到正文.></p>

  <h2>一、<描述性小节题></h2>
  <p>...</p>
  <p>$$ <公式> \tag{1} $$</p>
  <p>...</p>

  <h2>二、...</h2>
  ...

  <figure class="diagram-stub">
    <div class="stub-box">[此处应有一张图: <一句话描述, 含坐标、关键标注、配色提示, 让画师可以直接动手>]</div>
  </figure>

  <h2>三、...</h2>
  ...

  <h2>四、...</h2>
  ...

  <h2>五、历史的几道台阶</h2>
  <p><人 + 年份的链条, 至少 3 个名字, 一句一个地说他们干了什么.></p>

  <div class="small-summary">
  <h4>小结</h4>
  <p><把本节的几个公式 + 数字 + 人物再串一遍, 落到下一节的钩子.></p>
  <p style="text-align:right; color:var(--accent); margin-top:1em;">▲</p>
  </div>
</article>

<nav class="chapter-nav bottom">
  <a href="<prev>.html">← 上一节</a>
  <span class="chapter-title"><a href="index.html">目录</a></span>
  <a href="<next>.html">下一节 →</a>
</nav>

</body>
</html>
```

注意:
- `<title>` 写法: `节题? · 卷名`, 中间用一个空格 + `·` + 一个空格
- `--accent` 颜色不是手填, 而是 `style.css` 已经定义, 这里只引用
- `.disabled` class 的 `<a>` 用于第 1 节"上一节"和第 30 节"下一节"

---

## 5 · 数学与符号陷阱

这个项目用 MathJax v3, 跑在浏览器里. HTML parser 会先于 MathJax 处理文本, 所以一切像 HTML 标签的字符要转义:

| 想写 | 必须写成 |
|---|---|
| `a < b` 在 `$..$` 里 | `a \lt b` |
| `a > b` 在 `$..$` 里 | `a \gt b` |
| `a <= b` | `a \le b` |
| `a >= b` | `a \ge b` |
| `a << b` | `a \ll b` |
| `a >> b` | `a \gg b` |
| `&` (除非真的要 entity) | `\&` |

公式编号一律 `\tag{N}`, 不要 `\label{}` `\ref{}` `\eqref{}` (项目没用 amsmath equation environment).

inline 数学: `$...$`. display 数学: `$$...$$`. 不要 `\(...\)` `\[...\]`.

中文里需要 `\,` 隔开数字与单位: `$1.7\times 10^{-8}\,\Omega\!\cdot\!\mathrm{m}$` (而不是 `1.7e-8 Ω·m`).

---

## 6 · 标点风格

DevCollection 已有的卷不用全角句号 "。", 一律用半角 "." 加一个空格. 顿号 "、" 和括号 "()" 是全角. 引号用 `""` 或 `「」` 都行 (项目混用). 冒号 ":" 半角. 这是项目延续了一年的风格, 重写时保持.

---

## 7 · 三件 "一定别做"

1. 不要写 "我们将...", "本节要...", "本文将..." 这种自我说明. 直接进入物理.
2. 不要 "宇宙是奇迹", "光真神奇" 这种抒情句. 物理是 mechanics.
3. 不要全篇 inline 数学. 有 derivation 的地方就用 `$$...$$` 拆出来, 加 `\tag{N}`.

---

## 8 · "图占位" brief 的写法

写图占位时, 不要 "这里需要一张示意图". 要给画师足够动手的细节. 例:

❌ "[此处应有一张图: 涡街示意]"

✅ "[此处应有一张图: 圆柱后方 von Kármán 涡街 — 横轴流向 x, 圆柱直径 $D$ 标在原点, 后面交错排出蓝/红两排涡核, 间距比例 a/h ≈ 0.28 (Theodore von Kármán 1911 推导值), 标 Strouhal 数 $St = fD/U$ 在右下角, 给一个 $Re = 100$ 的脱落周期]"

只有具体到这个地步, 后续画图阶段才能 dispatch 给独立 agent 不再回来问.

---

## 9 · 收稿前的自检

每写完一节, agent (或人) 自己跑一遍:

- [ ] 文长 ≥ 3000 中文字
- [ ] 头三段里没有第 2 节列出的禁词
- [ ] 至少 4 个 `<h2>一、...` 编号小节
- [ ] 至少 2 个 `\tag{N}` 公式
- [ ] 至少 2 处具体数字 (有单位)
- [ ] 至少 1 个人 + 年份
- [ ] 数学里没有裸 `<` `>` `<<` `>>` `<=` `>=` (用 grep 跑 `\$[^\$]*[<>]+[^\$]*\$` 检查)
- [ ] 顶 + 底 chapter-nav, 链接对得上
- [ ] 末尾 `<div class="small-summary">` 带 ▲
- [ ] 恰好一个 `<figure class="diagram-stub">`

---

## 10 · 一节一节写, 不要批量

不要一次性输出 30 节. 每节单独写完, 自检, 再写下一节. 这样每一节的具体细节才能堆得够厚, 而不是退化成模板.

---

完毕. 有任何疑问, 回到 `vol-7-matter/01-crystals.html` 看一遍.

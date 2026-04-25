# SPEC — 第七卷 · 物质是什么? 单篇文章规范

> 与前 6 卷一致的写作口气. 从一块金属、一颗晶体、一团液氦出发, 第一性原理, 落到一个具体的物理量 (电导率、临界温度、霍尔电阻 h/e²). 本卷主角: 凝聚态物理.
>
> **不假设读者懂凝聚态**. 假设读者完成了 vol 1-6 — 会 SR/GR、QM、stat mech, 听过 Bloch 与 Fermi 海. 数学工具 (Brillouin 区、张量、对称群) 引用 vol 4 即可.

---

## 1 · 风格

### 1.1 结构
1. 标题 + `?`; 副标题 `——` + 关键概念
2. 摘要 — 一段路径
3. 开场 — 接日常或具体材料
4. 编号小节 (`一、` ...) — 描述性题目
5. 小结 — 在凝聚态/量子信息/拓扑/复杂性更大图景里的位置

### 1.2 腔调
- 第一性原理, 不挥手
- 例: 铜的电阻率 1.7×10⁻⁸ Ω·m, NbTi 超导临界温度 9.5 K, BCS 能隙 1.76 k_B T_c, 量子 Hall σ_xy = ne²/h, Si 带隙 1.12 eV
- 历史: Drude, Bloch, Fermi, Sommerfeld, Bardeen-Cooper-Schrieffer, Landau, Anderson, Kosterlitz-Thouless, von Klitzing, Laughlin

### 1.3 每篇必含 (checklist)
- [ ] 标题带问号
- [ ] **≥ 4 编号小节**
- [ ] **≥ 2 编号公式 / 定理**
- [ ] **≥ 1 处数字代入** (具体材料的具体数)
- [ ] **≥ 1 处实验/材料连结** (von Klitzing 1980, Cu, NbTi, MgB₂, YBa₂Cu₃O₇, graphene, Hg, ...)
- [ ] **≥ 1 历史人物**
- [ ] **恰好 1 个图占位** (见 §2.2)
- [ ] 顶部和底部两条导航栏齐全
- [ ] 不在 HTML 内 inline CSS

### 1.4 长度
- 简体中文; LaTeX 数学
- **3000-4000 中文字**

---

## 2 · HTML 骨架与图占位

### 2.1 骨架 (BOOK_NAME=第七卷·物质是什么?)

格式与第六卷骨架相同 (见 vol-6-quantum/SPEC.md §2.1), 仅 BOOK_NAME 与 title 替换.

### 2.2 图占位规则

**本卷只交付正文, 不渲染 TikZ.** 在最自然位置放:
```html
<figure class="diagram-stub">
  <div class="stub-box">[此处应有一张图: 描述图想说的事]</div>
</figure>
```

例:
```html
<figure class="diagram-stub">
  <div class="stub-box">[此处应有一张图: Cu 的能带结构 — 横轴 k 沿 Γ-X-W-L 高对称线, 纵轴 E, Fermi 能级 E_F 标在 sp 带上, 半充满]</div>
</figure>
```

**不要写 .tex, 不要 tectonic, 不要 SVG.**

---

## 3 · Topic Brief

```
=== 文件 ===
HTML: C:\...\vol-7-matter\NN-slug.html

=== 位置 ===
N=N/30, PART=第 X 部分 · 名称, PREV=..., NEXT=..., BOOK_NAME=第七卷·物质是什么?

=== 标题 ===
TITLE: ...?
SUBTITLE: ——...

=== 物理 brief ===
- 现象 / 材料 / 测量数据
- 关键机制 / 公式
- 关键数字
- 历史 / 实验

=== 图占位 brief ===
- 图想说什么 (一两句)
```

---

## 4 · 禁止
- 不假设读者会凝聚态
- 不写 TikZ / 不渲染 SVG
- 一次一篇

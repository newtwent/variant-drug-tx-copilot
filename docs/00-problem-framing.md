# 00 Problem framing / 问题形式化

## 1. Scope / 范围

This document states the research question formally, fixes the two tracks and the variant typology, and collects the hidden assumptions, common mistakes, missing information and the deeper question that frame every other document. It contains no new evidence: the evidence is in documents 01 to 07, the design consequences in document 08, the analysis of LabCompass in document 09 and the open questions in document 10.

> 本文档对研究问题做形式化陈述，确定两条轨道和变异类型学，并汇集贯穿其他所有文档的隐含假设、常见错误、缺失信息和更深层问题。它不包含新证据：证据在文档 01 至 07 中，设计上的后果在文档 08 中，LabCompass 的分析在文档 09 中，待确认问题在文档 10 中。

## 2. Formal statement / 形式化陈述

Let g be a genotype (a set of variants), c a cellular context (a cell type or line together with its baseline expression x0), d a drug with its dose and exposure time, and x the post-treatment transcriptome. The modeling target is the distribution of x given x0, c, d and g. The scientific target is narrower: the genotype-by-drug interaction, meaning how the drug-induced change in expression differs between two genotypes g and g' in the same context.

> 设 g 为基因型（一组变异），c 为细胞背景（细胞类型或细胞系及其基线表达 x0），d 为药物及其剂量和暴露时间，x 为处理后的转录组。建模目标是给定 x0、c、d 和 g 时 x 的分布。科学目标更窄：基因型×药物交互，即在同一背景下，药物诱导的表达变化在两个基因型 g 与 g' 之间有何不同。

```
effect(d | g, c)    = E[x | d, g, c] - E[x | control, g, c]
interaction(g, g')  = effect(d | g, c) - effect(d | g', c)
```

The interaction is a difference of differences. It is expected to be much smaller than the drug main effect, so a model can score well on the main effect while knowing nothing about genotype, and evaluation has to target the interaction directly (document 07).

> 交互项是差值的差值。预计它远小于药物主效应，因此模型可以在主效应上得分很高，却对基因型一无所知，所以评测必须直接针对交互项（文档 07）。

Two mechanisms are worth separating. In the mediation view, genotype changes the baseline state x0, and the drug then acts on that shifted state in the same way for everyone. In the operator view, genotype changes how the drug acts, through binding, the downstream pathway or feedback, so the response differs even for the same baseline. Document 08 turns this distinction into the falsifiable hypothesis HA. The two mechanisms can coexist, and their balance probably differs by variant class (document 02, J17).

> 有两种机制值得区分。在中介观点下，基因型改变基线状态 x0，药物随后以对所有人相同的方式作用于这个被改变的状态。在算子观点下，基因型通过结合、下游通路或反馈改变药物的作用方式，因此即使基线相同，响应也不同。文档 08 把这一区分转化为可证伪的假设 HA。两种机制可以并存，其平衡很可能因变异类别而异（文档 02，J17）。

## 3. Two tracks and a variant typology / 两条轨道与变异类型学

The somatic track (S) treats variation between cancer cell lines or tumors, such as driver mutations, as the source of genotype differences. The germline track (G) treats inherited variation between people or donor-derived lines. Track B marks method-level or resource-level sources that apply to both. The tracks differ in effect size, data availability and confounding, so they are analyzed separately and joined only where the evidence allows.

> 体细胞轨道（S）把癌症细胞系或肿瘤之间的变异（如驱动突变）视为基因型差异的来源。种系轨道（G）处理人与人之间或供体来源细胞系之间的遗传变异。轨道 B 标记方法层面或资源层面、对两者都适用的来源。两条轨道在效应大小、数据可得性和混杂方面不同，因此分开分析，只在证据允许时才合并。

Variants are tagged with five classes. Class 1 is target coding variants that change binding or function. Class 2 is target regulatory variants that change expression, such as cis-eQTLs. Class 3 is copy-number and structural variants. Class 4 is pathway upstream, downstream and bypass variants. Class 5 is pharmacokinetic (PK) gene variants affecting metabolism and transport, which confound a pharmacodynamic (PD) question. The tags in `data/sources.csv` (track, variant class, kind and relevance) are curator judgments, not claims made by the sources.

> 变异被标记为五类。类别 1 是改变结合或功能的靶点编码变异。类别 2 是改变表达的靶点调控变异，如 cis-eQTL。类别 3 是拷贝数与结构变异。类别 4 是通路上游、下游和旁路变异。类别 5 是影响代谢和转运的药代动力学（PK）基因变异，它们会混杂药效动力学（PD）问题。`data/sources.csv` 中的标签（轨道、变异类别、kind 和 relevance）是整理者的判断，不是来源本身的论断。

## 4. Hidden assumptions to confirm or drop / 需要确认或放弃的隐含假设

A1. Genetic variation changes drug-induced transcriptional responses enough, and broadly enough, to justify dedicated modeling. The evidence is present but sparse: see the response-eQTL studies [GD06, GD08, GD01].

> A1. 遗传变异对药物诱导转录响应的改变足够大、足够广，值得专门建模。证据存在但稀疏：见响应 eQTL 研究 [GD06, GD08, GD01]。

A2. The transcriptome is a meaningful mediating phenotype. The one study that links in-vitro response to in-vivo cardiotoxicity risk rests on a model trained on 3 versus 3 patients [GD06], and its generality is unknown.

> A2. 转录组是有意义的中介表型。把体外响应与体内心脏毒性风险联系起来的那项研究，依赖于在 3 对 3 名患者上训练的模型 [GD06]，其普遍性未知。

A3. A world-model architecture gives gains over conditional-generative or linear models. This is untested.

> A3. 世界模型架构相对条件生成模型或线性模型有增益。这一点尚未检验。

A4. Matched data of genotype, drug and post-treatment transcriptome can be obtained or constructed, or cell-line genotype can proxy individual genotype. That proxy is confounded with each line's background [DS07], and single-cell data that pair an inherited genotype, an exposure and a transcriptome exist only at the scale of tens of individuals [GD10].

> A4. 可以获得或构造基因型、药物与处理后转录组相匹配的数据，或者细胞系基因型可以代理个体基因型。该代理与每个细胞系自身的背景混杂 [DS07]，而把遗传性基因型、暴露和转录组配对的单细胞数据只有数十个个体的规模 [GD10]。

A5. In-vitro results transfer to in-vivo settings. The evidence is mixed: saturation screens matched 28 of 29 clinical resistance cases for FGFR [GV33], whereas the in-vivo link for a transcriptional response rests on 3 versus 3 patients [GD06].

> A5. 体外结果可迁移到体内情境。证据好坏参半：对 FGFR，饱和突变筛选与 29 个临床耐药病例中的 28 个相符 [GV33]，而转录响应的体内联系只依赖 3 对 3 名患者 [GD06]。

A6. End-point snapshots are enough to model dynamics and transitions. Metabolic labeling that separates new from old RNA gives measured state-transition supervision that snapshots lack [DS21, DS22].

> A6. 终点快照足以建模动力学与转移。分离新旧 RNA 的代谢标记提供了快照所缺少的、实测的状态转移监督 [DS21, DS22]。

A7. Somatic and germline variation can be handled in one framework.

> A7. 体细胞变异与种系变异可以在同一框架内处理。

A8. A model that predicts well can be used to decide which drug and dose to give. LabCompass frames the cell world model as a tool to decide what to do next, which is a different target from prediction accuracy [WM27, WM30].

> A8. 预测得好的模型就可以用来决定给哪种药物和剂量。LabCompass 把细胞世界模型表述为决定下一步做什么的工具，这与预测准确度是不同的目标 [WM27, WM30]。

A9. Abstract-level reading is good enough to rank relevance. Rows at tier T2 were read at abstract level only, and a blog's claims about LabCompass stay unchecked against the preprint [WM32].

> A9. 摘要层面的阅读足以排序相关性。T2 级条目只读到摘要层面，一篇博客关于 LabCompass 的论断也没有与预印本核对 [WM32]。

## 5. Common mistakes to avoid / 需要避免的常见错误

E1. Evaluating with genome-wide MSE or Pearson correlation lets mean baselines win [EV01, EV02].

> E1. 用全基因组 MSE 或 Pearson 相关评估，会让均值基线占优 [EV01, EV02]。

E2. Treating cell-line identity as genotype confounds lineage, epigenome and batch [DS07].

> E2. 把细胞系身份当作基因型，会混杂谱系、表观基因组和批次 [DS07]。

E3. Random splits leak information through neighboring drugs, cell lines and pathways. Use leave-one-line-out, leave-one-drug(-class)-out and leave-one-variant-out splits.

> E3. 随机划分会通过相近的药物、细胞系和通路泄漏信息。应使用留一细胞系、留一药物（或药物类别）和留一变异的划分。

E4. Treating sequence-model predictions as ground truth [GV05].

> E4. 把序列模型的预测当作真值 [GV05]。

E5. Treating GDSC, CTRP, CCLE and PRISM as interchangeable: cross-study label reproducibility was reported as 0.220 (self-reported) [EV18].

> E5. 把 GDSC、CTRP、CCLE 和 PRISM 视为可互换：跨研究的标签可重复性报告为 0.220（自报）[EV18]。

E6. Ignoring ancestry [EV23].

> E6. 忽略祖源 [EV23]。

E7. Ignoring cytotoxicity, proliferation and cell-cycle signals and composition changes. A genotype that changes survival changes the cell mix, not only the within-cell response [DS06].

> E7. 忽略细胞毒性、增殖和细胞周期信号以及组成变化。改变存活率的基因型改变的是细胞构成，而不仅仅是细胞内响应 [DS06]。

E8. Using array-imputed genotypes directly for pharmacogenomic variants. Copy-number variants and star alleles need dedicated calling [KB16, KB19].

> E8. 直接使用芯片填补的基因型处理药物基因组学变异。拷贝数变异和星等位基因需要专门的调用 [KB16, KB19]。

E9. Taking self-reported preprint numbers as facts.

> E9. 把预印本的自报数字当作事实。

E10. Treating "world model" as a premise instead of a hypothesis to be tested [WM21].

> E10. 把“世界模型”当作前提，而不是待检验的假设 [WM21]。

E11. Treating a search-tool, blog or news summary as the paper: such summaries relay claims that were not checked against the primary text [WM32].

> E11. 把检索工具、博客或新闻的摘要当作论文本身：这类摘要转述的论断没有对照一手文本核对 [WM32]。

E12. Reading "inverse design works for cytokines in blood progenitors" as evidence that genotype-aware drug design works. LabCompass uses protein-level readouts and no inherited genotype [WM27, WM28].

> E12. 把“细胞因子在血液祖细胞中的逆向设计有效”当作“基因型感知的药物设计有效”的证据。LabCompass 使用蛋白水平的读出，没有遗传性基因型 [WM27, WM28]。

E13. Pooling all variant classes into one genotype gain, which hides the difference between baseline mediation and a change of the response operator [GD45, GD10].

> E13. 把所有变异类别合并为一个基因型增益，这会掩盖基线中介与响应算子变化之间的区别 [GD45, GD10]。

E14. Counting a pooled-donor dataset as genotype-by-drug data when its donors may not be genotyped [DS16, MD42], and scoring with metrics that reward the average-effect baseline [EV29, EV30].

> E14. 在供体可能未做基因分型时，把混池供体数据集当作基因型×药物数据 [DS16, MD42]，以及用奖励平均效应基线的指标来评分 [EV29, EV30]。

E15. Calling non-mutant lines wild type in a cell-line panel where every line carries an annotated driver, and ignoring that lineage-matched arms are small [DS07].

> E15. 在每个细胞系都携带被注释驱动突变的细胞系面板中，把非突变系称为野生型，并忽略按谱系匹配的各臂很小这一事实 [DS07]。

E16. Taking model-proposed drug-target and mechanism labels as ground truth [DS07].

> E16. 把由模型提出的药物靶点和作用机制标签当作真值 [DS07]。

## 6. Missing information that could change the result / 可能改变结果的缺失信息

X1. The target variant track, somatic or germline, which determines data and evaluation (UQ01).

> X1. 目标变异轨道，体细胞还是种系，它决定数据与评测（UQ01）。

X2. The target drug classes and cell types, which determine prior availability (UQ02).

> X2. 目标药物类别和细胞类型，它们决定先验的可得性（UQ02）。

X3. The operational definition of "world model", which determines the tests (UQ03).

> X3. “世界模型”的操作性定义，它决定检验项（UQ03）。

X4. The data and compute budget, including whether new data may be generated; public data only is assumed (UQ04).

> X4. 数据与算力预算，包括能否产生新数据；这里假定只使用公开数据（UQ04）。

X5. The intended end use, prediction or decision, and the licence constraints, which decide whether hypothesis HD is run and whether non-commercial weights such as State and Stack can be used (UQ05, UQ10) [MD62, MD65].

> X5. 预期用途（预测还是决策）以及许可限制，它们决定是否运行假设 HD，以及能否使用 State 和 Stack 这类非商业权重（UQ05、UQ10）[MD62, MD65]。

X6. The LabCompass full text and the genotyping status of the donors of the large cytokine datasets, both unread or unknown (UQ20, UQ17) [WM27, DS16, MD42].

> X6. LabCompass 全文，以及大型细胞因子数据集供体的基因分型状态，两者都没有读到或未知（UQ20、UQ17）[WM27, DS16, MD42]。

## 7. The deeper question behind the request (inference) / 请求背后的更深层问题（推断）

The request that started this repository was a single message, so the deeper question is inferred, not drawn from a history of repeated discussion (confidence: medium). The end goal is a world model, but the question that may not yet have been asked directly is whether the available data hold a large enough, clean enough and falsifiable signal in the genotype-by-drug interaction; in Tahoe-100M the smaller arm of the 12 lineage-matched mutant contrasts computed holds only 1 to 6 lines [DS07], so the signal may sit in a small slice. Its twin question is how much of the genotype effect is mediated by baseline expression (HA).

> 开启本仓库的请求只有一条消息，因此更深层的问题是推断出来的，而不是从反复讨论的历史中归纳出来的（置信度：中）。最终目标是世界模型，但可能尚未被直接问出口的问题是：现有数据在基因型×药物交互项上，是否含有足够大、足够干净且可证伪的信号；在 Tahoe-100M 中，已计算的 12 个按谱系匹配的突变对比里，较小的一臂只有 1 至 6 个系 [DS07]，因此信号可能只存在于一小片区域。它的孪生问题是：基因型效应有多少是经由基线表达中介的（HA）。

Across three rounds the work has been reading, auditing and condensing sources rather than running the cheap HA test on public data, which postpones the question that could end the project; whether to stop collecting and run HA is UQ16 (inference, confidence: medium). A sibling question is whether the model is meant to predict or to decide (UQ05): if the end use is choosing a drug and dose for a genotype, the target is decision quality in a closed loop (HD), but HA still comes first, because if genotype adds nothing beyond baseline expression the rest is moot.

> 三轮以来，工作一直是阅读、稽查和精简来源，而不是在公开数据上运行成本很低的 HA 检验，这推迟了可能终结项目的那个问题；是否停止收集并运行 HA，见 UQ16（推断，置信度：中）。一个并列的问题是模型的用途是预测还是决策（UQ05）：如果最终用途是为某个基因型选择药物和剂量，目标就是闭环中的决策质量（HD），但 HA 仍然最先进行，因为如果基因型在基线表达之外没有任何增益，其余都无从谈起。

## 8. Glossary / 术语表

General definitions, not source claims.

> 一般性定义，不是来源论断。

| Term | Meaning | 含义 |
|---|---|---|
| reQTL (response eQTL) | A variant whose effect on expression differs between treated and control conditions | 其对表达的影响在处理组与对照组之间不同的变异 |
| sQTL | A variant associated with splicing; a response sQTL differs between conditions | 与剪接相关的变异；响应 sQTL 在不同条件间不同 |
| GxE | Gene-by-environment interaction; here, genotype by drug | 基因×环境交互；此处指基因型×药物 |
| Dynamic eQTL | An eQTL whose effect changes along time, pseudotime or differentiation | 其效应沿时间、拟时间或分化过程变化的 eQTL |
| Perturb-seq | Pooled genetic perturbation screens read out by single-cell RNA-seq | 以单细胞 RNA-seq 读出的混合遗传扰动筛选 |
| Base editing | CRISPR-based change of single bases without double-strand breaks, used to introduce variants at endogenous loci | 不产生双链断裂的 CRISPR 单碱基改变，用于在内源位点引入变异 |
| CRISPRi | CRISPR interference: knockdown by an inactive Cas9 fused to a repressor | CRISPR 干扰：由失活 Cas9 融合阻遏物实现的敲低 |
| MR (Mendelian randomization) | Use of genetic variants as instruments to infer causal effects of an exposure; for drug targets, variants near the target gene | 以遗传变异为工具变量推断暴露的因果效应；对药物靶点则使用靶基因附近的变异 |
| TWAS | Test of association between genetically predicted expression and a trait | 检验遗传预测表达与性状之间的关联 |
| PK / PD | Pharmacokinetics (what the body does to the drug) and pharmacodynamics (what the drug does to the body) | 药代动力学（机体对药物的作用）与药效动力学（药物对机体的作用） |
| Difference-in-differences | The change under treatment in one group minus the change in another group | 一个组在处理下的变化减去另一个组的变化 |
| Mediation | An effect that passes through an intermediate variable, here the baseline state | 经过中间变量（此处为基线状态）传递的效应 |
| Sparse mechanism shift | The assumption that an intervention changes only a few causal mechanisms | 干预只改变少数因果机制的假设 |
| World model | A model with a persistent state and an action-conditioned transition; see document 06 | 具有持久状态和动作条件转移的模型；见文档 06 |
| Virtual cell | A computational model meant to simulate cellular states and responses | 用于模拟细胞状态和响应的计算模型 |
| BINN | Biologically informed neural network, whose structure follows a prior biological graph | 生物学先验网络结构的神经网络，其结构遵循先验生物图 |
| Star allele | Haplotype nomenclature used for pharmacogenes | 用于药物基因的单倍型命名法 |
| VEP | Variant effect predictor | 变异效应预测器 |

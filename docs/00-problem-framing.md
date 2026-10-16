# 00 Problem framing / 问题形式化

## 1. Scope / 范围

This document states the research question formally, fixes the two tracks and the variant typology, and collects the assumptions, common mistakes, missing information and the deeper question that frame every other document. It contains no new evidence: the evidence is in documents 01 to 07, and the design consequences are in document 08.

> 本文档对研究问题做形式化陈述，确定两条轨道和变异类型学，并汇集贯穿其他所有文档的假设、常见错误、缺失信息和更深层问题。它不包含新证据：证据在文档 01 至 07 中，设计上的后果在文档 08 中。

## 2. Formal statement / 形式化陈述

Let g be a genotype (a set of variants), c a cellular context (a cell type or line together with its baseline expression x0), d a drug with its dose and exposure time, and x the post-treatment transcriptome. The modeling target is the distribution of x given x0, c, d and g. The scientific target is narrower: the genotype-by-drug interaction, meaning how the drug-induced change in expression differs between two genotypes g and g' in the same context.

> 设 g 为基因型（一组变异），c 为细胞背景（细胞类型或细胞系及其基线表达 x0），d 为药物及其剂量和暴露时间，x 为处理后的转录组。建模目标是给定 x0、c、d 和 g 时 x 的分布。科学目标更窄：基因型×药物交互，即在同一背景下，药物诱导的表达变化在两个基因型 g 与 g' 之间有何不同。

```
effect(d | g, c)    = E[x | d, g, c] - E[x | control, g, c]
interaction(g, g')  = effect(d | g, c) - effect(d | g', c)
```

The interaction is a difference of differences. It is expected to be much smaller than the drug main effect, so a model can score well on the main effect while knowing nothing about genotype. Evaluation therefore has to target the interaction directly, as set out in document 07.

> 交互项是差值的差值。预计它远小于药物主效应，因此模型可以在主效应上得分很高，却对基因型一无所知。所以评测必须直接针对交互项，详见文档 07。

Two mechanisms are worth separating. In the mediation view, genotype changes the baseline state x0, and the drug then acts on that shifted state in the same way for everyone. In the operator view, genotype changes how the drug acts, through binding, the downstream pathway or feedback, so the response differs even for the same baseline. Document 08 turns this distinction into a falsifiable hypothesis.

> 有两种机制值得区分。在中介观点下，基因型改变基线状态 x0，药物随后以对所有人相同的方式作用于这个被改变的状态。在算子观点下，基因型通过结合、下游通路或反馈改变药物的作用方式，因此即使基线相同，响应也不同。文档 08 把这一区分转化为可证伪的假设。

## 3. Two tracks and a variant typology / 两条轨道与变异类型学

The somatic track (S) treats variation between cancer cell lines or tumors, such as driver mutations, as the source of genotype differences. The germline track (G) treats inherited variation between people or donor-derived lines. Track B marks sources that are method-level or resource-level and apply to both. The tracks differ in effect size, data availability and confounding, so they are analyzed separately and joined only where the evidence allows.

> 体细胞轨道（S）把癌症细胞系或肿瘤之间的变异（如驱动突变）视为基因型差异的来源。种系轨道（G）处理人与人之间或供体来源细胞系之间的遗传变异。轨道 B 标记方法层面或资源层面、对两者都适用的来源。两条轨道在效应大小、数据可得性和混杂方面不同，因此分开分析，只在证据允许时才合并。

Variants are tagged with five classes. Class 1 is target coding variants that change binding or function. Class 2 is target regulatory variants that change expression, such as cis-eQTLs. Class 3 is copy-number and structural variants. Class 4 is pathway upstream, downstream and bypass variants. Class 5 is pharmacokinetic (PK) gene variants affecting metabolism and transport, which are a confounder when the question concerns pharmacodynamics (PD). The tags in `data/sources.csv` are curator judgments, not claims made by the sources.

> 变异被标记为五类。类别 1 是改变结合或功能的靶点编码变异。类别 2 是改变表达的靶点调控变异，如 cis-eQTL。类别 3 是拷贝数与结构变异。类别 4 是通路上游、下游和旁路变异。类别 5 是影响代谢和转运的药代动力学（PK）基因变异，当问题涉及药效动力学（PD）时它们是混杂因素。`data/sources.csv` 中的标签是整理者的判断，不是来源本身的论断。

## 4. Hidden assumptions to confirm or drop / 需要确认或放弃的隐含假设

H1. Genetic variation changes drug-induced transcriptional responses enough, and broadly enough, to justify dedicated modeling. The evidence is present but sparse: see the reQTL studies [GD06, GD08, GD01].

> H1. 遗传变异对药物诱导转录响应的改变足够大、足够广，值得专门建模。证据存在但稀疏：见 reQTL 研究 [GD06, GD08, GD01]。

H2. The transcriptome is a meaningful mediating phenotype. Only the doxorubicin study retrieved here links in-vitro response to in-vivo cardiotoxicity risk [GD06], and its generality is unknown.

> H2. 转录组是有意义的中介表型。此处检索到的研究中，只有阿霉素研究把体外响应与体内心脏毒性风险联系起来 [GD06]，其普遍性未知。

H3. A world-model architecture gives gains over conditional-generative or linear models. This is untested.

> H3. 世界模型架构相对条件生成模型或线性模型有增益。这一点尚未检验。

H4. Matched data of genotype, drug and post-treatment transcriptome can be obtained or constructed, or cell-line genotype can proxy individual genotype. The proxy is strongly confounded with lineage and epigenome [DS05].

> H4. 可以获得或构造基因型、药物与处理后转录组相匹配的数据，或者细胞系基因型可以代理个体基因型。该代理与谱系和表观基因组强烈混杂 [DS05]。

H5. In-vitro results transfer to in-vivo settings.

> H5. 体外结果可迁移到体内情境。

H6. End-point snapshots are enough to model dynamics and transitions.

> H6. 终点快照足以建模动力学与转移。

H7. Somatic and germline variation can be handled in one framework.

> H7. 体细胞变异与种系变异可以在同一框架内处理。

## 5. Common mistakes to avoid / 需要避免的常见错误

E1. Evaluating with genome-wide MSE or Pearson correlation lets mean baselines win [EV01, EV02].

> E1. 用全基因组 MSE 或 Pearson 相关评估，会让均值基线占优 [EV01, EV02]。

E2. Treating cell-line identity as genotype confounds lineage, epigenome and batch [DS05].

> E2. 把细胞系身份当作基因型，会混杂谱系、表观基因组和批次 [DS05]。

E3. Random splits leak information through neighboring drugs, cell lines and pathways. Use leave-one-line-out, leave-one-drug(-class)-out and leave-one-variant-out splits.

> E3. 随机划分会通过相近的药物、细胞系和通路泄漏信息。应使用留一细胞系、留一药物（或药物类别）和留一变异的划分。

E4. Treating sequence-model predictions as ground truth [GV05].

> E4. 把序列模型的预测当作真值 [GV05]。

E5. Treating GDSC, CTRP, CCLE and PRISM as interchangeable. Cross-dataset agreement is reportedly low, but that claim could not be tied to a source (see the search log, item F18 b), so it is unverified.

> E5. 把 GDSC、CTRP、CCLE 和 PRISM 视为可互换。据称跨数据集一致性较低，但该说法无法对应到具体来源（见检索日志的 F18 b 项），因此未经核验。

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

## 6. Missing information that could change the result / 可能改变结果的缺失信息

M1. Target variant track: somatic (cancer) or germline (population). It determines data and evaluation. Default: both tracks in parallel, somatic first.

> M1. 目标变异轨道：体细胞（癌症）还是种系（人群）。它决定数据与评测。默认：两条轨道并行，体细胞优先。

M2. Target drug classes and cell types. They determine prior availability. Default: do not restrict, and annotate by drug class.

> M2. 目标药物类别和细胞类型。它们决定先验的可得性。默认：不设限制，按药物类别标注。

M3. The operational definition of "world model". It determines the tests. Default: the definition recorded in document 06, kept as falsifiable items in document 08.

> M3. “世界模型”的操作性定义。它决定检验项。默认：采用文档 06 中记录的定义，并作为可证伪项保存在文档 08 中。

M4. Data and compute budget, including whether new Perturb-seq data can be generated. Default: public data only.

> M4. 数据与算力预算，包括能否自行产生新的 Perturb-seq 数据。默认：仅使用公开数据。

## 7. The deeper question behind the request (inference) / 请求背后的更深层问题（推断）

The request that started this repository was a single message, so there is no history of repeated discussion to draw on; the following is inferred from the request itself. The end goal is a world model, but the question that may not yet have been asked is whether the available data contain a large enough, clean enough, trainable and falsifiable signal in the genotype-by-drug interaction. If the signal lives only in a small slice, such as somatic driver mutations or a few reQTLs, then "does a world model beat linear baselines?" is not an architecture choice but an experiment that must first be designed to be falsifiable. Its twin question is how much of the genotype effect is mediated by baseline expression.

> 开启本仓库的请求只有一条消息，因此没有可归纳的反复讨论历史；以下是基于请求本身的推断。最终目标是世界模型，但可能尚未被问出口的问题是：现有数据在基因型×药物交互项上，是否含有足够大、足够干净、可训练且可证伪的信号。如果信号只存在于一小片区域，例如体细胞驱动突变或少数 reQTL，那么“世界模型是否优于线性基线”就不是架构选择，而是必须先设计成可证伪的实验。它的孪生问题是：基因型效应有多少是经由基线表达中介的。

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

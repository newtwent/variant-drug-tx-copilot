# 02 Genotype × drug → transcriptome evidence / 基因型×药物→转录组实证

## 1. Scope / 范围

This document collects the empirical evidence that genotype changes how cells respond to a drug at the transcriptome level: response-eQTL and gene-by-environment studies, dynamic and single-cell eQTL work, functional screens that read variant effects through the transcriptome, and the somatic-mutation literature on adaptive rewiring and resistance. It is the core evidence document for the question, and its main finding is that the evidence exists but is thin.

> 本文档汇集基因型在转录组层面改变细胞对药物响应的实证证据：响应型 eQTL 与基因×环境研究、动态与单细胞 eQTL 工作、通过转录组读出变异效应的功能筛选，以及关于适应性重编程和耐药的体细胞突变文献。它是本课题的核心证据文档，其主要发现是：证据存在，但很单薄。

## 2. Facts and evidence / 事实与证据

Response-eQTL (reQTL) studies exist, but each is small. Doxorubicin-treated iPSC-derived cardiomyocytes from 45 individuals yielded 376 reQTLs and 42 response sQTLs, and more than 6,000 genes were differentially spliced [GD06]. 114 lymphoblastoid lines treated with glucocorticoid showed genotype-by-treatment interactions for 26 genes, including NQO1, AIRE and SGK1, and for IL6 secretion, and genotype effects could appear only under treatment or only under control [GD08]. Primary hepatocytes from African American donors treated with several drugs reported 2,988 reQTLs, but the donor and drug counts were not retrieved [GD01].

> 响应型 eQTL（reQTL）研究确实存在，但每项规模都不大。来自 45 人的 iPSC 来源心肌细胞经阿霉素处理，得到 376 个 reQTL 和 42 个响应 sQTL，超过 6,000 个基因发生差异剪接 [GD06]。114 个淋巴母细胞系经糖皮质激素处理，26 个基因（包括 NQO1、AIRE 和 SGK1）以及 IL6 分泌存在基因型×处理交互，且基因型效应可以只出现在处理下或只出现在对照下 [GD08]。非裔供体的原代肝细胞经多种药物处理，报告 2,988 个 reQTL，但供体数与药物数未取得 [GD01]。

The doxorubicin study is the only one retrieved that connects in-vitro response to clinical risk: inter-individual differences in transcriptional response predicted in-vitro cell damage, and that damage was associated with in-vivo anthracycline cardiotoxicity risk [GD06]. A separate study of iPSC-derived cardiomyocytes from 6 women found a shared gene-expression response signature across anthracyclines [GD07].

> 阿霉素研究是检索到的唯一把体外响应与临床风险联系起来的研究：转录响应的个体间差异预测了体外细胞损伤，而这种损伤与体内蒽环类药物的心脏毒性风险相关 [GD06]。另一项针对 6 名女性 iPSC 来源心肌细胞的研究发现了蒽环类药物之间共享的基因表达响应特征 [GD07]。

A summary of related work states that treatment-specific interactions between the cellular environment and cis-variants were relatively rare, with one validated glucocorticoid-specific effect on TNC. The search output itself noted a separate osteoblast study, so it is unclear whether that statement belongs to [GD08] or to another study.

> 一份相关工作的总结称，细胞环境与 cis 变异之间的处理特异交互相对少见，并验证了一个糖皮质激素特异的 TNC 效应。检索输出本身提示另有一项成骨细胞研究，因此尚不清楚这一说法属于 [GD08] 还是另一项研究。

eQTL effects vary with cell state, stimulus and differentiation stage. 125 iPSC lines profiled at 4 time points of endoderm differentiation gave about 899 time-dynamic eQTLs according to a secondary summary [GD18], and a method for single-cell allele-specific expression, applied to the same iPSC differentiation data, found 657 dynamically regulated genes, again from a secondary summary [GD19]. T-cell-state-dependent eQTLs [GD20] and lineage-specific dynamic regulation during cardiomyocyte differentiation [GD21] have also been reported. The single-cell eQTLGen consortium describes dynamic eQTLs along pseudotime and notes that regulatory-network changes may explain part of the inter-individual variation in drug response, a point it says has not been studied in detail [GD14].

> eQTL 的效应随细胞状态、刺激和分化阶段而变化。125 株 iPSC 在内胚层分化的 4 个时间点被测定，据二手总结约有 899 个时间动态 eQTL [GD18]，一种单细胞等位基因特异表达方法应用于同一套 iPSC 分化数据，发现 657 个动态调控基因，同样来自二手总结 [GD19]。也已有 T 细胞状态依赖 eQTL [GD20] 以及心肌细胞分化过程中谱系特异动态调控 [GD21] 的报道。单细胞 eQTLGen 联盟描述了沿拟时间变化的动态 eQTL，并指出调控网络的变化可能解释药物反应个体间差异的一部分，但它称这一点尚未被详细研究 [GD14]。

Stimuli change both the mean and the variability of gene expression, and genetic variants have been identified for both [GD09]. Most context-specific eQTLs can already be detected in very large bulk RNA-seq data, but single cells are needed to pinpoint the relevant context [GD16].

> 刺激会同时改变基因表达的均值和变异度，并且已鉴定出针对两者的遗传变异 [GD09]。多数情境特异的 eQTL 已经可以在超大规模 bulk RNA-seq 数据中检出，但需要单细胞才能定位相关情境 [GD16]。

Functional screens that read variant effects at transcriptome level already exist. Base editing plus Perturb-seq was used for drug-resistance variants in 11 cancer genes (dabrafenib and cetuximab, HT-29 cells), and a sensitizing EGFR variant was validated [GD23]. Perturb(BE)-seq was used on GATA1 variants and fetal-hemoglobin promoter variants [GD24], and Perturb-seq has scored TP53 and KRAS coding variants [GD26]. Base editing keeps variants at endogenous expression levels but editing is incomplete, and editing efficiency depends on local sequence context [GD27, GD28].

> 在转录组层面读取变异效应的功能筛选已经存在。碱基编辑加 Perturb-seq 被用于 11 个癌症基因中的耐药变异（dabrafenib 和 cetuximab，HT-29 细胞），并验证了一个使 EGFR 敏化的变异 [GD23]。Perturb(BE)-seq 被用于 GATA1 变异和胎儿血红蛋白启动子变异 [GD24]，Perturb-seq 也对 TP53 和 KRAS 编码变异进行了打分 [GD26]。碱基编辑使变异保持在内源表达水平，但编辑不完全，且编辑效率取决于局部序列背景 [GD27, GD28]。

I did not find human data that combine several donor genotypes, Perturb-seq and drugs. The closest analogue is a yeast CRISPRi study across 169 segregants, in which 460 genes showed background-dependent perturbation effects, with 234 interacting loci and 4 hub loci [GD30]. The human perturbation panels retrieved here mostly use a single donor background: the iPSC-cardiomyocyte panel had 75 perturbation conditions [GD31], and the genome-wide iPSC CRISPRi atlas used one line [DS09]. The genome-scale screen in primary CD4+ T cells used 4 donors, but no donor-by-perturbation analysis was seen in the retrieved excerpt [DS08].

> 我没有找到同时包含多个供体基因型、Perturb-seq 和药物的人类数据。最接近的类比是跨 169 个分离子的酵母 CRISPRi 研究，其中 460 个基因的扰动效应依赖遗传背景，涉及 234 个交互位点和 4 个枢纽位点 [GD30]。此处检索到的人类扰动面板大多使用单一供体背景：iPSC 心肌细胞面板有 75 种扰动条件 [GD31]，全基因组 iPSC CRISPRi 图谱只用了一个细胞系 [DS09]。原代 CD4+ T 细胞的基因组规模筛选使用了 4 名供体，但在检索到的摘录中未见供体×扰动的交互分析 [DS08]。

The cell-type specificity of drug-induced transcription depends on drug class. In about 600 LINCS drug–cell-line pairs, inhibitors of signaling kinases gave cell-type-specific changes, whereas inhibitors of chaperones and cell-cycle kinases gave more uniform changes [GD41].

> 药物诱导转录的细胞类型特异性取决于药物类别。在约 600 个 LINCS 药物-细胞系对中，信号激酶抑制剂引起细胞类型特异的变化，而伴侣蛋白和细胞周期激酶抑制剂引起的变化较一致 [GD41]。

Somatic genotype shapes adaptive transcriptional rewiring. In BRAF-mutant melanoma, resistance was associated with BRAF V600E allele zygosity and receptor-tyrosine-kinase mutation status, with broad ErbB up-regulation after treatment [GD42]. Resistance to BRAF and EGFR inhibition in BRAF V600E colorectal tumors runs through an SRC–COX2 program that is reversible [GD32], and EGFR expression rose in 6 of 16 post-resistance melanoma biopsies [GD36]. Two TP53 wild-type colorectal lines responded differently to BRAF V600E expression [GD44], and mutant p53 shaped chromatin accessibility and drug tolerance in pancreatic cancer [GD43].

> 体细胞基因型塑造适应性转录重编程。在 BRAF 突变黑色素瘤中，耐药与 BRAF V600E 等位基因合子性及受体酪氨酸激酶突变状态相关，治疗后 ErbB 通路广泛上调 [GD42]。BRAF V600E 结直肠肿瘤对 BRAF 和 EGFR 抑制的耐药经由一个可逆的 SRC–COX2 程序 [GD32]，16 例耐药后黑色素瘤活检中有 6 例 EGFR 表达上升 [GD36]。两株 TP53 野生型结直肠细胞系对 BRAF V600E 表达的反应不同 [GD44]，突变型 p53 塑造了胰腺癌中的染色质可及性和药物耐受 [GD43]。

The search summaries suggest that non-genetic transcriptional adaptation often precedes genetic resistance; this is a synthesis across sources, not a single-paper result [GD33, GD34, GD37]. Different inhibitor classes give different kinome-reprogramming patterns: BRAF–MEK–ERK and PI3K–AKT inhibitors differ [GD34].

> 检索摘要提示，非遗传的转录适应常早于遗传耐药；这是跨来源的综合，不是单篇论文的结果 [GD33, GD34, GD37]。不同类别的抑制剂产生不同的激酶组重编程模式：BRAF–MEK–ERK 与 PI3K–AKT 抑制剂不同 [GD34]。

## 3. Evidence map / 证据地图

| Design | Example | Scale reported | Source IDs | 设计 / 示例（中文） |
|---|---|---|---|---|
| Bulk reQTL, drug dose series | iPSC cardiomyocytes, doxorubicin | 45 individuals; 376 reQTLs | GD06 | 批量 reQTL、药物剂量系列：iPSC 心肌细胞，阿霉素 |
| Gene-by-treatment in cell lines | Lymphoblastoid lines, glucocorticoid | 114 lines; 26 genes | GD08 | 细胞系中的基因×处理：淋巴母细胞系，糖皮质激素 |
| Multi-drug reQTL | Primary hepatocytes | 2,988 reQTLs | GD01 | 多药 reQTL：原代肝细胞 |
| Dynamic single-cell eQTL | iPSC endoderm differentiation | 125 lines; 4 time points | GD18 | 动态单细胞 eQTL：iPSC 内胚层分化 |
| Variant screen with drug | Base editing plus Perturb-seq, HT-29 | 11 cancer genes | GD23 | 带药物的变异筛选：碱基编辑加 Perturb-seq，HT-29 |
| Coding-variant screen | Perturb-seq of TP53 and KRAS variants | not retrieved | GD26 | 编码变异筛选：TP53 和 KRAS 变异的 Perturb-seq |
| Genotype-by-perturbation (yeast) | CRISPRi across segregants | 169 segregants | GD30 | 基因型×扰动（酵母）：跨分离子的 CRISPRi |
| Somatic mutation and rewiring | BRAF V600E, EGFR, SRC–COX2 | case-level | GD32, GD36, GD42 | 体细胞突变与重编程：BRAF V600E、EGFR、SRC–COX2 |
| Cell-line panels with drug transcriptomes | LINCS pairs; Tahoe-100M | about 600 pairs; 50 lines | GD41, DS05 | 带药物转录组的细胞系面板：LINCS 药物-细胞系对；Tahoe-100M |

## 4. Judgments / 判断

J1 (confidence: medium). This search did not find public data that pair germline genotype, drug exposure and post-treatment transcriptomes at a scale suitable for training deep models. Published reQTL studies cover roughly 45–114 individuals and few drugs, and cell-line panels offer only about 50–70 genotypes confounded with lineage and epigenome [GD06, GD08, DS01, DS05]. This is an absence claim from a limited search engine, so treat it as a hypothesis to be checked.

> J1（置信度：中）。本次检索没有找到规模适合训练深度模型、同时配对种系基因型、药物暴露和处理后转录组的公开数据。已发表的 reQTL 研究约覆盖 45–114 人且药物很少，细胞系面板只提供约 50–70 个与谱系和表观基因组混杂的基因型 [GD06, GD08, DS01, DS05]。这是基于受限搜索引擎的“缺失”判断，应作为待检验的假设。

J2 (confidence: medium). The most trainable slice is probably somatic driver mutations crossed with targeted drugs in cancer cell lines: effects are larger, annotations are complete, and data are abundant [DS01, DS05, GD42]. Common germline variants have small effects and are better used for external validation and as priors.

> J2（置信度：中）。最可训练的切片很可能是癌症细胞系中的体细胞驱动突变 × 靶向药物：效应更大，注释完整，数据丰富 [DS01, DS05, GD42]。常见的种系变异效应小，更适合用作外部验证和先验。

J3 (confidence: medium; the key testable hypothesis). Most genotype effects on drug-induced expression change may be mediated through the baseline transcriptional state. If so, a model conditioned on control expression already absorbs genotype implicitly, and explicit variant features help only when they change the response operator itself, through binding sites, gain or loss of function, or response-specific regulatory variants. The first experiment should therefore test whether genotype adds information beyond baseline expression; the only supporting hint is indirect [EV16].

> J3（置信度：中；关键的可检验假设）。基因型对药物诱导表达变化的大部分影响，可能是经由基线转录状态中介的。若如此，已条件于对照表达的模型就已隐式吸收了基因型，只有当变异通过结合位点、功能获得或丧失、或响应特异的调控变异改变响应算子本身时，显式变异特征才有帮助。因此第一个实验应检验基因型是否在基线表达之外提供额外信息；唯一的支持线索是间接的 [EV16]。

## 5. Recommended actions / 行动建议

Treat the somatic track as primary, and use published reQTL results, such as the anthracycline study, as external validation and positive controls for the germline track [GD06, DS13].

> 把体细胞轨道作为主要轨道，并把已发表的 reQTL 结果（如蒽环类药物研究）用作种系轨道的外部验证和阳性对照 [GD06, DS13]。

For every study added later, record the same fields so that studies can be compared: genotype source, drug, dose, time, cell type, readout and number of individuals or lines.

> 对以后加入的每项研究都记录相同的字段，以便比较各研究：基因型来源、药物、剂量、时间、细胞类型、读出方式以及个体数或细胞系数。

Run the mediation test described in document 08 before investing in explicit variant modeling.

> 在投入显式变异建模之前，先运行文档 08 中描述的中介检验。

## 6. Questions for confirmation / 待确认问题

Can new data be generated, for example a multi-line Perturb-seq experiment with drugs? Default: no, public data only (assumption M4 in document 00).

> 能否产生新数据，例如带药物的多细胞系 Perturb-seq 实验？默认：不能，仅使用公开数据（文档 00 中的假设 M4）。

## 7. Evidence gaps / 证据缺口

No result on drug-stimulation-specific single-cell eQTLs was found (query Q04). No human study combining multi-donor genotypes, Perturb-seq and drugs was found (queries Q12 and Q33). No statin study in lymphoblastoid lines or hepatocytes was found (queries Q17 and Q30). A study of 51 individuals exposed to ethanol, caffeine and nicotine, reported by a search summary, could not be tied to a source and is not recorded as a fact (item F18 a in the search log). No study stratifying BRAF, KRAS and TP53 status jointly with pharmacotranscriptomic readouts was found (query Q43).

> 未找到关于药物刺激特异的单细胞 eQTL 的结果（查询 Q04）。未找到同时包含多供体基因型、Perturb-seq 和药物的人类研究（查询 Q12 和 Q33）。未找到在淋巴母细胞系或肝细胞中的他汀研究（查询 Q17 和 Q30）。检索摘要报告的一项涉及 51 人、暴露于乙醇、咖啡因和尼古丁的研究无法对应到来源，因此不记为事实（检索日志中的 F18 a 项）。未找到把 BRAF、KRAS 和 TP53 状态与药物转录组读出联合分层的研究（查询 Q43）。

## 8. Source index (category GD) / 来源索引（类别 GD）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:GD:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| GD01 | T2 | [Leveraging drug perturbation to reveal genetic regulators of hepatic gene expression in African Americans](<https://pubmed.ncbi.nlm.nih.gov/36608685/>) | primary hepatocytes, several drugs; 2,988 reQTLs; rs61017966 with CYP3A5; 2.7-fold power gain from joint mapping; donor and drug counts not retrieved; CYP3A5 is a PK gene | 原代肝细胞、多种药物；2,988 个 reQTL；rs61017966 与 CYP3A5；联合作图检出力提高 2.7 倍；供体数与药物数未取得；CYP3A5 属 PK 基因 |
| GD02 | T2 | [Computational discovery of transcription factors associated with drug response (GENMi)](<https://www.nature.com/articles/tpj201574>) | TF-binding-site SNPs linked to drug response in lymphoblastoid lines; journal name to be verified | 淋巴母细胞系中，TF 结合位点 SNP 与药物反应相关联；期刊名待核 |
| GD03 | T2 | [Dissecting the Effect of Genetic Variation on the Hepatic Expression of Drug Disposition Genes across the Collaborative Cross Mouse Strains](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5050206/>) | mouse | 小鼠 |
| GD04 | T2 | [eQTLs identify regulatory networks and drivers of variation in the individual response to sepsis](<https://www.biorxiv.org/content/10.1101/2023.09.22.558983.full.pdf>) | title only | 仅标题级 |
| GD05 | T2 | [Identification of drug responsive enhancers by predicting chromatin accessibility change from perturbed gene expression profiles (PERD)](<https://pmc.ncbi.nlm.nih.gov/articles/PMC11139989>) | — | — |
| GD06 | T2 | [Determining the genetic basis of anthracycline-cardiotoxicity by molecular response QTL mapping in induced cardiomyocytes](<https://elifesciences.org/articles/33480>) | 45 individuals, iPSC cardiomyocytes, 24 h, several doxorubicin doses; 376 reQTLs and 42 response sQTLs; over 6,000 genes differentially spliced; in-vitro damage predicted from response relates to in-vivo cardiotoxicity risk | 45 人的 iPSC 心肌细胞，24 小时，多个阿霉素剂量；376 个 reQTL 和 42 个响应 sQTL；超过 6,000 个基因发生差异剪接；由响应预测的体外损伤与体内心脏毒性风险相关 |
| GD07 | T2 | [Anthracyclines induce cardiotoxicity through a shared gene expression response signature](<https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1011164>) | iPSC cardiomyocytes from 6 women; several breast-cancer drugs | 来自 6 名女性的 iPSC 心肌细胞；多种乳腺癌药物 |
| GD08 | T2 | [Interactions between Glucocorticoid Treatment and Cis-Regulatory Polymorphisms Contribute to Cellular Response Phenotypes](<https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1002162>) | 114 EBV-transformed B-cell lines (African and European ancestry); interactions for 26 genes (for example NQO1, AIRE, SGK1) and IL6 secretion; a related summary says treatment-specific interactions were relatively rare and validated one TNC effect, but the search output itself flagged a separate osteoblast study, so attribution is unclear | 114 个 EBV 转化 B 细胞系（非洲与欧洲祖源）；26 个基因（如 NQO1、AIRE、SGK1）和 IL6 分泌存在交互；相关摘要称处理特异交互相对少见并验证了一个 TNC 效应，但检索输出自身提示另有一项成骨细胞研究，归属不明 |
| GD09 | T2 | [Genetic control of the dynamic transcriptional response to immune stimuli and glucocorticoids at single-cell resolution](<https://genome.cshlp.org/content/33/6/839>) | stimuli change both mean and variability of expression | 刺激同时改变表达的均值与变异度 |
| GD10 | T2 | [Disease-associated loci share properties with response eQTLs under common environmental exposures](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12136233/>) | — | — |
| GD11 | T2 | [Multiomics Analysis of the Molecular Response to Glucocorticoids: Insights Into Shared Genetic Risk From Psychiatric to Medical Disorders](<https://www.biologicalpsychiatryjournal.com/article/S0006-3223(24)01653-6/fulltext>) | — | — |
| GD12 | T2 | [Allele-specific expression reveals interactions between genetic variation and environment](<https://www.biorxiv.org/content/10.1101/025874.full.pdf>) | — | — |
| GD13 | T2 | [Global Analysis of the Impact of Environmental Perturbation on cis-Regulation of Gene Expression](<https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1001279>) | species and design not retrieved | 物种与设计未取得 |
| GD14 | T2 | [The single-cell eQTLGen consortium](<https://elifesciences.org/articles/52155>) | dynamic eQTLs along pseudotime; authors note regulatory-network changes may explain part of inter-individual variation in drug response, but this has not been studied in detail | 沿拟时间的动态 eQTL；作者指出调控网络变化可能解释药物反应个体差异的一部分，但尚未被详细研究 |
| GD15 | T2 | [An atlas of single-cell eQTLs dissects autoimmune disease genes and identifies novel drug classes for treatment](<https://www.sciencedirect.com/science/article/pii/S2666979X2500076X>) | JOBS finds 586% more eQTLs in OneK1K plus eQTLGen (secondary) | JOBS 在 OneK1K 加 eQTLGen 中多检出 586% 的 eQTL（二手） |
| GD16 | T2 | [Single-cell RNA-sequencing of peripheral blood mononuclear cells reveals widespread, context-specific gene expression regulation upon pathogenic exposure](<https://www.nature.com/articles/s41467-022-30893-5>) | most context-specific eQTLs are detectable in very large bulk RNA-seq, but single cells pinpoint the context | 多数情境特异 eQTL 可在超大规模 bulk RNA-seq 中检出，但需单细胞才能定位情境 |
| GD17 | T2 | [Identification of genes conferring individual-level variation responsible for MASH using single-cell eQTL analysis](<https://www.biorxiv.org/content/10.1101/2024.09.20.614203.full.pdf>) | peripheral | 外围条目 |
| GD18 | T2 | [Single-cell RNA-sequencing of differentiating iPS cells reveals dynamic genetic effects on gene expression](<https://www.biorxiv.org/content/10.1101/630996v1.full>) | 125 iPSC lines, endoderm differentiation, 4 time points; about 899 time-dynamic eQTLs (secondary) | 125 株 iPSC，内胚层分化，4 个时间点；约 899 个时间动态 eQTL（二手） |
| GD19 | T2 | [Single-cell allele-specific expression analysis reveals dynamic and cell-type-specific regulatory effects (DAESC)](<https://www.nature.com/articles/s41467-023-42016-9>) | 657 dynamically regulated genes (secondary) | 657 个动态调控基因（二手） |
| GD20 | T2 | [Single-cell eQTL models reveal dynamic T cell state dependence of disease loci](<https://www.nature.com/articles/s41586-022-04713-1>) | — | — |
| GD21 | T2 | [Single-cell sequencing reveals lineage-specific dynamic genetic regulation of gene expression during human cardiomyocyte differentiation](<https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1009666>) | — | — |
| GD22 | T2 | [eQTL Studies: from Bulk Tissues to Single Cells](<https://arxiv.org/pdf/2302.11662>) | review | 综述 |
| GD23 | T2 | [Base editing screens define the genetic landscape of cancer drug resistance mechanisms](<https://www.nature.com/articles/s41588-024-01948-8>) | 11 cancer genes; Perturb-seq of variants conferring dabrafenib / cetuximab resistance in HT-29 cells; validated a sensitizing EGFR variant | 11 个癌症基因；在 HT-29 细胞中对赋予 dabrafenib / cetuximab 耐药的变异做 Perturb-seq；验证了一个使 EGFR 敏化的变异 |
| GD24 | T2 | [Base-editing screens illuminate variant effects in human hematopoiesis (Perturb(BE)-seq)](<https://www.sciencedirect.com/science/article/pii/S2667237523001789>) | GATA1 and HbF promoter variants | GATA1 与 HbF 启动子变异 |
| GD25 | T3 | [Perturb-seq Using ABE8e Base Editing to Functionally Characterize a Subset of Blood Pressure- and CAD-Associated Genetic Variants in TeloHAEC Cells (protocol)](<https://www.researchgate.net/publication/392671077_Perturb-seq_Using_ABE8e_Base_Editing_to_Functionally_Characterize_a_Subset_of_Blood_Pressure-_and_CAD-Associated_Genetic_Variants_in_TeloHAEC_Cells_v1>) | endothelial cells; protocol | 内皮细胞；实验方案 |
| GD26 | T2 | [Massively parallel phenotyping of coding variants in cancer with Perturb-seq](<https://www.nature.com/articles/s41587-021-01160-7>) | TP53 and KRAS variants | TP53 与 KRAS 变异 |
| GD27 | T3 | [Interface-guided phenotyping of coding variants in ... (title truncated; abstract mentions RUNX1)](<https://idekerlab.ucsd.edu/wp-content/uploads/2024/10/Ozturk-CellReports-2024-2.pdf>) | base editing keeps endogenous expression levels but editing is incomplete | 碱基编辑保留内源表达水平，但编辑不完全 |
| GD28 | T2 | [Joint genotypic and phenotypic outcome modeling improves base editing variant effect quantification](<https://www.medrxiv.org/content/10.1101/2023.09.08.23295253.full.pdf>) | editing efficiency depends on local sequence context | 编辑效率取决于局部序列背景 |
| GD29 | T2 | [Massively parallel assessment of human variants with base editor screens](<https://www.biorxiv.org/content/10.1101/2020.05.17.100818.full.pdf>) | — | — |
| GD30 | T2 | [Genome-scale analysis of interactions between genetic perturbations and natural variation](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11102447/>) | yeast; CRISPRi across 169 segregants; 460 genes with background-dependent effects; 234 interacting loci; 4 hub loci | 酵母；跨 169 个分离子的 CRISPRi；460 个基因的效应依赖遗传背景；234 个交互位点；4 个枢纽位点 |
| GD31 | T2 | [Responsiveness to perturbations is a hallmark of transcription factors that maintain cell identity in vitro (P³)](<https://www.cell.com/cell-systems/fulltext/S2405-4712(21)00281-7>) | iPSC cardiomyocytes, 75 perturbation conditions; single donor background | iPSC 心肌细胞，75 种扰动条件；单一供体背景 |
| GD32 | T2 | [A reversible SRC-relayed COX2 inflammatory program drives resistance to BRAF and EGFR inhibition in BRAFV600E colorectal tumors](<https://www.nature.com/articles/s43018-022-00508-5>) | SRC activation drives beta-catenin-dependent transcriptional changes; COX2 inhibitor co-targeting works in PDX | SRC 激活驱动依赖 β-连环蛋白的转录改变；COX2 抑制剂共靶向在 PDX 中有效 |
| GD33 | T2 | [Signaling and transcriptional dynamics underlying early adaptation to oncogenic BRAF inhibition](<https://www.biorxiv.org/content/10.1101/2024.02.19.581004.full.pdf>) | preprint | 预印本 |
| GD34 | T2 | [Adaptive chromatin remodeling and transcriptional changes of the functional kinome in tumor cells in response to targeted kinase inhibition](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8888345/>) | BRAF–MEK–ERK and PI3K–AKT inhibitors give different patterns | BRAF–MEK–ERK 与 PI3K–AKT 抑制剂的模式不同 |
| GD35 | T2 | [Mechanistic model of MAPK signaling reveals how allostery and rewiring contribute to drug resistance](<https://www.biorxiv.org/content/10.1101/2022.02.17.480899.full.pdf>) | mechanistic model | 机制模型 |
| GD36 | T2 | [EGFR Activation Constitutes an Adaptive Response to BRAF Inhibitor Therapy](<https://aacrjournals.org/cancerdiscovery/article/4/6/OF17/4795/EGFR-Activation-Constitutes-an-Adaptive-Response>) | EGFR expression up in 6 of 16 post-resistance melanoma biopsies | 16 例耐药后黑色素瘤活检中 6 例 EGFR 表达上升 |
| GD37 | T2 | [The Inhibition of CDK8/19 Mediator Kinases Prevents the Development of Resistance to EGFR-Targeting Drugs](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7828184/>) | — | — |
| GD38 | T2 | [Bayesian model of signal rewiring reveals mechanisms of gene dysregulation in acquired drug resistance in breast cancer](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5348014/>) | — | — |
| GD39 | T2 | [Ribosomal Biogenesis Hyperactivation and ErbB signalling Mediated Network Rewiring Causes Adaptive Resistance to FGFR2 Inhibition](<https://www.biorxiv.org/content/10.1101/2024.10.27.620536.full.pdf>) | peripheral | 外围条目 |
| GD40 | T2 | [BRAF inhibitor resistance in melanoma: from resistance mechanisms to therapeutic innovations](<https://link.springer.com/article/10.1186/s43556-026-00425-4>) | review | 综述 |
| GD41 | T2 | [Common and cell-type specific responses to anti-cancer drugs revealed by high throughput transcript profiling](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5662764/>) | about 600 LINCS drug–cell-line pairs; signaling-kinase inhibitors give cell-type-specific changes | 约 600 个 LINCS 药物-细胞系对；信号激酶抑制剂引起细胞类型特异的变化 |
| GD42 | T2 | [Systems Analysis of Adaptive Responses to MAP Kinase Pathway Blockade in BRAF Mutant Melanoma](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4583389/>) | resistance linked to BRAF V600E zygosity and RTK mutation status; broad ErbB up-regulation | 耐药与 BRAF V600E 合子性及 RTK 突变状态相关；ErbB 广泛上调 |
| GD43 | T2 | [p53 mutations define the chromatin landscape to confer drug tolerance in pancreatic cancer](<https://pmc.ncbi.nlm.nih.gov/articles/PMC8936522/>) | — | — |
| GD44 | T2 | [BRAFV600E-induced distinct DNA damage response defines the therapeutic potential of p53 activation for TP53 wild-type colorectal cancer](<https://doi.org/10.1093/carcin/bgae040>) | two TP53-wild-type lines responded differently | 两株 TP53 野生型细胞系的反应不同 |
<!-- source-index:GD:end -->

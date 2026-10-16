# 03 Data resources / 数据资源

## 1. Scope / 范围

This document describes the datasets that could feed a model of how variants shape drug-induced transcriptional responses: drug-perturbation transcriptomes, Perturb-seq atlases, response-QTL and eQTL data, and cell-line annotation resources. It records what was retrieved about their scale and about the genotype information they carry. Nothing here has been downloaded or inspected, so access routes, licenses and exact schemas are unchecked.

> 本文档描述可能用于建模“变异如何塑造药物诱导转录响应”的数据集：药物扰动转录组、Perturb-seq 图谱、响应 QTL 与 eQTL 数据，以及细胞系注释资源。它记录了检索到的关于其规模和所含基因型信息的内容。这里的任何数据都没有被下载或检查，因此获取途径、许可和确切模式均未核查。

## 2. Facts and evidence / 事实与证据

LINCS L1000 has 1,319,138 profiles [DS01, DS03]. An earlier pilot of the connectivity-map idea covered only 164 drug perturbations across 3 cancer cell lines, which motivated the scale-up [DS01]. A secondary description gives about 19,811 compounds across about 70 cell lines, and a beta successor with more than 80k perturbations, more than 200 cell lines and more than 3 million profiles [DS04]. TranSiGen, a chemical-response model built on L1000, predicts 978 landmark genes and then infers the rest of the transcriptome with a weight matrix from the L1000 project, which suggests that the assay measures a reduced gene set (an inference from the model description, not a statement about the assay itself) [MD03].

> LINCS L1000 有 1,319,138 个谱 [DS01, DS03]。连接图谱思路的早期试点只覆盖 164 次药物扰动和 3 个癌症细胞系，这促成了规模扩大 [DS01]。一份二手描述给出约 19,811 种化合物 × 约 70 个细胞系，以及一个含超过 8 万（80k）次扰动、超过 200 个细胞系、超过 300 万个谱的测试版后继数据集 [DS04]。TranSiGen 是基于 L1000 构建的化学响应模型，它预测 978 个 landmark 基因，再用来自 L1000 项目的权重矩阵推断转录组的其余部分，这提示该检测只测量缩减的基因集（这是根据模型描述做出的推断，不是关于检测本身的陈述）[MD03]。

Tahoe-100M has about 100 million cells from 50 cancer cell lines and about 1,100 drug-dose conditions. Other sources give different counts, such as 379 drugs across 25 mechanisms and 52,886 cell-line–drug conditions, or 1,200 perturbations. Cells from genetically distinct lines are pooled in "cell villages" and assigned to their line by SNP-based deconvolution, and cell-line identity rather than batch dominates the clustering [DS05]. The published version reports that single-cell profiles retain proliferation, cytotoxicity and cell-cycle signals [DS06]. The dataset is public on Hugging Face [DS07].

> Tahoe-100M 含约 1 亿（100 million）个细胞，来自 50 个癌症细胞系，约 1,100 个药物-剂量条件。其他来源给出不同的计数，例如 25 种机制下的 379 种药物和 52,886 个细胞系-药物条件，或 1,200 次扰动。来自遗传上不同细胞系的细胞被混合成“细胞村”，并通过基于 SNP 的解卷积归属到各自的细胞系，主导聚类的是细胞系身份而不是批次 [DS05]。已发表版本报告单细胞谱保留增殖、细胞毒性和细胞周期信号 [DS06]。该数据集在 Hugging Face 上公开 [DS07]。

Perturb-seq resources are mostly genetic. A genome-scale screen in primary human CD4+ T cells covers about 22 million cells from 4 donors [DS08]. A genome-wide CRISPRi atlas in iPSCs uses the single KOLF2.1J line [DS09]. A benchmarking study in differentiating pluripotent stem cells found similar results in the H9 and WTC11 lines [DS10]. The original Perturb-seq method and a genetic-interaction study with rich single-cell phenotypes are the methodological roots [DS11, DS12].

> Perturb-seq 资源以遗传扰动为主。原代人 CD4+ T 细胞中的基因组规模筛选覆盖来自 4 名供体的约 2,200 万（22 million）个细胞 [DS08]。iPSC 中的全基因组 CRISPRi 图谱使用单一的 KOLF2.1J 细胞系 [DS09]。一项在分化中的多能干细胞上的基准研究发现 H9 和 WTC11 细胞系的结果相近 [DS10]。最初的 Perturb-seq 方法以及一项利用丰富单细胞表型的遗传互作研究是方法学的源头 [DS11, DS12]。

For the germline track, the response-QTL data of the anthracycline study have a Zenodo record, whose availability still has to be checked [DS13]. The benchmarks also use cell-line omics and drug-sensitivity compendia (DepMap, GDSC, PRISM), whose prediction targets are viability and gene dependency, not transcriptomes [EV15, EV16, EV17].

> 对于种系轨道，蒽环类药物研究的响应 QTL 数据有一个 Zenodo 记录，其可得性仍需核查 [DS13]。这些基准还使用细胞系组学与药物敏感性汇编（DepMap、GDSC、PRISM），其预测目标是活力和基因依赖性，而不是转录组 [EV15, EV16, EV17]。

Chemical and cytokine screens with single-cell readouts add dose and donor axes. sci-Plex measured dose-dependent responses to 188 compounds in 3 cancer cell lines (MCF7, K562 and A549), about 650,000 cells across 5,000 samples, with substantial intercellular heterogeneity of response [DS15]. The Parse PBMC atlas has 9,697,974 cells in 18 immune cell types from 12 donors treated with 90 cytokines or PBS for 24 hours, under commercial licence terms with a Hugging Face copy, and the retrieved text does not say whether the donors are genotyped [DS16]. The OP3 set has 146 chemical perturbations in PBMCs from 3 donors [DS17].

> 带单细胞读出的化学和细胞因子筛选增加了剂量轴和供体轴。sci-Plex 在 3 个癌细胞系（MCF7、K562 和 A549）中测量了对 188 种化合物的剂量依赖响应，约 650,000（65 万）个细胞、5,000 个样本，响应存在显著的细胞间异质性 [DS15]。Parse PBMC 图谱包含来自 12 名供体的 9,697,974 个细胞、18 种免疫细胞类型，用 90 种细胞因子或 PBS 处理 24 小时，适用商业许可条款并有 Hugging Face 副本，检索到的文字没有说明供体是否做了基因分型 [DS16]。OP3 数据集在来自 3 名供体的 PBMC 中有 146 种化学扰动 [DS17]。

Larger genetic screens report graded knockdown. X-Atlas/Orion has about 8 million cells in two genome-wide CRISPR screens (HCT116 and HEK293T), with median on-target knockdown of 75.4% and 51.5%, and argues that knockdown should be modeled as graded rather than on or off [DS18]. The genome-scale CRISPRi Perturb-seq in K562 and RPE1 has more than 2.5 million cells with median knockdown of 85.5% and 91.6% [DS19]. scPerturb harmonizes 44 public single-cell perturbation datasets and introduces E-statistics to quantify and test perturbation effects [DS20].

> 更大的遗传筛选报告了梯度敲低。X-Atlas/Orion 在两次全基因组 CRISPR 筛选（HCT116 和 HEK293T）中有约 8 million（800 万）个细胞，中位靶向敲低为 75.4% 和 51.5%，并主张应把敲低建模为梯度而不是开关 [DS18]。K562 和 RPE1 中的基因组规模 CRISPRi Perturb-seq 有超过 2.5 million（250 万）个细胞，中位敲低为 85.5% 和 91.6% [DS19]。scPerturb 把 44 个公开的单细胞扰动数据集做了协调，并引入 E 统计量来量化和检验扰动效应 [DS20]。

Time-resolved data and closed-loop data are sparse. scNT-seq and Well-TEMP-seq use 4sU metabolic labeling to separate new from old RNA, which resolves RNA trajectories after brief versus sustained stimulation and, for Well-TEMP-seq, after exposure of colorectal cancer cells to the DNA-demethylating drug 5-AZA-CdR [DS21, DS22]. LabCompass publishes about 60 GB of per-loop spectral flow cytometry measurements and about 1.07 million designs on Hugging Face, as described by its reproducibility README; the dataset page itself could not be read [DS23, WM29]. These are protein-level data on blood progenitors, so no transcriptome-level closed-loop data were found (query Q51).

> 时间分辨数据和闭环数据都很稀少。scNT-seq 和 Well-TEMP-seq 使用 4sU 代谢标记把新旧 RNA 分开，从而解析短暂与持续刺激后的 RNA 轨迹，Well-TEMP-seq 还解析了结直肠癌细胞暴露于 DNA 去甲基化药物 5-AZA-CdR 之后的轨迹 [DS21, DS22]。据其可复现 README 的描述，LabCompass 在 Hugging Face 上公布了约 60 GB 的逐轮光谱流式细胞术测量和约 1.07 million（107 万）个设计；数据集页面本身无法读取 [DS23, WM29]。这些是血液祖细胞的蛋白水平数据，因此没有找到转录组层面的闭环数据（查询 Q51）。

## 3. Dataset table / 数据集表

Generated from `data/datasets.csv`; all values are as retrieved, and NA means not retrieved.

> 由 `data/datasets.csv` 生成；所有值均为检索所得，NA 表示未取得。

<!-- dataset-table:start -->
| Dataset | Scale reported | Genotype information | Sources | Caveats | 注意事项（中文） |
|---|---|---|---|---|---|
| LINCS L1000 / CMap (2017 release) | 1,319,138 profiles (DS01, DS03); secondary description: about 19,811 compounds x about 70 cell lines (DS04) | cell-line identity only; no donor genotype retrieved | DS01, DS03, DS04 | Exact cell-line count of the 2017 release was not found; compound and cell-line counts are secondary. | 未找到 2017 年版本的确切细胞系数；化合物与细胞系数量为二手信息。 |
| LINCS2 beta (secondary description) | more than 80k perturbations; more than 200 cell lines; more than 3 million profiles (secondary) | — | DS04 | Known only from a Bioconductor package description; verify at the data provider. | 仅见于 Bioconductor 软件包的描述；需在数据提供方核实。 |
| Tahoe-100M | about 100 million cells; 50 cancer cell lines; about 1,100 drug-dose conditions (other sources: 379 drugs / 25 mechanisms / 52,886 cell-line-drug conditions; 1,200 perturbations) | cell-line identity assigned by SNP-based deconvolution of pooled cell villages | DS05, DS06, DS07 | Condition counts differ between sources; profiles retain proliferation, cytotoxicity and cell-cycle signals, so composition effects must be handled. | 各来源给出的条件数不一致；谱中保留增殖、细胞毒性和细胞周期信号，必须处理细胞构成效应。 |
| Genome-scale Perturb-seq in primary human CD4+ T cells | about 22 million cells; 4 donors; all expressed genes perturbed | donor identity (4 donors) | DS08 | The URL is the paper, not a data portal; data access was not checked. | 该 URL 是论文而不是数据门户；数据获取方式未核查。 |
| Perturbation cell atlas of human iPSCs (KOLF2.1J) | — | single iPSC line | DS09 | Scale not retrieved; the URL is the paper. | 规模未取得；该 URL 是论文。 |
| Anthracycline response-QTL dataset (iPSC-derived cardiomyocytes) | 45 individuals; 376 reQTLs; 42 response sQTLs | individual-level genotypes implied by QTL mapping; availability not checked | GD06, DS13 | Only 45 individuals; data availability to be checked. | 仅 45 人；数据可得性待核。 |
| Hepatocyte response-QTL study (African American donors) | 2,988 reQTLs; donor and drug counts not retrieved | donor genotypes (African American donors) | GD01 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| Glucocorticoid-treated lymphoblastoid lines | 114 EBV-transformed B-cell lines; 26 genes with genotype-by-treatment interactions | cell-line genotypes; African and European ancestry | GD08 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| iPSC endoderm-differentiation sc-eQTL (125 lines) | 125 iPSC lines; 4 time points; about 899 time-dynamic eQTLs (secondary) | 125 donor-derived lines | GD18 | The eQTL count is from a secondary summary. | eQTL 数量来自二手总结。 |
| Geuvadis (lymphoblastoid RNA-seq plus whole-genome data) | 421 individuals | whole-genome data | GV05 | Access route not retrieved. | 获取途径未取得。 |
| GTEx v8 | up to 15% non-European-ancestry individuals (EV25) | — | EV25, GV02 | Size and access route not retrieved. | 规模与获取途径未取得。 |
| OneK1K plus eQTLGen (single-cell eQTL atlas) | — | — | GD15 | Scale not retrieved; the 586% gain is a secondary figure. | 规模未取得；586% 的提升为二手数字。 |
| DepMap, GDSC and PRISM (cell-line omics and drug sensitivity) | — | cell-line-level mutation features | EV15, EV16, EV17 | Targets are viability and gene dependency, not transcriptomes; cross-dataset agreement is reportedly low (F18 item b, unverified). | 目标是活力和基因依赖性，而不是转录组；据称跨数据集一致性较低（F18 的 b 项，未核验）。 |
| Virtual Cell Challenge 2026 CRISPRi cell-line datasets | 6 CRISPRi cancer cell lines (3 validation, 3 test); about 300 target genes; 400 cells per perturbation x 18,533 genes (third-party description) | cell-line identity | EV07, EV09, EV11 | Details come from a third-party repository; check the official site, including the reported 22 Oct and 5 Nov 2026 dates. | 细节来自第三方仓库；请在官网核实，包括所报告的 2026 年 10 月 22 日和 11 月 5 日。 |
| Virtual Cell Challenge 2025 H1 hESC genetic-perturbation benchmark | — | single line (H1 hESC) | EV05, WM10 | Details not retrieved; the search summary mentions Tahoe-100M, K562 and A375 as other cell-line datasets. | 细节未取得；检索摘要把 Tahoe-100M、K562 和 A375 提作其他细胞系数据集。 |
| sci-Plex3 (used to train PRnet) | 188 compounds; 3 cancer cell lines (MCF7, K562, A549); about 650,000 cells; 5,000 samples | — | DS15, MD02 | Known only through the PRnet paper; scale not retrieved. Scale from the sci-Plex paper (DS15); substantial intercellular heterogeneity of response is reported. | 仅通过 PRnet 论文得知；规模未取得。 规模来自 sci-Plex 论文（DS15）；论文报告响应存在显著的细胞间异质性。 |
| Perturbation panel profiling (P3) in iPSC-derived cardiomyocytes | 75 perturbation conditions (triplicate or vehicle control) | single donor background | GD31 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| Yeast CRISPRi across 169 segregants | 169 segregants; 460 genes with background-dependent effects; 234 interacting loci; 4 hub loci | segregant genotypes from natural variation | GD30 | Yeast; transfer to human cells is untested. | 酵母；向人类细胞的迁移未经检验。 |
| Base-editing plus Perturb-seq of cancer drug-resistance variants (HT-29) | 11 cancer genes | engineered variants in one cell line (HT-29) | GD23 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| Perturb-seq of TP53 and KRAS coding variants | — | engineered coding variants in A549 cells (from a search summary) | GD26 | Scale not retrieved; no drug arm reported in the excerpt. A search summary reports a functional gradient of cell states rather than a binary effect (see GD26). | 规模未取得；摘录中未见药物处理组。 检索摘要报告的是细胞状态的功能梯度，而不是二元效应（见 GD26）。 |
| Parse 10 Million PBMC cytokine atlas | 9,697,974 cells; 18 cell types; 12 donors; 90 cytokines or PBS; 24 hours; about 7,400 cells per condition | donors present; genotyping not stated in the retrieved text | DS16 | Commercial licence terms apply, with a Hugging Face copy; whether the donors are genotyped is not stated. | 适用商业许可条款，另有 Hugging Face 副本；未说明供体是否做了基因分型。 |
| OP3 PBMC chemical perturbation set (GSE279945) | 146 chemical perturbations; 3 donors; T, B, NK and myeloid cells (the earlier competition release had 144 compounds) | donor identity only (3 donors) | DS17 | Donor-held-out evaluation is not described; the URL is an OmicsDI record of the GEO series. | 未描述留出供体的评测；该 URL 是 GEO 系列在 OmicsDI 中的记录。 |
| X-Atlas/Orion genome-wide Perturb-seq | about 8 million cells in HCT116 and HEK293T (one post says 8.4 million); median 16,000 UMIs per cell; median on-target knockdown 75.4% (HCT116) and 51.5% (HEK293T) | none (cell lines) | DS18 | Cell counts differ between sources; the dataset card was seen only in a search result. | 各来源给出的细胞数不一致；数据集卡片只在检索结果中见到。 |
| Genome-scale CRISPRi Perturb-seq in K562 and RPE1 | more than 2.5 million cells; K562 screen covers all expressed genes and RPE1 covers essential genes; median knockdown 85.5% (K562) and 91.6% (RPE1) | none (cell lines) | DS19 | Processed data are said to be on Figshare+, but no link was retrieved; the URL is the paper. | 据称处理后的数据在 Figshare+ 上，但未取回链接；该 URL 是论文。 |
| scPerturb harmonized collection | 44 public datasets | varies by dataset; not summarized | DS20 | A Python package is on PyPI according to the retrieved text; data access paths were not checked. | 据检索到的文字，有一个 Python 包发布在 PyPI 上；数据获取路径未核查。 |
| scNT-seq time-resolved single-cell RNA profiles | — | — | DS21 | Method paper; scale and data access not retrieved. | 方法论文；规模和数据获取方式未取得。 |
| Well-TEMP-seq time-resolved single-cell RNA profiles | — | none (cell line) | DS22 | Scale and data access not retrieved. | 规模和数据获取方式未取得。 |
| LabCompass loop data (Hugging Face) | about 60 GB raw loop files (loop 0 alone 36 GB); 500k-cell subsamples; 4.7 GB derived inputs; 13 GB inference-only checkpoints; about 1.07 million unfiltered designs; the abstract reports a 78-million-cell dataset | none | DS23, WM29 | The dataset page could not be read; contents are as described by the reproducibility README (WM29); the chain of eight stages versus four loops in the abstract is unexplained. | 数据集页面无法读取；内容据可复现 README（WM29）的描述；八个阶段的链条与摘要中的 4 轮之间的差异未得到解释。 |
| Response-eQTL cultures with nicotine, caffeine and ethanol | 51 individuals; about 1.4 million cells; 31 to 110 response eQTLs per cell type; 380, 336 and 276 eGenes per condition | genotypes present (response-eQTL mapping) | GD10 | A 2026 review gives 53 individuals while the paper reports 51; data access not checked. | 2026 年的一篇综述给出 53 名个体，而论文报告 51 名；数据获取方式未核查。 |
| Influenza-exposed PBMCs from 90 individuals | 90 individuals; influenza A virus or mock for 6 hours | genotypes and ancestry present | GD49 | The stimulus is a virus, not a drug; data access not checked. | 刺激物是病毒而不是药物；数据获取方式未核查。 |
| Village-in-a-dish hiPSC lines (104-donor village) | 104 donors; 86,185 cells | genotype demultiplexing of pooled lines | GD47, GD48 | Pooled composition shifts between village and uni-culture and cross-line signalling can confound drug responses; no drug arm in the retrieved text. | 村落与单独培养之间混池构成会变化，细胞系间信号可能混杂药物响应；检索到的文字中没有药物处理组。 |
| MIX-Seq pooled cell lines | pool including 7 TP53 wild-type lines; total scale not retrieved | cell-line identity by genotype demultiplexing | GD45 | Compound and pool size not retrieved; the claim that response signatures predict viability is from the preprint. | 化合物和混池规模未取得；响应特征可预测活力这一说法来自预印本。 |
| MCF10A isogenic mutant panel with 90 compounds | 51 stable lines; 90 compounds | engineered wild-type or mutant cancer genes in one background | GD46 | The readout is proliferation, not transcription. | 读出是增殖，而不是转录。 |
| Caffeine reporter-assay variants in vascular endothelial cells | more than 43,000 variants tested; 665 with allelic effects; 6 interacting with caffeine (FDR below 5%) | reporter alleles | GD50 | Reporter assay, not endogenous expression; one drug and one cell type. | 报告基因实验，而不是内源表达；只有一种药物和一种细胞类型。 |
| CRISPR-drug perturbational map (18 cell lines, 8 drugs) | 18 cell lines; 8 drugs; knockouts of druggable genes | none | GD53 | The readout is pooled growth; no transcriptome. | 读出是混池生长；没有转录组。 |
<!-- dataset-table:end -->

## 4. Judgments / 判断

J2 (confidence: medium). The most trainable slice is probably somatic driver mutations crossed with targeted drugs in cancer cell lines, because Tahoe-100M and LINCS supply the drug responses and cell-line annotation supplies the mutation features [DS01, DS05, EV16]. Common germline variants have small effects and are better used for external validation and as priors.

> J2（置信度：中）。最可训练的切片很可能是癌症细胞系中的体细胞驱动突变 × 靶向药物，因为 Tahoe-100M 和 LINCS 提供药物响应，而细胞系注释提供突变特征 [DS01, DS05, EV16]。常见的种系变异效应小，更适合用作外部验证和先验。

J12 (confidence: medium). Neither L1000 nor Tahoe-100M carries donor-level germline variation beyond cell-line identity, so they can support the somatic track but not, by themselves, the germline track [DS01, DS05].

> J12（置信度：中）。L1000 和 Tahoe-100M 都不携带超出细胞系身份的供体层面种系变异，因此它们可以支撑体细胞轨道，但不能单独支撑种系轨道 [DS01, DS05]。

J21 (confidence: low-medium). The donor-by-perturbation grids (the Parse PBMC atlas and the 40-donor T-cell dataset) are the largest testbeds for unseen-donor generalization and for the mediation ablation in a germline-like setting, but their genotyping status is unknown, so they test donor effects rather than genotype effects until genotypes are linked [DS16, MD42]. X-Atlas/Orion and the K562 and RPE1 screens give graded and strong knockdown, which is the closest public proxy for hypomorphic and loss-of-function alleles when no drug is present [DS18, DS19].

> J21（置信度：低中）。供体×扰动网格（Parse PBMC 图谱和 40 名供体 T 细胞数据集）是检验未见供体泛化以及类种系情形下中介消融的最大测试平台，但其基因分型状态未知，因此在关联基因型之前，它们检验的是供体效应而不是基因型效应 [DS16, MD42]。X-Atlas/Orion 以及 K562 和 RPE1 筛选给出梯度的和强的敲低，这是在没有药物时亚效等位基因和功能缺失等位基因最接近的公开代理 [DS18, DS19]。

## 5. Recommended actions / 行动建议

Use Tahoe-100M as the backbone of the somatic track and LINCS L1000 for breadth across cell lines and compounds, and join both to cell-line mutation annotation through a stable cell-line identifier [DS05, DS01].

> 把 Tahoe-100M 用作体细胞轨道的骨干，把 LINCS L1000 用于覆盖更多细胞系和化合物，并通过稳定的细胞系标识符把两者与细胞系突变注释连接起来 [DS05, DS01]。

Before any modeling, count how many cell lines carry each driver mutation in the Tahoe-100M panel and how many are matched by lineage, because power for any genotype contrast depends on those counts, which are unknown today.

> 在任何建模之前，先统计 Tahoe-100M 面板中各驱动突变有多少细胞系携带、其中有多少按谱系匹配，因为任何基因型对比的统计效能都取决于这些目前未知的计数。

Treat composition effects as a first-class issue: a genotype that changes survival or proliferation changes the mix of surviving cells, and the single-cell profiles retain those signals [DS06].

> 把细胞构成效应作为首要问题处理：改变存活或增殖的基因型会改变存活细胞的构成，而单细胞谱保留了这些信号 [DS06]。

Check access routes, licenses and exact schemas of every dataset before use, including the Zenodo record [DS13] and the Hugging Face dataset [DS07].

> 使用任何数据集之前，先核查其获取途径、许可和确切模式，包括 Zenodo 记录 [DS13] 和 Hugging Face 数据集 [DS07]。

Check whether the donors of the Parse PBMC atlas and of the OP3 set can be linked to genotypes, calibrate gene-loss effect sizes on X-Atlas/Orion and the K562 and RPE1 screens, and use the E-distance of scPerturb as a distribution-level distance for the interaction score [DS16, DS17, DS18, DS19, DS20].

> 核查 Parse PBMC 图谱和 OP3 数据集的供体能否与基因型关联，用 X-Atlas/Orion 以及 K562 和 RPE1 筛选校准基因缺失的效应大小，并把 scPerturb 的 E-distance 用作交互项评分的分布层面距离 [DS16, DS17, DS18, DS19, DS20]。

## 6. Questions for confirmation / 待确认问题

Is a public-data-only plan acceptable even though the germline track then depends on published summary results and a single small individual-level dataset? Default: yes (assumption M4 in document 00).

> 即使种系轨道因此要依赖已发表的汇总结果和一个小型的个体层面数据集，仅用公开数据的方案是否可以接受？默认：可以（文档 00 中的假设 M4）。

## 7. Evidence gaps / 证据缺口

The exact cell-line count of the 2017 L1000 release was not found (query Q35), and no direct comparison of Tahoe-100M with L1000 was found (query Q11). The time points of Tahoe-100M, the dose grid of either resource, and the scale of the GTEx, OneK1K and Geuvadis resources were not retrieved. The data licenses and download routes are unchecked.

> 未找到 2017 年版 L1000 的确切细胞系数（查询 Q35），也未找到 Tahoe-100M 与 L1000 的直接比较（查询 Q11）。Tahoe-100M 的时间点、两种资源的剂量网格，以及 GTEx、OneK1K 和 Geuvadis 资源的规模均未取得。数据许可与下载途径未核查。

The Hugging Face page of the LabCompass data could not be read (query Q123), the scale of the scNT-seq and Well-TEMP-seq data was not retrieved (query Q87), and the genotyping status of the donors of the Parse PBMC atlas was not stated in the retrieved text (queries Q58 and Q111).

> LabCompass 数据的 Hugging Face 页面无法读取（查询 Q123），scNT-seq 和 Well-TEMP-seq 数据的规模未取得（查询 Q87），Parse PBMC 图谱供体的基因分型状态在检索到的文字中没有说明（查询 Q58 和 Q111）。

## 8. Source index (category DS) / 来源索引（类别 DS）

Generated from `data/sources.csv`; regenerate when the CSV changes. Rows whose status is retired are omitted, and each key point is followed by its "so what" where one was written.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。状态为 retired 的条目被省略，写有“意义”的条目在要点之后附上意义。

<!-- source-index:DS:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| DS01 | T2 | [A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles](<https://www.biorxiv.org/content/10.1101/136168.full.pdf>) | 1,319,138 profiles; earlier pilot had only 164 drugs × 3 cell lines | 1,319,138 个谱；早期试点仅 164 种药物 × 3 个细胞系 |
| DS03 | T2 | [GEO series GSE92742 (via OmicsDI)](<https://omicsdi.org/dataset/geo/GSE92742>) | same 1,319,138 count | 同样的 1,319,138 计数 |
| DS04 | T3 | [signatureSearchData (Bioconductor secondary description)](<https://www.gitlink.org.cn/NSCCN/bioconductor-signaturesearchdata>) | about 19,811 compounds × about 70 cell lines (secondary); LINCS2 beta above 80k perturbations, above 200 cell lines, above 3 million profiles (secondary) | 约 19,811 种化合物 × 约 70 个细胞系（二手）；LINCS2 测试版超过 8 万（80k）次扰动、超过 200 个细胞系、超过 300 万个谱（二手） |
| DS05 | T2 | [Tahoe-100M: A Giga-Scale Single-Cell Perturbation Atlas for Context-Dependent Gene Function and Cellular Modeling](<https://www.biorxiv.org/content/10.1101/2025.02.20.639398.full.pdf>) | about 100 million cells, 50 cancer cell lines, about 1,100 drug-dose conditions; SNP-based cell-village deconvolution; cell-line identity dominates clustering; counts differ by source (379 drugs / 25 mechanisms / 52,886 cell-line–drug conditions in one; 1,200 perturbations in another) | 约 1 亿个细胞，50 个癌症细胞系，约 1,100 个药物-剂量条件；基于 SNP 的细胞村解卷积；细胞系身份主导聚类；各来源计数不同（一处为 379 种药物 / 25 种机制 / 52,886 个细胞系-药物条件；另一处为 1,200 次扰动） |
| DS06 | T2 | [Tahoe-100M: Mapping drug-induced molecular phenotypes at single-cell resolution (Cell)](<https://www.cell.com/cell/fulltext/S0092-8674(26)01008-1>) | single-cell profiles retain proliferation, cytotoxicity and cell-cycle signals | 单细胞谱保留增殖、细胞毒性和细胞周期信号 |
| DS07 | T2 | [tahoebio/Tahoe-100M (Hugging Face dataset page)](<https://huggingface.co/datasets/tahoebio/Tahoe-100M>) | publicly available | 公开可得 |
| DS08 | T2 | [Genome-scale perturb-seq in primary human CD4+ T cells maps context-specific regulators of T cell programs and human immune traits](<https://www.cell.com/cell/fulltext/S0092-8674(26)00929-3>) | 4 donors, about 22 million cells; no donor-by-perturbation interaction analysis seen in the excerpt | 4 名供体，约 2,200 万（22 million）个细胞；摘录中未见供体×扰动交互分析 |
| DS09 | T2 | [A perturbation cell atlas of human induced pluripotent stem cells](<https://www.biorxiv.org/content/10.1101/2024.11.03.621734v2.full.pdf>) | single KOLF2.1J line, genome-wide CRISPRi | 单一 KOLF2.1J 细胞系，全基因组 CRISPRi |
| DS10 | T2 | [Benchmarking and optimizing Perturb-seq in differentiating human pluripotent stem cells](<https://www.cell.com/stem-cell-reports/fulltext/S2213-6711(25)00317-0>) | H9 and WTC11 gave similar results | H9 与 WTC11 结果相近 |
| DS11 | T2 | [Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens](<https://www.cell.com/cell/fulltext/S0092-8674(16)31610-5>) | method origin | 方法起源 |
| DS12 | T2 | [Exploring genetic interaction manifolds constructed from rich single-cell phenotypes](<https://www.science.org/doi/10.1126/science.aax4438>) | genetic interactions | 遗传互作 |
| DS13 | T2 | [Data from: Determining the genetic basis of anthracycline-cardiotoxicity by response QTL mapping in induced cardiomyocytes (Zenodo)](<https://zenodo.org/records/5000833>) | candidate germline-track positive-control data; availability to be checked | 种系轨道阳性对照数据的候选；可得性待核 |
| DS15 | T2 | [Massively multiplex chemical transcriptomics at single-cell resolution (sci-Plex)](<https://www.science.org/doi/10.1126/science.aax6234>) | nuclear hashing with sci-RNA-seq; dose-dependent responses to 188 compounds in 3 cancer cell lines (MCF7, K562, A549); about 650,000 cells across 5,000 samples; substantial intercellular heterogeneity of response **So what:** provides the dose axis and single-cell heterogeneity, the standard testbed for dose rollouts and distribution-level metrics | 核哈希结合 sci-RNA-seq；在 3 个癌细胞系（MCF7、K562、A549）中检测 188 种化合物的剂量依赖响应；约 650,000（65 万）个细胞、5,000 个样本；响应存在显著的细胞间异质性 **意义：** 提供剂量轴和单细胞异质性，是剂量展开和分布层面指标的标准测试平台 |
| DS16 | T2 | [10 Million Human PBMCs in a Single Experiment (Parse Biosciences)](<https://www.parsebiosciences.com/datasets/10-million-human-pbmcs-in-a-single-experiment/>) | 9,697,974 cells in 18 immune cell types from 12 donors treated with 90 cytokines or PBS for 24 hours, about 7,400 cells per condition; donor-specific response variation reported in the accompanying cytokine dictionary; commercial licence terms, with a Hugging Face copy **So what:** the largest donor-by-perturbation single-cell grid, the testbed for unseen-donor generalization and for the mediation ablation in a germline-like setting; the retrieved text does not say whether donors are genotyped | 来自 12 名供体的 9,697,974 个细胞、18 种免疫细胞类型，用 90 种细胞因子或 PBS 处理 24 小时，每个条件约 7,400 个细胞；配套的细胞因子字典报告了供体特异的响应变异；有商业许可条款，另有 Hugging Face 副本 **意义：** 最大的供体×扰动单细胞网格，是未见供体泛化以及类种系情形下中介消融的测试平台；检索到的文字未说明供体是否做了基因分型 |
| DS17 | T2 | [OP3: single-cell multimodal dataset in PBMCs for perturbation prediction benchmarking (GSE279945)](<https://www.omicsdi.org/dataset/geo/GSE279945>) | 146 chemical perturbations in PBMCs from 3 donors (the earlier competition release had 144 compounds); T, B, NK and myeloid cells; the benchmark extrapolates perturbation effects to unseen cell types **So what:** a small-donor, multi-cell-type chemical grid for unseen-cell-type tests; donor-held-out evaluation is not described | 来自 3 名供体的 PBMC 中的 146 种化学扰动（早期竞赛版本为 144 种化合物）；T、B、NK 和髓系细胞；基准把扰动效应外推到未见的细胞类型 **意义：** 供体数少、细胞类型多的化学网格，用于未见细胞类型的检验；未描述留出供体的评测 |
| DS18 | T2 | [X-Atlas/Orion: genome-wide Perturb-seq datasets via a scalable fix-cryopreserve platform for training dose-dependent biological foundation models](<https://www.biorxiv.org/content/10.1101/2025.06.11.659105v1>) | two genome-wide CRISPR screens in HCT116 and HEK293T cells, about 8 million cells (one post says 8.4 million), median 16,000 UMIs per cell; median on-target knockdown 75.4% in HCT116 and 51.5% in HEK293T; argues that knockdown should be modeled as graded, not on or off **So what:** graded knockdown is the closest public proxy for hypomorphic alleles, supporting a continuous perturbation-strength covariate | 在 HCT116 和 HEK293T 细胞中做两次全基因组 CRISPR 筛选，约 800 万个细胞（一则帖子称 8.4 million，即 840 万），每个细胞中位数 16,000 个 UMI；HCT116 的中位靶向敲低为 75.4%，HEK293T 为 51.5%；主张敲低应被建模为梯度而不是开关 **意义：** 梯度敲低是亚效等位基因最接近的公开代理，支持使用连续的扰动强度协变量 |
| DS19 | T2 | [Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq](<https://www.sciencedirect.com/science/article/pii/S0092867422005979>) | genome-scale CRISPRi Perturb-seq with more than 2.5 million cells; the K562 screen covers all expressed genes and RPE1 covers essential genes; median knockdown 85.5% in K562 and 91.6% in RPE1; processed data on Figshare+ **So what:** the reference for pretraining gene-loss effects and calibrating effect sizes; pathway-gene knockouts stand in for loss-of-function variants (classes 1 and 4) when no drug is present | 基因组规模的 CRISPRi Perturb-seq，细胞数超过 2.5 million（250 万）；K562 筛选覆盖所有表达基因，RPE1 覆盖必需基因；K562 中位敲低 85.5%，RPE1 为 91.6%；处理后的数据在 Figshare+ 上 **意义：** 用于预训练基因缺失效应并校准效应大小的参考；在没有药物时，通路基因敲除可以代理功能缺失变异（类别 1 和 4） |
| DS20 | T2 | [scPerturb: harmonized single-cell perturbation data](<https://www.nature.com/articles/s41592-023-02144-y>) | 44 public single-cell perturbation datasets harmonized with uniform processing; introduces E-statistics (E-distance and E-test) to quantify and test perturbation effects; a Python package is on PyPI **So what:** one entry point to data and a distribution-level distance that I plan to use for the interaction score | 把 44 个公开的单细胞扰动数据集用统一流程做了协调；引入 E 统计量（E-distance 和 E-test）来量化和检验扰动效应；Python 包发布在 PyPI 上 **意义：** 数据的统一入口，以及我计划用于交互项评分的分布层面距离 |
| DS21 | T2 | [Massively parallel, time-resolved single-cell RNA sequencing with scNT-Seq](<https://www.biorxiv.org/content/10.1101/2019.12.19.882050.full.pdf>) | 4sU metabolic labeling with chemical recoding separates new from old transcripts in each cell and resolves RNA trajectories after brief versus sustained stimulation **So what:** the only route found that identifies state-update dynamics from snapshots, which is what multi-step world-model claims need | 4sU 代谢标记加化学重编码把每个细胞中的新转录本与旧转录本区分开，并解析短暂与持续刺激后的 RNA 轨迹 **意义：** 发现的唯一一条能从快照中识别状态更新动力学的途径，而这正是多步世界模型主张所需要的 |
| DS22 | T2 | [Well-TEMP-seq as a microwell-based strategy for massively parallel profiling of single-cell temporal RNA dynamics](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9992361/>) | metabolic labeling in microwells, applied to colorectal cancer cells exposed to the DNA-demethylating drug 5-AZA-CdR **So what:** a drug-exposure example of time-resolved scRNA-seq that could provide transition targets | 在微孔中做代谢标记，应用于暴露于 DNA 去甲基化药物 5-AZA-CdR 的结直肠癌细胞 **意义：** 时间分辨 scRNA-seq 的药物暴露示例，可提供转移目标 |
| DS23 | T2 | [theislab/LabCompass (Hugging Face dataset)](<https://huggingface.co/datasets/theislab/LabCompass>) | per-loop AnnData files plus 500k-cell subsamples, about 60 GB raw, with derived inputs, inference-only checkpoints and about 1.07 million unfiltered inverse-design protocols (as described by the reproducibility README; the dataset page itself could not be read) **So what:** the first public closed-loop design data found in this search, but in spectral flow cytometry, so a transcriptomic analogue is missing | 逐轮的 AnnData 文件以及 500k（50 万）细胞的子样本，原始数据约 60 GB，另有衍生输入、仅用于推理的检查点和约 1.07 million（107 万）个未过滤的逆向设计方案（据可复现 README 的描述；数据集页面本身无法读取） **意义：** 本次检索中发现的首个公开闭环设计数据，但属于光谱流式细胞术，因此缺少转录组层面的类似物 |
<!-- source-index:DS:end -->

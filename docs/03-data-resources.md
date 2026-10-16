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
| sci-Plex3 (used to train PRnet) | — | — | MD02 | Known only through the PRnet paper; scale not retrieved. | 仅通过 PRnet 论文得知；规模未取得。 |
| Perturbation panel profiling (P3) in iPSC-derived cardiomyocytes | 75 perturbation conditions (triplicate or vehicle control) | single donor background | GD31 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| Yeast CRISPRi across 169 segregants | 169 segregants; 460 genes with background-dependent effects; 234 interacting loci; 4 hub loci | segregant genotypes from natural variation | GD30 | Yeast; transfer to human cells is untested. | 酵母；向人类细胞的迁移未经检验。 |
| Base-editing plus Perturb-seq of cancer drug-resistance variants (HT-29) | 11 cancer genes | engineered variants in one cell line (HT-29) | GD23 | The URL is the paper; data access not checked. | 该 URL 是论文；数据获取方式未核查。 |
| Perturb-seq of TP53 and KRAS coding variants | — | — | GD26 | Scale not retrieved; no drug arm reported in the excerpt. | 规模未取得；摘录中未见药物处理组。 |
<!-- dataset-table:end -->

## 4. Judgments / 判断

J2 (confidence: medium). The most trainable slice is probably somatic driver mutations crossed with targeted drugs in cancer cell lines, because Tahoe-100M and LINCS supply the drug responses and cell-line annotation supplies the mutation features [DS01, DS05, EV16]. Common germline variants have small effects and are better used for external validation and as priors.

> J2（置信度：中）。最可训练的切片很可能是癌症细胞系中的体细胞驱动突变 × 靶向药物，因为 Tahoe-100M 和 LINCS 提供药物响应，而细胞系注释提供突变特征 [DS01, DS05, EV16]。常见的种系变异效应小，更适合用作外部验证和先验。

J12 (confidence: medium). Neither L1000 nor Tahoe-100M carries donor-level germline variation beyond cell-line identity, so they can support the somatic track but not, by themselves, the germline track [DS01, DS05].

> J12（置信度：中）。L1000 和 Tahoe-100M 都不携带超出细胞系身份的供体层面种系变异，因此它们可以支撑体细胞轨道，但不能单独支撑种系轨道 [DS01, DS05]。

## 5. Recommended actions / 行动建议

Use Tahoe-100M as the backbone of the somatic track and LINCS L1000 for breadth across cell lines and compounds, and join both to cell-line mutation annotation through a stable cell-line identifier [DS05, DS01].

> 把 Tahoe-100M 用作体细胞轨道的骨干，把 LINCS L1000 用于覆盖更多细胞系和化合物，并通过稳定的细胞系标识符把两者与细胞系突变注释连接起来 [DS05, DS01]。

Before any modeling, count how many cell lines carry each driver mutation in the Tahoe-100M panel and how many are matched by lineage, because power for any genotype contrast depends on those counts, which are unknown today.

> 在任何建模之前，先统计 Tahoe-100M 面板中各驱动突变有多少细胞系携带、其中有多少按谱系匹配，因为任何基因型对比的统计效能都取决于这些目前未知的计数。

Treat composition effects as a first-class issue: a genotype that changes survival or proliferation changes the mix of surviving cells, and the single-cell profiles retain those signals [DS06].

> 把细胞构成效应作为首要问题处理：改变存活或增殖的基因型会改变存活细胞的构成，而单细胞谱保留了这些信号 [DS06]。

Check access routes, licenses and exact schemas of every dataset before use, including the Zenodo record [DS13] and the Hugging Face dataset [DS07].

> 使用任何数据集之前，先核查其获取途径、许可和确切模式，包括 Zenodo 记录 [DS13] 和 Hugging Face 数据集 [DS07]。

## 6. Questions for confirmation / 待确认问题

Is a public-data-only plan acceptable even though the germline track then depends on published summary results and a single small individual-level dataset? Default: yes (assumption M4 in document 00).

> 即使种系轨道因此要依赖已发表的汇总结果和一个小型的个体层面数据集，仅用公开数据的方案是否可以接受？默认：可以（文档 00 中的假设 M4）。

## 7. Evidence gaps / 证据缺口

The exact cell-line count of the 2017 L1000 release was not found (query Q35), and no direct comparison of Tahoe-100M with L1000 was found (query Q11). The time points of Tahoe-100M, the dose grid of either resource, and the scale of the GTEx, OneK1K and Geuvadis resources were not retrieved. The data licenses and download routes are unchecked.

> 未找到 2017 年版 L1000 的确切细胞系数（查询 Q35），也未找到 Tahoe-100M 与 L1000 的直接比较（查询 Q11）。Tahoe-100M 的时间点、两种资源的剂量网格，以及 GTEx、OneK1K 和 Geuvadis 资源的规模均未取得。数据许可与下载途径未核查。

## 8. Source index (category DS) / 来源索引（类别 DS）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:DS:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| DS01 | T2 | [A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles](<https://www.biorxiv.org/content/10.1101/136168.full.pdf>) | 1,319,138 profiles; earlier pilot had only 164 drugs × 3 cell lines | 1,319,138 个谱；早期试点仅 164 种药物 × 3 个细胞系 |
| DS02 | T2 | [A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles (Broad publication page)](<https://golublab.broadinstitute.org/publications/next-generation-connectivity-map-l1000-platform-and-first-1000000-profiles>) | — | — |
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
| DS14 | T2 | [AI virtual cells for drug discovery and pharmacology](<https://www.sciencedirect.com/science/article/pii/S0165614726002038>) | review | 综述 |
<!-- source-index:DS:end -->

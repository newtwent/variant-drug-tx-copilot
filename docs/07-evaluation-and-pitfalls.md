# 07 Evaluation, baseline critiques and bias / 评测、基线批判与偏倚

## 1. Scope / 范围

This document collects what the retrieved sources say about how perturbation-prediction models are evaluated and where those evaluations fail: baseline critiques, metric pitfalls, community challenges, foundation-model evaluations and ancestry bias. It ends with an evaluation checklist for the genotype-by-drug question. No benchmark that targets the genotype-by-drug interaction was found.

> 本文档汇集检索到的来源关于扰动预测模型如何评估、这些评估在哪里失效的说法：基线批判、指标陷阱、社区挑战赛、基础模型评测和祖源偏倚。末尾给出针对基因型×药物问题的评测清单。没有找到针对基因型×药物交互的基准。

## 2. Facts and evidence / 事实与证据

Deep perturbation predictors have not reliably beaten simple baselines. A 2025 Nature Methods study of genetic perturbations found that no deep model consistently outperformed the mean prediction or a linear model, that a linear model using the same embeddings performed as well as or better than scGPT and GEARS with their built-in decoders, and that GEARS extrapolates through shared Gene Ontology annotations. CPA was excluded because it is not designed to predict unseen perturbations. The study concerns genetic perturbations, not drugs [EV01].

> 深度扰动预测模型尚未稳定地击败简单基线。2025 年一项针对基因扰动的 Nature Methods 研究发现，没有深度模型稳定优于均值预测或线性模型；使用相同嵌入的线性模型表现与带内置解码器的 scGPT 和 GEARS 相当或更好；GEARS 通过共享的基因本体注释进行外推。CPA 因并非为预测未见扰动而设计而被排除。该研究针对的是基因扰动，不是药物 [EV01]。

PerturBench argues that rank-based measures should sit alongside RMSE because they check whether perturbations are ordered correctly, reports mode collapse in widely used models, finds that simpler architectures are generally competitive and scale well, and includes distributional metrics such as the E-distance, equivalent to an energy-distance MMD [EV02]. The same paper describes an earlier community challenge as limited to a single covariate-transfer task and a single metric; whether that description refers to the benchmark paper listed as [EV14] is unconfirmed. The EFFECT suite shows that common metrics such as Pearson correlation can mislead because of biases in cancer-sensitivity data [EV15].

> PerturBench 主张排名指标应与 RMSE 并用，因为它们检查扰动的排序是否正确；报告了广泛使用的模型中的模式坍塌；发现较简单的架构通常有竞争力且扩展性好；并包含 E-distance 等分布指标，它等价于基于能量距离的 MMD [EV02]。同一篇论文把较早的一次社区挑战赛描述为只有单一的协变量迁移任务和单一指标；这一描述是否指向列为 [EV14] 的基准论文尚未确认。EFFECT 套件表明，由于癌症敏感性数据中的偏倚，Pearson 相关等常用指标可能产生误导 [EV15]。

Foundation-model evaluations point the same way. One evaluation reports only limited improvement of single-cell foundation models over GEARS on genetic perturbation prediction [EV21]. A preprint title states that parameter-free representations outperform single-cell foundation models on downstream benchmarks, and another reports harmonised benchmarking with context-dependent generalisation; both are known by title only [EV13, EV12]. A systematic comparison of single-cell perturbation-response models and the recommendations of a virtual-cell workshop on benchmarking also exist [EV20, EV22].

> 基础模型的评测指向同样的方向。一项评测报告单细胞基础模型在基因扰动预测上相对 GEARS 仅有有限提升 [EV21]。一篇预印本的标题称无参数表示在下游基准上优于单细胞基础模型，另一篇报告了对情境依赖泛化的统一基准评测；两者都只知道标题 [EV13, EV12]。另外还有对单细胞扰动响应模型的系统比较，以及一个虚拟细胞研讨会关于基准评测的建议 [EV20, EV22]。

For cancer cell lines, one benchmark preprint found that raw cell-line expression beat foundation-model embeddings and genotype-based encodings, and that STRING-based encodings were best for genetic perturbations. Its prediction targets were cell viability and gene dependency, not transcriptomes [EV16].

> 对于癌症细胞系，一篇基准预印本发现原始细胞系表达优于基础模型嵌入和基于基因型的编码，且对基因扰动基于 STRING 的编码最好。其预测目标是细胞活力和基因依赖性，而不是转录组 [EV16]。

The Arc Virtual Cell Challenge 2025 wrap-up says that models do not yet consistently beat naive baselines across metrics, that winning approaches combined deep learning with classical statistical features, and that multimodal features were valuable [EV05]. A news report counts over 5,000 registrants from 114 countries and over 1,200 teams submitting results; this is a secondary figure [EV06].

> Arc 的 2025 年虚拟细胞挑战赛总结称，模型在各项指标上还不能稳定超过朴素基线，获胜的方法把深度学习与经典统计特征结合，多模态特征很有价值 [EV05]。一则新闻报道统计有来自 114 个国家的 5,000 多名注册者和 1,200 多支队伍提交了结果；这是二手数字 [EV06]。

The 2026 challenge moves from prediction inside one context to zero-shot generalization across cellular contexts [EV07, EV08], using 6 CRISPRi cancer cell lines [EV09]. A third-party repository describes 3 validation and 3 test lines, about 300 target genes, 400 cells per perturbation across 18,533 genes, and six metrics normalized so that the mean-response baseline scores 0 and an experimental replicate scores 1. The same repository gives 22 October 2026 for the release of the final contexts and 5 November 2026 for submissions; these details are unverified and must be checked on the official site [EV11, EV10].

> 2026 年的挑战赛从单一情境内的预测转向跨细胞情境的零样本泛化 [EV07, EV08]，使用 6 个 CRISPRi 癌症细胞系 [EV09]。一个第三方仓库描述了 3 个验证细胞系和 3 个测试细胞系、约 300 个靶基因、每个扰动 400 个细胞 × 18,533 个基因，以及六项指标，归一化后均值响应基线得 0 分、实验重复得 1 分。同一仓库给出最终情境于 2026 年 10 月 22 日发布、提交于 2026 年 11 月 5 日截止；这些细节未经核验，必须在官网核实 [EV11, EV10]。

Ancestry matters. Reference panels for expression prediction and eQTLs are dominated by European-ancestry samples, and GTEx v8 includes up to 15% non-European-ancestry individuals [EV23, EV25]. Prediction is best when the training and testing ancestry match [EV26]. Allele-frequency differences are the main driver of lost portability [EV24], and the definitions and methods used to assess portability are inconsistent across studies, with power a major confounder [EV27].

> 祖源很重要。表达预测和 eQTL 的参考面板以欧洲祖源样本为主，GTEx v8 中非欧洲祖源个体最多占 15% [EV23, EV25]。当训练和测试的祖源一致时预测最好 [EV26]。等位基因频率差异是可迁移性下降的主要驱动因素 [EV24]，而且各研究评估可迁移性所用的定义和方法并不一致，统计效能是一个主要的混杂因素 [EV27]。

## 3. Evaluation checklist / 评测清单

| Item | Requirement | Reason | Source IDs | 要求与理由（中文） |
|---|---|---|---|---|
| Splits | Leave-one-line-out within lineage, leave-one-drug(-class)-out, leave-one-variant-out | Random splits leak through neighboring drugs, lines and pathways | EV01, EV02 | 在谱系内留一细胞系、留一药物（或药物类别）、留一变异；随机划分会通过相近药物、细胞系和通路泄漏信息 |
| Primary metric | Difference-in-differences on differentially expressed genes between genotypes | Targets the interaction, not the drug main effect | EV15 | 在基因型之间对差异表达基因做双重差分；针对交互项而不是药物主效应 |
| Secondary metrics | Rank-based and distributional metrics (E-distance, MMD) | Genome-wide MSE or Pearson favors the mean | EV02 | 基于排名的指标和分布指标（E-distance、MMD）；全基因组 MSE 或 Pearson 偏向均值 |
| Baselines | Mean, drug-wise linear, one-step conditional generative | A model must beat every rung | EV01, MD05, MD06 | 均值、逐药物线性、单步条件生成；模型必须击败每一级 |
| Score anchoring | Normalize between the mean baseline (0) and a replicate anchor (1) | Makes scores comparable across metrics | EV11 | 在均值基线（0）与重复锚点（1）之间归一化；使各指标的分数可比 |
| Controls | Genotype permutation; benign or no-effect contrasts; drug-class-matched controls | Detects leakage and spurious gains | EV02 | 基因型置换；良性或无效应对比；药物类别匹配的对照；用于发现泄漏和虚假增益 |
| Composition | Report cell-fraction changes and score within cell states | Survival-changing genotypes change the mix | DS06 | 报告细胞比例变化，并在细胞状态内评分；改变存活率的基因型会改变细胞构成 |
| Ancestry | Stratify germline-track evaluation by ancestry | Portability falls across ancestries | EV23, EV24 | 按祖源对种系轨道的评测分层；跨祖源的可迁移性下降 |
| Uncertainty and power | Report confidence intervals and a power estimate from the counted mutant and wild-type lines | A 50-line panel may be underpowered | DS05 | 报告置信区间，以及基于所统计的突变株与野生株数量的效能估计；50 个细胞系的面板可能效能不足 |

## 4. Judgments / 判断

J5 (confidence: high for the evaluation claim). Evaluation design matters more than architecture. The drug main effect is expected to be much larger than the genotype-by-drug interaction, and genome-wide MSE or Pearson correlation is dominated by mean baselines [EV01, EV02]. What is needed: difference-in-differences between genotypes, rank and distributional metrics, and positive and negative controls such as genotype permutation and benign variants.

> J5（评测相关结论的置信度：高）。评测设计比架构更重要。预计药物主效应远大于基因型×药物交互项，而全基因组 MSE 或 Pearson 相关会被均值基线主导 [EV01, EV02]。需要：基因型之间的双重差分、排名与分布指标，以及基因型置换和良性变异等阳性与阴性对照。

J9 (confidence: medium). Ancestry should be a first-class covariate with stratified evaluation, given the European bias of eQTL and expression-prediction resources [EV23, EV24, EV26].

> J9（置信度：中）。鉴于 eQTL 和表达预测资源偏向欧洲人群，祖源应作为一等协变量，并进行分层评估 [EV23, EV24, EV26]。

J16 (confidence: medium). Statistical power is likely the binding constraint on any genotype contrast in a 50-line panel, so every result should carry an uncertainty estimate and a power statement based on the counted mutant and wild-type lines [DS05].

> J16（置信度：中）。在 50 个细胞系的面板中，统计效能很可能是任何基因型对比的限制因素，因此每个结果都应附带不确定性估计，以及基于所统计的突变株与野生株数量的效能说明 [DS05]。

## 5. Recommended actions / 行动建议

Fix the evaluation protocol before any model is built, using the checklist above, and publish it with the baselines so that results can be compared across experiments [EV02, EV11].

> 在构建任何模型之前，先依据上面的清单确定评测协议，并连同基线一起公布，以便各实验的结果可以比较 [EV02, EV11]。

Verify the Virtual Cell Challenge 2026 details on the official site before using it as an external benchmark, and treat its dates as unconfirmed until then [EV10, EV11].

> 在把虚拟细胞挑战赛 2026 用作外部基准之前，先在官网核实其细节，并在那之前把其日期视为未经确认 [EV10, EV11]。

Add a positive control that has a known genotype-by-drug effect, for example the response QTLs of the anthracycline study, and a negative control built by permuting genotype labels, so that the evaluation can tell a real gain from leakage [GD06].

> 加入一个已知存在基因型×药物效应的阳性对照，例如蒽环类药物研究的响应 QTL，并加入通过置换基因型标签构建的阴性对照，使评测能够区分真实增益与泄漏 [GD06]。

## 6. Questions for confirmation / 待确认问题

Should the 2026 Virtual Cell Challenge be recorded only, or also used as an external benchmark? Default: recorded only, not entered, because it concerns CRISPRi knockdowns in cell lines and not genotype-by-drug effects [EV07, EV09].

> 2026 年虚拟细胞挑战赛只记录，还是也用作外部基准？默认：只记录、不参赛，因为它涉及细胞系中的 CRISPRi 敲低，而不是基因型×药物效应 [EV07, EV09]。

## 7. Evidence gaps / 证据缺口

The official details of the 2026 challenge were not read [EV10]. The claim that drug-response agreement between GDSC, CTRP and CCLE on one side and PRISM on the other is low could not be tied to a source and is not recorded as a fact (item F18 b in the search log). The pitfalls section of PerturBench was not retrieved (query Q32). No benchmark targeting the genotype-by-drug interaction was found.

> 2026 年挑战赛的官方细节没有读到 [EV10]。关于 GDSC、CTRP 和 CCLE 与 PRISM 之间药物响应一致性较低的说法无法对应到来源，因此不记为事实（检索日志中的 F18 b 项）。PerturBench 关于陷阱的部分没有取回（查询 Q32）。没有找到针对基因型×药物交互的基准。

## 8. Source index (category EV) / 来源索引（类别 EV）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:EV:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| EV01 | T2 | [Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](<https://www.nature.com/articles/s41592-025-02772-6>) | no deep model consistently beats the mean or a linear model; GEARS extrapolates via GO annotations; CPA excluded because it cannot predict unseen perturbations; about genetic, not drug, perturbations | 没有深度模型稳定优于均值或线性模型；GEARS 借助 GO 注释外推；CPA 因不能预测未见扰动被排除；针对的是基因扰动而不是药物 |
| EV02 | T2 | [PerturBench: Benchmarking Machine Learning Models for Cellular Perturbation Analysis](<https://arxiv.org/pdf/2408.10609>) | rank metrics complement RMSE; mode collapse; simple architectures are competitive; includes E-distance / MMD | 排名指标与 RMSE 互补；模式坍塌；简单架构有竞争力；包含 E-distance / MMD |
| EV03 | T3 | [scPerturBench (GitHub)](<https://github.com/bm2-lab/scPerturBench>) | — | — |
| EV04 | T3 | [A recap of virtual cell releases circa June 2025 (blog)](<https://ekernf01.github.io/virtual-cell-june-2025>) | secondary | 二手 |
| EV05 | T2 | [Virtual Cell Challenge 2025 Wrap-Up: Winners and Reflections (Arc)](<https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up>) | models not yet consistently above naive baselines across metrics; hybrid methods won; multimodal features useful | 模型在各项指标上尚不能稳定超过朴素基线；混合方法获胜；多模态特征有价值 |
| EV06 | T3 | [NeurIPS 2025: Altos Labs Wins Generalist Prize at Arc's Virtual Cell Challenge (news)](<https://www.genengnews.com/topics/artificial-intelligence/neurips-2025-altos-labs-wins-generalist-prize-at-arcs-virtual-cell-challenge/>) | over 5,000 registrants from 114 countries, over 1,200 teams submitted; top-3 teams (secondary) | 超过 5,000 名注册者，来自 114 个国家，超过 1,200 支队伍提交；前 3 名队伍（二手） |
| EV07 | T2 | [Virtual Cell Challenge 2026: Benchmarking zero-shot generalization across cellular contexts](<https://www.cell.com/cell/fulltext/S0092-8674(26)00931-1>) | moves from single-context to cross-context zero-shot | 从单一上下文转向跨上下文零样本 |
| EV08 | T2 | [The 2026 Virtual Cell Challenge: predicting perturbation responses in cell contexts a model has never seen (Arc)](<https://arcinstitute.org/news/virtual-cell-challenge-2026>) | — | — |
| EV09 | T2 | [Generating high-quality Perturb-seq data for the 2026 Virtual Cell Challenge (Arc)](<https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge-2026>) | 6 cell lines | 6 个细胞系 |
| EV10 | T2 | [Virtual Cell Challenge evaluation page](<https://virtualcellchallenge.org/evaluation>) | official site, details to be checked | 官网，细节待核 |
| EV11 | T3 | [yashnil/virtual-cell-generalization (third-party repository)](<https://github.com/yashnil/virtual-cell-generalization>) | 6 CRISPRi lines (3 validation, 3 test); about 300 target genes; 400 cells per perturbation × 18,533 genes; 6 metrics normalized with mean baseline = 0 and replicate anchor = 1; dates 22 Oct / 5 Nov (must be checked on the official site) | 6 个 CRISPRi 细胞系（3 个验证、3 个测试）；约 300 个靶基因；每个扰动 400 个细胞 × 18,533 个基因；6 项指标按均值基线 = 0、重复锚点 = 1 归一；日期 10 月 22 日 / 11 月 5 日（必须在官网核实） |
| EV12 | T2 | [Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation](<https://arxiv.org/pdf/2607.17227>) | — | — |
| EV13 | T2 | [Parameter-free representations outperform single-cell foundation models on downstream benchmarks](<https://arxiv.org/pdf/2602.16696>) | — | — |
| EV14 | T2 | [A benchmark for prediction of transcriptomic responses to ... (title truncated)](<https://proceedings.neurips.cc/paper_files/paper/2024/file/24c4d51f3ef48dd2dbab78243ecb26a1-Paper-Datasets_and_Benchmarks_Track.pdf>) | NeurIPS 2024 datasets-and-benchmarks track paper on transcriptomic responses; PerturBench's authors describe an earlier challenge as limited to one covariate-transfer task and one metric, but whether that description refers to this paper is unconfirmed | NeurIPS 2024 数据集与基准赛道中关于转录组响应的论文；PerturBench 的作者把较早的一次挑战赛描述为只有一个协变量迁移任务和一个指标，但该描述是否指向本文尚未确认 |
| EV15 | T2 | [The EFFECT benchmark suite: measuring cancer sensitivity prediction performance - without the bias](<https://www.biorxiv.org/content/10.1101/2023.10.02.560281v2.full>) | common metrics can mislead because of data biases | 常用指标可能因数据偏倚而产生误导 |
| EV16 | T2 | [Benchmarking Chemical, Genetic, and Cell Line Encodings for Cancer Perturbation Response Prediction](<https://www.biorxiv.org/content/10.64898/2025.12.15.694331v1.full>) | raw cell-line expression beats foundation-model embeddings and genotype encodings; STRING-based encodings best for genetic perturbations; targets are viability and gene dependency, not transcriptomes | 原始细胞系表达优于基础模型嵌入和基因型编码；对基因扰动，基于 STRING 的编码最好；目标是活力和基因依赖性，而不是转录组 |
| EV17 | T2 | [Learning and actioning general principles of cancer cell drug sensitivity](<https://www.nature.com/articles/s41467-025-56827-5>) | GDSC plus PRISM transcriptomes | GDSC 加 PRISM 的转录组 |
| EV18 | T2 | [Predicting gene essentiality and drug response from ... (title truncated)](<https://arxiv.org/pdf/2502.15646>) | candidate source for F18 item b | F18 的 b 项的候选来源之一 |
| EV19 | T2 | [A gene essentiality signature enables predicting the ... (title truncated)](<https://www.biorxiv.org/content/10.1101/2022.11.07.514541v2.full.pdf>) | candidate source for F18 item b | F18 的 b 项的候选来源之一 |
| EV20 | T2 | [A Systematic Comparison of Single-Cell Perturbation Response Prediction Models](<https://www.biorxiv.org/content/10.1101/2024.12.23.630036.full.pdf>) | — | — |
| EV21 | T2 | [Single Cell Foundation Models Evaluation (scFME) for In-Silico Perturbation](<https://www.biorxiv.org/content/10.1101/2025.09.22.677811.full.pdf>) | another evaluation reports only limited gains over GEARS | 另一项评测称相对 GEARS 仅有限提升 |
| EV22 | T2 | [Benchmarking and Evaluation of AI Models in Biology: Outcomes and Recommendations from the CZI Virtual Cells Workshop](<https://arxiv.org/pdf/2507.10502>) | — | — |
| EV23 | T2 | [On the cross-population generalizability of gene expression prediction models](<https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1008927>) | prediction quality depends on both shared eQTL architecture and shared ancestry | 预测质量同时取决于共享的 eQTL 结构和共享的祖源 |
| EV24 | T2 | [Allele frequency impacts the cross-ancestry portability of gene expression prediction in lymphoblastoid cell lines](<https://www.cell.com/ajhg/fulltext/S0002-9297(24)00378-1>) | allele-frequency differences are the main driver | 等位基因频率差异是主要驱动因素 |
| EV25 | T2 | [Impact of admixture and ancestry on eQTL analysis and GWAS colocalization in GTEx](<https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02113-0>) | GTEx v8 has up to 15% non-European ancestry | GTEx v8 中非欧洲祖源最多占 15% |
| EV26 | T2 | [Transferability of Single- and Cross-Tissue Transcriptome Imputation Models Across Ancestry Groups](<https://pubmed.ncbi.nlm.nih.gov/39812501/>) | best when training and test ancestry match | 训练与测试祖源一致时最好 |
| EV27 | T2 | [Power is a major confounder in the analysis of cross-ancestry 'portability' in ...](<https://www.biorxiv.org/content/10.64898/2026.02.26.708346v1.full.pdf>) | definitions and methods are inconsistent across studies | 各研究的定义和方法不一致 |
| EV28 | T2 | [Empirical Evaluation of Single-Cell Foundation Models for Predicting Cancer Outcomes](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12637420/>) | peripheral | 外围条目 |
<!-- source-index:EV:end -->

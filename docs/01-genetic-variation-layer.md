# 01 Genetic variation layer / 遗传变异层

## 1. Scope / 范围

This document covers what is known about variants in drug targets and signaling pathways before any drug is applied: how variants change target expression, how coding variants change protein function and drug binding, how well sequence models predict expression in individual people, and what population-genetics methods such as Mendelian randomization (MR) and transcriptome-wide association studies (TWAS) add. Evidence about drug-induced transcriptional responses is in document 02.

> 本文档涵盖在施加任何药物之前，关于药物靶点和信号通路中变异的已知信息：变异如何改变靶点表达，编码变异如何改变蛋白功能和药物结合，序列模型对个体表达的预测有多好，以及孟德尔随机化（MR）和全转录组关联研究（TWAS）等群体遗传学方法能增加什么。关于药物诱导转录响应的证据在文档 02 中。

## 2. Facts and evidence / 事实与证据

Variants in drug-target genes can change the expression or the function of the target, and binding-site variants have been reported to strongly alter ACE-inhibitor activity [GV01].

> 药物靶基因中的变异可以改变靶点的表达或功能，已有报道称结合位点变异会显著改变 ACE 抑制剂的活性 [GV01]。

Sequence-to-expression models explain personal variation poorly. On 421 Geuvadis individuals, the across-gene Spearman correlations were 0.57 for Enformer, 0.52 for Basenji2, 0.53 for ExPecto and 0.33 for Xpresso, yet the models explained differences between individuals weakly and often got the effect direction wrong [GV05, GV06]. A review quotes a cross-individual Spearman of only 0.045 for Enformer on Geuvadis, which is a secondary figure [GV07].

> 序列到表达的模型对个体间差异解释很差。在 421 名 Geuvadis 个体上，跨基因 Spearman 相关对 Enformer 为 0.57、对 Basenji2 为 0.52、对 ExPecto 为 0.53、对 Xpresso 为 0.33，但这些模型对个体间差异的解释力弱，且常判错效应方向 [GV05, GV06]。一篇综述引用了 Enformer 在 Geuvadis 上仅 0.045 的跨个体 Spearman，这是二手数字 [GV07]。

AlphaGenome self-reports state-of-the-art results on 22 of 24 track tasks and 24 of 26 variant-effect tasks. Its eQTL results are better for direction than for magnitude: signed Spearman 0.50 against unsigned Spearman 0.10 [GV02]. A 2025 preprint notes that models trained only on the reference genome cannot capture individual-specific regulatory variants, and proposes fine-tuning with simulated personal genomes [GV09].

> AlphaGenome 自报在 24 项 track 任务中的 22 项、26 项变异效应任务中的 24 项达到最先进水平。其 eQTL 结果在方向上优于幅度：带符号 Spearman 为 0.50，不带符号为 0.10 [GV02]。一篇 2025 年的预印本指出，只在参考基因组上训练的模型无法捕获个体特异的调控变异，并提出用模拟的个人基因组做微调 [GV09]。

For coding variants, ESM1b and AlphaMissense score missense variants at scale: ESM1b scored about 450 million variants with a 650M-parameter model, and AlphaMissense reports a ClinVar auROC above 0.9, both self-reported. AlphaMissense's authors warn that methods trained on ClinVar may have inflated performance on that benchmark [GV16, GV17].

> 对于编码变异，ESM1b 和 AlphaMissense 可大规模给错义变异打分：ESM1b 用 650M 参数的模型给约 4.5 亿（450 million）个变异打分，AlphaMissense 报告 ClinVar auROC 高于 0.9，两者均为自报。AlphaMissense 的作者提醒，在 ClinVar 上训练的方法在该基准上的性能可能被高估 [GV16, GV17]。

For mutation effects on drug binding, Boltz-2 is self-reported and its authors state that no AI model has yet matched free-energy-perturbation or laboratory-assay accuracy [GV18]. BoltzOmics applies Boltz-2 to hERG, NaV1.5, HER2 and CYP3A4 and reports Pearson correlations with IC50 of up to 0.76 for wild-type and 0.60 for mutant proteins, again self-reported [GV19]. Few crystal structures of kinase mutants exist, which limits the accuracy of both physics-based and learned methods [GV20].

> 关于突变对药物结合的影响，Boltz-2 为自报，其作者称尚无 AI 模型达到自由能微扰或实验测定的准确度 [GV18]。BoltzOmics 把 Boltz-2 应用于 hERG、NaV1.5、HER2 和 CYP3A4，报告与 IC50 的 Pearson 相关性最高为野生型 0.76、突变体 0.60，同样是自报 [GV19]。激酶突变体的晶体结构很少，限制了基于物理的方法和学习方法的准确度 [GV20]。

Population-genetics methods are already used for targets and drug response. Drug-target MR uses variants in or near the target gene as instruments, with HMGCR, PCSK9, NPC1L1 and CETP as positive controls, and tissue-eQTL-weighted results may disagree with blood pQTL analyses [GV10]. A TWAS of thiopurine response in 663 pediatric ALL patients found 31 associated genes, with imputed GNAQ expression correlated with 6MP dose intensity, and the authors present this as a candidate for dose adjustment, not as validated practice [GV13]. TxEWAS tests imputed expression by environment interactions and was applied to statins, warfarin and methotrexate in UK Biobank [GV14].

> 群体遗传学方法已被用于靶点和药物反应。药物靶点 MR 使用靶基因内或附近的变异作为工具变量，以 HMGCR、PCSK9、NPC1L1 和 CETP 作阳性对照，且组织 eQTL 加权的结果可能与血液 pQTL 分析不一致 [GV10]。对 663 名儿童 ALL 患者硫嘌呤反应的 TWAS 发现 31 个相关基因，其中填补的 GNAQ 表达与 6MP 剂量强度相关，作者把它作为剂量调整的候选，而不是已验证的做法 [GV13]。TxEWAS 检验填补表达与环境的交互，并被应用于 UK Biobank 中的他汀、华法林和甲氨蝶呤 [GV14]。

Sequence models now reach single-cell resolution. scooby adds a cell-specific decoder to Borzoi and predicts single-cell RNA-seq coverage and ATAC insertion profiles from sequence, trained on a 10x Multiome bone-marrow dataset of 63,683 cells; the authors report single-cell expression Pearson correlations of 0.77 to 0.87 on unseen sequences and cell-type-specific eQTLs that are masked in bulk [GV26, GV03]. Its repository is MIT-licensed, offers pretrained models for bone-marrow, OneK1K and epicardioid data and takes 1 to 2 days of training on 8 A40 GPUs, and its README does not mention variant-effect scoring [GV27].

> 序列模型现已达到单细胞分辨率。scooby 在 Borzoi 上加了一个细胞特异解码器，由序列预测单细胞 RNA-seq 覆盖度和 ATAC 插入谱，在 63,683 个细胞的 10x Multiome 骨髓数据集上训练；作者报告在未见序列上的单细胞表达 Pearson 相关为 0.77 至 0.87，并发现了在 bulk 中被掩盖的细胞类型特异 eQTL [GV26, GV03]。其仓库采用 MIT 许可，提供骨髓、OneK1K 和心外膜类器官数据的预训练模型，在 8 块 A40 GPU 上训练需 1 至 2 天，其 README 没有提到变异效应打分 [GV27]。

Coding-variant maps under drugs show that binding is not enough. In BCR-ABL1 saturation mutagenesis tested under several drug conditions, predicting clinical resistance needed a variant's growth effect without drug as well as with drug [GV28]. Binding constants alone were not a good indicator of resistance to imatinib, nilotinib, dasatinib, bosutinib and ponatinib [GV29]. A base-editing screen with deep mutational scanning of the hotspots found that resistance can arise outside the kinase domain and tested epistasis with an edit-on-edit background carrying Y253H [GV30].

> 药物下的编码变异图谱表明，仅有结合是不够的。在多种药物条件下检测的 BCR-ABL1 饱和突变中，预测临床耐药既需要变异在无药时的生长效应，也需要其有药时的生长效应 [GV28]。仅凭结合常数不足以指示对 imatinib、nilotinib、dasatinib、bosutinib 和 ponatinib 的耐药 [GV29]。对热点做深度突变扫描的碱基编辑筛选发现，耐药可以出现在激酶结构域之外，并用携带 Y253H 的“编辑叠加编辑”背景检验了上位性 [GV30]。

For non-coding variants, pooled single-cell CRISPR screens (STING-seq) linked 91 non-coding blood-trait loci to 124 cis-target genes, found trans-effect networks when the cis targets were transcription factors or microRNAs, and used base editing to link specific variants to expression changes; the counts differ between versions of the paper [GV31].

> 对于非编码变异，混池单细胞 CRISPR 筛选（STING-seq）把 91 个非编码血液性状位点与 124 个 cis 靶基因联系起来，在 cis 靶标是转录因子或 microRNA 时发现了 trans 效应网络，并用碱基编辑把具体变异与表达变化联系起来；各版本论文中的计数不同 [GV31]。

## 3. Judgments / 判断

J7 (confidence: medium). Variant effects predicted by sequence models (Enformer, Borzoi, AlphaGenome) can serve only as weak prior features and must be evaluated against observed eQTLs and reQTLs [GV02, GV05, GV06].

> J7（置信度：中）。序列模型（Enformer、Borzoi、AlphaGenome）预测的变异效应只能作为弱先验特征，并且必须用观测到的 eQTL 和 reQTL 来评估 [GV02, GV05, GV06]。

J8 (confidence: medium). Pharmacokinetics (PK) and pharmacodynamics (PD) must be separated. Fixed-concentration in-vitro experiments hide PK genotype effects, and the best-known hepatocyte reQTL example involves CYP3A5, a drug-metabolism gene [GD01]. If the scope is target or pathway variation (PD), PK variants are confounders in human data.

> J8（置信度：中）。必须区分药代动力学（PK）与药效动力学（PD）。固定浓度的体外实验会掩盖 PK 的基因型效应，而肝细胞 reQTL 最著名的例子涉及 CYP3A5，这是一个药物代谢基因 [GD01]。如果研究范围是靶点或通路变异（PD），那么人类数据中的 PK 变异就是混杂因素。

J11 (confidence: medium). MR and TWAS evidence can supply prior directions of effect for modulating a target, but not drug-induced transcriptome changes, because their outputs are trait associations [GV10, GV13, GV14].

> J11（置信度：中）。MR 和 TWAS 的证据可以为调节某个靶点提供效应方向的先验，但不能提供药物诱导的转录组变化，因为它们的输出是性状关联 [GV10, GV13, GV14]。

J19 (confidence: medium). A coding variant should not be represented by binding-affinity features alone. Binding constants alone were not a good indicator of resistance, predicting clinical resistance needed the variant's drug-free fitness as well as its fitness under drug, and resistance can arise outside the kinase domain and depend on the background [GV28, GV29, GV30]. Functional maps should supervise the variant representation, with structure and language-model scores as optional extra features [GV16, GV17, GV18].

> J19（置信度：中）。不应仅用结合亲和力特征来表示编码变异。仅凭结合常数不足以指示耐药，预测临床耐药既需要变异在无药时的适应度也需要其有药时的适应度，且耐药可以出现在激酶结构域之外并依赖于背景 [GV28, GV29, GV30]。应当由功能图谱来监督变异表示，把结构和语言模型分数作为可选的额外特征 [GV16, GV17, GV18]。

J20 (confidence: low-medium). For expression-level (class 2) variants, a single-cell sequence model such as scooby is a candidate way to turn a germline variant into a cell-type-specific shift of the baseline state that seeds the source distribution of a world model [GV26, GV27]. Personal-expression prediction by sequence models is still weak [GV05, GV06] and scooby has been shown in one tissue, so any such module must be validated against observed single-cell eQTLs before it is used.

> J20（置信度：低中）。对于表达水平（类别 2）变异，像 scooby 这样的单细胞序列模型是把种系变异转化为细胞类型特异的基线状态偏移的候选方式，该偏移可作为世界模型源分布的种子 [GV26, GV27]。序列模型对个体表达的预测仍然很弱 [GV05, GV06]，而 scooby 只在一种组织中得到展示，因此任何这样的模块在使用前都必须用观测到的单细胞 eQTL 来验证。

## 4. Recommended actions / 行动建议

Use sequence-model scores only as weak prior features, and always evaluate them against observed eQTL and reQTL data rather than against other model outputs [GV05, GV06].

> 只把序列模型的分数用作弱先验特征，并且始终用观测到的 eQTL 和 reQTL 数据而不是其他模型的输出来评估它们 [GV05, GV06]。

For coding variants, treat language-model and structure-based scores (ESM1b, AlphaMissense, Boltz-2) as optional input features whose performance is self-reported, and flag them as such wherever they are used [GV16, GV17, GV18].

> 对于编码变异，把语言模型和基于结构的分数（ESM1b、AlphaMissense、Boltz-2）视为性能为自报的可选输入特征，并在使用处加以标注 [GV16, GV17, GV18]。

Tag PK-gene variants as class 5 and keep them out of the main pharmacodynamic analysis, or model them in a separate branch.

> 把 PK 基因变异标记为类别 5，并让它们不进入主要的药效动力学分析，或在单独的分支中建模。

Use MR and TWAS results as external sanity checks on the direction of target modulation, not as training signals for transcriptome prediction.

> 把 MR 和 TWAS 的结果用作对靶点调节方向的外部合理性检查，而不是转录组预测的训练信号。

Wherever a drug is involved, supervise coding-variant representations with functional maps (saturation, base-editing and deep-mutational data) rather than with affinity predictions alone [GV28, GV29, GV30].

> 凡涉及药物之处，用功能图谱（饱和突变、碱基编辑和深度突变数据）而不是仅用亲和力预测来监督编码变异的表示 [GV28, GV29, GV30]。

Test whether the OneK1K model of scooby can produce cell-type-specific baseline shifts for common variants, by adding variant scoring and validating it against observed single-cell eQTLs; the README does not mention variant scoring, so this is an extension that has to be built and checked [GV26, GV27].

> 检验 scooby 的 OneK1K 模型能否为常见变异给出细胞类型特异的基线偏移：加入变异打分并用观测到的单细胞 eQTL 验证；README 没有提到变异打分，因此这是需要自行构建并核查的扩展 [GV26, GV27]。

## 5. Questions for confirmation / 待确认问题

Should PK-gene variants be excluded from the main analysis or modeled in a separate branch? Default: tagged as class 5 and excluded from the main pharmacodynamic analysis.

> PK 基因变异应排除在主要分析之外，还是在单独的分支中建模？默认：标记为类别 5，并排除在主要药效动力学分析之外。

## 6. Evidence gaps / 证据缺口

No application of AlphaGenome to whole-expression prediction for a personal genome was found (query Q06). No head-to-head comparison of AlphaFold 3 and Boltz-2 on resistance mutations was found (query Q34), and the comparison of AlphaMissense and ESM1b against EVE was not retrieved (query Q39). The findings of the 65-predictor benchmark were not retrieved, only its keywords [GV24].

> 未找到把 AlphaGenome 应用于个人基因组整体表达预测的研究（查询 Q06）。未找到 AlphaFold 3 与 Boltz-2 在耐药突变上的直接对比（查询 Q34），也未取回 AlphaMissense 和 ESM1b 与 EVE 的比较（查询 Q39）。65 个预测器基准的结论未取回，只取回了其关键词 [GV24]。

No application of scooby to variant-effect scoring in a donor cohort was found, and its README does not mention variant scoring (queries Q84 and Q122) [GV27]. A search for transcriptional-response comparisons between target-mutant and wild-type cells under the same drug returned resistance-mechanism papers only (query Q62).

> 未找到 scooby 在供体队列中用于变异效应打分的应用，其 README 也没有提到变异打分（查询 Q84 和 Q122）[GV27]。针对同一药物下目标突变细胞与野生型细胞之间转录响应比较的检索，只返回了耐药机制论文（查询 Q62）。

## 7. Source index (category GV) / 来源索引（类别 GV）

Generated from `data/sources.csv`; regenerate when the CSV changes. Rows whose status is retired are omitted, and each key point is followed by its "so what" where one was written.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。状态为 retired 的条目被省略，写有“意义”的条目在要点之后附上意义。

<!-- source-index:GV:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| GV01 | T2 | [Rare genetic variability in human drug target genes modulates drug response and can guide precision medicine](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8442892/>) | target-gene variants can change expression or function; binding-site variants strongly altered ACE-inhibitor activity | 药靶基因变异可改变表达或功能；结合位点变异显著改变 ACE 抑制剂活性 |
| GV02 | T2 | [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](<https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1.full>) | self-reported state of the art on 22 of 24 track tasks and 24 of 26 variant-effect tasks; eQTL direction better than magnitude (signed Spearman 0.50, unsigned 0.10) | 自报在 24 项 track 任务中的 22 项、26 项变异效应任务中的 24 项达到最先进；eQTL 方向优于幅度（带符号 Spearman 0.50，不带符号 0.10） |
| GV03 | T2 | [Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation (Borzoi)](<https://www.nature.com/articles/s41588-024-02053-6>) | title-level: predicts RNA-seq coverage from DNA sequence as a unifying model of gene regulation (Nature Genetics 2024); scooby builds on Borzoi with a cell-specific decoder for single-cell profiles (GV26, GV27); GV05 reports, at title level, that current genomic deep learning models explain personal transcriptome variation poorly **So what:** the sequence backbone of a variant-to-expression module; its use for personal variant effects must be validated, not assumed (GV05) | 标题层面：由 DNA 序列预测 RNA-seq 覆盖度，作为基因调控的统一模型（Nature Genetics 2024 年）；scooby 在 Borzoi 基础上加上细胞特异解码器来预测单细胞谱（GV26、GV27）；GV05 在标题层面报告当前的基因组深度学习模型对个体转录组变异的解释很差 **意义：** 变异到表达模块的序列骨干；用于个体变异效应时必须验证，而不能假定可行（GV05） |
| GV05 | T2 | [Personal transcriptome variation is poorly explained by current genomic deep learning models](<https://www.nature.com/articles/s41588-023-01574-w>) | 421 Geuvadis individuals; across-gene Spearman 0.57 / 0.52 / 0.53 / 0.33 (Enformer / Basenji2 / ExPecto / Xpresso); weak between-individual explanation, often wrong direction | 421 名 Geuvadis 个体；跨基因 Spearman 0.57 / 0.52 / 0.53 / 0.33（Enformer / Basenji2 / ExPecto / Xpresso）；对个体间差异解释力弱，常判错方向 |
| GV06 | T2 | [Benchmarking of deep neural networks for predicting personal gene expression from DNA sequence highlights shortcomings](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10055057/>) | independent benchmark, consistent conclusions | 独立基准，结论一致 |
| GV07 | T2 | [Personalized gene expression prediction in the era of deep learning: a review](<https://academic.oup.com/bib/article/27/1/bbag022/8445445>) | secondary review reports Enformer cross-individual Spearman of only 0.045 on Geuvadis | 二手综述称 Enformer 在 Geuvadis 上的跨个体 Spearman 仅 0.045 |
| GV09 | T2 | [Preference-Based Fine-Tuning of Genomic Sequence Models for Personal Expression Prediction with Data Augmentation](<https://www.biorxiv.org/content/10.1101/2025.11.09.687505v1.full>) | models trained on the reference genome cannot capture individual-specific regulatory variants | 在参考基因组上训练的模型无法捕获个体特异的调控变异 |
| GV10 | T2 | [Genetic drug target validation using Mendelian randomisation](<https://www.nature.com/articles/s41467-020-16969-0>) | cis instruments; HMGCR / PCSK9 / NPC1L1 / CETP as positive controls; tissue-eQTL-weighted results may disagree with blood pQTL analyses | cis 工具变量；HMGCR / PCSK9 / NPC1L1 / CETP 作阳性对照；组织 eQTL 加权结果可能与血液 pQTL 分析不一致 |
| GV13 | T2 | [Unraveling Novel Genetic Determinants of Thiopurine Response Via TWAS](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12746518/>) | 663 pediatric ALL patients; 31 genes; GNAQ linked to 6MP dose intensity; not clinically validated | 663 名儿童 ALL 患者；31 个基因；GNAQ 与 6MP 剂量强度相关；未经临床验证 |
| GV14 | T2 | [Characterizing the genetic architecture of drug response using gene-context interaction methods](<https://www.cell.com/cell-genomics/fulltext/S2666-979X(24)00351-3>) | TxEWAS tests imputed expression × environment; UK Biobank statins / warfarin / methotrexate | TxEWAS 检验填补表达 × 环境；UK Biobank 中的他汀 / 华法林 / 甲氨蝶呤 |
| GV16 | T2 | [Genome-wide prediction of disease variants with a deep protein language model (ESM1b)](<https://www.biorxiv.org/content/10.1101/2022.08.25.505311.full.pdf>) | 650M-parameter model; about 450 million missense variants scored; 28 DMS datasets (self-reported) | 6.5 亿（650M）参数模型；约 4.5 亿（450 million）个错义变异被打分；28 个 DMS 数据集（自报） |
| GV17 | T2 | [AlphaMissense (DeepMind)](<https://deepmind.google/research/projects/alphamissense/>) | ClinVar auROC above 0.9; mean Spearman about 0.5 on assays of 25 proteins (self-reported); warns of ClinVar training contamination | ClinVar auROC 高于 0.9；25 个蛋白的实验平均 Spearman 约 0.5（自报）；提示 ClinVar 训练污染 |
| GV18 | T2 | [Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction](<https://www.biorxiv.org/content/10.1101/2025.06.14.659707.full.pdf>) | self-reported; authors state no AI model has yet matched FEP or lab-assay accuracy | 自报；作者称尚无 AI 模型达到 FEP 或实验测定的准确度 |
| GV19 | T2 | [BoltzOmics: Predicting genetic variant effects on drug binding with Boltz-2](<https://www.sciencedirect.com/science/article/pii/S2589004226021759>) | hERG, NaV1.5, HER2, CYP3A4; Pearson with IC50 up to 0.76 (wild type) and 0.60 (mutant) | hERG、NaV1.5、HER2、CYP3A4；与 IC50 的 Pearson 最高 0.76（野生型）和 0.60（突变体） |
| GV20 | T2 | [Predicting Mutation-Induced Relative Protein-Ligand Binding Affinity Changes via Conformational Sampling and Diversity Integration with Subsampled AlphaFold2 in Few-Shot Learning](<https://www.biorxiv.org/content/10.1101/2025.02.09.637298.full.pdf>) | few kinase-mutant crystal structures limit accuracy | 激酶突变体晶体结构稀少，限制准确度 |
| GV24 | T2 | [Insights for variant clinical interpretation based on a benchmark of 65 variant effect predictors](<https://hal-emse.ccsd.cnrs.fr/BIGR/hal-05110149v1>) | only keywords retrieved; findings not retrieved | 仅取得关键词，结论未取得 |
| GV26 | T2 | [scooby: modeling multimodal genomic profiles from DNA sequence at single-cell resolution](<https://www.nature.com/articles/s41592-025-02854-5>) | Borzoi plus a cell-specific decoder with LoRA-fine-tuned sequence embeddings predicts scRNA-seq coverage and scATAC-seq insertion profiles per cell; trained on a 10x Multiome bone-marrow dataset of 63,683 cells; self-reported single-cell expression Pearson 0.77 to 0.87 on unseen sequences; finer variant analysis uncovers cell-type-specific eQTLs masked in bulk **So what:** a candidate module that turns a germline variant into a cell-type-specific shift of the baseline state seeding the world model's source distribution, the mediation path for class-2 variants; one tissue only | Borzoi 加上采用 LoRA 微调序列嵌入的细胞特异解码器，可按单个细胞预测 scRNA-seq 覆盖度和 scATAC-seq 插入谱；在 63,683 个细胞的 10x Multiome 骨髓数据集上训练；单细胞表达的 Pearson 自报由 0.77 提高到 0.87（未见序列）；更精细的变异分析发现了在 bulk 中被掩盖的细胞类型特异 eQTL **意义：** 把种系变异转化为细胞类型特异的基线状态偏移的候选模块，该偏移作为世界模型源分布的种子，即类别 2 变异的中介路径；仅一种组织 |
| GV27 | T1 | [gagneurlab/scooby (GitHub)](<https://github.com/gagneurlab/scooby>) | MIT licence; the decoder is conditioned on each cell's position in a precomputed single-cell embedding; pretrained models for NeurIPS (bone marrow), OneK1K and Epicardioids data on Hugging Face; training takes 1 to 2 days on 8 A40 GPUs; the README does not mention variant-effect scoring **So what:** licence passes the reuse check and a donor-level pretrained model (OneK1K) exists, but variant scoring would have to be added and validated | MIT 许可；解码器以每个细胞在预先计算的单细胞嵌入中的位置为条件；Hugging Face 上有 NeurIPS（骨髓）、OneK1K 和 Epicardioids 数据的预训练模型；在 8 块 A40 GPU 上训练需 1 至 2 天；README 未提及变异效应打分 **意义：** 许可通过复用检查，并且有供体层面的预训练模型（OneK1K），但变异打分需要自行添加并验证 |
| GV28 | T2 | [CRISPR-Cas9–mediated saturated mutagenesis screen predicts clinical drug resistance with improved accuracy](<https://www.pnas.org/doi/10.1073/pnas.1708268114>) | BCR-ABL1 saturation mutagenesis tested under several drug conditions; a variant's growth effect without drug as well as with drug was needed to predict clinical resistance; the prediction score correlated highly with clinical prevalence **So what:** a class-1 variant-by-drug effect must be modeled jointly with the variant's drug-free fitness, and such maps are a label source for supervision | 对 BCR-ABL1 做饱和突变并在多种药物条件下检测；预测临床耐药既需要变异在无药时的生长效应也需要有药时的效应；预测分数与临床发生率高度相关 **意义：** 类别 1 变异×药物的效应必须与变异在无药时的适应度联合建模，这类图谱可作为监督的标签来源 |
| GV29 | T2 | [A combined computational and experimental strategy identifies mutations conferring resistance to drugs targeting the BCR-ABL fusion protein](<https://www.nature.com/articles/s42003-019-0743-5>) | recovered clinically observed resistance mutations to imatinib, nilotinib, dasatinib, bosutinib and ponatinib; binding constants alone were not a good indicator of drug resistance **So what:** structure- or affinity-based variant features (for example Boltz-2) cannot be the only variant representation; functional maps should supervise | 重现了对 imatinib、nilotinib、dasatinib、bosutinib 和 ponatinib 的临床观察到的耐药突变；仅凭结合常数不足以指示耐药 **意义：** 基于结构或亲和力的变异特征（例如 Boltz-2）不能作为唯一的变异表示；应由功能图谱来监督 |
| GV30 | T2 | [Dual functional genomics reveals a broad and convergent landscape of asciminib resistance in BCR::ABL1](<https://link.springer.com/article/10.1186/s13073-026-01679-x>) | a base-editing screen across BCR::ABL1 found resistance hotspots, deep mutational scanning mapped every amino-acid change in them, an edit-on-edit background carrying Y253H tested epistasis, and a FRET biosensor linked conformation to sensitivity; resistance can arise outside the kinase domain **So what:** variant-by-variant epistasis under a drug is measurable, so the variant feature space must allow background dependence and non-active-site effects | 对 BCR::ABL1 的碱基编辑筛选找出耐药热点，深度突变扫描绘制了其中每一种氨基酸改变，携带 Y253H 的“编辑叠加编辑”背景检验了上位性，FRET 生物传感器把构象与敏感性联系起来；耐药可出现在激酶结构域之外 **意义：** 药物下变异间的上位性是可测量的，因此变异特征空间必须允许背景依赖和非活性位点效应 |
| GV31 | T2 | [Discovery of target genes and pathways at GWAS loci by pooled single-cell CRISPR screens (STING-seq)](<https://www.science.org/doi/10.1126/science.adh7699>) | CRISPR silencing of candidate regulatory elements read out by single-cell RNA-seq; 124 cis-target genes of 91 noncoding blood-trait loci; trans-effect networks when cis targets are transcription factors or microRNAs; base editing linked specific variants to expression changes **So what:** the template for the middle layer between a non-coding variant and a transcriptional programme, which a drug-response model would otherwise treat as a black box | 对候选调控元件做 CRISPR 沉默并用单细胞 RNA-seq 读出；找到 91 个非编码血液性状位点的 124 个 cis 靶基因；当 cis 靶标是转录因子或 microRNA 时发现 trans 效应网络；碱基编辑把具体变异与表达变化联系起来 **意义：** 非编码变异与转录程序之间中间层的模板，否则药物响应模型会把它当作黑箱 |
<!-- source-index:GV:end -->

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

## 3. Judgments / 判断

J7 (confidence: medium). Variant effects predicted by sequence models (Enformer, Borzoi, AlphaGenome) can serve only as weak prior features and must be evaluated against observed eQTLs and reQTLs [GV02, GV05, GV06].

> J7（置信度：中）。序列模型（Enformer、Borzoi、AlphaGenome）预测的变异效应只能作为弱先验特征，并且必须用观测到的 eQTL 和 reQTL 来评估 [GV02, GV05, GV06]。

J8 (confidence: medium). Pharmacokinetics (PK) and pharmacodynamics (PD) must be separated. Fixed-concentration in-vitro experiments hide PK genotype effects, and the best-known hepatocyte reQTL example involves CYP3A5, a drug-metabolism gene [GD01]. If the scope is target or pathway variation (PD), PK variants are confounders in human data.

> J8（置信度：中）。必须区分药代动力学（PK）与药效动力学（PD）。固定浓度的体外实验会掩盖 PK 的基因型效应，而肝细胞 reQTL 最著名的例子涉及 CYP3A5，这是一个药物代谢基因 [GD01]。如果研究范围是靶点或通路变异（PD），那么人类数据中的 PK 变异就是混杂因素。

J11 (confidence: medium). MR and TWAS evidence can supply prior directions of effect for modulating a target, but not drug-induced transcriptome changes, because their outputs are trait associations [GV10, GV13, GV14].

> J11（置信度：中）。MR 和 TWAS 的证据可以为调节某个靶点提供效应方向的先验，但不能提供药物诱导的转录组变化，因为它们的输出是性状关联 [GV10, GV13, GV14]。

## 4. Recommended actions / 行动建议

Use sequence-model scores only as weak prior features, and always evaluate them against observed eQTL and reQTL data rather than against other model outputs [GV05, GV06].

> 只把序列模型的分数用作弱先验特征，并且始终用观测到的 eQTL 和 reQTL 数据而不是其他模型的输出来评估它们 [GV05, GV06]。

For coding variants, treat language-model and structure-based scores (ESM1b, AlphaMissense, Boltz-2) as optional input features whose performance is self-reported, and flag them as such wherever they are used [GV16, GV17, GV18].

> 对于编码变异，把语言模型和基于结构的分数（ESM1b、AlphaMissense、Boltz-2）视为性能为自报的可选输入特征，并在使用处加以标注 [GV16, GV17, GV18]。

Tag PK-gene variants as class 5 and keep them out of the main pharmacodynamic analysis, or model them in a separate branch.

> 把 PK 基因变异标记为类别 5，并让它们不进入主要的药效动力学分析，或在单独的分支中建模。

Use MR and TWAS results as external sanity checks on the direction of target modulation, not as training signals for transcriptome prediction.

> 把 MR 和 TWAS 的结果用作对靶点调节方向的外部合理性检查，而不是转录组预测的训练信号。

## 5. Questions for confirmation / 待确认问题

Should PK-gene variants be excluded from the main analysis or modeled in a separate branch? Default: tagged as class 5 and excluded from the main pharmacodynamic analysis.

> PK 基因变异应排除在主要分析之外，还是在单独的分支中建模？默认：标记为类别 5，并排除在主要药效动力学分析之外。

## 6. Evidence gaps / 证据缺口

No application of AlphaGenome to whole-expression prediction for a personal genome was found (query Q06). No head-to-head comparison of AlphaFold 3 and Boltz-2 on resistance mutations was found (query Q34), and the comparison of AlphaMissense and ESM1b against EVE was not retrieved (query Q39). The findings of the 65-predictor benchmark were not retrieved, only its keywords [GV24].

> 未找到把 AlphaGenome 应用于个人基因组整体表达预测的研究（查询 Q06）。未找到 AlphaFold 3 与 Boltz-2 在耐药突变上的直接对比（查询 Q34），也未取回 AlphaMissense 和 ESM1b 与 EVE 的比较（查询 Q39）。65 个预测器基准的结论未取回，只取回了其关键词 [GV24]。

## 7. Source index (category GV) / 来源索引（类别 GV）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:GV:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| GV01 | T2 | [Rare genetic variability in human drug target genes modulates drug response and can guide precision medicine](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8442892/>) | target-gene variants can change expression or function; binding-site variants strongly altered ACE-inhibitor activity | 药靶基因变异可改变表达或功能；结合位点变异显著改变 ACE 抑制剂活性 |
| GV02 | T2 | [AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](<https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1.full>) | self-reported state of the art on 22 of 24 track tasks and 24 of 26 variant-effect tasks; eQTL direction better than magnitude (signed Spearman 0.50, unsigned 0.10) | 自报在 24 项 track 任务中的 22 项、26 项变异效应任务中的 24 项达到最先进；eQTL 方向优于幅度（带符号 Spearman 0.50，不带符号 0.10） |
| GV03 | T2 | [Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation (Borzoi)](<https://www.nature.com/articles/s41588-024-02053-6>) | — | — |
| GV04 | T2 | [Leveraging genomic deep learning models for the prediction of non-coding variant effects](<https://arxiv.org/html/2411.11158v2>) | review | 综述 |
| GV05 | T2 | [Personal transcriptome variation is poorly explained by current genomic deep learning models](<https://www.nature.com/articles/s41588-023-01574-w>) | 421 Geuvadis individuals; across-gene Spearman 0.57 / 0.52 / 0.53 / 0.33 (Enformer / Basenji2 / ExPecto / Xpresso); weak between-individual explanation, often wrong direction | 421 名 Geuvadis 个体；跨基因 Spearman 0.57 / 0.52 / 0.53 / 0.33（Enformer / Basenji2 / ExPecto / Xpresso）；对个体间差异解释力弱，常判错方向 |
| GV06 | T2 | [Benchmarking of deep neural networks for predicting personal gene expression from DNA sequence highlights shortcomings](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10055057/>) | independent benchmark, consistent conclusions | 独立基准，结论一致 |
| GV07 | T2 | [Personalized gene expression prediction in the era of deep learning: a review](<https://academic.oup.com/bib/article/27/1/bbag022/8445445>) | secondary review reports Enformer cross-individual Spearman of only 0.045 on Geuvadis | 二手综述称 Enformer 在 Geuvadis 上的跨个体 Spearman 仅 0.045 |
| GV08 | T2 | [Deep-learning prediction of gene expression from personal genomes](<https://link.springer.com/article/10.1186/s13059-025-03926-7>) | — | — |
| GV09 | T2 | [Preference-Based Fine-Tuning of Genomic Sequence Models for Personal Expression Prediction with Data Augmentation](<https://www.biorxiv.org/content/10.1101/2025.11.09.687505v1.full>) | models trained on the reference genome cannot capture individual-specific regulatory variants | 在参考基因组上训练的模型无法捕获个体特异的调控变异 |
| GV10 | T2 | [Genetic drug target validation using Mendelian randomisation](<https://www.nature.com/articles/s41467-020-16969-0>) | cis instruments; HMGCR / PCSK9 / NPC1L1 / CETP as positive controls; tissue-eQTL-weighted results may disagree with blood pQTL analyses | cis 工具变量；HMGCR / PCSK9 / NPC1L1 / CETP 作阳性对照；组织 eQTL 加权结果可能与血液 pQTL 分析不一致 |
| GV11 | T2 | [Mendelian randomization as a tool to inform drug development using human genetics](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10953771/>) | — | — |
| GV12 | T2 | [Validation of lipid-related therapeutic targets for coronary heart disease prevention using human genetics](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8531035/>) | — | — |
| GV13 | T2 | [Unraveling Novel Genetic Determinants of Thiopurine Response Via TWAS](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12746518/>) | 663 pediatric ALL patients; 31 genes; GNAQ linked to 6MP dose intensity; not clinically validated | 663 名儿童 ALL 患者；31 个基因；GNAQ 与 6MP 剂量强度相关；未经临床验证 |
| GV14 | T2 | [Characterizing the genetic architecture of drug response using gene-context interaction methods](<https://www.cell.com/cell-genomics/fulltext/S2666-979X(24)00351-3>) | TxEWAS tests imputed expression × environment; UK Biobank statins / warfarin / methotrexate | TxEWAS 检验填补表达 × 环境；UK Biobank 中的他汀 / 华法林 / 甲氨蝶呤 |
| GV15 | T2 | [Clinical and Therapeutic Applications of Individual-level Tissue-Specific Imputed Transcriptomes](<https://www.medrxiv.org/content/10.1101/2022.11.23.22282644.full.pdf>) | — | — |
| GV16 | T2 | [Genome-wide prediction of disease variants with a deep protein language model (ESM1b)](<https://www.biorxiv.org/content/10.1101/2022.08.25.505311.full.pdf>) | 650M-parameter model; about 450 million missense variants scored; 28 DMS datasets (self-reported) | 6.5 亿（650M）参数模型；约 4.5 亿（450 million）个错义变异被打分；28 个 DMS 数据集（自报） |
| GV17 | T2 | [AlphaMissense (DeepMind)](<https://deepmind.google/research/projects/alphamissense/>) | ClinVar auROC above 0.9; mean Spearman about 0.5 on assays of 25 proteins (self-reported); warns of ClinVar training contamination | ClinVar auROC 高于 0.9；25 个蛋白的实验平均 Spearman 约 0.5（自报）；提示 ClinVar 训练污染 |
| GV18 | T2 | [Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction](<https://www.biorxiv.org/content/10.1101/2025.06.14.659707.full.pdf>) | self-reported; authors state no AI model has yet matched FEP or lab-assay accuracy | 自报；作者称尚无 AI 模型达到 FEP 或实验测定的准确度 |
| GV19 | T2 | [BoltzOmics: Predicting genetic variant effects on drug binding with Boltz-2](<https://www.sciencedirect.com/science/article/pii/S2589004226021759>) | hERG, NaV1.5, HER2, CYP3A4; Pearson with IC50 up to 0.76 (wild type) and 0.60 (mutant) | hERG、NaV1.5、HER2、CYP3A4；与 IC50 的 Pearson 最高 0.76（野生型）和 0.60（突变体） |
| GV20 | T2 | [Predicting Mutation-Induced Relative Protein-Ligand Binding Affinity Changes via Conformational Sampling and Diversity Integration with Subsampled AlphaFold2 in Few-Shot Learning](<https://www.biorxiv.org/content/10.1101/2025.02.09.637298.full.pdf>) | few kinase-mutant crystal structures limit accuracy | 激酶突变体晶体结构稀少，限制准确度 |
| GV21 | T2 | [Towards Precision Protein-Ligand Affinity Prediction Benchmark: A Complete and Modification-Aware DAVIS Dataset](<https://arxiv.org/pdf/2512.00708>) | — | — |
| GV22 | T2 | [From Prediction to Simulation: AlphaFold 3 as a Differentiable Framework for Structural Biology](<https://arxiv.org/pdf/2508.18446>) | perspective, not a benchmark | 观点文章，不是基准 |
| GV23 | T2 | [Benchmarking DNA Foundation Models for zero-shot variant effect prediction: the role of context, training, and architecture](<https://www.biorxiv.org/content/10.1101/2025.06.15.659748.full.pdf>) | — | — |
| GV24 | T2 | [Insights for variant clinical interpretation based on a benchmark of 65 variant effect predictors](<https://hal-emse.ccsd.cnrs.fr/BIGR/hal-05110149v1>) | only keywords retrieved; findings not retrieved | 仅取得关键词，结论未取得 |
| GV25 | T2 | [Expanding the utility of variant effect predictions with phenotype-specific models (V2P)](<https://www.nature.com/articles/s41467-025-66607-w>) | — | — |
<!-- source-index:GV:end -->

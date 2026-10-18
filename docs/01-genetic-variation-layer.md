# 01 Genetic variation layer / 遗传变异层

## 1. Scope / 范围

This document covers what is known about variants in drug targets and signaling pathways before any drug is applied: how variants change target expression, how coding variants change protein function and drug binding, how well sequence models predict expression in individual people, and what population-genetics methods add. Evidence about drug-induced responses is in document 02.

> 本文档涵盖在施加任何药物之前，关于药物靶点和信号通路中变异的已知信息：变异如何改变靶点表达，编码变异如何改变蛋白功能和药物结合，序列模型对个体表达的预测有多好，以及群体遗传学方法能补充什么。关于药物诱导响应的证据在文档 02 中。

## 2. Facts and evidence / 事实与证据

Variants in drug-target genes alter drug response. Of 1,094 population variants within 6 Å of bound drugs, 18 of 19 tested in vitro abrogated function or altered the drug effect, and ACE variants left baseline activity unchanged yet differed more than 10-fold in ACE-inhibitor response, while pathogenicity-predictor accuracy dropped below 76% on drug-altering variants [GV01].

> 药物靶点基因中的变异会改变药物响应。在与结合药物相距 6 Å 以内的 1,094 个人群变异中，经体外检测的 19 个里有 18 个丧失了功能或改变了药物效应；ACE 变异使基线活性保持不变，但对 ACE 抑制剂的响应相差 10 倍以上，而致病性预测器在改变药物效应的变异上的准确度降到了 76% 以下 [GV01]。

Binding is not enough to predict resistance. In BCR-ABL1 saturation mutagenesis, a variant's drug-free growth added to its growth under drug predicted clinical prevalence better than either alone [GV28]; affinity change alone did not mark clinical resistance, whereas IC50 shift and preserved catalytic activity did [GV29]; and an asciminib screen found 279 resistance variants across SH3, SH2 and kinase domains with rare epistasis in a Y253H background (two guides) [GV30]. Saturation mutagenesis of FGFR matched 28 of 29 acquired-resistance cases in trials, and REVEL, EVE and AlphaMissense did not predict gain of function [GV33]; an EGFR screen predicted combination escape from single-agent profiles [GV32]. The Boltz-2 authors state that no AI model has yet matched free-energy-perturbation or laboratory-assay accuracy [GV18], and a Boltz-2 pipeline ranked variants within a drug weakly in two of three settings (r 0.19 and 0.30) [GV19].

> 仅凭结合不足以预测耐药。在 BCR-ABL1 饱和突变中，变异在无药时的生长加上有药时的生长，比任何单独一项都更能预测临床流行率 [GV28]；仅有亲和力变化并不能标志临床耐药，而 IC50 变化和保留的催化活性可以 [GV29]；asciminib 筛选在 SH3、SH2 和激酶结构域中找到 279 个耐药变异，在 Y253H 背景下上位效应很少见（两条向导 RNA）[GV30]。FGFR 的饱和突变与试验中 29 个获得性耐药病例里的 28 个相符，而 REVEL、EVE 和 AlphaMissense 没有预测出功能获得 [GV33]；一个 EGFR 筛选由单药谱预测出了联合用药的逃逸 [GV32]。Boltz-2 的作者声明，还没有哪个 AI 模型达到自由能微扰或实验测定的准确度 [GV18]，而一个 Boltz-2 流程在三种设置中的两种里对同一药物下的变异排序很弱（r 为 0.19 和 0.30）[GV19]。

Sequence-to-expression models explain personal variation poorly. Across 421 Geuvadis individuals, four models reached across-gene Spearman correlations of 0.33 to 0.57 but cross-individual correlations near zero with frequent wrong direction [GV05]; Enformer on 839 individuals reached a mean cross-individual Pearson of 0.01, and PrediXcan significantly predicted 921 genes against 162 for Enformer among 1,570 [GV06]. AlphaGenome self-reports state-of-the-art results on 22 of 24 track and 25 of 26 variant-effect evaluations, with signed Spearman 0.50 on fine-mapped eQTLs against 0.10 on absolute values, and its authors state that personal-genome prediction is not benchmarked [GV02]. Fine-tuning on simulated personal genomes has been proposed (abstract level) [GV09].

> 序列到表达模型对个人间变异的解释很差。在 421 个 Geuvadis 个体中，四个模型的跨基因 Spearman 相关为 0.33 至 0.57，但个体间相关接近零且方向经常错误 [GV05]；Enformer 在 839 个个体上的个体间平均 Pearson 为 0.01，在 1,570 个基因中 PrediXcan 显著预测了 921 个，而 Enformer 为 162 个 [GV06]。AlphaGenome 自报在 24 项轨道评估中的 22 项和 26 项变异效应评估中的 25 项达到最先进水平，在精细定位的 eQTL 上带符号 Spearman 为 0.50，而取绝对值时为 0.10，其作者声明个人基因组预测没有被基准评估 [GV02]。有人提出用模拟的个人基因组做微调（摘要层面）[GV09]。

Sequence models now reach single-cell resolution. scooby adds a cell-specific decoder to Borzoi and predicts single-cell expression from sequence (63,683 bone-marrow cells; Pearson 0.77 to 0.87 across genes, self-reported), and its OneK1K model outperforms Borzoi on cell-type eQTLs; its code is MIT-licensed and its README does not mention variant scoring [GV26, GV27].

> 序列模型现在已达到单细胞分辨率。scooby 给 Borzoi 加上细胞特异的解码器，由序列预测单细胞表达（63,683 个骨髓细胞；跨基因 Pearson 为 0.77 至 0.87，自报），其 OneK1K 模型在细胞类型 eQTL 上优于 Borzoi；其代码采用 MIT 许可，README 没有提到变异打分 [GV26, GV27]。

Population-genetics methods give priors, not transcriptomes. Cis-variant instruments for drug-target MR flip sign between tissues (PCSK9 expression raised coronary heart disease risk in adrenal gland and lowered it in uterus) [GV10]; a TWAS of thiopurine response in 663 patients found 31 genes at a permissive cutoff and only GNAQ validated [GV13]; and in 342,257 UK Biobank individuals, all 131 modifier genes with additive effects were sign-opposed to the baseline effect, so statins uniformly dampened genetic effects [GV14]. Pooled single-cell CRISPR screens linked 91 non-coding blood-trait loci to 124 cis-target genes (abstract level) [GV31].

> 群体遗传学方法给出的是先验，而不是转录组。药物靶点 MR 的顺式变异工具变量在不同组织间符号会翻转（PCSK9 表达在肾上腺中升高冠心病风险，在子宫中降低）[GV10]；一项针对 663 名患者的硫嘌呤响应 TWAS 在宽松阈值下找到 31 个基因，只有 GNAQ 得到验证 [GV13]；在 342,257 名 UK Biobank 个体中，有加性效应的 131 个修饰基因全部与基线效应符号相反，所以他汀类均匀地削弱了遗传效应 [GV14]。混池单细胞 CRISPR 筛选把 91 个非编码血液性状位点与 124 个顺式靶基因联系起来（摘要层面）[GV31]。

## 3. Judgments / 判断

J7 (confidence: medium). Variant effects predicted by sequence models (Enformer, Borzoi, AlphaGenome) can serve only as weak prior features and must be evaluated against observed eQTLs and reQTLs [GV02, GV05, GV06].

> J7（置信度：中）。序列模型（Enformer、Borzoi、AlphaGenome）预测的变异效应只能作为弱先验特征，并且必须对照观测到的 eQTL 和 reQTL 来评估 [GV02, GV05, GV06]。

J8 (confidence: medium). Pharmacokinetics (PK) and pharmacodynamics (PD) must be separated. Fixed-concentration in-vitro experiments hide PK genotype effects, and the best-known hepatocyte reQTL example involves CYP3A5, a drug-metabolism gene [GD01]. If the scope is target or pathway variation (PD), PK variants are confounders in human data.

> J8（置信度：中）。必须区分药代动力学（PK）与药效动力学（PD）。固定浓度的体外实验掩盖了 PK 基因型效应，而最著名的肝细胞 reQTL 例子涉及药物代谢基因 CYP3A5 [GD01]。如果范围是靶点或通路变异（PD），那么 PK 变异在人类数据中是混杂因素。

J11 (confidence: medium). MR and TWAS evidence can supply prior directions of effect for modulating a target, but not drug-induced transcriptome changes, because their outputs are trait associations and the sign can flip between tissues [GV10, GV13, GV14]. A drug can also dampen baseline genetic effects uniformly, so a genotype-aware model should learn drug-dependent attenuation, not only additive shifts [GV14].

> J11（置信度：中）。MR 和 TWAS 证据可以为调节靶点提供效应方向的先验，但不能提供药物诱导的转录组变化，因为它们的输出是性状关联，而且符号在不同组织间可能翻转 [GV10, GV13, GV14]。药物还可能均匀地削弱基线遗传效应，所以基因型感知模型应当学习依赖药物的衰减，而不只是加性偏移 [GV14]。

J19 (confidence: medium). A coding variant should not be represented by binding-affinity features alone: affinity change did not mark clinical resistance, predicting resistance needed the variant's drug-free fitness, resistance arises outside the kinase domain and depends on background, and pathogenicity scores did not predict gain of function or lost accuracy on drug-altering variants [GV28, GV29, GV30, GV33, GV01]. Functional maps should supervise the variant representation, with structure and language-model scores as optional extra features [GV16, GV17, GV18].

> J19（置信度：中）。不应仅用结合亲和力特征来表示编码变异：亲和力变化并不能标志临床耐药，预测耐药需要变异在无药时的适应度，耐药可出现在激酶结构域之外并取决于背景，而致病性分数没有预测出功能获得，或在改变药物效应的变异上失去了准确度 [GV28, GV29, GV30, GV33, GV01]。应当用功能图谱监督变异表示，结构和语言模型分数只作为可选的额外特征 [GV16, GV17, GV18]。

J20 (confidence: low-medium). For expression-level (class 2) variants, a single-cell sequence model such as scooby is a candidate way to turn a germline variant into a cell-type-specific shift of the baseline state that seeds the source distribution of a world model [GV26, GV27]. Personal-expression prediction by sequence models is still weak [GV05, GV06] and scooby has been shown in one tissue, so any such module must be validated against observed single-cell eQTLs before it is used.

> J20（置信度：低中）。对表达水平（类别 2）变异，像 scooby 这样的单细胞序列模型，是把种系变异转化为基线状态的细胞类型特异偏移、进而为世界模型的源分布提供种子的候选方式 [GV26, GV27]。序列模型对个人表达的预测仍然很弱 [GV05, GV06]，而 scooby 只在一种组织中得到展示，因此任何这样的模块在使用前都必须对照观测到的单细胞 eQTL 加以验证。

## 4. Recommended actions / 行动建议

Use sequence-model scores only as weak prior features, evaluated against observed eQTL and reQTL data rather than against other model outputs [GV05, GV06].

> 只把序列模型分数用作弱先验特征，并对照观测到的 eQTL 和 reQTL 数据，而不是对照其他模型的输出来评估 [GV05, GV06]。

Treat language-model and structure-based scores (ESM1b, AlphaMissense, Boltz-2) as optional input features whose performance is self-reported [GV16, GV17, GV18], and supervise coding-variant representations with functional maps (saturation, base-editing and deep-mutational data) [GV28, GV29, GV30, GV32, GV33].

> 把语言模型和基于结构的分数（ESM1b、AlphaMissense、Boltz-2）视为性能为自报的可选输入特征 [GV16, GV17, GV18]，并用功能图谱（饱和突变、碱基编辑和深度突变数据）监督编码变异的表示 [GV28, GV29, GV30, GV32, GV33]。

Tag PK-gene variants as class 5 and keep them out of the main pharmacodynamic analysis, or model them in a separate branch.

> 把 PK 基因变异标记为类别 5，并让它们不进入主要的药效动力学分析，或在单独的分支中对其建模。

Use MR and TWAS results as external sanity checks on the direction of target modulation, not as training signals for transcriptome prediction.

> 把 MR 和 TWAS 结果用作靶点调节方向的外部合理性检查，而不是转录组预测的训练信号。

Test whether the OneK1K model of scooby can produce cell-type-specific baseline shifts for common variants by adding variant scoring and validating it against observed single-cell eQTLs; the README does not mention variant scoring, so this extension has to be built and checked [GV26, GV27].

> 检验 scooby 的 OneK1K 模型能否为常见变异产生细胞类型特异的基线偏移：加入变异打分，并对照观测到的单细胞 eQTL 验证；README 没有提到变异打分，因此这一扩展必须自行构建并核对 [GV26, GV27]。

## 5. Questions for confirmation / 待确认问题

Open decisions for this topic are kept in `data/questions.csv` and listed in `docs/10-open-questions.md`: UQ11 (PK-gene variants: exclude or separate branch) and UQ15 (the five-class variant scheme).

> 本主题的待决事项保存在 `data/questions.csv` 中，并列在 `docs/10-open-questions.md` 里：UQ11（PK 基因变异：排除还是单独分支）和 UQ15（五类变异体系）。

## 6. Evidence gaps / 证据缺口

No application of AlphaGenome to whole-expression prediction for a personal genome was found (Q06), and no head-to-head comparison of AlphaFold 3 and Boltz-2 on resistance mutations was found (Q34). No application of scooby to variant-effect scoring in a donor cohort was found (Q84, Q122) [GV27], and a search for transcriptional-response comparisons between target-mutant and wild-type cells under the same drug returned resistance-mechanism papers only (Q62).

> 没有找到 AlphaGenome 用于个人基因组整体表达预测的应用（Q06），也没有找到 AlphaFold 3 与 Boltz-2 在耐药突变上的直接比较（Q34）。没有找到 scooby 在供体队列中用于变异效应打分的应用（Q84、Q122）[GV27]，而针对“同一药物下靶点突变细胞与野生型细胞转录响应比较”的检索只返回了耐药机制论文（Q62）。

## 7. Source index (category GV) / 来源索引（类别 GV）

Generated from `data/sources.csv`; regenerate when the CSV changes. Rows whose status is retired are omitted, and each key point is followed by its "so what" where one was written.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。状态为 retired 的条目被省略，写有“意义”的条目在要点之后附上意义。

<!-- source-index:GV:start -->
| ID | Tier | Source | So what | 意义（中文） |
|---|---|---|---|---|
| GV01 | T1 | [Rare genetic variability in human drug target genes modulates drug response and can guide precision medicine](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8442892/>) | ACE variants change the drug response with baseline activity unchanged (operator change), and pathogenicity-predictor accuracy drops below 76% on drug-altering variants; variant features need drug-specific supervision. | ACE 变异在基线活性不变的情况下改变药物响应（算子变化），而致病性预测器在改变药效的变异上准确度降至 76% 以下；变异特征需要药物特异的监督。 |
| GV02 | T1 | [Advancing regulatory variant effect prediction with AlphaGenome](<https://www.biorxiv.org/content/10.1101/2025.06.25.661532v1.full>) | Usable as a population-level eQTL-effect prior for class-2 variants; personal-genome prediction is unbenchmarked and condition-specific effects remain challenging, so genotype-by-drug use needs its own validation. | 可作为类别 2 变异群体层面 eQTL 效应的先验；个人基因组预测未经基准评测，条件特异效应仍具挑战，因此任何基因型×药物用途都需要自行验证。 |
| GV03 | T1 | [Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation](<https://www.nature.com/articles/s41588-024-02053-6>) | Sequence backbone for variant-to-expression scoring, benchmarked here on population-level eQTLs; GV05 shows related models fail across individuals, so use for personal variant effects must be validated. | 用于变异到表达评分的序列骨干，此处在群体层面的 eQTL 上做了基准评测；GV05 表明相关模型在个体间失效，因此用于个人变异效应必须经过验证。 |
| GV05 | T1 | [Personal transcriptome variation is poorly explained by current genomic deep learning models](<https://www.nature.com/articles/s41588-023-01574-w>) | Across-gene accuracy hides the failure: a genotype-aware model must be scored on cross-individual (delta) correlation and direction against a per-gene linear baseline. | 跨基因准确度掩盖了失败：基因型感知模型必须在跨个体（差值）相关性和方向上评分，并与逐基因线性基线比较。 |
| GV06 | T1 | [Benchmarking of deep neural networks for predicting personal gene expression from DNA sequence highlights shortcomings](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10055057/>) | A second cohort, a different tissue and 839 donors reproduce the GV05 pattern, so the cross-individual weakness is not a Geuvadis artefact; a per-gene linear baseline is the bar. | 第二个队列、不同组织、839 名供体复现了 GV05 的模式，说明跨个体的弱点不是 Geuvadis 特有的假象；逐基因线性基线是需要超越的标准。 |
| GV07 | T1 | [Personalized gene expression prediction in the era of deep learning: a review](<https://academic.oup.com/bib/article/27/1/bbag022/8445445>) | A genotype-aware model must beat a per-gene linear baseline on cross-individual, held-out-gene and cross-ancestry tests; the review reports fine-tuned deep models at best match it. | 基因型感知模型必须在跨个体、留出基因和跨族裔检验上超过逐基因线性基线；综述报告微调后的深度模型至多与之持平。 |
| GV09 | T2 | [Preference-Based Fine-Tuning of Genomic Sequence Models for Personal Expression Prediction with Data Augmentation](<https://www.biorxiv.org/content/10.1101/2025.11.09.687505v1.full>) | Design hint: augment scarce paired genotype-expression data with simulated genotypes and eQTL-model pseudo-labels, trained with a relative (preference) objective; effect sizes are not available at abstract level. | 设计提示：用模拟基因型和 eQTL 模型伪标签扩充稀缺的基因型–表达配对数据，并用相对（偏好）目标训练；摘要层面无法得到效应量。 |
| GV10 | T1 | [Genetic drug target validation using Mendelian randomisation](<https://www.nature.com/articles/s41467-020-16969-0>) | Cis-variant direction priors for a target are tissue-dependent (sign flips between adrenal gland and uterus), so they need cell-type conditioning; outputs are disease risks, not transcriptomes. | 为靶点调节提供 cis 变异方向先验时，符号随组织而变（肾上腺与子宫相反），因此需要按细胞类型条件化；输出是疾病风险而非转录组。 |
| GV13 | T1 | [Unraveling Novel Genetic Determinants of Thiopurine Response Via TWAS](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12746518/>) | Genotype-to-drug-tolerance evidence via imputed expression is sparse (one validated gene of 31 at q < 0.90) and yields no transcriptome response; use only as a direction prior. | 经填补表达得到的基因型–药物耐受证据稀少（q < 0.90 下 31 个基因中只有 1 个得到验证），且不给出转录组响应；只宜用作方向先验。 |
| GV14 | T1 | [Characterizing the genetic architecture of drug response using gene-context interaction methods](<https://www.cell.com/cell-genomics/fulltext/S2666-979X(24)00351-3>) | A drug can uniformly dampen baseline genetic effects (statins, LDL), so a genotype-aware model should learn drug-dependent attenuation of genotype effects, not only additive shifts. | 药物可以均匀地削弱基线遗传效应（他汀、LDL），因此基因型感知模型应学习药物依赖的基因型效应衰减，而不只是加性偏移。 |
| GV16 | T2 | [Genome-wide prediction of disease variants with a deep protein language model](<https://www.biorxiv.org/content/10.1101/2022.08.25.505311.full.pdf>) | Cheap genome-wide coding-variant feature that scores damage, not drug response; GV01 reports pathogenicity predictors drop below 76% accuracy on drug-altering variants, so use it only as an input feature. | 廉价的全基因组编码变异特征，评分的是损伤而非药物响应；GV01 报告致病性预测器在改变药效的变异上准确度降至 76% 以下，因此只宜作输入特征。 |
| GV17 | T1 | [A catalogue of genetic mutations to help pinpoint the cause of diseases](<https://deepmind.google/research/projects/alphamissense/>) | Free genome-wide coding-variant feature labelled by population frequency, not drug response; use as an input feature only, since GV01 shows pathogenicity predictors lose accuracy on drug-altering variants. | 免费的全基因组编码变异特征，标签来自群体频率而非药物响应；只宜作输入特征，因为 GV01 表明致病性预测器在改变药效的变异上会损失准确度。 |
| GV18 | T1 | [Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction](<https://www.biorxiv.org/content/10.1101/2025.06.14.659707.full.pdf>) | Benchmarks rank ligand analogues per target, not protein variants, and accuracy varies by assay, so variant-affinity use is unvalidated; the pairwise intra-assay loss is a template for genotype contrasts. | 基准按靶点对配体类似物排序，而不是对蛋白变异排序，且准确度随测定而异，因此用于变异亲和力尚未验证；成对的测定内差值损失可作为监督基因型对比的模板。 |
| GV19 | T1 | [BoltzOmics: Predicting genetic variant effects on drug binding with Boltz-2](<https://www.sciencedirect.com/science/article/pii/S2589004226021759>) | Reported correlations mostly rank drugs within a variant; the one within-drug variant ranking (CYP3A4) was weak in two of three settings (0.19 and 0.30), so genotype-effect accuracy is unproven. | 报告的相关性多为同一变异内对药物排序；唯一的药物内变异排序（CYP3A4）在三个设置中的两个较弱（0.19 和 0.30），因此基因型效应的准确度尚未证实。 |
| GV20 | T2 | [Predicting Mutation-Induced Relative Protein-Ligand Binding Affinity Changes via Conformational Sampling and Diversity Integration with Subsampled AlphaFold2 in Few-Shot Learning](<https://www.biorxiv.org/content/10.1101/2025.02.09.637298.full.pdf>) | A relative (pairwise Siamese) target suits mutation-induced affinity change when mutant structures are missing; evidence is limited to 31 ABL variants and one kinase, at abstract level. | 当突变体结构缺失时，相对（成对 Siamese）目标适合预测突变引起的亲和力变化；证据仅限于 31 个 ABL 变异和一种激酶，且为摘要层面。 |
| GV24 | T2 | [Insights for variant clinical interpretation based on a benchmark of 65 variant effect predictors](<https://hal-emse.ccsd.cnrs.fr/BIGR/hal-05110149v1>) | Independent evidence that ClinVar-only benchmarks are easy and may flatter predictors; evaluate coding-variant features on functional data as well. | 独立证据表明仅用 ClinVar 的基准较易，可能抬高预测器的表现；评估编码变异特征时也应使用功能数据。 |
| GV26 | T1 | [scooby: modeling multimodal genomic profiles from DNA sequence at single-cell resolution](<https://www.nature.com/articles/s41592-025-02854-5>) | Candidate route to cell-type-specific class-2 effects by scoring reference versus alternative alleles, without donor genotype input; distal and sign accuracy are limited, so it needs validation. | 通过比较参考与替代等位基因来评分，是得到细胞类型特异的类别 2 效应的候选途径，且没有供体基因型输入；远端变异和符号准确度有限，因此需要验证。 |
| GV27 | T1 | [gagneurlab/scooby (GitHub)](<https://github.com/gagneurlab/scooby>) | Code is reusable under MIT and a OneK1K-trained model exists; the README points to a separate repository of notebooks that reproduce the paper's results (GV26). | 代码可在 MIT 许可下复用，并且存在在 OneK1K 上训练的模型；README 指向一个单独的笔记本仓库，用于复现论文结果（GV26）。 |
| GV28 | T1 | [CRISPR-Cas9–mediated saturated mutagenesis screen predicts clinical drug resistance with improved accuracy](<https://www.pnas.org/doi/10.1073/pnas.1708268114>) | A class-1 variant's drug effect must be modelled with its drug-free fitness; FoldX stability scores predicted clinical prevalence poorly (R² < 0.2), so functional maps are the better supervision. | 类别 1 变异的药物效应必须与其无药适应度联合建模；FoldX 稳定性评分对临床流行度的预测很差（R² < 0.2），因此功能图谱是更好的监督来源。 |
| GV29 | T1 | [A combined computational and experimental strategy identifies mutations conferring resistance to drugs targeting the BCR-ABL fusion protein](<https://www.nature.com/articles/s42003-019-0743-5>) | Affinity change alone does not mark clinical resistance; IC50 shift and preserved catalytic activity do, as GV28 also found with growth data, so supervise variant features with functional readouts. | 单靠亲和力变化无法标示临床耐药；IC50 位移和保留的催化活性才可以，GV28 用生长数据也得出同样结论，因此应以功能读出来监督变异特征。 |
| GV30 | T1 | [Dual functional genomics reveals a broad and convergent landscape of asciminib resistance in BCR::ABL1](<https://link.springer.com/article/10.1186/s13073-026-01679-x>) | Variant-by-background epistasis under a drug is rare (two guides), supporting a sparse interaction term; resistance also arises outside the kinase domain; the readout is growth, not transcription. | 药物下的变异×背景上位性罕见（两个引导），支持稀疏的交互项；耐药也可出现在激酶结构域之外；读出是生长而非转录。 |
| GV31 | T2 | [Discovery of target genes and pathways at GWAS loci by pooled single-cell CRISPR screens](<https://www.science.org/doi/10.1126/science.adh7699>) | Maps non-coding variants to cis target genes and trans networks at single-cell resolution, the middle layer a drug-response model would otherwise treat as a black box. | 把非编码变异映射到 cis 靶基因和 trans 网络（单细胞分辨率），这是药物响应模型原本会当作黑箱的中间层。 |
| GV32 | T1 | [Deep Mutational Scanning Reveals EGFR Mutations Conferring Resistance to the 4th-generation EGFR tyrosine kinase inhibitor BLU-945](<https://doi.org/10.1101/2025.03.31.646429>) | Drug-by-variant resistance map for a class-1 target; single-agent profiles predicted combination escape. Allelic context was L858R only, so labels may not transfer to other EGFR alleles. | 针对第 1 类靶点的药物×变异耐药图谱；单药谱预测了联合用药的逃逸。等位背景仅为 L858R，因此标签未必能迁移到其他 EGFR 等位基因。 |
| GV33 | T1 | [Saturation mutagenesis identifies activating and resistance-inducing FGFR kinase domain mutations](<https://doi.org/10.1038/s41588-025-02431-8>) | Measured class-1 variant-by-drug labels that matched clinical resistance (28 of 29 cases), plus a caution for GV17: pathogenicity scores did not predict gain of function. | 实测的第 1 类变异×药物标签与临床耐药相符（29 例中 28 例），并对 GV17 提出警示：致病性评分未能预测功能获得。 |
<!-- source-index:GV:end -->

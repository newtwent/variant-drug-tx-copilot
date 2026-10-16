# 08 Design implications / 设计启示

## 1. Scope / 范围

This document turns the evidence in documents 01 to 07 into design proposals. Everything here is a proposal or a hypothesis to be tested, not a finding. It gives principles drawn from the evidence, three falsifiable hypotheses with minimal experiments and one optional decision-centric hypothesis, five candidate architectures, a data plan for each track, milestones with decision gates, and kill criteria. It deliberately puts the hypotheses before the architectures.

> 本文档把文档 01 至 07 中的证据转化为设计提案。这里的一切都是待检验的提案或假设，不是发现。它给出从证据得出的原则、三个带最小实验的可证伪假设和一个可选的以决策为中心的假设、五种候选架构、每条轨道的数据计划、带决策门的里程碑以及终止标准。它有意把假设放在架构之前。

## 2. Design principles drawn from the evidence / 从证据得出的设计原则

P1. Target the interaction, not the main effect. The drug main effect is expected to dominate (J5), so every model must be judged on the difference-in-differences between genotypes [EV01, EV02, EV15].

> P1. 以交互项为目标，而不是主效应。预计药物主效应占主导（J5），因此每个模型都必须按基因型之间的双重差分来评判 [EV01, EV02, EV15]。

P2. Start from the somatic track. It has larger effects, complete annotation and abundant data (J2, J12), whereas the germline track rests on small public datasets (J1) [DS05, GD06].

> P2. 从体细胞轨道开始。它的效应更大、注释完整、数据丰富（J2、J12），而种系轨道依赖小型公开数据集（J1）[DS05, GD06]。

P3. Test mediation before modeling variants. If baseline expression already carries the genotype effect (J3), explicit variant modeling adds little [EV16].

> P3. 在对变异建模之前先检验中介。如果基线表达已经承载了基因型效应（J3），显式的变异建模增益很小 [EV16]。

P4. Keep priors weak and swappable. Sequence-model scores and network priors are priors, and each must be evaluated by ablation (J7, J10) [GV05, EV16].

> P4. 让先验保持弱且可替换。序列模型分数和网络先验都只是先验，每一个都必须通过消融来评估（J7、J10）[GV05, EV16]。

P5. Separate pharmacokinetics from pharmacodynamics and track ancestry (J8, J9) [GD01, EV23].

> P5. 区分药代动力学与药效动力学，并追踪祖源（J8、J9）[GD01, EV23]。

P6. Make the world-model claim falsifiable. A world model has to pass multi-step, composition, counterfactual and state-update tests, and several of them may be infeasible with current data (J6) [WM17, WM21].

> P6. 让世界模型的主张可证伪。世界模型必须通过多步、组合、反事实和状态更新检验，而其中若干项在现有数据下可能无法进行（J6）[WM17, WM21]。

P7. Keep the model modular and test decisions, not only predictions. LabCompass separates a forward generative model, a prior over actions and a guided inverse-design step, so that a new objective needs no retraining [WM28, WM29, WM32]. A genotype-aware model should expose the same seams, and its decisions should be tested in a retrospective closed loop [MD48, MD49].

> P7. 保持模型模块化，并检验决策而不只检验预测。LabCompass 把前向生成模型、动作先验和引导式逆向设计步骤分开，因此新的目标无需重新训练 [WM28, WM29, WM32]。基因型感知模型应当提供同样的接口，其决策应在回溯式闭环中检验 [MD48, MD49]。

## 3. Three falsifiable hypotheses and one optional extension / 三个可证伪假设和一个可选扩展

### 3.1 HA: mediation / HA：中介

HA statement. After conditioning on the baseline (control) expression of the same cell population, adding mutation or genotype features does not improve the prediction of the drug-induced expression change on interaction-specific metrics.

> HA 陈述。在条件于同一细胞群体的基线（对照）表达之后，加入突变或基因型特征，并不能在交互项专用指标上改善对药物诱导表达变化的预测。

HA relevance. If HA holds, explicit variant modeling in the somatic track is not worth its cost, and the project should pivot to models conditioned on baseline state. If HA is rejected, there is room for variant-aware models.

> HA 的意义。如果 HA 成立，体细胞轨道中的显式变异建模就不值得其成本，项目应转向以基线状态为条件的模型。如果 HA 被拒绝，则变异感知模型有空间。

HA minimal experiment. In the somatic track, choose driver mutations carried by enough cell lines in the Tahoe-100M panel, with the threshold set after counting (document 03). For each drug, fit (a) the mean response, (b) a drug-wise linear model on the control expression profile, and (c) the same linear model plus mutation indicators, and evaluate all three on held-out lines matched by lineage.

> HA 最小实验。在体细胞轨道中，选择在 Tahoe-100M 面板里有足够多细胞系携带的驱动突变，阈值在统计之后确定（文档 03）。对每种药物拟合 (a) 均值响应，(b) 基于对照表达谱的逐药物线性模型，(c) 在同一线性模型上加入突变指示变量，并在按谱系匹配的留出细胞系上评估这三者。

HA metrics and decision rule. Use difference-in-differences on differentially expressed genes between mutant and wild-type test lines, rank-based metrics and the E-distance, together with a genotype-permutation control and a benign-variant control (document 07). HA is rejected if (c) beats (b) on the interaction metric across held-out lines and the permutation control gives no gain. HA is supported if (c) does not beat (b) and power is adequate (J16). Otherwise the result is inconclusive.

> HA 的指标与判定规则。使用突变株与野生株测试细胞系之间差异表达基因上的双重差分、基于排名的指标和 E-distance，并配合基因型置换对照和良性变异对照（文档 07）。如果 (c) 在留出细胞系的交互指标上优于 (b)，且置换对照没有增益，则 HA 被拒绝。如果 (c) 没有优于 (b) 且效能充足（J16），则 HA 得到支持。否则结果不确定。

HA risks. Mutation is confounded with lineage, and mutant lines may be few. Control expression may itself encode the mutation, which is exactly the mediation that HA tests, so any interpretation must say so explicitly.

> HA 的风险。突变与谱系混杂，且突变株可能很少。对照表达本身可能编码了突变，这恰恰是 HA 所检验的中介，因此任何解释都必须明确说明这一点。

HA by variant class. Report the genotype gain separately for expression-level variants (class 2), coding or binding variants (class 1) and pathway variants (class 4) instead of one pooled number. Mediation through the baseline state is plausible for class 2, because response eQTLs are regulatory and cell-type specific [GD10, GD49] and a sequence model could in principle shift the baseline [GV26]. It is implausible for classes 1 and 4, where the operator itself changes: TP53 status switches a drug-induced programme off [GD45], and BCR-ABL1 resistance depends on the variant's drug-free fitness, on background and on sites outside the kinase domain, which binding constants alone do not capture [GV28, GV29, GV30]. Rare pre-existing resistant cell states show that baseline heterogeneity matters even within one genotype [GD51], so the target should be a distribution of cell states.

> 按变异类别的 HA。分别报告表达水平变异（类别 2）、编码或结合变异（类别 1）和通路变异（类别 4）的基因型增益，而不是给出一个合并的数字。经由基线状态的中介对类别 2 是合理的，因为响应 eQTL 是调控性的、具细胞类型特异性 [GD10, GD49]，序列模型原则上也可以改变基线 [GV26]。对类别 1 和 4 则不合理，因为算子本身发生了变化：TP53 状态会把药物诱导的程序关闭 [GD45]，而 BCR-ABL1 的耐药取决于变异在无药时的适应度、背景以及激酶结构域之外的位点，仅凭结合常数无法捕获 [GV28, GV29, GV30]。稀有的预先存在的耐药细胞状态表明，即使在同一基因型内，基线异质性也很重要 [GD51]，所以目标应当是细胞状态的分布。

HA ablation with a genotype-matched source. Add genotype as one more covariate group in the condition encoder and keep the source population genotype-matched, as the CellFlow donor tutorial does for donors [MD61, MD63]. Then remove the genotype covariate while keeping the matched source and check whether the interaction metric changes; this separates information carried by the source cells from information carried by the covariate [WM28].

> 带基因型匹配源的 HA 消融。把基因型作为条件编码器中的又一个协变量组，并保持源群体与基因型匹配，就像 CellFlow 的供体教程对供体所做的那样 [MD61, MD63]。然后在保持匹配源的同时去掉基因型协变量，检查交互指标是否变化；这把源细胞所携带的信息与协变量所携带的信息区分开 [WM28]。

### 3.2 HB: sparse shift / HB：稀疏偏移

HB statement. For a given driver mutation, the difference between mutant and reference responses to the same drug is low-rank or sparse, meaning that a few latent directions or network edges carry most of it.

> HB 陈述。对于给定的驱动突变，在同一药物下突变株与参考株的响应差异是低秩或稀疏的，即少数潜在方向或网络边承载了其中的大部分。

HB relevance. If HB holds, variants can be modeled as small edits to the response operator, which gives interpretability and data efficiency. If HB fails, a sparse-shift parameterization is the wrong inductive bias.

> HB 的意义。如果 HB 成立，变异可以被建模为对响应算子的小幅编辑，这带来可解释性和数据效率。如果 HB 不成立，稀疏偏移的参数化就是错误的归纳偏置。

HB minimal experiment. From the matrices of differences of differences (drugs by genes) for each mutation, compute the singular-value spectrum and the sparsity. Then compare, at equal parameter count, models with a sparse variant-specific shift against models with a dense one, on held-out drugs.

> HB 最小实验。对每个突变，由差值的差值矩阵（药物×基因）计算奇异值谱和稀疏度。然后在参数量相等的条件下，在留出药物上比较带稀疏的变异特异偏移的模型与带稠密偏移的模型。

HB decision rule and risks. HB is rejected if the spectrum is flat and a dense parameterization beats the sparse one at equal capacity. HB is supported if the spectrum decays quickly and the sparse form matches or beats the dense one. Noise inflates apparent rank, and small effect sizes erase the benefit of sparsity [MD17].

> HB 的判定规则与风险。如果谱是平的，且稠密参数化在容量相等时优于稀疏参数化，则 HB 被拒绝。如果谱衰减很快，且稀疏形式与稠密形式相当或更好，则 HB 得到支持。噪声会抬高表观秩，而较小的效应大小会抹去稀疏性的收益 [MD17]。

HB prior evidence (confidence: low-medium). Several independent anchors point to sparse genotype-specific effects: about 1% of allelic variants in a reporter assay interact with a drug (6 of 665 at a false discovery rate below 5%; the first version of the paper reported 29 variants at a looser threshold) [GD50], 21% of subsystems carry about 80% of the importance in a yeast genotype model [MD54], perturbation-specific signal is sparse relative to invariant structure in expression data [MD22], and in TP53-mutant lines a programme is switched off rather than rewritten [GD45]. None of these is a transcriptome-wide drug-response test, so HB remains untested.

> HB 的先验证据（置信度：低中）。若干独立的锚点都指向稀疏的基因型特异效应：在报告基因实验中约 1% 的等位基因变异与药物发生交互（FDR 低于 5% 时 665 个中的 6 个；论文第一版在较宽松的阈值下报告了 29 个变异）[GD50]，在酵母基因型模型中 21% 的子系统承载约 80% 的重要性 [MD54]，在表达数据中相对不变结构而言扰动特异信号是稀疏的 [MD22]，在 TP53 突变系中是一个程序被关闭而不是被重写 [GD45]。这些都不是全转录组的药物响应检验，因此 HB 仍未经检验。

### 3.3 HC: world-model gain / HC：世界模型增益

HC statement. An action-conditioned latent transition model with an explicit state beats capacity-matched mean, linear and one-step conditional baselines on the feasible tests of the battery in document 06: multi-step dose rollouts, held-out drug combinations and counterfactual variant swaps.

> HC 陈述。带显式状态的动作条件潜在转移模型，在文档 06 检验清单中可行的检验上击败容量匹配的均值、线性和单步条件基线：多步剂量展开、留出的药物组合和反事实的变异互换。

HC relevance. This is the claim that motivates the architecture. If the baselines match the model on every feasible test, the world-model label adds nothing for this problem.

> HC 的意义。这是促成该架构的主张。如果基线在每一项可行检验上都与该模型相当，那么对这个问题而言，世界模型的标签没有增加任何东西。

HC minimal experiment. Train on single-drug dose series from Tahoe-100M, and test rollouts from low to high dose against held-out measurements. Test the counterfactual swap on lineage-matched mutant and wild-type pairs. Test combinations only if combination data are found, and none have been retrieved so far.

> HC 最小实验。在 Tahoe-100M 的单药剂量系列上训练，并把从低剂量到高剂量的展开与留出的测量进行比较。在谱系匹配的突变株与野生株配对上检验反事实互换。只有在找到组合数据时才检验药物组合，而目前尚未检索到任何组合数据。

HC decision rule and risks. HC is rejected if the baselines are within the uncertainty of the world model on all feasible tests. If only the rollout test is feasible, the conclusion is limited to dose dynamics. The counterfactual swap is weakly identified, and a dose series is not a time course.

> HC 的判定规则与风险。如果在所有可行检验上，基线都落在世界模型的不确定范围之内，则 HC 被拒绝。如果只有展开检验可行，结论就仅限于剂量动力学。反事实互换的可识别性弱，而且剂量系列不是时间进程。

HC additions. State-update dynamics cannot be identified from snapshots alone, and metabolic-labeling methods that separate new from old RNA are the only route found to time-resolved targets [DS21, DS22]. Cell-number changes are part of the phenotype and should be predicted together with the state [MD38]. Candidate transition cores are the unbalanced and trajectory-aware models of documents 05 and 06 [MD38, WM33, WM36, WM37]; a retrospective closed-loop test, described under HD, is added to the battery as a decision-level check.

> HC 的补充。状态更新动力学不能仅凭快照识别，而分离新旧 RNA 的代谢标记方法是找到的通往时间分辨目标的唯一途径 [DS21, DS22]。细胞数量变化是表型的一部分，应与状态一起预测 [MD38]。候选的转移核心是文档 05 和 06 中的非平衡和轨迹感知模型 [MD38, WM33, WM36, WM37]；回溯式闭环检验（见 HD）作为决策层面的检查加入检验清单。

### 3.4 HD: decision quality (optional) / HD：决策质量（可选）

HD statement. A planner that samples candidate drugs, doses or combinations from a learned action prior and guides them by the gradient of an objective through a genotype-aware forward model reaches better decisions than random and greedy selection in a retrospective closed loop on held-out conditions.

> HD 陈述。从学得的动作先验中采样候选药物、剂量或组合，并通过基因型感知前向模型沿目标的梯度加以引导的规划器，在留出条件上的回溯式闭环中，比随机选择和贪心选择做出更好的决策。

HD relevance. This is the decision-centric claim suggested by LabCompass [WM27, WM28]. It matters only if the end use is choosing a drug and dose for a genotype; if the end use is prediction, HD can be skipped. It should run last, because it needs a genotype-aware forward model that has already passed the HA and HB tests.

> HD 的意义。这是 LabCompass 所提示的以决策为中心的主张 [WM27, WM28]。只有当最终用途是为某个基因型选择药物和剂量时它才有意义；如果最终用途是预测，可以跳过 HD。它应当最后运行，因为它需要一个已经通过 HA 和 HB 检验的基因型感知前向模型。

HD minimal experiment. Build a retrospective loop on the dose-resolved screens in Tahoe-100M or sci-Plex [DS05, DS15]: reveal conditions in rounds, retrain after each round, and score how quickly each planner reaches conditions that satisfy a stated objective, with random, greedy and acquisition-function planners as baselines [MD48, MD49]. Use two objectives with the same forward model: resistance reversal, which moves the predicted response of a mutant context toward the wild-type response, and selective killing, which maximizes the effect in mutant contexts under a cap on the effect in wild-type contexts [WM28].

> HD 最小实验。在 Tahoe-100M 或 sci-Plex 的剂量分辨筛选上构建回溯式循环 [DS05, DS15]：分轮揭示条件，每轮之后重新训练，并评估各规划器多快能到达满足既定目标的条件，以随机、贪心和采集函数规划器为基线 [MD48, MD49]。用同一个前向模型设置两个目标：耐药逆转，即把突变背景的预测响应移向野生型响应；以及选择性杀伤，即在对野生型背景效应设置上限的条件下，最大化突变背景中的效应 [WM28]。

HD decision rule and risks. HD is rejected if guided sampling does not beat greedy selection by more than the round-to-round variation. The risks are planning on a confidently wrong model, which needs uncertainty-aware scoring through ensembles or conformal calibration; a many-to-one mapping from designs to states, which the action prior must handle [WM27]; objectives that depend on readouts the model does not predict faithfully [EV33]; and the absence of a wet-lab loop, so the test stays retrospective.

> HD 的判定规则与风险。如果引导采样没有以超过轮间变异的幅度优于贪心选择，则 HD 被拒绝。风险包括：在自信但错误的模型上做规划，这需要通过集成或共形校准做感知不确定性的打分；从设计到状态的多对一映射，动作先验必须能处理它 [WM27]；依赖模型预测不忠实的读出的目标 [EV33]；以及缺少湿实验闭环，因此检验只能是回溯式的。

## 4. Candidate architectures / 候选架构

| Architecture | How the variant enters | Hypothesis tested | Main risk | 说明（中文） |
|---|---|---|---|---|
| A. Baseline ladder: mean, drug-wise linear on control expression, one-step conditional generative model (CellFlow- or State-like) | Mutation indicators added to the linear and conditional models | HA | Strong baselines may already match everything | A. 基线阶梯：均值、基于对照表达的逐药物线性模型、单步条件生成模型（类 CellFlow 或 State）；变异以突变指示变量加入线性和条件模型；检验 HA；风险是强基线可能已经与一切相当 |
| B. Conditional model with explicit variant features | Mutation vector, with optional ESM1b, AlphaMissense or Boltz-2 scores as self-reported priors | HA, HB | Confounding with lineage | B. 带显式变异特征的条件模型；变异以突变向量加入，可选用 ESM1b、AlphaMissense 或 Boltz-2 分数作为自报的先验；检验 HA、HB；风险是与谱系混杂 |
| C. Mechanism-informed network (LEMBAS-style) | Variants modify nodes or edges of the prior signaling graph; the drug enters as target inhibition | HB | Errors in the prior network; sparse edits may be wrong | C. 机制导向网络（LEMBAS 式）；变异修改先验信号图的节点或边，药物以靶点抑制的形式输入；检验 HB；风险是先验网络有误、稀疏编辑可能不对 |
| D. Action-conditioned latent transition model (world-model design) | Variant conditions or modifies the transition operator F(z, a) | HC | Tests may be infeasible; decoder-free objectives may under-represent effect sizes | D. 动作条件的潜在转移模型（世界模型设计）；变异为转移算子 F(z, a) 提供条件或对其修改；检验 HC；风险是检验可能无法进行、无解码器的目标可能低估效应大小 |
| E. Forward generative model, action prior and guided inverse design (LabCompass-style) | Genotype is a covariate group of the forward model and enters the objective; guidance follows the gradient of the objective through the forward model, with KKT constraints for caps and bounds | HD, and HA through the genotype ablation | Planning on a wrong model; evidence only at protein level and from one cell system; package at version 0.0.1 | E. 前向生成模型、动作先验和引导式逆向设计（LabCompass 式）；基因型是前向模型的协变量组并进入目标；引导沿着目标穿过前向模型的梯度进行，并用 KKT 约束表示上限和界限；检验 HD，并通过基因型消融检验 HA；风险是在错误的模型上做规划、证据只有蛋白水平且来自一个细胞系统、软件包为 0.0.1 版本 |

Architectures D and E are complementary rather than competing: D supplies the transition core that predicts how a state evolves under an action, and E supplies the planner that chooses actions. A complete cell world model would combine them, whereas LabCompass itself covers only the decision half [WM27, WM28].

> 架构 D 和 E 是互补而不是竞争关系：D 提供预测状态在动作下如何演化的转移核心，E 提供选择动作的规划器。完整的细胞世界模型应当把两者结合起来，而 LabCompass 本身只覆盖决策这一半 [WM27, WM28]。

## 5. Data plan by track / 按轨道的数据计划

Somatic track. Use Tahoe-100M as the backbone and LINCS L1000 for breadth, join both to cell-line mutation annotation through a stable cell-line identifier, and use OmniPath and SIGNOR for prior networks [DS05, DS01, KB01, KB04]. The first task is to count, per driver mutation and lineage, how many mutant and wild-type lines the panel contains, and to define the lineage-matched contrasts.

> 体细胞轨道。以 Tahoe-100M 为骨干，以 LINCS L1000 提供广度，通过稳定的细胞系标识符把两者与细胞系突变注释连接，并用 OmniPath 和 SIGNOR 构建先验网络 [DS05, DS01, KB01, KB04]。第一项任务是按驱动突变和谱系统计面板中有多少突变株和野生株，并定义按谱系匹配的对比。

Germline track. Use published response-QTL data as positive controls and external validation, Geuvadis and GTEx as sources of baseline genotype–expression relations, and sequence-model scores only as weak priors [GD06, DS13, GV05, EV25]. No deep genotype model is planned for this track unless larger datasets with genotype, drug and transcriptome are found, and every evaluation is stratified by ancestry [EV23].

> 种系轨道。把已发表的响应 QTL 数据用作阳性对照和外部验证，把 Geuvadis 和 GTEx 用作基线基因型-表达关系的来源，并且只把序列模型分数用作弱先验 [GD06, DS13, GV05, EV25]。除非找到同时含基因型、药物和转录组的更大数据集，否则不为该轨道规划深度基因型模型，且每项评测都按祖源分层 [EV23]。

Before use, verify the access routes, licenses and schemas of every dataset, because none has been inspected [DS07, DS13].

> 使用之前，要核查每个数据集的获取途径、许可和模式，因为没有一个被检查过 [DS07, DS13]。

Germline-like evaluation data. For the mediation ablation, the closest available data with inherited genotype are the response-eQTL cultures from 51 individuals [GD10], the influenza-exposed PBMCs from 90 individuals [GD49] and the village design for pooled donors [GD47]. Larger donor-by-perturbation grids exist (12 donors with 90 cytokines [DS16], 40 donors with 11 cytokines [MD42]), but the retrieved text does not say whether their donors are genotyped, which has to be checked before they are used for genotype questions.

> 类种系的评测数据。对中介消融而言，最接近的带遗传性基因型的现有数据是来自 51 个个体的响应 eQTL 培养 [GD10]、来自 90 个个体的流感暴露 PBMC [GD49]，以及混池供体的村落设计 [GD47]。也存在更大的供体×扰动网格（12 名供体、90 种细胞因子 [DS16]；40 名供体、11 种细胞因子 [MD42]），但检索到的文字没有说明其供体是否做了基因分型，在把它们用于基因型问题之前必须核查。

Somatic label sources. Variant-by-drug labels beyond Tahoe-100M come from saturation, base-editing and deep-mutational maps of BCR-ABL1 [GV28, GV29, GV30], an isogenic panel of 51 lines with 90 compounds [GD46], a CRISPR-drug map of 18 cell lines and 8 drugs [GD53] and genotype-demultiplexed pooled lines [GD45]; only the pooled single-cell design has a transcriptomic readout.

> 体细胞的标签来源。Tahoe-100M 之外的变异×药物标签来自 BCR-ABL1 的饱和突变、碱基编辑和深度突变图谱 [GV28, GV29, GV30]、含 51 个细胞系和 90 种化合物的同基因面板 [GD46]、涵盖 18 个细胞系和 8 种药物的 CRISPR–药物图谱 [GD53]，以及按基因型解复用的混池细胞系 [GD45]；只有混池的单细胞设计具有转录组读出。

Decision-test data. The retrospective loop of HD can run on the dose-resolved single-cell screens in sci-Plex and Tahoe-100M [DS15, DS05]. LabCompass publishes closed-loop data only at the protein level [DS23], so no transcriptome-level closed-loop data are available and the test must stay retrospective.

> 决策检验的数据。HD 的回溯式循环可以在 sci-Plex 和 Tahoe-100M 的剂量分辨单细胞筛选上运行 [DS15, DS05]。LabCompass 只在蛋白水平公布闭环数据 [DS23]，因此没有转录组层面的闭环数据，检验只能是回溯式的。

## 6. Milestones and decision gates / 里程碑与决策门

M0, verification. Open outbound network access (bioRxiv, PubMed and the plugin servers that currently fail to connect) and verify the load-bearing claims by reading the primary sources: the response-eQTL counts [GD10], the reporter-assay ratio of 6 of 665 [GD50], the Systema reference shift [EV29], and the LabCompass full text with its baselines, ablations, uncertainty handling and viral-infection analysis [WM27]. Spot checks by search (Q126 to Q132) have already reconfirmed the 51 individuals of [GD10], the 6 of 665 variants at a false discovery rate below 5% for the published version of [GD50] and, through the authors' repository, the perturbed-centroid reference of [EV29] [EV36]; the per-cell-type response-eQTL counts remain unconfirmed. Run the unit tests of the labcompass package [WM28], then update tiers and the verified flag. No other milestone should rely on a claim that is still unverified.

> M0，核验。开放出站网络访问（bioRxiv、PubMed 以及目前连接失败的插件服务器），通过阅读原始来源核验承重主张：响应 eQTL 的计数 [GD10]、报告基因实验的比例 665 个中的 6 个 [GD50]、Systema 的参照重设 [EV29]，以及 LabCompass 全文及其基线、消融、不确定性处理和病毒感染分析 [WM27]。通过检索进行的抽查（Q126 至 Q132）已经再次确认了 [GD10] 的 51 名个体、[GD50] 已发表版本在 FDR 低于 5% 时 665 个变异中的 6 个，以及（通过作者的仓库）[EV29] 的扰动后质心参照 [EV36]；每种细胞类型的响应 eQTL 计数仍未确认。运行 labcompass 软件包的单元测试 [WM28]，然后更新等级和 verified 标记。其他里程碑都不应依赖仍未核验的主张。

M1, data assembly. Check access and licenses, count mutant and wild-type lines per driver mutation and lineage, and define the contrasts and the minimum number of lines per contrast from a power calculation.

> M1，数据整理。核查获取方式和许可，按驱动突变和谱系统计突变株与野生株的数量，并根据效能计算确定对比以及每个对比所需的最少细胞系数。

M2, harness. Build the evaluation harness and the baseline ladder, and confirm that the controls behave as expected: the genotype-permutation control must produce no gain. Include splits for unseen context, unseen perturbation, unseen dataset and unseen genotype [EV35], and decide at this point whether the labcompass package serves as a baseline implementation [WM28].

> M2，评测框架。构建评测框架和基线阶梯，并确认对照表现符合预期：基因型置换对照必须不产生增益。加入对未见背景、未见扰动、未见数据集和未见基因型的划分 [EV35]，并在此时决定 labcompass 软件包是否作为基线实现 [WM28]。

M3, test HA. Gate: if HA is supported, stop explicit variant modeling in the somatic track and pivot to models conditioned on baseline state; if HA is rejected, continue to M4.

> M3，检验 HA。决策门：如果 HA 得到支持，就停止体细胞轨道中的显式变异建模，转向以基线状态为条件的模型；如果 HA 被拒绝，则继续到 M4。

M4, test HB. Gate: the result decides between sparse and dense variant parameterizations.

> M4，检验 HB。决策门：结果决定采用稀疏还是稠密的变异参数化。

M5, test HC. Run it only if M3 and M4 justify a dynamic model and at least one feasible test exists.

> M5，检验 HC。只有当 M3 和 M4 证明动态模型有必要，且至少存在一项可行检验时才运行。

M6, test HD (optional). Run it only if the end use is decision-making and M3 and M4 have produced a genotype-aware forward model that passes them. Gate: guided sampling must beat greedy selection in the retrospective loop; otherwise report prediction results only.

> M6，检验 HD（可选）。只有当最终用途是决策、且 M3 和 M4 已经产生通过检验的基因型感知前向模型时才运行。决策门：引导采样必须在回溯式循环中优于贪心选择；否则只报告预测结果。

## 7. Risks and kill criteria / 风险与终止标准

The main risks are low statistical power in a 50-line panel (J16), confounding of mutation with lineage, self-reported results that do not replicate, and the possible infeasibility of the combination and time tests. Mitigations are lineage-matched contrasts, per-contrast power calculations in M1, the verification in M0, and an explicit record of which tests the data can support.

> 主要风险是 50 个细胞系的面板中统计效能低（J16）、突变与谱系混杂、自报结果无法复现，以及组合检验和时间检验可能无法进行。缓解措施是谱系匹配的对比、M1 中逐对比的效能计算、M0 中的核验，以及对数据能支持哪些检验的明确记录。

A further risk is that planning amplifies model errors, because the guidance step follows gradients of an objective through the forward model and can exploit regions where the model is confidently wrong [WM28]. Mitigations are uncertainty-aware scoring, constraints that keep samples near the action prior, and retrospective checks on held-out conditions.

> 另一项风险是规划会放大模型误差，因为引导步骤沿着目标穿过前向模型的梯度前进，可能利用模型自信出错的区域 [WM28]。缓解措施是感知不确定性的打分、让样本保持在动作先验附近的约束，以及在留出条件上的回溯式检查。

Kill criterion. If, after M3 and M4, HA is supported and HB is not, stop the variant-aware modeling in the somatic track and report the negative result; the evidence base in this repository remains useful on its own.

> 终止标准。如果在 M3 和 M4 之后，HA 得到支持而 HB 不成立，就停止体细胞轨道中的变异感知建模并报告阴性结果；本仓库中的证据库本身仍然有用。

## 8. Questions for confirmation / 待确认问题

Is the order HA, HB, HC acceptable, with the world-model test last? Default: yes.

> 按 HA、HB、HC 的顺序、把世界模型检验放在最后，是否可以接受？默认：可以。

Is a negative result on HA an acceptable outcome of the project? Default: yes, because it would redirect the architecture toward baseline-conditioned models rather than waste effort on variant modeling.

> 在 HA 上得到阴性结果，是否是本项目可接受的结果？默认：可以，因为这会把架构引向以基线为条件的模型，而不是把精力浪费在变异建模上。

Is the end use prediction or decision? Default: treat decision (HD) as an optional last step, and ask again after M3 and M4.

> 最终用途是预测还是决策？默认：把决策（HD）当作可选的最后一步，并在 M3 和 M4 之后再次询问。

Which variant class should be modeled first? Default: class 1 somatic variants with large effects, for example TP53 status, because the operator change is visible there [GD45].

> 应先对哪一类变异建模？默认：效应大的类别 1 体细胞变异，例如 TP53 状态，因为那里算子的变化清晰可见 [GD45]。

## 9. Evidence gaps / 证据缺口

The number of mutant lines per driver mutation in the Tahoe-100M panel is unknown, as are its dose grid and time points (Q11, Q77). No combination data were found (Q67). The mapping between cell-line annotation sources has not been examined. All source claims are tier T2 or T3, so every design choice that rests on one is provisional until M0.

> Tahoe-100M 面板中每个驱动突变的突变株数量未知，其剂量网格和时间点也未知（Q11、Q77）。没有找到组合数据（Q67）。细胞系注释来源之间的映射尚未检查。所有来源论断都是 T2 或 T3 级，因此凡建立在其上的设计选择，在 M0 之前都是暂定的。

Whether the donors of the large cytokine datasets are genotyped is not stated [DS16, MD42]. The LabCompass full text, its baselines and its viral-infection analysis were not read [WM27], and no transcriptome-level closed-loop design data exist [DS23].

> 大型细胞因子数据集的供体是否做了基因分型，没有说明 [DS16, MD42]。LabCompass 的全文、基线和病毒感染分析没有读到 [WM27]，并且不存在转录组层面的闭环设计数据 [DS23]。

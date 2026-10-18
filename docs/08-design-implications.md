# 08 Design implications / 设计启示

## 1. Scope / 范围

This document turns the evidence of documents 01 to 07 into design proposals; everything here is a hypothesis or a proposal to be tested, not a finding. The hypotheses come before the architectures on purpose.

> 本文档把文档 01 至 07 中的证据转化为设计提案；这里的一切都是待检验的假设或提案，不是发现。有意把假设放在架构之前。

## 2. Design principles drawn from the evidence / 从证据得出的设计原则

P1. Target the interaction, not the main effect. The drug main effect is expected to dominate (J5), so every model must be judged on the difference-in-differences between genotypes [EV01, EV02, EV15].

> P1. 以交互项为目标，而不是主效应。预计药物主效应占主导（J5），因此每个模型都必须按基因型之间的双重差分来评判 [EV01, EV02, EV15]。

P2. Start from the somatic track, which has larger effects, complete annotation and abundant data (J2, J12), whereas the germline track rests on small public datasets (J1) [DS07, GD06].

> P2. 从体细胞轨道开始：它的效应更大、注释完整、数据丰富（J2、J12），而种系轨道依赖小型公开数据集（J1）[DS07, GD06]。

P3. Test mediation before modeling variants: if baseline expression already carries the genotype effect (J3), explicit variant modeling adds little [EV16].

> P3. 在对变异建模之前先检验中介：如果基线表达已经承载了基因型效应（J3），显式的变异建模增益很小 [EV16]。

P4. Keep priors weak and swappable: sequence-model scores and network priors are priors, and each must be evaluated by ablation (J7, J10) [GV05, EV16].

> P4. 让先验保持弱且可替换：序列模型分数和网络先验都只是先验，每一个都必须通过消融来评估（J7、J10）[GV05, EV16]。

P5. Separate pharmacokinetics from pharmacodynamics and track ancestry (J8, J9) [GD01, EV23].

> P5. 区分药代动力学与药效动力学，并追踪祖源（J8、J9）[GD01, EV23]。

P6. Make the world-model claim falsifiable: a world model has to pass multi-step, composition, counterfactual and state-update tests, and several of them may be infeasible with current data (J6) [WM17, WM21].

> P6. 让世界模型的主张可证伪：世界模型必须通过多步、组合、反事实和状态更新检验，而其中若干项在现有数据下可能无法进行（J6）[WM17, WM21]。

P7. Keep the model modular and test decisions, not only predictions: a forward generative model, a prior over actions and guided inverse design, as in LabCompass [WM28, WM29], tested in a retrospective closed loop [MD48, MD49].

> P7. 保持模型模块化，并检验决策而不只检验预测：前向生成模型、动作先验和引导式逆向设计，如 LabCompass [WM28, WM29]，并在回溯式闭环中检验 [MD48, MD49]。

## 3. Three falsifiable hypotheses and one optional extension / 三个可证伪假设和一个可选扩展

### 3.1 HA: mediation / HA：中介

HA statement. After conditioning on the baseline (control) expression of the same cell population, adding mutation or genotype features does not improve prediction of the drug-induced expression change on interaction-specific metrics. If HA holds, the project pivots to baseline-conditioned models; if it is rejected, variant-aware models have room.

> HA 陈述。在条件于同一细胞群体的基线（对照）表达之后，加入突变或基因型特征，并不能在交互项专用指标上改善对药物诱导表达变化的预测。如果 HA 成立，项目转向以基线状态为条件的模型；如果 HA 被拒绝，则变异感知模型有空间。

HA minimal experiment. In the Tahoe-100M panel TP53 is annotated in 33 of 50 lines, KRAS in 24, CDKN2A in 22 and BRAF in 9, but every line carries at least one annotated driver and, in the 12 lineage-matched mutant-versus-other contrasts computed, the smaller arm holds 1 to 6 lines (TP53 in lung: 12 versus 3; derived, Q137) [DS07]. For each drug, fit (a) the mean response, (b) a drug-wise linear model on the control expression profile and (c) the same model plus mutation indicators, and evaluate all three on held-out lines matched by lineage. As an ablation, add genotype as one covariate group beside a genotype-matched source population and then remove only the covariate (document 09, I4) [MD61, WM28].

> HA 最小实验。在 Tahoe-100M 面板中，50 个系里 TP53 有 33 个被注释，KRAS 有 24 个，CDKN2A 有 22 个，BRAF 有 9 个，但每个系都至少携带一个被注释的驱动突变，并且在已计算的 12 个按谱系匹配的突变株对其他株对比中，较小的一臂只有 1 至 6 个系（肺中 TP53：12 对 3；推导，Q137）[DS07]。对每种药物拟合 (a) 均值响应，(b) 基于对照表达谱的逐药物线性模型，(c) 在同一模型上加入突变指示变量，并在按谱系匹配的留出细胞系上评估这三者。作为消融，把基因型作为一个协变量组放在与基因型匹配的源群体旁边，然后只去掉该协变量（文档 09，I4）[MD61, WM28]。

HA decision rule and risks. Score difference-in-differences on genes that differ between mutant and non-mutant test lines, plus rank-based metrics and the E-distance, with a genotype-permutation control and a benign-variant control (document 07). HA is rejected if (c) beats (b) across held-out lines and the permutation control gives no gain, and supported if (c) does not beat (b) with adequate power (J16). Lineage confounding, small arms and control expression that already encodes the mutation (the mediation HA tests) limit power; engineered isogenic data are a cleaner but growth-only secondary test [GD46, GD54].

> HA 的判定规则与风险。对突变株与非突变株测试细胞系之间有差异的基因计算双重差分，并使用基于排名的指标和 E-distance，配合基因型置换对照和良性变异对照（文档 07）。如果 (c) 在留出细胞系上优于 (b)，且置换对照没有增益，则 HA 被拒绝；如果 (c) 没有优于 (b) 且效能充足（J16），则 HA 得到支持。谱系混杂、各臂很小，以及对照表达本身已经编码了突变（即 HA 所检验的中介），都会限制效能；工程化同基因数据能提供更干净、但只有生长读出的次级检验 [GD46, GD54]。

HA by variant class. Report the genotype gain separately for expression-level (class 2), coding or binding (class 1) and pathway (class 4) variants. Mediation through the baseline is plausible for class 2, where response eQTLs are regulatory and cell-type specific [GD10, GD49]; it is implausible for classes 1 and 4, where the operator itself changes, as when TP53 status switches a drug-induced programme off [GD45] or BCR-ABL1 resistance depends on drug-free fitness, background and sites outside the kinase domain [GV28, GV29, GV30]. Cell states differ even within one genotype [GD51, GD55], so the target is a distribution of cell states.

> 按变异类别的 HA。分别报告表达水平（类别 2）、编码或结合（类别 1）和通路（类别 4）变异的基因型增益。经由基线状态的中介对类别 2 是合理的，因为响应 eQTL 是调控性的、具细胞类型特异性 [GD10, GD49]；对类别 1 和 4 则不合理，因为算子本身发生了变化，例如 TP53 状态把药物诱导的程序关闭 [GD45]，或 BCR-ABL1 的耐药取决于无药时的适应度、背景以及激酶结构域之外的位点 [GV28, GV29, GV30]。即使在同一基因型内，细胞状态也不同 [GD51, GD55]，所以目标是细胞状态的分布。

### 3.2 HB: sparse shift / HB：稀疏偏移

HB statement. For a given driver mutation, the difference between mutant and reference responses to the same drug is low-rank or sparse, so a few latent directions or network edges carry most of it. If HB fails, a sparse-shift parameterization is the wrong inductive bias.

> HB 陈述。对于给定的驱动突变，在同一药物下突变株与参考株的响应差异是低秩或稀疏的，即少数潜在方向或网络边承载了其中的大部分。如果 HB 不成立，稀疏偏移的参数化就是错误的归纳偏置。

HB minimal experiment and decision rule. From the matrices of differences of differences (drugs by genes) for each mutation, compute the singular-value spectrum and the sparsity, then compare, at equal parameter count and on held-out drugs, models with a sparse variant-specific shift against models with a dense one. HB is rejected if the spectrum is flat and the dense form wins, and supported if the spectrum decays quickly and the sparse form matches or wins. Noise inflates apparent rank, and small effect sizes erase the benefit of sparsity [MD17].

> HB 最小实验与判定规则。对每个突变，由差值的差值矩阵（药物×基因）计算奇异值谱和稀疏度，然后在参数量相等、使用留出药物的条件下，比较带稀疏的变异特异偏移的模型与带稠密偏移的模型。如果谱是平的且稠密形式更优，则 HB 被拒绝；如果谱衰减很快且稀疏形式与稠密形式相当或更好，则 HB 得到支持。噪声会抬高表观秩，而较小的效应大小会抹去稀疏性的收益 [MD17]。

HB prior evidence (confidence: low-medium). 6 of 15,927 tested variants showed a conditional allele-specific effect under caffeine at a false discovery rate below 5% in a reporter assay [GD50]; a CRISPR-screen model works best with 85 invariant and 20 responsive latents [MD22]; variant-by-background epistasis under asciminib was rare, with two guides [GV30]; and in TP53-mutant lines a programme is switched off rather than rewritten [GD45]. None is a transcriptome-wide drug-response test, so HB remains untested.

> HB 的先验证据（置信度：低中）。在报告基因实验中，15,927 个被检测变异里有 6 个在咖啡因下表现出条件性等位基因特异效应（FDR 低于 5%）[GD50]；一个 CRISPR 筛选模型在 85 个不变潜变量加 20 个响应潜变量时效果最好 [MD22]；asciminib 下变异×背景的上位效应很少见，只有两条向导 RNA [GV30]；在 TP53 突变系中是一个程序被关闭而不是被重写 [GD45]。这些都不是全转录组的药物响应检验，因此 HB 仍未经检验。

### 3.3 HC: world-model gain / HC：世界模型增益

HC statement. An action-conditioned latent transition model with an explicit state beats capacity-matched mean, linear and one-step conditional baselines on the feasible tests of document 06: multi-step dose rollouts, held-out drug combinations and counterfactual variant swaps. If the baselines match it on every feasible test, the world-model label adds nothing for this problem.

> HC 陈述。带显式状态的动作条件潜在转移模型，在文档 06 中可行的检验上击败容量匹配的均值、线性和单步条件基线：多步剂量展开、留出的药物组合和反事实的变异互换。如果基线在每一项可行检验上都与它相当，那么对这个问题而言，世界模型的标签没有增加任何东西。

HC minimal experiment and risks. Train on single-drug dose series from Tahoe-100M, which has only 3 doses per drug [DS07], and test low-to-high-dose rollouts against held-out measurements and counterfactual swaps on lineage-matched mutant and non-mutant pairs; test combinations only if combination data are found, and none were (Q67). HC is rejected if the baselines are within the uncertainty of the world model on all feasible tests. The swap is weakly identified, a dose series is not a time course, cell-number change belongs in the prediction [MD38], and metabolic labeling of new versus old RNA is the source of time-resolved targets [DS21, DS22].

> HC 最小实验与风险。在 Tahoe-100M 的单药剂量系列上训练（每种药物只有 3 个剂量 [DS07]），并把低剂量到高剂量的展开与留出的测量进行比较，在谱系匹配的突变株与非突变株配对上检验反事实互换；只有在找到组合数据时才检验药物组合，而没有找到任何组合数据（Q67）。如果在所有可行检验上，基线都落在世界模型的不确定范围之内，则 HC 被拒绝。反事实互换的可识别性弱，剂量系列不是时间进程，细胞数量变化应纳入预测 [MD38]，而分离新旧 RNA 的代谢标记是时间分辨目标的来源 [DS21, DS22]。

### 3.4 HD: decision quality (optional) / HD：决策质量（可选）

HD statement. A planner that samples candidate drugs, doses or combinations from a learned action prior and guides them by the gradient of an objective through a genotype-aware forward model makes better decisions than random and greedy selection in a retrospective closed loop on held-out conditions [WM27, WM28]. It matters only if the end use is choosing a drug and dose for a genotype, and it runs last.

> HD 陈述。从学得的动作先验中采样候选药物、剂量或组合，并通过基因型感知前向模型沿目标的梯度加以引导的规划器，在留出条件上的回溯式闭环中，比随机选择和贪心选择做出更好的决策 [WM27, WM28]。只有当最终用途是为某个基因型选择药物和剂量时它才有意义，并且它最后运行。

HD minimal experiment and risks. Reveal the dose-resolved conditions of Tahoe-100M or sci-Plex in rounds [DS07, DS15], retrain after each round, and score how quickly random, greedy, acquisition-function and guided planners reach conditions that satisfy resistance reversal or selective killing under a cap on the non-mutant effect [MD48, MD49, WM28]. HD is rejected if guided sampling does not beat greedy selection by more than the round-to-round variation. The risks are planning on a confidently wrong model, many designs mapping to one state [WM27], objectives on readouts the model predicts poorly [EV33], the boundary-only KKT behavior of the reference code [WM28] and the lack of a wet-lab loop.

> HD 最小实验与风险。分轮揭示 Tahoe-100M 或 sci-Plex 的剂量分辨条件 [DS07, DS15]，每轮之后重新训练，并评估随机、贪心、采集函数和引导式规划器多快能到达满足耐药逆转、或在对非突变背景效应设置上限条件下的选择性杀伤的条件 [MD48, MD49, WM28]。如果引导采样没有以超过轮间变异的幅度优于贪心选择，则 HD 被拒绝。风险包括：在自信但错误的模型上做规划、多个设计映射到同一状态 [WM27]、依赖模型预测不好的读出的目标 [EV33]、参考代码中 KKT 约束只在边界起作用的行为 [WM28]，以及缺少湿实验闭环。

## 4. Candidate architectures / 候选架构

| Architecture | 架构 | How the variant enters | 变异如何进入 | Main risk | 主要风险 |
|---|---|---|---|---|---|
| A. Baseline ladder: mean, drug-wise linear on control expression, one-step conditional generative model (CellFlow- or State-like); tests HA | A. 基线阶梯：均值、基于对照表达的逐药物线性模型、单步条件生成模型（类 CellFlow 或 State）；检验 HA | Mutation indicators added to the linear and conditional models | 变异以突变指示变量加入线性和条件模型 | Strong baselines may already match everything | 强基线可能已经与一切相当 |
| B. Conditional model with explicit variant features; tests HA and HB | B. 带显式变异特征的条件模型；检验 HA 和 HB | Mutation vector, with optional ESM1b, AlphaMissense or Boltz-2 scores as self-reported priors | 突变向量，可选用 ESM1b、AlphaMissense 或 Boltz-2 分数作为自报的先验 | Confounding with lineage | 与谱系混杂 |
| C. Mechanism-informed network (LEMBAS-style); tests HB | C. 机制导向网络（LEMBAS 式）；检验 HB | Variants modify nodes or edges of the prior signaling graph; the drug enters as target inhibition | 变异修改先验信号图的节点或边，药物以靶点抑制的形式输入 | Errors in the prior network; sparse edits may be wrong | 先验网络有误；稀疏编辑可能不对 |
| D. Action-conditioned latent transition model (world-model design); tests HC | D. 动作条件的潜在转移模型（世界模型设计）；检验 HC | Variant conditions or modifies the transition operator F(z, a) | 变异为转移算子 F(z, a) 提供条件或对其修改 | Tests may be infeasible; decoder-free objectives may under-represent effect sizes | 检验可能无法进行；无解码器的目标可能低估效应大小 |
| E. Forward generative model, action prior and guided inverse design (LabCompass-style); tests HD, and HA through the genotype ablation | E. 前向生成模型、动作先验和引导式逆向设计（LabCompass 式）；检验 HD，并通过基因型消融检验 HA | Genotype is a covariate group of the forward model and enters the objective; guidance follows the gradient of the objective through the forward model, with KKT constraints for caps and bounds | 基因型是前向模型的协变量组并进入目标；引导沿着目标穿过前向模型的梯度进行，并用 KKT 约束表示上限和界限 | Planning on a wrong model; protein-level evidence from one cell system; package at version 0.0.1 | 在错误的模型上做规划；证据只有来自一个细胞系统的蛋白水平；软件包为 0.0.1 版本 |

D supplies the transition core and E the planner; a complete cell world model combines them, whereas LabCompass covers only the decision half [WM27, WM28].

> D 提供转移核心，E 提供规划器；完整的细胞世界模型把两者结合起来，而 LabCompass 只覆盖决策这一半 [WM27, WM28]。

## 5. Data plan by track / 按轨道的数据计划

Somatic track. Use Tahoe-100M as the backbone (50 lines with driver annotation, 379 drugs at 3 doses [DS07]) with LINCS L1000 for breadth [DS01], join both to cell-line mutation annotation, and use OmniPath and SIGNOR for prior networks [KB01, KB04]. Because lineage-matched contrasts are small, add labels and cross-checks from an isogenic chemical-genetic map of 51 aberrant cancer genes by 90 drugs [GD46], a 100-line knockout panel [GD54], a CRISPR–drug map of 18 cell lines and 8 drugs [GD53] and genotype-demultiplexed pooled lines [GD45]; variant maps of BCR-ABL1, EGFR and FGFR give class-1 labels [GV28, GV29, GV30, GV32, GV33]. Only the pooled single-cell design has a transcriptomic readout.

> 体细胞轨道。以 Tahoe-100M 为骨干（50 个带驱动突变注释的细胞系，379 种药物各 3 个剂量 [DS07]），以 LINCS L1000 提供广度 [DS01]，把两者与细胞系突变注释连接，并用 OmniPath 和 SIGNOR 构建先验网络 [KB01, KB04]。由于按谱系匹配的对比很小，要从涵盖 51 个异常癌基因×90 种药物的同基因化学-遗传图谱 [GD46]、100 个敲除系的面板 [GD54]、涵盖 18 个细胞系和 8 种药物的 CRISPR–药物图谱 [GD53] 以及按基因型解复用的混池细胞系 [GD45] 补充标签和交叉核对；BCR-ABL1、EGFR 和 FGFR 的变异图谱给出类别 1 的标签 [GV28, GV29, GV30, GV32, GV33]。只有混池的单细胞设计具有转录组读出。

Germline track. Use published response-QTL data as positive controls and external validation [GD06, DS13, GD10], Geuvadis and GTEx for baseline genotype–expression relations [GV05, EV25], sequence-model scores only as weak priors, and stratify every evaluation by ancestry [EV23]. Data with inherited genotype are small: 51 individuals [GD10], influenza-exposed PBMCs with an unverified individual count [GD49] and pooled donors in villages [GD47]; larger donor-by-perturbation grids (12 donors with 90 cytokines [DS16], 40 donors reported for Stack [MD42]) have no stated genotypes (UQ17).

> 种系轨道。把已发表的响应 QTL 数据用作阳性对照和外部验证 [GD06, DS13, GD10]，把 Geuvadis 和 GTEx 用作基线基因型-表达关系的来源 [GV05, EV25]，只把序列模型分数用作弱先验，并且每项评测都按祖源分层 [EV23]。带遗传性基因型的数据规模很小：51 个个体 [GD10]、个体数未经核实的流感暴露 PBMC [GD49]，以及村落中的混池供体 [GD47]；更大的供体×扰动网格（12 名供体、90 种细胞因子 [DS16]；Stack 报告的 40 名供体 [MD42]）没有说明基因型（UQ17）。

Decision-test data. The retrospective loop of HD runs on the dose-resolved screens of sci-Plex and Tahoe-100M [DS15, DS07]; LabCompass publishes closed-loop data only at the protein level [DS23] (UQ21).

> 决策检验的数据。HD 的回溯式循环在 sci-Plex 和 Tahoe-100M 的剂量分辨筛选上运行 [DS15, DS07]；LabCompass 只在蛋白水平公布闭环数据 [DS23]（UQ21）。

## 6. Milestones and decision gates / 里程碑与决策门

M0, verification. Every row that carries a number in documents 01 to 07 has been read against its text (Q143); claims that remain unverified sit in rows at tier T2, and the LabCompass full text is unread (UQ20) [WM27]. Run the unit tests of the labcompass package before any reuse (UQ09) [WM28].

> M0，核验。文档 01 至 07 中带数字的每个条目都已对照其文本阅读（Q143）；仍未核验的论断位于 T2 级条目中，LabCompass 全文未读到（UQ20）[WM27]。在任何复用之前，运行 labcompass 软件包的单元测试（UQ09）[WM28]。

M1, data assembly. Check access and licences (UQ10), define the lineage-matched contrasts from the counts above, and fix the minimum number of lines per contrast from a power calculation.

> M1，数据整理。核查获取方式和许可（UQ10），根据上述计数定义按谱系匹配的对比，并根据效能计算确定每个对比所需的最少细胞系数。

M2, harness. Build the evaluation harness and the baseline ladder, and confirm that the genotype-permutation control produces no gain. Include splits for unseen context, unseen perturbation, unseen dataset and unseen genotype [EV35].

> M2，评测框架。构建评测框架和基线阶梯，并确认基因型置换对照不产生增益。加入对未见背景、未见扰动、未见数据集和未见基因型的划分 [EV35]。

M3, test HA. Gate: if HA is supported, stop explicit variant modeling in the somatic track and pivot to models conditioned on baseline state; if HA is rejected, continue to M4.

> M3，检验 HA。决策门：如果 HA 得到支持，就停止体细胞轨道中的显式变异建模，转向以基线状态为条件的模型；如果 HA 被拒绝，则继续到 M4。

M4, test HB. Gate: the result decides between sparse and dense variant parameterizations.

> M4，检验 HB。决策门：结果决定采用稀疏还是稠密的变异参数化。

M5, test HC. Run it only if M3 and M4 justify a dynamic model and at least one feasible test exists.

> M5，检验 HC。只有当 M3 和 M4 证明动态模型有必要，且至少存在一项可行检验时才运行。

M6, test HD (optional). Run it only if the end use is decision-making and M3 and M4 have produced a genotype-aware forward model that passes them. Gate: guided sampling must beat greedy selection in the retrospective loop; otherwise report prediction results only.

> M6，检验 HD（可选）。只有当最终用途是决策、且 M3 和 M4 已经产生通过检验的基因型感知前向模型时才运行。决策门：引导采样必须在回溯式循环中优于贪心选择；否则只报告预测结果。

## 7. Risks and kill criteria / 风险与终止标准

The main risks are low power in a 50-line panel with small lineage-matched arms (J16) [DS07], confounding of mutation with lineage, self-reported results that do not replicate, infeasible combination and time tests, and planning that amplifies model errors [WM28]. Mitigations are lineage-matched contrasts, per-contrast power calculations in M1, uncertainty-aware scoring and a record of which tests the data can support.

> 主要风险是 50 个细胞系的面板中、按谱系匹配的各臂很小所导致的效能低（J16）[DS07]、突变与谱系混杂、自报结果无法复现、组合检验和时间检验无法进行，以及规划会放大模型误差 [WM28]。缓解措施是谱系匹配的对比、M1 中逐对比的效能计算、感知不确定性的打分，以及对数据能支持哪些检验的记录。

Kill criterion (UQ06). If, after M3 and M4, HA is supported and HB is not, stop variant-aware modeling in the somatic track and report the negative result; the evidence base in this repository remains useful on its own.

> 终止标准（UQ06）。如果在 M3 和 M4 之后，HA 得到支持而 HB 不成立，就停止体细胞轨道中的变异感知建模并报告阴性结果；本仓库中的证据库本身仍然有用。

## 8. Questions for confirmation / 待确认问题

Open decisions for the design are kept in `data/questions.csv` and listed in `docs/10-open-questions.md`: UQ05 (prediction or decision), UQ06 (negative HA result and stopping rule), UQ07 (order of the hypotheses), UQ08 (first variant class), UQ16 (stop collecting literature) and UQ21 (wet-lab capacity).

> 设计相关的待决事项保存在 `data/questions.csv` 中，并列在 `docs/10-open-questions.md` 里：UQ05（预测还是决策）、UQ06（HA 的阴性结果与终止规则）、UQ07（假设的顺序）、UQ08（先对哪一类变异建模）、UQ16（停止收集文献）和 UQ21（湿实验能力）。

## 9. Evidence gaps / 证据缺口

No combination data were found (Q67), the Tahoe-100M dose grid has 3 levels and its time point is not stated on the card [DS07], and the mapping between cell-line annotation sources has not been examined (UQ19). The donors of the large cytokine datasets have no stated genotypes (UQ17) [DS16, MD42], the LabCompass full text was not read [WM27], and no transcriptome-level closed-loop design data were found (Q97) [DS23].

> 没有找到组合数据（Q67），Tahoe-100M 的剂量网格只有 3 个水平，其卡片也没有说明时间点 [DS07]，细胞系注释来源之间的映射尚未检查（UQ19）。大型细胞因子数据集的供体没有说明基因型（UQ17）[DS16, MD42]，LabCompass 的全文没有读到 [WM27]，并且没有找到转录组层面的闭环设计数据（Q97）[DS23]。

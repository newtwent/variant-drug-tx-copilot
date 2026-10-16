# 08 Design implications / 设计启示

## 1. Scope / 范围

This document turns the evidence in documents 01 to 07 into design proposals. Everything here is a proposal or a hypothesis to be tested, not a finding. It gives principles drawn from the evidence, three falsifiable hypotheses with minimal experiments, four candidate architectures, a data plan for each track, milestones with decision gates, and kill criteria. It deliberately puts the hypotheses before the architectures.

> 本文档把文档 01 至 07 中的证据转化为设计提案。这里的一切都是待检验的提案或假设，不是发现。它给出从证据得出的原则、三个带最小实验的可证伪假设、四种候选架构、每条轨道的数据计划、带决策门的里程碑以及终止标准。它有意把假设放在架构之前。

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

## 3. Three falsifiable hypotheses / 三个可证伪假设

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

### 3.2 HB: sparse shift / HB：稀疏偏移

HB statement. For a given driver mutation, the difference between mutant and reference responses to the same drug is low-rank or sparse, meaning that a few latent directions or network edges carry most of it.

> HB 陈述。对于给定的驱动突变，在同一药物下突变株与参考株的响应差异是低秩或稀疏的，即少数潜在方向或网络边承载了其中的大部分。

HB relevance. If HB holds, variants can be modeled as small edits to the response operator, which gives interpretability and data efficiency. If HB fails, a sparse-shift parameterization is the wrong inductive bias.

> HB 的意义。如果 HB 成立，变异可以被建模为对响应算子的小幅编辑，这带来可解释性和数据效率。如果 HB 不成立，稀疏偏移的参数化就是错误的归纳偏置。

HB minimal experiment. From the matrices of differences of differences (drugs by genes) for each mutation, compute the singular-value spectrum and the sparsity. Then compare, at equal parameter count, models with a sparse variant-specific shift against models with a dense one, on held-out drugs.

> HB 最小实验。对每个突变，由差值的差值矩阵（药物×基因）计算奇异值谱和稀疏度。然后在参数量相等的条件下，在留出药物上比较带稀疏的变异特异偏移的模型与带稠密偏移的模型。

HB decision rule and risks. HB is rejected if the spectrum is flat and a dense parameterization beats the sparse one at equal capacity. HB is supported if the spectrum decays quickly and the sparse form matches or beats the dense one. Noise inflates apparent rank, and small effect sizes erase the benefit of sparsity [MD17].

> HB 的判定规则与风险。如果谱是平的，且稠密参数化在容量相等时优于稀疏参数化，则 HB 被拒绝。如果谱衰减很快，且稀疏形式与稠密形式相当或更好，则 HB 得到支持。噪声会抬高表观秩，而较小的效应大小会抹去稀疏性的收益 [MD17]。

### 3.3 HC: world-model gain / HC：世界模型增益

HC statement. An action-conditioned latent transition model with an explicit state beats capacity-matched mean, linear and one-step conditional baselines on the feasible tests of the battery in document 06: multi-step dose rollouts, held-out drug combinations and counterfactual variant swaps.

> HC 陈述。带显式状态的动作条件潜在转移模型，在文档 06 检验清单中可行的检验上击败容量匹配的均值、线性和单步条件基线：多步剂量展开、留出的药物组合和反事实的变异互换。

HC relevance. This is the claim that motivates the architecture. If the baselines match the model on every feasible test, the world-model label adds nothing for this problem.

> HC 的意义。这是促成该架构的主张。如果基线在每一项可行检验上都与该模型相当，那么对这个问题而言，世界模型的标签没有增加任何东西。

HC minimal experiment. Train on single-drug dose series from Tahoe-100M, and test rollouts from low to high dose against held-out measurements. Test the counterfactual swap on lineage-matched mutant and wild-type pairs. Test combinations only if combination data are found, and none have been retrieved so far.

> HC 最小实验。在 Tahoe-100M 的单药剂量系列上训练，并把从低剂量到高剂量的展开与留出的测量进行比较。在谱系匹配的突变株与野生株配对上检验反事实互换。只有在找到组合数据时才检验药物组合，而目前尚未检索到任何组合数据。

HC decision rule and risks. HC is rejected if the baselines are within the uncertainty of the world model on all feasible tests. If only the rollout test is feasible, the conclusion is limited to dose dynamics. The counterfactual swap is weakly identified, and a dose series is not a time course.

> HC 的判定规则与风险。如果在所有可行检验上，基线都落在世界模型的不确定范围之内，则 HC 被拒绝。如果只有展开检验可行，结论就仅限于剂量动力学。反事实互换的可识别性弱，而且剂量系列不是时间进程。

## 4. Candidate architectures / 候选架构

| Architecture | How the variant enters | Hypothesis tested | Main risk | 说明（中文） |
|---|---|---|---|---|
| A. Baseline ladder: mean, drug-wise linear on control expression, one-step conditional generative model (CellFlow- or State-like) | Mutation indicators added to the linear and conditional models | HA | Strong baselines may already match everything | A. 基线阶梯：均值、基于对照表达的逐药物线性模型、单步条件生成模型（类 CellFlow 或 State）；变异以突变指示变量加入线性和条件模型；检验 HA；风险是强基线可能已经与一切相当 |
| B. Conditional model with explicit variant features | Mutation vector, with optional ESM1b, AlphaMissense or Boltz-2 scores as self-reported priors | HA, HB | Confounding with lineage | B. 带显式变异特征的条件模型；变异以突变向量加入，可选用 ESM1b、AlphaMissense 或 Boltz-2 分数作为自报的先验；检验 HA、HB；风险是与谱系混杂 |
| C. Mechanism-informed network (LEMBAS-style) | Variants modify nodes or edges of the prior signaling graph; the drug enters as target inhibition | HB | Errors in the prior network; sparse edits may be wrong | C. 机制导向网络（LEMBAS 式）；变异修改先验信号图的节点或边，药物以靶点抑制的形式输入；检验 HB；风险是先验网络有误、稀疏编辑可能不对 |
| D. Action-conditioned latent transition model (world-model design) | Variant conditions or modifies the transition operator F(z, a) | HC | Tests may be infeasible; decoder-free objectives may under-represent effect sizes | D. 动作条件的潜在转移模型（世界模型设计）；变异为转移算子 F(z, a) 提供条件或对其修改；检验 HC；风险是检验可能无法进行、无解码器的目标可能低估效应大小 |

## 5. Data plan by track / 按轨道的数据计划

Somatic track. Use Tahoe-100M as the backbone and LINCS L1000 for breadth, join both to cell-line mutation annotation through a stable cell-line identifier, and use OmniPath and SIGNOR for prior networks [DS05, DS01, KB01, KB04]. The first task is to count, per driver mutation and lineage, how many mutant and wild-type lines the panel contains, and to define the lineage-matched contrasts.

> 体细胞轨道。以 Tahoe-100M 为骨干，以 LINCS L1000 提供广度，通过稳定的细胞系标识符把两者与细胞系突变注释连接，并用 OmniPath 和 SIGNOR 构建先验网络 [DS05, DS01, KB01, KB04]。第一项任务是按驱动突变和谱系统计面板中有多少突变株和野生株，并定义按谱系匹配的对比。

Germline track. Use published response-QTL data as positive controls and external validation, Geuvadis and GTEx as sources of baseline genotype–expression relations, and sequence-model scores only as weak priors [GD06, DS13, GV05, EV25]. No deep genotype model is planned for this track unless larger datasets with genotype, drug and transcriptome are found, and every evaluation is stratified by ancestry [EV23].

> 种系轨道。把已发表的响应 QTL 数据用作阳性对照和外部验证，把 Geuvadis 和 GTEx 用作基线基因型-表达关系的来源，并且只把序列模型分数用作弱先验 [GD06, DS13, GV05, EV25]。除非找到同时含基因型、药物和转录组的更大数据集，否则不为该轨道规划深度基因型模型，且每项评测都按祖源分层 [EV23]。

Before use, verify the access routes, licenses and schemas of every dataset, because none has been inspected [DS07, DS13].

> 使用之前，要核查每个数据集的获取途径、许可和模式，因为没有一个被检查过 [DS07, DS13]。

## 6. Milestones and decision gates / 里程碑与决策门

M0, verification. Open outbound network access and verify the load-bearing claims listed in the search log by reading the primary sources, then update tiers and the verified flag. No other milestone should rely on a claim that is still unverified.

> M0，核验。开放出站网络访问，通过阅读原始来源核验检索日志中列出的承重主张，然后更新等级和 verified 标记。其他里程碑都不应依赖仍未核验的主张。

M1, data assembly. Check access and licenses, count mutant and wild-type lines per driver mutation and lineage, and define the contrasts and the minimum number of lines per contrast from a power calculation.

> M1，数据整理。核查获取方式和许可，按驱动突变和谱系统计突变株与野生株的数量，并根据效能计算确定对比以及每个对比所需的最少细胞系数。

M2, harness. Build the evaluation harness and the baseline ladder, and confirm that the controls behave as expected: the genotype-permutation control must produce no gain.

> M2，评测框架。构建评测框架和基线阶梯，并确认对照表现符合预期：基因型置换对照必须不产生增益。

M3, test HA. Gate: if HA is supported, stop explicit variant modeling in the somatic track and pivot to models conditioned on baseline state; if HA is rejected, continue to M4.

> M3，检验 HA。决策门：如果 HA 得到支持，就停止体细胞轨道中的显式变异建模，转向以基线状态为条件的模型；如果 HA 被拒绝，则继续到 M4。

M4, test HB. Gate: the result decides between sparse and dense variant parameterizations.

> M4，检验 HB。决策门：结果决定采用稀疏还是稠密的变异参数化。

M5, test HC. Run it only if M3 and M4 justify a dynamic model and at least one feasible test exists.

> M5，检验 HC。只有当 M3 和 M4 证明动态模型有必要，且至少存在一项可行检验时才运行。

## 7. Risks and kill criteria / 风险与终止标准

The main risks are low statistical power in a 50-line panel (J16), confounding of mutation with lineage, self-reported results that do not replicate, and the possible infeasibility of the combination and time tests. Mitigations are lineage-matched contrasts, per-contrast power calculations in M1, the verification in M0, and an explicit record of which tests the data can support.

> 主要风险是 50 个细胞系的面板中统计效能低（J16）、突变与谱系混杂、自报结果无法复现，以及组合检验和时间检验可能无法进行。缓解措施是谱系匹配的对比、M1 中逐对比的效能计算、M0 中的核验，以及对数据能支持哪些检验的明确记录。

Kill criterion. If, after M3 and M4, HA is supported and HB is not, stop the variant-aware modeling in the somatic track and report the negative result; the evidence base in this repository remains useful on its own.

> 终止标准。如果在 M3 和 M4 之后，HA 得到支持而 HB 不成立，就停止体细胞轨道中的变异感知建模并报告阴性结果；本仓库中的证据库本身仍然有用。

## 8. Questions for confirmation / 待确认问题

Is the order HA, HB, HC acceptable, with the world-model test last? Default: yes.

> 按 HA、HB、HC 的顺序、把世界模型检验放在最后，是否可以接受？默认：可以。

Is a negative result on HA an acceptable outcome of the project? Default: yes, because it would redirect the architecture toward baseline-conditioned models rather than waste effort on variant modeling.

> 在 HA 上得到阴性结果，是否是本项目可接受的结果？默认：可以，因为这会把架构引向以基线为条件的模型，而不是把精力浪费在变异建模上。

## 9. Evidence gaps / 证据缺口

The number of mutant lines per driver mutation in the Tahoe-100M panel is unknown, as are its dose grid and time points. No combination data were found. The mapping between cell-line annotation sources has not been examined. All source claims are tier T2 or T3, so every design choice that rests on one is provisional until M0.

> Tahoe-100M 面板中每个驱动突变的突变株数量未知，其剂量网格和时间点也未知。没有找到组合数据。细胞系注释来源之间的映射尚未检查。所有来源论断都是 T2 或 T3 级，因此凡建立在其上的设计选择，在 M0 之前都是暂定的。

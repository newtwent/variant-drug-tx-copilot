# 09 LabCompass and decision-oriented world modeling / LabCompass 与面向决策的世界建模

## 1. Scope / 范围

This document extracts what LabCompass, the generative inverse-design framework for cell culture presented by Fabian Theis, offers to the design of a genotype-aware cell world model. Facts LC1 to LC7 state what the sources show, and insights I1 to I9 are inferences for this project. They rest on a preprint abstract (tier T2), two code repositories and a dataset card (tier T1) and secondary posts (tier T3); the preprint's full text was not read.

> 本文档提炼 LabCompass（由 Fabian Theis 介绍的、面向细胞培养的生成式逆向设计框架）能为基因型感知细胞世界模型的设计提供什么。事实 LC1 至 LC7 陈述来源所显示的内容，启示 I1 至 I9 是为本项目所做的推断。它们依据的是预印本摘要（T2 级）、两个代码仓库和一张数据集卡片（T1 级），以及二手帖子（T3 级）；预印本全文没有读到。

## 2. Facts and evidence / 事实与证据

LC1 (tier T2). The preprint abstract describes a flow-matching generative model guided by a forward surrogate that predicts cell phenotypes, proposing culture designs (continuous cytokine and small-molecule parameters) toward target states in primary CD34+ cells. Four lab-in-the-loop rounds yielded a 78-million-cell spectral flow cytometry dataset (self-reported), and the authors argue that virtual cell models should be judged by how effectively they guide experiments [WM27]. The bioRxiv record names Fabian J. Theis as corresponding author (Q140), and a post by him frames the method as using cellular world models to help decide what experiment to do next [WM30].

> LC1（T2 级）。预印本摘要描述了一个由前向代理模型引导的流匹配生成模型，该代理模型预测细胞表型，并针对原代 CD34+ 细胞中的目标状态提出培养设计（连续的细胞因子和小分子参数）。四轮实验室闭环产生了一个 78 百万（7,800 万）个细胞的光谱流式细胞术数据集（自报），作者主张虚拟细胞模型应以其引导实验的有效程度来评判 [WM27]。bioRxiv 记录把 Fabian J. Theis 列为通讯作者（Q140），他的一条帖子把该方法表述为利用细胞世界模型帮助决定下一步做什么实验 [WM30]。

LC2 (tier T1). The reproducibility pipeline chains a conditional flow-matching forward model with a cell-type classifier, a flow-matching prior over protocols, loss-guided inverse design (default 350 forward passes per candidate) and re-scoring of candidates over noise draws; models train on cumulative data from all earlier loops. The public data are eight chained loop datasets (about 60 GB), inference-only checkpoints and about 1.07 million unfiltered designs, whereas the abstract counts four loops, so the counting convention is unclear [WM29, DS23, WM27].

> LC2（T1 级）。可复现流程把条件流匹配前向模型、细胞类型分类器、方案上的流匹配先验、损失引导的逆向设计（默认每个候选 350 次前向传播）以及在噪声抽样下对候选重新打分串联起来；模型在此前所有轮次的累积数据上训练。公开的数据是八个相互衔接的闭环数据集（约 60 GB）、仅用于推理的检查点和约 1.07 百万（107 万）个未过滤的设计，而摘要计为四轮，因此计数约定不明 [WM29, DS23, WM27]。

LC3 (tier T1). The `labcompass` package (BSD-3, version 0.0.1) implements the forward model as conditional flow matching with one encoder per covariate group (drugs, genetic edits, dose, time) held in AnnData columns, and two inverse routes: covariate optimization (MAP, Langevin or amortized, with an optional log-prior) and training-free guidance of a pretrained flow by a loss or a KKT-constrained Lagrangian. Its `train_inverse_model` builds the validation loader from the training data, so the validation curve of the inverse model is not held out (code read) [WM28].

> LC3（T1 级）。`labcompass` 软件包（BSD-3，版本 0.0.1）把前向模型实现为条件流匹配，每个协变量组（药物、基因编辑、剂量、时间）在 AnnData 各列上各有一个编码器，并提供两条逆向路径：协变量优化（MAP、Langevin 或摊销方式，可选对数先验），以及用损失或受 KKT 约束的拉格朗日量对预训练流做免训练引导。其 `train_inverse_model` 用训练数据构建验证加载器，因此逆向模型的验证曲线并非留出数据（已读代码）[WM28]。

LC4 (tier T1). Guidance steers a one-step endpoint estimate, and in the KKT variant a constraint counts as active only within 1e-6 of its boundary, so a strictly met constraint and a violated one both receive no multiplier (code read) [WM28]. What this means for a cap on the effect in wild-type cells is an inference (I2), not a tested result.

> LC4（T1 级）。引导作用于一步终点估计；在 KKT 变体中，只有约束位于其边界 1e-6 以内时才被视为活动约束，因此严格满足的约束和被违反的约束都得不到乘子（已读代码）[WM28]。这对野生型细胞效应上限意味着什么，是一项推断（I2），不是经过检验的结果。

LC5 (tier T1). The protocol schema grows across loops: later loops add axes that earlier loops held at zero, and a naive concatenation silently drops them [DS23]. Re-scoring earlier candidates under later loops' checkpoints quantifies how much each loop reduced uncertainty [WM29].

> LC5（T1 级）。方案模式随各轮增长：后续轮次加入了前面各轮保持为零的轴，简单拼接会悄悄丢掉它们 [DS23]。在后续轮次的检查点下对更早的候选重新打分，可量化每一轮对不确定性的降低 [WM29]。

LC6 (tier T3). A blog summary, secondary and unchecked against the preprint, reports a 116-condition training screen of 10 cytokines or small molecules under hypoxia and normoxia read by 20-color spectral flow cytometry, a design prior with a differentiable surrogate that needs no retraining for new targets, uncertainty that fell with each round (up to 66% on held-out conditions), and a scRNA-seq demonstration on HCMV infection [WM32].

> LC6（T3 级）。一篇博客摘要（二手，未与预印本核对）报告：在缺氧与常氧下对 10 种细胞因子或小分子做了 116 个条件的训练筛选，用 20 色光谱流式细胞术读出；设计先验加可微代理模型，对新目标无需重新训练；不确定性随每一轮下降（在留出条件上最多 66%）；以及一个针对 HCMV 感染的 scRNA-seq 演示 [WM32]。

LC7 (not retrieved). The preprint's full text, baselines, ablations and scRNA-seq analysis were not read, because bioRxiv blocked retrieval (Q138) and only the abstract was obtained (Q140).

> LC7（未取回）。预印本的全文、基线、消融和 scRNA-seq 分析没有读到，因为 bioRxiv 阻止了抓取（Q138），只拿到了摘要（Q140）。

## 3. Component map to this project / 与本项目的组件对照

The columns on what the sources say are facts. The proposed roles are judgments to be tested.

> 来源所述的各列是事实。提议的角色是有待检验的判断。

| Component | What the sources say | 来源所述 | Proposed role (judgment) | 提议角色（判断） | Source IDs |
|---|---|---|---|---|---|
| Forward model | Conditional flow matching from control to perturbed cell states given covariates | 在给定协变量时，条件流匹配把对照细胞状态映射到扰动后状态 | Genotype-conditioned generator of drug-induced state distributions; the baseline ladder of document 08 supplies its competitors | 基因型条件的药物诱导状态分布生成器；其竞争对手来自文档 08 的基线阶梯 | WM28 |
| Covariate encoders | One encoder per covariate group over AnnData columns | 在 AnnData 各列上，每个协变量组一个编码器 | Add genotype as one more group and keep the source population genotype-matched | 把基因型作为又一个协变量组，并保持源群体与基因型匹配 | WM28, MD61 |
| Protocol prior | Flow-matching prior over protocols | 方案上的流匹配先验 | Prior over drug, dose and combination designs limited to an available library | 限制在可用化合物库内的药物、剂量和组合设计先验 | WM29 |
| Guidance | Loss gradient at a one-step endpoint estimate; a KKT variant with a boundary-only active set | 在一步终点估计处的损失梯度；活动集只含边界的 KKT 变体 | Objective-guided design (resistance reversal, selective killing) with caps enforced by a penalty or barrier, not by the multiplier alone | 目标引导的设计（耐药逆转、选择性杀伤），上限由惩罚项或障碍项而不是仅靠乘子来执行 | WM28 |
| Covariate inversion | MAP, Langevin or amortized inference of covariates for a target state, with an optional log-prior | 针对目标状态，用 MAP、Langevin 或摊销方式推断协变量，可选对数先验 | Amortized proposals when drugs and doses are discrete | 药物和剂量为离散时的摊销式提议 | WM28 |
| Uncertainty re-scoring | Candidates re-scored over noise draws and across loops | 在噪声抽样中以及跨轮次对候选重新打分 | Add ensembles or conformal calibration for epistemic uncertainty | 加入集成或共形校准以覆盖认知不确定性 | WM29 |
| Loop data chain | Cumulative per-loop datasets, per-loop checkpoints and a growing protocol schema | 累积的逐轮数据集、逐轮检查点和不断增长的方案模式 | Retrospective loop benchmark on public data; prospective use needs a wet lab | 在公开数据上做回溯式闭环基准；前瞻使用需要湿实验 | WM29, DS23 |

## 4. Judgments / 判断

All items below are judgments drawn from LC1 to LC6, not findings of the paper. "Testable" names the cheapest check.

> 下列各项都是基于 LC1 至 LC6 的判断，不是论文的发现。“可检验”指出最便宜的检验方式。

I1 (confidence: medium-high). Split the world model into replaceable parts: a forward generative model of cell-state distributions given covariates, a prior over actions, an objective model, and a guidance rule that connects them. LabCompass is built this way [WM28, WM29], and the blog reports that a new target needs no retraining [WM32]. The same forward model could then serve resistance reversal and mutant-selective killing by swapping only the objective. Testable: one forward model, two objectives, both met on held-out contrasts.

> I1（置信度：中高）。把世界模型拆成可替换的部分：给定协变量时细胞状态分布的前向生成模型、动作先验、目标模型，以及连接它们的引导规则。LabCompass 正是这样构建的 [WM28, WM29]，博客报告新目标无需重新训练 [WM32]。这样同一个前向模型只需更换目标，就能服务于耐药逆转和针对突变体的选择性杀伤。可检验：同一前向模型、两个目标，在留出的对比上都达到。

I2 (confidence: medium). Treat inverse design as guided sampling from a learned action prior rather than as scalar optimization: it returns a set of candidates and accepts constraints such as a compound library, dose bounds and a cap on the predicted effect in wild-type cells. Because the KKT variant acts only within 1e-6 of a constraint boundary (LC4) [WM28], such a cap also needs an explicit penalty or barrier; this is an inference from reading the code and has not been run. Testable on a synthetic problem with a violated constraint: does the sample move back inside?

> I2（置信度：中）。把逆向设计视为从学得的动作先验中做引导采样，而不是标量优化：它返回一组候选，并接受化合物库、剂量上限和对野生型细胞预测效应上限之类的约束。由于 KKT 变体只在约束边界 1e-6 以内起作用（LC4）[WM28]，这样的上限还需要显式的惩罚项或障碍项；这是读代码得出的推断，尚未运行。可在带有被违反约束的合成问题上检验：样本是否会回到约束之内？

I3 (confidence: medium). The strongest test of a decision-oriented model is prospective (propose, measure, update). With public data the achievable analogue is a retrospective loop that reveals conditions in rounds and scores how fast a planner reaches good ones, as IterPert does with eight acquisition baselines [MD48, MD49]. LabCompass adds a metric for the loop itself: re-scoring earlier candidates under later checkpoints measures how much each round reduced uncertainty (LC5) [WM29]. Testable: build a retrospective-loop benchmark on Tahoe-100M or sci-Plex and compare planners [DS07, DS15].

> I3（置信度：中）。对面向决策的模型，最强的检验是前瞻性的（提出、测量、更新）。仅用公开数据时，可行的类比是回溯式循环：分轮揭示条件，评估规划器多快到达好的条件，IterPert 就是这样做的，并比较了八种采集基线 [MD48, MD49]。LabCompass 为循环本身增加了一个指标：在后续检查点下对更早的候选重新打分，可衡量每一轮降低了多少不确定性（LC5）[WM29]。可检验：在 Tahoe-100M 或 sci-Plex 上建立回溯循环基准并比较规划器 [DS07, DS15]。

I4 (confidence: medium). Put genotype into the condition encoder as another covariate group and keep the source population genotype-matched. LabCompass gives each covariate group its own encoder over AnnData columns [WM28], the CellFlow PBMC tutorial splits controls by donor so that mappings stay within a donor [MD61], and State and Stack document only perturbation, cell-type or donor split columns [MD62, MD65]. This turns hypothesis HA into an ablation: remove the genotype covariate, keep the matched source, and see whether the interaction metric changes.

> I4（置信度：中）。把基因型作为另一个协变量组放进条件编码器，并保持源群体与基因型匹配。LabCompass 在 AnnData 各列上为每个协变量组配一个编码器 [WM28]，CellFlow 的 PBMC 教程按供体拆分对照，使映射保持在同一供体之内 [MD61]，而 State 和 Stack 只记录了扰动、细胞类型或供体拆分列 [MD62, MD65]。这把假设 HA 变成一个消融实验：去掉基因型协变量，保持匹配的源，看交互指标是否变化。

I5 (confidence: medium). Make actions continuous and let the action space widen. Later LabCompass loops added protocol axes that earlier data hold at zero (LC5) [DS23], so a conditioning interface that accepts new factors is feasible. The same interface could take allelic dosage or knockdown strength as a continuous covariate, in line with graded-knockdown data as the closest public proxy for hypomorphic alleles [DS24]. Testable: train with a hypomorphic-dose covariate and check dose-ordered predictions on held-out doses.

> I5（置信度：中）。让动作连续，并让动作空间可以变宽。LabCompass 的后续轮次加入了更早数据中保持为零的方案轴（LC5）[DS23]，因此接受新因素的条件接口是可行的。同一接口可以把等位基因剂量或敲低强度作为连续协变量，这与把梯度敲低数据视为亚效等位基因最接近的公开代理一致 [DS24]。可检验：用亚效等位基因剂量协变量训练，并在留出的剂量上检查按剂量排序的预测。

I6 (confidence: medium). Score candidates under generative noise and under model uncertainty. LabCompass re-scores candidates over noise draws and across loops [WM29], which captures generative spread but, in what was read, not epistemic uncertainty. With the small genotype counts of the germline track (J1), planning on a confidently wrong model is the main risk, so ensembles or conformal calibration should be added; this is a proposal, not something the sources describe.

> I6（置信度：中）。在生成噪声和模型不确定性两种情形下给候选打分。LabCompass 在噪声抽样中以及跨轮次对候选重新打分 [WM29]，这捕获了生成的离散程度，但就所读内容而言，没有认知不确定性。种系轨道的基因型数量很少（J1），在一个自信但错误的模型上做规划是主要风险，因此应加入集成或共形校准；这是一项提议，不是来源中描述的内容。

I7 (confidence: low-medium). Guidance details decide behavior. The gradient is taken at a one-step endpoint estimate [WM28], while other work suggests choosing the method by dimension and smoothness [WM45], using gradient-free guidance when the objective is not differentiable [WM46], and calibrating the per-step weights instead of setting them by hand [WM44]. Testable on a synthetic curved-path problem: compare the endpoint predictors and guidance families on one objective.

> I7（置信度：低中）。引导的细节决定行为。梯度取自一步终点估计 [WM28]，而其他工作提示：应按维度和平滑性选择方法 [WM45]，目标不可微时用无梯度引导 [WM46]，并校准逐步权重而不是手工设定 [WM44]。可在合成的弯曲路径问题上检验：在同一目标上比较终点预测器和引导方法族。

I8 (confidence: medium). LabCompass supports the decision half of a world model but not the dynamics half. Its forward model gives a distribution over end states given a protocol, and no multi-step rollout or state-update test appears in what was read. For trajectories the references are PerturbGen, scDiffEq, PRESCIENT and PerturbRx [WM33, WM36, WM37, MD46], and for sequential decisions DiRL [WM35]; a complete cell world model would combine a transition core with a LabCompass-style planner.

> I8（置信度：中）。LabCompass 支持世界模型的决策一半，而不支持动力学一半。其前向模型给出给定方案时终态的分布，所读内容中没有出现多步展开或状态更新的检验。对于轨迹，参考是 PerturbGen、scDiffEq、PRESCIENT 和 PerturbRx [WM33, WM36, WM37, MD46]，对于序贯决策则是 DiRL [WM35]；完整的细胞世界模型应当把转移核心与 LabCompass 式的规划器结合起来。

I9 (confidence: low; a proposal). Two genotype-aware designs follow. Resistance reversal searches drug, dose and combination designs that move a mutant context's predicted response toward the wild-type response. Selective killing maximizes the predicted effect in mutant contexts under a cap on the effect in wild-type contexts (I2); a multi-objective planner may fit this better than a single cap [WM47]. Both need a genotype-aware forward model and a validated objective, for which TF activities [KB20] and mechanism-fidelity scoring [EV33] are candidates. Testable only after hypotheses HA and HB have been answered.

> I9（置信度：低；一项提议）。随之而来的有两种基因型感知的设计。耐药逆转搜索使突变背景的预测响应趋近野生型响应的药物、剂量和组合设计。选择性杀伤在对野生型背景效应设置上限的条件下，最大化突变背景中的预测效应（I2）；多目标规划器可能比单一上限更合适 [WM47]。两者都需要基因型感知的前向模型和经过验证的目标，可选的目标有 TF 活性 [KB20] 和机制保真度评分 [EV33]。只有在回答了假设 HA 和 HB 之后才能检验。

Limits of transfer. The LabCompass readout is protein-level spectral flow cytometry, not a transcriptome, and its design space is a handful of cytokines, small molecules and oxygen with no inherited genotype variation [WM27, WM32]. The preprint is a recent, unreviewed first version and the package is at version 0.0.1 with the validation-loader defect noted above [WM28]. LabCompass therefore transfers as an architecture pattern and a validation philosophy, not as evidence that genotype-aware inverse design works.

> 迁移的局限。 LabCompass 的读出是蛋白水平的光谱流式细胞术，而不是转录组，其设计空间只是少数细胞因子、小分子和氧浓度，没有遗传性基因型变异 [WM27, WM32]。预印本是较新的、未经评审的第一版，软件包为 0.0.1 版本，并存在上文所述的验证加载器缺陷 [WM28]。因此 LabCompass 可迁移的是一种架构模式和一种验证理念，而不是基因型感知逆向设计行之有效的证据。

## 5. Recommended actions / 行动建议

Before any reuse of the labcompass package, run its unit tests and a toy reproduction, and avoid or fix the validation-loader defect of `train_inverse_model` [WM28].

> 在任何复用 labcompass 软件包之前，运行其单元测试和一个玩具级复现，并避免或修复 `train_inverse_model` 的验证加载器缺陷 [WM28]。

Build the retrospective closed-loop benchmark of hypothesis HD on Tahoe-100M or sci-Plex, with random, greedy and acquisition-function planners from the IterPert harness (Apache-2.0) as baselines [DS07, DS15, MD48, MD49].

> 在 Tahoe-100M 或 sci-Plex 上构建假设 HD 的回溯式闭环基准，以 IterPert 框架（Apache-2.0）中的随机、贪心和采集函数规划器为基线 [DS07, DS15, MD48, MD49]。

Add a genotype covariate group with a genotype-matched source population to the forward model and run the HA ablation of document 08 before any design experiment [WM28, MD61].

> 给前向模型加入带基因型匹配源群体的基因型协变量组，并在任何设计实验之前运行文档 08 中的 HA 消融 [WM28, MD61]。

Add epistemic uncertainty (ensembles or conformal calibration) to the planner, and test the boundary-only behavior of the KKT variant on a synthetic violated constraint before relying on caps [WM28, WM29].

> 给规划器加入认知不确定性（集成或共形校准），并在依赖上限之前，在带有被违反约束的合成问题上检验 KKT 变体只在边界起作用的行为 [WM28, WM29]。

Compare endpoint predictors and guidance families (gradient, gradient-free and multi-objective) on one synthetic objective [WM28, WM39, WM45, WM46, WM47].

> 在同一个合成目标上比较终点预测器和引导方法族（梯度、无梯度和多目标）[WM28, WM39, WM45, WM46, WM47]。

When the full text is readable, read the preprint for its baselines, ablations, uncertainty handling and scRNA-seq analysis, and check the blog claims against it [WM27, WM32].

> 当全文可读时，阅读预印本的基线、消融、不确定性处理和 scRNA-seq 分析，并据此核对博客中的论断 [WM27, WM32]。

## 6. Questions for confirmation / 待确认问题

Open decisions for this topic are kept in `data/questions.csv` and listed in `docs/10-open-questions.md`: UQ05 (prediction or decision as the end use), UQ09 (reuse of the labcompass package), UQ10 (non-commercial licences) and UQ20 (the preprint's full text).

> 本主题的待决事项保存在 `data/questions.csv` 中，并列在 `docs/10-open-questions.md` 里：UQ05（最终用途是预测还是决策）、UQ09（是否复用 labcompass 软件包）、UQ10（非商业许可）和 UQ20（预印本全文）。

## 7. Evidence gaps / 证据缺口

The preprint's baselines, ablations, epistemic-uncertainty treatment and scRNA-seq analysis are unknown because only the abstract was obtained (Q138, Q140) [WM27, WM32].

> 预印本的基线、消融、认知不确定性处理和 scRNA-seq 分析均未知，因为只拿到了摘要（Q138，Q140）[WM27, WM32]。

The abstract counts four loops whereas the data chain has eight loop datasets, and the dataset card's citation fields are unfilled, so the card cannot be matched to the paper [WM27, WM29, DS23].

> 摘要计为四轮，而数据链有八个闭环数据集，数据集卡片的引用字段也未填写，因此无法把卡片与论文对应起来 [WM27, WM29, DS23]。

The boundary-only behavior of the KKT variant was inferred from the code and not run [WM28].

> KKT 变体只在边界起作用的行为是从代码推断的，没有运行过 [WM28]。

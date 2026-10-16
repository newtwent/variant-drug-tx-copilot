# 09 LabCompass and decision-oriented world modeling / LabCompass 与面向决策的世界建模

## 1. Scope / 范围

This document analyzes LabCompass, the generative inverse-design framework from Fabian Theis's group, for what it offers to the design of a genotype-aware cell world model. It separates what the sources state about LabCompass (facts LC1 to LC7) from what I infer for this project (the component map and insights I1 to I9), and it ends with actions, questions and evidence gaps. It rests on a preprint seen at abstract level, on code and README pages retrieved in this session, and on third-party summaries; the full paper was not read.

> 本文档分析 Fabian Theis 课题组的生成式逆向设计框架 LabCompass，说明它能为基因型感知的细胞世界模型设计提供什么。它把来源对 LabCompass 的陈述（事实 LC1 至 LC7）与我为本项目所做的推断（组件对照和启示 I1 至 I9）分开，并以行动、问题和证据缺口结尾。它依据的是只读到摘要层面的预印本、本会话中取回的代码和 README 页面，以及第三方摘要；论文全文没有读到。

## 2. Facts and evidence / 事实与证据

LC1 (tier T2, abstract level). The bioRxiv preprint "Generative inverse design steers human hematopoietic cell fate in vitro" (posted early October 2026; Fabian Theis is a corresponding author) introduces LabCompass, an inverse-modeling framework that optimizes experimental designs toward candidates expected to yield specified target cell states, using a flow-matching generative model guided by phenotypes predicted by a forward surrogate. It was tested on primary human CD34+ cultures whose fate is governed by continuous cytokine and small-molecule parameters. In four lab-in-the-loop rounds the authors report that it recovered known lineage-inducing designs, improved its predictions as data arrived, and enriched target populations across lineages, that adding parameters widened the design space, and that different culture conditions reached the same target states. The run produced a 78-million-cell spectral flow cytometry dataset [WM27]. I read only the abstract-level text, not the full paper, and found no peer-reviewed version or independent replication.

> LC1（T2 级，摘要层面）。bioRxiv 预印本《Generative inverse design steers human hematopoietic cell fate in vitro》（2026 年 10 月初发布；Fabian Theis 为通讯作者之一）提出了 LabCompass，这是一个逆向建模框架：用由前向代理模型预测的表型来引导流匹配生成模型，把实验设计优化到预期产生指定目标细胞状态的候选上。它在原代人 CD34+ 培养上进行了测试，细胞命运由连续的细胞因子和小分子参数决定。作者报告，在 4 轮实验室闭环中，它恢复了已知的谱系诱导设计，随着数据到来预测不断改进，并在多个谱系上富集了目标群体；增加参数拓宽了设计空间，不同的培养条件能达到相同的目标状态。整个过程产生了 7,800 万（78 million）个细胞的光谱流式细胞术数据集 [WM27]。我只读到摘要层面的文字，没有读到全文，也没有找到同行评议版本或独立复现。

LC2 (tier T1, official repository page). The reproducibility repository is described on GitHub as the repository for the collaboration with the Göttgens lab on spectral flow cytometry data; which group ran which experiments is not stated in what I read, and one search summary instead attributes the work to the labs of Hornung, Mann and Theis (see [WM31]). Its README calls each wet-lab cycle a loop and documents a pipeline. It builds cumulative loop datasets, trains a forward model (a conditional flow-matching model that maps noise to cell states given the protocol, together with a cell-type classifier), trains a prior over protocols (optionally distilled into a few-step flow-map student), runs loss-guided inverse design that samples candidate protocols (defaults: 50 candidates with 350 forward passes each) while sweeping target cell type, scheduler, optimization type and query type, and re-scores candidates under many noise draws (for example 5,000) [WM29]. That the model-driven designs were then tested in the lab and the measurements fed back is stated in the abstract [WM27].

> LC2（T1 级，官方仓库页面）。该可复现仓库在 GitHub 上被描述为与 Göttgens 实验室合作处理光谱流式细胞术数据的仓库；我读到的内容没有说明哪个团队做了哪些实验，而一份检索摘要则把这项工作归于 Hornung、Mann 和 Theis 的实验室（见 [WM31]）。其 README 把每个湿实验周期称为一个“loop”并记录了一条流程。它构建累积的各轮数据集，训练前向模型（在给定实验方案时把噪声映射到细胞状态的条件流匹配模型，加上细胞类型分类器），训练方案先验（可选地蒸馏为少步流映射学生模型），运行损失引导的逆向设计，在对目标细胞类型、调度器、优化类型和查询类型做扫描的同时采样候选方案（默认：50 个候选，每个 350 次前向传播），并在大量噪声抽样下（例如 5,000 次）对候选重新打分 [WM29]。模型驱动的设计随后在实验室中得到测试且测量结果被反馈回去，这一点由摘要陈述 [WM27]。

LC3 (tier T1, package README and source files). The separate `labcompass` package (BSD-3-Clause, version 0.0.1, Python 3.10 or newer, built on torch, torchdiffeq, POT and AnnData) is described as generative modeling for experimental design in single-cell data. Its forward model is conditional flow matching, with a score-augmented variant and a two-time "flow map" variant for few-step sampling. Perturbation covariates such as drugs, genetic edits, dose or time live in AnnData `.obs`, and each covariate group gets its own encoder. Its `InverseModel` infers covariates by MAP optimization, Langevin sampling or an amortized network (discrete covariates by Gumbel-softmax). Its `TargetPredictionModel` is a supervised proxy that predicts target covariates from cell states [WM28].

> LC3（T1 级，软件包 README 与源文件）。独立的 `labcompass` 软件包（BSD-3-Clause，版本 0.0.1，Python 3.10 或更高，基于 torch、torchdiffeq、POT 和 AnnData）被描述为单细胞数据中面向实验设计的生成建模。其前向模型是条件流匹配，另有带得分的变体，以及用于少步采样的双时间“流映射”变体。药物、基因编辑、剂量或时间等扰动协变量存放在 AnnData 的 `.obs` 中，每个协变量组有自己的编码器。其 `InverseModel` 通过 MAP 优化、Langevin 采样或摊销网络来推断协变量（离散协变量用 Gumbel-softmax）。其 `TargetPredictionModel` 是从细胞状态预测目标协变量的监督代理模型 [WM28]。

LC4 (tier T1, source code). The guidance rule is explicit. `LossGuidedFlow` wraps a pretrained flow-matching model without retraining it. At each time t it predicts the endpoint, by one Euler step that assumes a linear path or by a flow-map jump, evaluates a task loss (plus optional regularizers) at that endpoint, differentiates it with respect to the current state through the network by a vector-Jacobian product, and subtracts the scheduled gradient from the velocity before integrating (Euler, 100 steps by default; no gradient normalization). `ImpliciDualGuidedFlow` replaces the plain loss by a KKT-constrained Lagrangian so that inequality constraints g_i(x1) ≤ 0 can be imposed, with options for a least-squares multiplier solve and an active-set tolerance; the multiplier code itself is in a file (kkt.py) that I did not read. In the package the constrained variable is the terminal state x1 of the guided flow; in the reproducibility pipeline the flow being guided is the prior over protocols, so I infer that the constraints act on protocols [WM28, WM29].

> LC4（T1 级，源代码）。引导规则是明确的。`LossGuidedFlow` 在不重新训练的前提下包装一个预训练的流匹配模型。在每个时间 t，它先预测终点（用假设路径为线性的一步 Euler，或用流映射跳跃），在该终点处计算任务损失（可附加正则项），经网络通过向量-雅可比乘积对当前状态求导，并在积分前从速度场中减去按计划缩放的梯度（Euler，默认 100 步；不做梯度归一化）。`ImpliciDualGuidedFlow` 用受 KKT 约束的拉格朗日量取代普通损失，从而可以施加不等式约束 g_i(x1) ≤ 0，并提供最小二乘求解乘子和活动集容差的选项；乘子代码本身在我没有读过的文件（kkt.py）中。在该软件包中，受约束的变量是被引导的流的终态 x1；在可复现流程中，被引导的流是方案的先验，因此我推断约束作用于方案 [WM28, WM29]。

LC5 (tier T1 for the README's statements, with one unresolved discrepancy). The Hugging Face data, as described by the reproducibility README (the dataset page itself could not be read), hold per-loop AnnData files and 500k-cell subsamples, about 60 GB raw (loop 0 alone is 36 GB), 4.7 GB of derived inputs, 13 GB of inference-only checkpoints, and about 1.07 million unfiltered inverse-design protocols. Each loop's training set is the previous loop's set plus the new measurements, and the chain in the README runs loop0, loop1, loop2, loop2p5, loop3, loop4, loop4p5 and loop5. That is more steps than the "four loops" in the abstract, so the counting convention is unclear [WM29, WM27].

> LC5（README 的陈述为 T1 级，另有一处未解决的出入）。据可复现 README 的描述（数据集页面本身无法读取），Hugging Face 上的数据包含逐轮的 AnnData 文件和 500k（50 万）细胞的子样本，原始数据约 60 GB（仅 loop 0 就有 36 GB），4.7 GB 的衍生输入，13 GB 仅用于推理的检查点，以及约 107 万（1.07 million）个未过滤的逆向设计方案。每一轮的训练集是上一轮训练集加上新的测量，README 中的链条为 loop0、loop1、loop2、loop2p5、loop3、loop4、loop4p5 和 loop5。这比摘要中的“4 轮”步骤更多，因此计数约定不明 [WM29, WM27]。

LC6 (tier T3, third-party and social posts, all seen only through search-tool summaries). A newsletter summary reports that the model was built on a 116-condition screen covering 10 cytokines and small molecules under hypoxia and normoxia, read by 20-color spectral flow cytometry, and that switching to a new target cell type needs no retraining [WM32]. A search excerpt of a post on X by Fabian Theis describes LabCompass as using cellular world models "not just to predict biology, but to help decide what experiment to do next" [WM30]. A LinkedIn post (the author is not verified as a co-author) is summarized as saying that the method was also applied to single-cell transcriptomic data from viral infection and that drug combinations, differentiation and organoids are possible uses, with no details; two summaries disagree on whether the post says the method is not tied to a particular virtual cell model, and a third attributes the work to the labs of Hornung, Mann and Theis, so these points are unresolved [WM31].

> LC6（T3 级，第三方与社交媒体帖子，均只通过检索工具的摘要见到）。一份通讯总结称，该模型建立在一个 116 条件的筛选之上，涵盖缺氧与常氧下的 10 种细胞因子和小分子，用 20 色光谱流式细胞术读出，并且切换到新的目标细胞类型无需重新训练 [WM32]。Fabian Theis 在 X 上一条帖子的检索摘录把 LabCompass 描述为使用细胞世界模型，“不仅用来预测生物学，还用来帮助决定下一步做什么实验” [WM30]。一则 LinkedIn 帖子（作者未证实为共同作者）被概括为：该方法也被应用于病毒感染的单细胞转录组数据，药物组合、分化和类器官是可能的用途，但没有细节；两份摘要对帖子是否说该方法不依赖于某个特定的虚拟细胞模型意见不一，第三份则把这项工作归于 Hornung、Mann 和 Theis 的实验室，因此这些点没有定论 [WM31]。

LC7 (not retrieved). The preprint's full text, its viral-infection analysis, its quantitative results and baselines, and any epistemic-uncertainty treatment beyond noise-draw re-scoring were not available to me, because the bioRxiv and Hugging Face fetches failed (Q123), the bio-research servers did not connect (Q125) and the targeted searches returned only the abstract (Q48, Q112). Statements about those would be guesses, so none are made.

> LC7（未取回）。预印本全文、其病毒感染分析、定量结果与基线，以及除噪声抽样重新打分之外的任何认知不确定性处理，我都没有读到，因为对 bioRxiv 和 Hugging Face 的抓取失败（Q123），bio-research 服务器未能连接（Q125），针对性检索只返回了摘要（Q48、Q112）。关于这些的陈述只能是猜测，因此不作任何陈述。

## 3. Component map to this project / 与本项目的组件对照

The second column states what the sources say each component does (facts). The third column is my proposed role in a genotype-aware world model (a judgment, to be tested).

> 第二列陈述来源所说的各组件的作用（事实）。第三列是我提出的它在基因型感知世界模型中的角色（判断，有待检验）。

| Component | What the sources say it does | Proposed role (judgment) | Source IDs | 说明（中文） |
|---|---|---|---|---|
| Forward model (FlowMatching, FlowMatchingWithScore, FlowMap) | Conditional flow matching from noise to cell states given covariates; a two-time flow map gives few-step sampling | Genotype-conditioned generator of drug-induced cell-state distributions; the baseline ladder of document 08 supplies its competitors | WM28 | 前向模型：条件流匹配，在给定协变量时把噪声映射到细胞状态；双时间流映射给出少步采样；提议角色：基因型条件的药物诱导细胞状态分布生成器，其竞争对手来自文档 08 的基线阶梯 |
| Covariate encoders | Perturbation covariates live in AnnData .obs and each representation has its own encoder | Add genotype as one more covariate group and keep the source population genotype-matched | WM28, MD63 | 协变量编码器：扰动协变量放在 AnnData 的 .obs 中，每种表示有自己的编码器；提议角色：把基因型作为又一个协变量组，并保持源群体与基因型匹配 |
| Prior over protocols | Generative model over plausible protocols, optionally distilled into a few-step student | Prior over drug, dose and combination designs restricted to an available compound library | WM29 | 方案先验：可选地蒸馏为少步学生模型的合理方案生成模型；提议角色：限制在可用化合物库内的药物、剂量和组合设计先验 |
| LossGuidedFlow | Predicts the endpoint by one Euler step or a flow map, takes the gradient of a loss at the endpoint through the network, subtracts the scheduled gradient from the velocity, Euler with 100 steps by default | Objective-guided design: resistance reversal and selective killing | WM28 | LossGuidedFlow：用一步 Euler 或流映射预测终点，经网络对终点处的损失求梯度，从速度场中减去按计划缩放的梯度，默认 Euler 100 步；提议角色：由目标引导的设计：耐药逆转和选择性杀伤 |
| ImpliciDualGuidedFlow | KKT Lagrangian for inequality constraints g_i(x1) <= 0; the multiplier code was not read | Caps on the effect in wild-type contexts, dose bounds and library constraints | WM28 | ImpliciDualGuidedFlow：针对不等式约束 g_i(x1) <= 0 的 KKT 拉格朗日量；乘子代码未读；提议角色：对野生型背景效应的上限、剂量界限和化合物库约束 |
| InverseModel | Infers covariates for a desired target state by MAP optimization, Langevin sampling or an amortized network; discrete covariates by Gumbel-softmax | Amortized proposal of designs when candidate drugs and doses are discrete | WM28 | InverseModel：通过 MAP 优化、Langevin 采样或摊销网络为期望的目标状态推断协变量；离散协变量用 Gumbel-softmax；提议角色：候选药物和剂量为离散时的摊销式设计提议 |
| TargetPredictionModel | Supervised proxy that predicts target covariates from cell states | Surrogate for objectives defined on readouts the forward model does not generate | WM28 | TargetPredictionModel：从细胞状态预测目标协变量的监督代理模型；提议角色：针对前向模型不生成的读出所定义目标的代理 |
| Uncertainty step | Re-scores candidates under many noise draws, for example 5,000 | Extend with ensembles or conformal calibration to cover epistemic uncertainty | WM29 | 不确定性步骤：在大量噪声抽样下（例如 5,000 次）对候选重新打分；提议角色：用集成或共形校准扩展以覆盖认知不确定性 |
| Lab-in-the-loop data chain | Cumulative per-loop datasets and per-loop checkpoints | Retrospective loop benchmark on public data; prospective use only with a wet lab | WM29, DS23 | 实验室闭环数据链：累积的逐轮数据集和逐轮检查点；提议角色：在公开数据上做回溯式循环基准；只有具备湿实验时才能前瞻使用 |

## 4. Judgments / 判断

All items below are judgments drawn from LC1 to LC6, not findings of the paper. "Testable" names the cheapest check.

> 下列各项都是基于 LC1 至 LC6 的判断，不是论文的发现。“可检验”指出最便宜的检验方式。

I1 (confidence: medium-high). Split the world model into replaceable parts: a forward generative model of cell-state distributions given covariates, a prior over actions, and a separate objective model, with a guidance rule connecting them. LabCompass is built exactly this way, and a reported consequence is that a new target needs no retraining [WM28, WM32]. For genotype-by-drug work this means the same forward model could serve several goals, such as resistance reversal and mutant-selective killing, by swapping only the objective. Testable: one forward model, two objectives, both met on held-out contrasts.

> I1（置信度：中高）。把世界模型拆成可替换的部分：给定协变量时细胞状态分布的前向生成模型、动作先验、独立的目标模型，以及连接它们的引导规则。LabCompass 正是这样构建的，据报道其结果是新目标无需重新训练 [WM28, WM32]。对基因型×药物研究而言，这意味着同一个前向模型只需更换目标，就可以服务于多种目的，例如逆转耐药和针对突变体的选择性杀伤。可检验：同一前向模型、两个目标，在留出的对比上都达到。

I2 (confidence: medium). Treat inverse design as guided sampling from a learned action prior, not as scalar optimization. This returns a set of candidates, copes with the many-to-one structure the authors report (different protocols reaching the same state) [WM27], and accepts constraints through the KKT mechanism [WM28]. For drugs, the natural constraints are the available compound library, dose bounds, and a cap on the predicted effect in wild-type cells. Testable in retrospect: do sampled designs enrich the target in held-out conditions better than random or greedy choices?

> I2（置信度：中）。把逆向设计视为从学得的动作先验中做引导采样，而不是标量优化。这样得到的是一组候选，能够应对作者报告的多对一结构（不同方案达到同一状态）[WM27]，并通过 KKT 机制接受约束 [WM28]。对药物而言，自然的约束是可用的化合物库、剂量上限，以及对野生型细胞预测效应的上限。可回溯检验：采样得到的设计在留出条件下对目标的富集是否优于随机或贪心选择？

I3 (confidence: medium). The strongest test of a decision-oriented world model is prospective: propose, measure, update. LabCompass trains each loop on all earlier loops and publishes per-loop checkpoints, so the improvement curve can be inspected [WM29]. With public data only, the achievable analogue is a retrospective loop that reveals conditions in rounds and scores how fast a planner reaches good conditions, as IterPert does on Perturb-seq data with eight acquisition baselines [MD48, MD49]. Testable: build a retro-loop benchmark on Tahoe-100M or sci-Plex and compare planners.

> I3（置信度：中）。对面向决策的世界模型，最强的检验是前瞻性的：提出、测量、更新。LabCompass 的每一轮都在此前所有轮次上训练，并公布逐轮的检查点，因此可以查看改进曲线 [WM29]。仅用公开数据时，可行的类比是回溯式循环：分轮揭示条件，评估规划器多快能到达好的条件，IterPert 在 Perturb-seq 数据上就是这样做的，并比较了八种采集基线 [MD48, MD49]。可检验：在 Tahoe-100M 或 sci-Plex 上建立回溯循环基准并比较规划器。

I4 (confidence: medium). Put genotype into the condition encoder as another covariate group and keep the source population genotype-matched. LabCompass gives each covariate group its own encoder over AnnData columns [WM28], which makes this a column, not a redesign. CellFlow's own PBMC tutorial is reported (through a search summary of the documentation page) to split the control distribution by donor so that one donor's controls are never mapped onto another donor's treated cells [MD61], and State and Stack expose only perturbation, cell type or a donor split column, with no genotype covariate in their READMEs [MD62, MD65]. This also turns hypothesis HA into an ablation: remove the genotype covariate, keep the matched source, and see whether the interaction metric changes. Testable directly.

> I4（置信度：中）。把基因型作为另一个协变量组放进条件编码器，并保持源群体与基因型匹配。LabCompass 为 AnnData 各列的每个协变量组各配一个编码器 [WM28]，所以这只是增加一列，而不是重新设计。据报道（通过对文档页面的检索摘要），CellFlow 自己的 PBMC 教程按供体拆分对照分布，使某个供体的对照永远不会被映射到另一个供体的处理细胞上 [MD61]；而 State 和 Stack 的 README 只暴露扰动、细胞类型或供体拆分列，没有基因型协变量 [MD62, MD65]。这也把假设 HA 变成一个消融实验：去掉基因型协变量，保持匹配的源，看交互指标是否变化。可直接检验。

I5 (confidence: medium). Make actions continuous and modular. The reported expansion of the design space by adding parameters [WM27] implies a conditioning interface that accepts new factors. The same logic supports encoding variant penetrance or allelic dosage as a continuous covariate, in line with the argument of graded-knockdown datasets that knockdown strength should be modeled as continuous [DS18]; whether the large X-Cell model conditions on knockdown strength is not established by the retrieved text [MD57]. Testable: train with a hypomorphic-dose covariate and check dose-ordered predictions on held-out doses.

> I5（置信度：中）。让动作连续且模块化。据报道增加参数可以扩展设计空间 [WM27]，这意味着条件接口可以接受新的因素。同样的逻辑支持把变异的外显程度或等位基因剂量编码为连续协变量，这与梯度敲低数据集主张敲低强度应被建模为连续量的论点一致 [DS18]；大型 X-Cell 模型是否以敲低强度为条件，检索到的文字并未确定 [MD57]。可检验：用亚效等位基因剂量协变量训练，并在留出的剂量上检查按剂量排序的预测。

I6 (confidence: medium). Score candidates under generative noise and under model uncertainty. LabCompass re-scores candidates over thousands of noise draws [WM29], which captures the generative spread but, as far as the README shows, not epistemic uncertainty. With the small genotype counts of the germline track (J1), planning on a confidently wrong model is the main risk, so ensembles or conformal calibration should be added. This is an extension I propose, not something the sources describe.

> I6（置信度：中）。在生成噪声和模型不确定性两种情形下给候选打分。LabCompass 在数千次噪声抽样下重新给候选打分 [WM29]，这捕获了生成的离散程度，但就 README 所示，没有认知不确定性。种系轨道的基因型数量很少（J1），在一个自信但错误的模型上做规划是主要风险，因此应加入集成或共形校准。这是我提出的扩展，不是来源中描述的内容。

I7 (confidence: low-medium). The endpoint predictor matters. The guidance gradient is taken at a predicted endpoint, which by default is a one-step linear extrapolation and can be replaced by a learned flow map [WM28]. If the probability path is curved, the linear extrapolation is biased at early times, and unguided gradients through a classifier can be exploited by regions where the classifier is confidently wrong; the regularizer hook is the place to keep samples near the prior. Testable on a synthetic curved-path problem: compare Euler-endpoint and flow-map-endpoint guidance.

> I7（置信度：低中）。终点预测器很重要。引导梯度是在预测的终点处计算的，默认是一步线性外推，也可以换成学得的流映射 [WM28]。如果概率路径是弯曲的，线性外推在早期时刻会有偏差，而通过分类器的无约束梯度可能被分类器自信出错的区域所利用；正则项的接口正是用来让样本保持在先验附近的地方。可在合成的弯曲路径问题上检验：比较 Euler 终点引导与流映射终点引导。

I8 (confidence: medium). LabCompass supports the decision-making half of a world model but not the dynamics half. Its forward model gives a distribution over end states given a protocol, and the framework plans over protocols; the sources show no multi-step rollout, state update or composition test from the battery in document 06. For trajectories and transitions the better references are PerturbGen, scDiffEq, PRESCIENT and PerturbRx [WM33, WM36, WM37, MD46], and for sequential decisions DiRL [WM35]. A complete cell world model would combine a transition core with a LabCompass-style planner.

> I8（置信度：中）。LabCompass 支持世界模型的决策一半，而不支持动力学一半。其前向模型给出给定方案时终态的分布，框架在方案上做规划；来源中没有显示文档 06 检验清单中的多步展开、状态更新或组合检验。对于轨迹与转移，更好的参考是 PerturbGen、scDiffEq、PRESCIENT 和 PerturbRx [WM33, WM36, WM37, MD46]，对于序贯决策则是 DiRL [WM35]。完整的细胞世界模型应当把转移核心与 LabCompass 式的规划器结合起来。

I9 (confidence: low; a proposal). Two genotype-aware designs follow naturally. Resistance reversal would search drug, dose and combination designs that move a mutant context's predicted response toward the wild-type response. Selective killing would maximize the predicted effect in mutant contexts under a KKT inequality cap on the effect in wild-type contexts. Both need a genotype-aware forward model and a validated objective, for which interpretable readouts such as TF activities from CollecTRI [KB20] and mechanism-fidelity scoring [EV33] are candidates. Testable only after hypotheses HA and HB have been answered.

> I9（置信度：低；一项提案）。两种基因型感知的设计自然随之而来。耐药逆转会搜索药物、剂量和组合设计，使突变背景的预测响应趋近野生型响应。选择性杀伤会在对野生型背景效应设置 KKT 不等式上限的条件下，最大化突变背景中的预测效应。两者都需要基因型感知的前向模型和经过验证的目标，可选的目标有可解释的读出，如来自 CollecTRI 的 TF 活性 [KB20] 和机制保真度评分 [EV33]。只有在回答了假设 HA 和 HB 之后才能检验。

Limits of transfer. The LabCompass readout is protein-level spectral flow cytometry with about 20 colors, not a transcriptome. Its design space is a handful of cytokines, small molecules and oxygen, with no inherited genotype variation. It is a recent, unreviewed preprint whose package is at version 0.0.1. A page-summarizing tool also flagged a validation-loader mistake in `InverseModel.train_inverse_model`, which I could not confirm. So LabCompass transfers as an architecture pattern and a validation philosophy, not as evidence that genotype-aware inverse design works.

> 迁移的局限。 LabCompass 的读出是约 20 色的蛋白水平光谱流式细胞术，而不是转录组。其设计空间只是少数细胞因子、小分子和氧浓度，没有遗传性基因型变异。它是一篇较新的、未经评审的预印本，软件包版本为 0.0.1。网页总结工具还指出 `InverseModel.train_inverse_model` 中有一处验证加载器的错误，我无法确认。因此 LabCompass 可迁移的是一种架构模式和一种验证理念，而不是基因型感知逆向设计行之有效的证据。

## 5. Recommended actions / 行动建议

Run the unit tests of the labcompass package and a toy reproduction before any reuse; the package is at version 0.0.1 under the BSD-3-Clause licence [WM28].

> 在任何复用之前，运行 labcompass 软件包的单元测试和一个玩具级复现；该软件包为 0.0.1 版本，采用 BSD-3-Clause 许可 [WM28]。

Build the retrospective closed-loop benchmark of hypothesis HD on Tahoe-100M or sci-Plex, with random, greedy and acquisition-function planners from the IterPert harness (Apache-2.0) as baselines [DS05, DS15, MD48, MD49].

> 在 Tahoe-100M 或 sci-Plex 上构建假设 HD 的回溯式闭环基准，以 IterPert 框架（Apache-2.0）中的随机、贪心和采集函数规划器为基线 [DS05, DS15, MD48, MD49]。

Add a genotype covariate group with a genotype-matched source population to the forward model and run the HA ablation of document 08 before any design experiment [WM28, MD63].

> 给前向模型加入带基因型匹配源群体的基因型协变量组，并在任何设计实验之前运行文档 08 中的 HA 消融 [WM28, MD63]。

Add epistemic uncertainty (ensembles or conformal calibration) to the planner, because the README shows only re-scoring under generative noise [WM29].

> 给规划器加入认知不确定性（集成或共形校准），因为 README 只显示了在生成噪声下的重新打分 [WM29]。

Compare endpoint predictors (a one-step linear extrapolation against a learned flow map) on a synthetic curved-path problem, and compare gradient guidance with sampling-based search on the same objective [WM28, WM39, WM38].

> 在合成的弯曲路径问题上比较终点预测器（一步线性外推与学得的流映射），并在同一目标上比较梯度引导与基于采样的搜索 [WM28, WM39, WM38]。

When the full text becomes readable, read the LabCompass paper for its baselines, ablations, uncertainty handling and viral-infection analysis, and re-screen the held candidates listed in the search log [WM27].

> 当全文可读时，阅读 LabCompass 论文的基线、消融、不确定性处理和病毒感染分析，并重新筛选检索日志中列出的被搁置候选 [WM27]。

## 6. Questions for confirmation / 待确认问题

Is the end use prediction or decision? Default: prediction first, with decision (hypothesis HD) as an optional last step.

> 最终用途是预测还是决策？默认：预测优先，决策（假设 HD）作为可选的最后一步。

Should the labcompass package serve as a baseline implementation instead of a reimplementation? Default: decide at milestone M2, after its unit tests have run.

> labcompass 软件包是否应作为基线实现，而不是重新实现？默认：在里程碑 M2 时、运行其单元测试之后决定。

Can outbound access to bioRxiv and PubMed be opened so that the full paper can be read? Default: proceed without it, and keep every dependent claim unverified.

> 能否开放对 bioRxiv 和 PubMed 的出站访问，以便读取论文全文？默认：不开放也继续进行，并把所有依赖它的主张都保持为未经核验。

Are non-commercial licences acceptable? Default: the non-commercial State and Stack terms are flagged and no decision is taken on using the models until the licence constraint is known [MD62, MD65].

> 非商业许可是否可以接受？默认：标注 State 和 Stack 的非商业条款，在许可限制明确之前不就是否使用这些模型作出决定 [MD62, MD65]。

## 7. Evidence gaps / 证据缺口

The LabCompass full text was not read, so its baselines, ablations, epistemic-uncertainty treatment and viral-infection analysis are unknown, and the social-media descriptions disagree on some points [WM27, WM31].

> LabCompass 的全文没有读到，因此其基线、消融、认知不确定性处理和病毒感染分析均未知，社交媒体上的描述在某些点上相互矛盾 [WM27, WM31]。

Which group ran the wet-lab work is unclear: the repository description names the Göttgens lab, whereas a search summary attributes the work to other labs, and a targeted search found nothing (queries Q45, Q49 and Q104) [WM29, WM31].

> 湿实验由哪个团队完成并不清楚：仓库描述点名 Göttgens 实验室，而一份检索摘要把这项工作归于其他实验室，针对性检索则一无所获（查询 Q45、Q49 和 Q104）[WM29, WM31]。

The abstract says four loops, whereas the dataset chain has eight stages, so the counting convention is unclear (queries Q49 and Q51) [WM27, WM29]. The Hugging Face dataset page could not be read (query Q123) [DS23].

> 摘要说 4 轮，而数据集链条有八个阶段，因此计数约定不明（查询 Q49 和 Q51）[WM27, WM29]。Hugging Face 数据集页面无法读取（查询 Q123）[DS23]。

A page-summarizing tool flagged a possible validation-loader mistake in the training method of InverseModel, which was not confirmed, and the multiplier code of the KKT variant was not read [WM28].

> 一个网页摘要工具指出 InverseModel 的训练方法中可能有验证加载器的错误，该点未得到确认；KKT 变体的乘子代码也没有读 [WM28]。

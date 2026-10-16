# 05 Perturbation-prediction models / 扰动预测模型

## 1. Scope / 范围

This document surveys the model families that predict transcriptional responses to perturbations and asks one question of each: how could inherited or somatic genotype enter? It covers chemistry-conditioned models, generative flow and diffusion models, the Arc State model, mechanism-informed networks, causal representation learning and simple baselines. Benchmarks and metrics are in document 07, and world-model claims are in document 06.

> 本文档综述预测对扰动的转录响应的模型家族，并对每一类提出一个问题：遗传或体细胞基因型如何进入模型？涵盖以化学为条件的模型、生成式流模型与扩散模型、Arc 的 State 模型、机制导向网络、因果表示学习以及简单基线。基准和指标在文档 07 中，世界模型的主张在文档 06 中。

## 2. Facts and evidence / 事实与证据

Chemistry-conditioned models predict responses to compounds that were not seen in training. chemCPA represents each drug with a fixed Morgan fingerprint derived from its SMILES string [MD01]. PRnet conditions on the compound's SMILES and an unperturbed expression profile, was trained on bulk L1000 and the single-cell sci-Plex3 data, and self-reports an average Pearson correlation of 0.8 on unseen compounds [MD02]. TranSiGen predicts the 978 landmark genes and then infers the rest of the transcriptome, and was evaluated with chemical-blind and cell-blind splits [MD03]. A third-party benchmark reports less favorable numbers on different metrics, so they are not directly comparable: for PRnet on a scaffold split, MAE 0.87 and Spearman 0.50, with TranSiGen similar [MD04].

> 以化学为条件的模型可预测训练中未见过的化合物的响应。chemCPA 用从 SMILES 字符串导出的固定 Morgan 指纹表示每种药物 [MD01]。PRnet 以化合物的 SMILES 和未扰动表达谱为条件，在 bulk L1000 和单细胞 sci-Plex3 数据上训练，自报在未见化合物上的平均 Pearson 相关为 0.8 [MD02]。TranSiGen 预测 978 个 landmark 基因，再推断转录组的其余部分，并用化合物盲和细胞系盲的划分进行评估 [MD03]。一项第三方基准在不同指标上报告了不那么有利的数字，因此二者不能直接比较：PRnet 在骨架划分上 MAE 为 0.87、Spearman 为 0.50，TranSiGen 与之相近 [MD04]。

Generative models treat the response as a shift between cell populations. CellFlow combines optimal-transport pairing of unperturbed and perturbed cells with conditional flow matching, aggregates sets of perturbations in a permutation-invariant way, and uses pretrained embeddings of biological entities for out-of-distribution prediction, often in PCA or VAE latent spaces [MD05]. Diffusion models for single-cell drug response [MD08], discrete diffusion with regulation reinforcement [MD24] and distributional flow matching [MD09] follow the same generative line.

> 生成式模型把响应视为细胞群体之间的偏移。CellFlow 把未扰动与已扰动细胞的最优传输配对和条件流匹配结合起来，以置换不变的方式聚合扰动集合，并使用生物实体的预训练嵌入做分布外预测，通常在 PCA 或 VAE 潜空间中进行 [MD05]。用于单细胞药物响应的扩散模型 [MD08]、带调控强化的离散扩散 [MD24] 以及分布式流匹配 [MD09] 沿着同一条生成式路线。

The Arc State model has two modules: a State Embedding model that represents individual cells and a State Transition model that predicts perturbation effects across cell populations [MD06]. Arc's launch statements report training on observational data from about 170 million cells and perturbational data from over 100 million cells across 70 cell lines, and a 50% gain in perturbation discrimination on Tahoe-100M; these are launch statements, not independent evaluation [MD07].

> Arc 的 State 模型有两个模块：表示单个细胞的 State Embedding 模型，以及预测细胞群体扰动效应的 State Transition 模型 [MD06]。Arc 的发布声明报告其在约 1.7 亿（170 million）个细胞的观测数据和 70 个细胞系中超过 1 亿（100 million）个细胞的扰动数据上训练，并在 Tahoe-100M 上扰动区分度提高 50%；这些是发布声明，不是独立评测 [MD07]。

Mechanism-informed networks put prior biology into the architecture. LEMBAS is a recurrent network on a signaling graph [MD12], and a phosphoproteomic extension can be queried with a perturbation such as drug-target inhibition without providing phosphoproteomic measurements [MD14]. P-NET builds a hierarchical network from 3,007 pathways [MD15], and a simulation study evaluates how such networks perform [MD16].

> 机制导向网络把先验生物学放入架构。LEMBAS 是建立在信号图上的循环网络 [MD12]，其磷酸化蛋白质组扩展可以用药物靶点抑制之类的扰动来查询，而无需提供磷酸化蛋白质组测量 [MD14]。P-NET 由 3,007 条通路构建层级网络 [MD15]，一项模拟研究评估了这类网络的表现 [MD16]。

Causal representation learning treats a perturbation as an intervention on latent variables. The sparse-mechanism-shift model assumes that an intervention changes only a few latent mechanisms, and its benefit shrinks when effects are small [MD17]. A factorized model splits the representation into covariate, treatment and interaction blocks and proves that the interaction block is identifiable component by component [MD18]. Other work reports identifiability for latent dynamical processes [MD19] and for soft interventions [MD20]; a talk abstract claims identifiability with unobserved causal variables under a generalized faithfulness condition, a tier-T3 source with no retrievable year [MD21].

> 因果表示学习把扰动视为对潜变量的干预。稀疏机制偏移模型假设干预只改变少数潜在机制，当效应较小时其收益会下降 [MD17]。一个因子化模型把表示分成协变量、处理和交互三块，并证明交互块可逐分量识别 [MD18]。其他工作报告了潜在动力学过程 [MD19] 和软干预 [MD20] 的可识别性；一份讲座摘要声称在广义忠实性条件下，即使因果变量未被观测也可识别，这是年份无法取得的 T3 级来源 [MD21]。

Simple models are competitive. OCOO-T denoises continuous expression profiles with a plain Transformer and no autoencoder [MD23], and a preprint title states that parameter-free representations outperform single-cell foundation models on downstream benchmarks, which is title-level information only [EV13]. The baseline critique is in document 07.

> 简单模型很有竞争力。OCOO-T 用普通 Transformer 直接对连续表达谱去噪，不使用自编码器 [MD23]，一篇预印本的标题称无参数表示在下游基准上优于单细胞基础模型，这只是标题级信息 [EV13]。基线批判见文档 07。

Current models take perturbation labels, cell type or donor identity as conditions, not inherited donor genotype. PertAdapt attaches a perturbation encoder to a pretrained single-cell model, and its inputs are gene edits [MD11]. pertTF lets embedding weights favor either genotype (perturbation) prediction or cell-type separation, and was transferred from stem-cell-derived data to primary human islets, where donor-level shifts in predicted perturbation states were detected [MD10]. Lingshu-Cell conditions on cell type or donor identity plus perturbation [WM10]. I did not find a model that takes inherited donor genotype as an input (queries Q12 and Q31).

> 当前的模型以扰动标签、细胞类型或供体身份为条件，而不是遗传性的供体基因型。PertAdapt 在预训练的单细胞模型上附加扰动编码器，其输入是基因编辑 [MD11]。pertTF 让嵌入权重偏向基因型（扰动）预测或细胞类型区分，并从干细胞来源的数据迁移到原代人胰岛，在那里检测到预测扰动状态的供体层面偏移 [MD10]。Lingshu-Cell 以细胞类型或供体身份加扰动为条件 [WM10]。我没有找到以遗传性供体基因型为输入的模型（查询 Q12 和 Q31）。

## 3. Model table / 模型表

| Model family | Perturbation representation | Context or genotype input | Source IDs | 说明（中文） |
|---|---|---|---|---|
| chemCPA | Morgan fingerprint of the drug | not retrieved | MD01 | 药物的 Morgan 指纹；上下文输入未取得 |
| PRnet | SMILES of the compound | unperturbed expression profile | MD02 | 化合物的 SMILES；未扰动表达谱 |
| TranSiGen | compound, with chemical-blind splits | cell-blind splits test unseen cell lines | MD03 | 化合物，含化合物盲划分；细胞系盲划分检验未见细胞系 |
| CellFlow | set of perturbations, permutation-invariant | source cell population; pretrained embeddings | MD05 | 扰动集合，置换不变；源细胞群体；预训练嵌入 |
| State | State Transition over cell populations | State Embedding of cells | MD06, MD07 | 细胞群体上的 State Transition；细胞的 State Embedding |
| PertAdapt | gene edits through a perturbation encoder | pretrained single-cell model | MD11 | 通过扰动编码器输入基因编辑；预训练单细胞模型 |
| pertTF | genotype (perturbation) labels | cell type; weights trade off the two | MD10 | 基因型（扰动）标签；细胞类型；权重在两者间权衡 |
| LEMBAS | ligand or target-inhibition input | fixed prior signaling graph | MD12, MD14 | 配体或靶点抑制输入；固定的先验信号图 |
| P-NET | none (classifier) | hierarchy of 3,007 pathways | MD15 | 无（分类器）；由 3,007 条通路构成的层级 |
| Sparse-mechanism-shift models | interventions on latent variables | latent space | MD17, MD18 | 对潜变量的干预；潜空间 |
| OCOO-T | not retrieved | Transformer denoising, no autoencoder | MD23 | 未取得；Transformer 去噪，无自编码器 |

## 4. Judgments / 判断

J4 (confidence: low; untested). A variant may act as a sparse intervention on the transition operator rather than as a global shift of the state. This agrees with reQTLs being sparse across the transcriptome and with the sparse-mechanism-shift literature [MD17, MD18], but it is untested here, and the benefit of the sparsity assumption shrinks when effects are small [MD17].

> J4（置信度：低；未检验）。变异作用于转移算子的方式可能是稀疏干预，而不是对状态的全局偏移。这与 reQTL 在转录组中稀疏、以及稀疏机制偏移文献一致 [MD17, MD18]，但此处尚未检验，且当效应较小时稀疏假设的收益会下降 [MD17]。

J15 (confidence: low). The covariate–treatment–interaction split of the factorized model maps naturally onto genotype, drug and genotype-by-drug interaction, so it is a candidate formalism for the interaction term, but its identifiability results rest on assumptions that real data may not meet [MD18, MD17, MD19].

> J15（置信度：低）。因子化模型的协变量-处理-交互划分可以自然地对应到基因型、药物和基因型×药物交互，因此它是处理交互项的候选形式化框架，但其可识别性结果依赖于真实数据可能不满足的假设 [MD18, MD17, MD19]。

## 5. Recommended actions / 行动建议

Build a baseline ladder with matched capacity and identical splits: the mean response, a drug-wise linear model on the same inputs, and a one-step conditional generative model of the CellFlow or State type. Any proposed architecture must beat every rung on interaction-specific metrics [EV01, MD05, MD06].

> 建立容量匹配、划分相同的基线阶梯：均值响应、在相同输入上的逐药物线性模型，以及 CellFlow 或 State 类型的单步条件生成模型。任何提出的架构都必须在交互项专用指标上击败每一级 [EV01, MD05, MD06]。

Use chemistry encoders only if generalization to unseen compounds matters. In the somatic track with a fixed drug set, the drug can be a categorical label [MD01, MD02].

> 只有当对未见化合物的泛化重要时才使用化学编码器。在药物集合固定的体细胞轨道中，药物可以是类别标签 [MD01, MD02]。

Treat every self-reported performance number as unverified until it is reproduced, and prefer the third-party benchmark numbers where both exist [MD02, MD04].

> 在复现之前，把每个自报的性能数字都视为未经核验，并且在两者都存在时优先采用第三方基准的数字 [MD02, MD04]。

Before relying on a sparse-shift assumption, measure the effect sizes of the genotype contrast in the data at hand [MD17].

> 在依赖稀疏偏移假设之前，先在手头数据中测量基因型对比的效应大小 [MD17]。

## 6. Evidence gaps / 证据缺口

No model that takes inherited donor genotype as input was found (queries Q12 and Q31). CellBox returned no hits (query Q10). The critique of chemCPA specifically was thin (query Q07). Beyond launch statements, the details of the State paper were not retrieved because the primary host could not be reached. No independent head-to-head comparison of generative models on genotype dependence was found.

> 未找到以遗传性供体基因型为输入的模型（查询 Q12 和 Q31）。CellBox 没有命中（查询 Q10）。针对 chemCPA 的批评很少（查询 Q07）。除发布声明外，State 论文的细节没有取回，因为主要站点无法访问。未找到在基因型依赖性上对生成式模型的独立直接比较。

## 7. Source index (category MD) / 来源索引（类别 MD）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:MD:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| MD01 | T2 | [Predicting Cellular Responses to Novel Drug Perturbations at a Single-Cell Resolution (chemCPA)](<https://proceedings.neurips.cc/paper_files/paper/2022/file/aa933b5abc1be30baece1d230ec575a7-Paper-Conference.pdf>) | drugs encoded as Morgan fingerprints | 药物以 Morgan 指纹编码 |
| MD02 | T2 | [Predicting transcriptional responses to novel chemical perturbations using deep generative model for drug discovery (PRnet)](<https://www.nature.com/articles/s41467-024-53457-1>) | SMILES-conditioned; L1000 plus sci-Plex3; average Pearson 0.8 on unseen compounds (self-reported) | 以 SMILES 为条件；L1000 加 sci-Plex3；未见化合物上平均 Pearson 为 0.8（自报） |
| MD03 | T2 | [Deep representation learning of chemical-induced transcriptional profile for phenotype-based drug discovery (TranSiGen)](<https://www.nature.com/articles/s41467-024-49620-3>) | predicts 978 landmark genes then extends to the transcriptome; chemical-blind and cell-blind splits | 先预测 978 个 landmark 基因再外推到全转录组；化合物盲与细胞系盲划分 |
| MD04 | T2 | [ExPO: an exposure-conditioned neural operator for L1000 signature prediction](<https://link.springer.com/article/10.1186/s13321-026-01226-1>) | third-party benchmark: PRnet on a scaffold split gives MAE 0.87 and Spearman 0.50 | 第三方基准：PRnet 在骨架划分上 MAE 为 0.87，Spearman 为 0.50 |
| MD05 | T2 | [CellFlow enables generative single-cell phenotype modeling with flow matching](<https://www.biorxiv.org/content/10.1101/2025.04.11.648220v1.full.pdf>) | optimal-transport pairing plus conditional flow matching; permutation-invariant aggregation of perturbation sets; pretrained embeddings | 最优传输配对加条件流匹配；对扰动集合做置换不变聚合；预训练嵌入 |
| MD06 | T2 | [Predicting cellular responses to perturbation across diverse contexts with State](<https://www.cell.com/cell/fulltext/S0092-8674(26)00921-9>) | State Embedding plus State Transition modules | State Embedding 加 State Transition 两个模块 |
| MD07 | T3 | [Arc: State release and tool pages](<https://arcinstitute.org/news/virtual-cell-model-state>) | release claims about 170 million observational and over 100 million perturbation cells across 70 cell lines, and +50% perturbation discrimination on Tahoe-100M (launch statements) | 发布声明称约 1.7 亿（170 million）观测细胞和超过 1 亿（100 million）扰动细胞、70 个细胞系，在 Tahoe-100M 上扰动区分度提高 50%（均为发布声明） |
| MD08 | T2 | [scPPDM: A Diffusion Model for Single-Cell Drug-Response Prediction](<https://arxiv.org/pdf/2510.11726>) | — | — |
| MD09 | T2 | [scDFM: Distributional Flow Matching Model for Robust Single-Cell Perturbation Prediction](<https://arxiv.org/pdf/2602.07103>) | — | — |
| MD10 | T2 | [pertTF: context-aware AI modeling for genome-scale and cross-system perturbation prediction](<https://pmc.ncbi.nlm.nih.gov/articles/PMC13015719/>) | embedding weights tune genotype versus cell-type emphasis; hPSC to human islet transfer | 嵌入权重可调节基因型与细胞类型的侧重；从 hPSC 迁移到人胰岛 |
| MD11 | T2 | [PertAdapt: Unlocking Single-Cell Foundation Models for Genetic Perturbation Prediction via Condition-Sensitive Adaptation](<https://www.biorxiv.org/content/10.1101/2025.11.21.689655.full.pdf>) | inputs are gene edits, not donor genotype | 输入是基因编辑，而不是供体基因型 |
| MD12 | T2 | [A mechanism-informed deep neural network enables prioritization of regulators that drive cell state transitions (LEMBAS)](<https://www.nature.com/articles/s41467-025-56475-9>) | signaling-network RNN with weights restricted to real interactions | 信号网络 RNN，权重限制在真实相互作用上 |
| MD13 | T2 | [Biologically informed neural network models are robust to spurious interactions via self-pruning](<https://academic.oup.com/bioinformatics/article/42/8/btag556/8742075>) | GPU version more than 7-fold faster; false edges pruned with sufficient L2 | GPU 版本快 7 倍以上；足够的 L2 正则下错误边被剪除 |
| MD14 | T2 | [Zero-shot prediction of drug responses using biologically informed neural networks trained on phosphoproteomic timeseries](<https://pmc.ncbi.nlm.nih.gov/articles/PMC13035234/>) | a perturbation such as target inhibition can be specified without measurements | 可直接指定扰动（如靶点抑制）而无需测量 |
| MD15 | T2 | [Biologically informed deep neural network for prostate cancer classification and discovery (P-NET)](<https://www.biorxiv.org/content/10.1101/2020.12.08.416446v1.full>) | hierarchical network from 3,007 pathways | 由 3,007 条通路构建的层级网络 |
| MD16 | T2 | [Simulation and empirical evaluation of biologically-informed neural network performance](<https://www.biorxiv.org/content/10.1101/2025.11.13.687845.full.pdf>) | — | — |
| MD17 | T2 | [Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling](<https://arxiv.org/pdf/2211.03553>) | perturbations as latent interventions; benefit of sparsity shrinks when effects are small | 把扰动视为潜空间干预；效应较小时稀疏假设的收益下降 |
| MD18 | T2 | [Learning Identifiable Factorized Causal Representations of Cellular Responses](<https://proceedings.neurips.cc/paper_files/paper/2024/file/dc4f891373d19087d1ddda33e81e00e4-Paper-Conference.pdf>) | covariate / treatment / interaction blocks; interaction block component-wise identifiable | 协变量 / 处理 / 交互三块表示；交互块分量可识别 |
| MD19 | T2 | [Learning Latent Dynamical Causal Processes for Single-Cell Perturbation Prediction](<https://arxiv.org/pdf/2605.25581>) | — | — |
| MD20 | T2 | [Identifiability Guarantees for Causal Disentanglement from Soft Interventions](<https://arxiv.org/pdf/2307.06250>) | — | — |
| MD21 | T3 | [Causal representation learning of genetic perturbations: identifiability and combinatorial extrapolation (Broad talk abstract)](<https://www.broadinstitute.org/talks/tbd-5>) | talk abstract, year not retrieved | 讲座摘要，年份未取得 |
| MD22 | T2 | [What Makes a Representation Good for Single-Cell Perturbation Prediction?](<https://arxiv.org/pdf/2605.19343>) | — | — |
| MD23 | T2 | [OCOO-T: A Simple and Scalable Virtual Cell Model for Transcriptional Perturbation Response Prediction](<https://arxiv.org/pdf/2606.12838>) | Transformer denoising without autoencoders | 不用自编码器的 Transformer 去噪 |
| MD24 | T2 | [D²R²: Discrete Diffusion with Regulation Reinforcement for Single-Cell Perturbation Prediction](<https://arxiv.org/pdf/2608.15288>) | — | — |
| MD25 | T2 | [Generalizable single-cell perturbation response prediction using energy-guided flow matching](<https://arxiv.org/html/2610.02232>) | peripheral | 外围条目 |
| MD26 | T2 | [TempoBridge: Source-Conditioned Flow Matching with Optimal Transport Couplings for Single-Cell Population Transitions](<https://arxiv.org/html/2610.04945>) | peripheral | 外围条目 |
| MD27 | T2 | [DRIFT: Disentangled Responsive-Invariant Flow Transport for Single-Cell Perturbation Prediction](<https://arxiv.org/html/2609.35106v1>) | peripheral | 外围条目 |
| MD28 | T2 | [StateXDiff: Cell State-Contextualized Multimodal Diffusion for Single-Cell Perturbation Prediction](<https://arxiv.org/pdf/2605.16104>) | peripheral | 外围条目 |
| MD29 | T2 | [GeneSpeak-FP: Target and Compound Retrieval from Observed Cell-Level Perturbation Signatures](<https://arxiv.org/pdf/2607.17671>) | peripheral | 外围条目 |
| MD30 | T2 | [LLM-Guided Retrieval for Prediction of Molecular Perturbation Responses](<https://arxiv.org/pdf/2608.01734>) | peripheral | 外围条目 |
| MD31 | T2 | [GeneMamba: An Efficient and Effective Foundation Model on Single Cell Data](<https://arxiv.org/pdf/2504.16956>) | peripheral | 外围条目 |
| MD32 | T2 | [Learning Cross-Domain Representations for Transferable Drug Perturbations on Single-Cell Transcriptional Responses](<https://arxiv.org/pdf/2412.19228>) | peripheral | 外围条目 |
| MD33 | T2 | [Interpretable Modeling of Single-cell perturbation Responses to Novel Drugs Using Cycle Consistence Learning](<https://arxiv.org/pdf/2311.10315>) | peripheral | 外围条目 |
| MD34 | T2 | [Condition-Controlled optimal transport for cellular perturbation response prediction](<https://link.springer.com/article/10.1007/s10489-026-07521-6>) | peripheral | 外围条目 |
| MD35 | T3 | [xTrimoSCPerturb (VCC 2025 first place, BioMap; improves scFoundation; via news)](<https://www.genengnews.com/topics/artificial-intelligence/neurips-2025-altos-labs-wins-generalist-prize-at-arcs-virtual-cell-challenge/>) | secondary | 二手 |
<!-- source-index:MD:end -->

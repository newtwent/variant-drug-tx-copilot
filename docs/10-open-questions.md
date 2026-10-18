# 10 Open questions / 待确认问题

## 1. How to answer / 如何回答

Each question below has a default that stays in force until it is answered, and each says what to change if the answer differs. To answer, edit the `answer` and `status` columns of the question's row in `data/questions.csv` and commit: use `answered` and write the answer in any language when it differs from the default, use `default` when you confirm the default, and set `answered_on` to the date. The next round applies the answers, writes the date in `applied_on`, adds new questions, and keeps every row listed.

> 下面每个问题都有一个默认值，在回答之前一直有效，并说明答案不同时要改什么。要回答，请编辑 `data/questions.csv` 中该问题所在行的 `answer` 和 `status` 列并提交：答案与默认值不同时用 `answered` 并以任意语言写下答案，确认默认值时用 `default`，并把 `answered_on` 设为日期。下一轮会应用这些回答，在 `applied_on` 中写入日期，加入新问题，并保留每一行。

A `decision` is a choice that belongs to the owner, `missing-information` is something that could not be retrieved or inferred, and `attention` is a limit or risk that the owner should know about. The questions that need your attention come first, and this file is generated from the CSV by `tools/fill_tables.py`, so edit the CSV and not this file.

> `decision` 是属于所有者的选择，`missing-information` 是无法取回或推断的信息，`attention` 是所有者应当知道的局限或风险。需要你关注的问题排在最前面；本文件由 `tools/fill_tables.py` 根据 CSV 生成，所以请编辑 CSV 而不是本文件。

## 2. Needs your attention / 需要你关注

<!-- questions-attention:start -->

**UQ01** (decision; needs your attention; status: open). Which variant track should the first analyses target: somatic (cancer cell lines and tumors), germline (donors and inherited variants), or both? Why: The tracks differ in effect size, data and confounding. Public somatic data are large (Tahoe-100M has 50 cell lines with driver annotation [DS07]), whereas germline response-eQTL studies cover tens of individuals (45 individuals in the doxorubicin study [GD06]). Default: Both tracks in parallel, somatic first; germline data serve external validation and priors. If the answer differs: If germline only: make the response-eQTL datasets (GD06, GD10, GD49) the primary data and demote Tahoe-100M to a method testbed. If somatic only: keep the germline rows for priors and drop the germline milestones of document 08. Affects: docs/00, docs/02, docs/08.

> **UQ01**（决策；需要你关注；状态：open）。首批分析应瞄准哪条变异轨道：体细胞（癌症细胞系和肿瘤）、种系（供体和遗传性变异），还是两者？ 原因：两条轨道在效应大小、数据和混杂上不同。公开的体细胞数据规模大（Tahoe-100M 有 50 个带驱动突变注释的细胞系 [DS07]），而种系响应 eQTL 研究只涵盖数十个个体（阿霉素研究中为 45 个个体 [GD06]）。 默认值：两条轨道并行，体细胞优先；种系数据用于外部验证和先验。 若答案不同：若只做种系：把响应 eQTL 数据集（GD06、GD10、GD49）作为主要数据，并把 Tahoe-100M 降为方法试验场。若只做体细胞：保留种系条目作先验，并删去文档 08 中的种系里程碑。 影响范围：docs/00, docs/02, docs/08。

**UQ04** (decision; needs your attention; status: open). May new data be generated (for example a donor-genotyped drug Perturb-seq pilot), and what data and compute budget applies? Why: The plan assumes public data only. No retrieved dataset pairs inherited genotype, a drug and a single-cell transcriptome beyond tens of individuals [GD10, GD49], so the germline track stays limited to small samples unless new data are produced. Default: No new data; public data only. Compute is unspecified, so the first analyses use methods that run on a workstation. If the answer differs: If new data are allowed, add a pilot design to document 02 and document 08 and revisit the power of HA; if a large compute budget exists, allow pretraining-scale models in documents 05 and 06. Affects: docs/02, docs/03, docs/08.

> **UQ04**（决策；需要你关注；状态：open）。能否产生新数据（例如带供体基因型的药物 Perturb-seq 先导实验），数据和算力预算是多少？ 原因：方案假定只用公开数据。检索到的数据集中，没有哪个把遗传性基因型、药物和单细胞转录组配对到数十个个体以上 [GD10, GD49]，因此除非产生新数据，种系轨道只能停留在小样本。 默认值：不产生新数据，仅用公开数据。算力未作规定，因此首批分析使用可在工作站上运行的方法。 若答案不同：若允许新数据，就在文档 02 和文档 08 中加入先导实验设计并重新评估 HA 的检验功效；若有大量算力，则在文档 05 和 06 中允许预训练规模的模型。 影响范围：docs/02, docs/03, docs/08。

**UQ05** (decision; needs your attention; status: open). Is the end use to predict transcriptional responses, or to decide which drug and dose to give for a genotype? Why: Decision quality needs an action prior and a retrospective closed-loop test (hypothesis HD) in addition to prediction accuracy; LabCompass frames the world model as a tool for deciding the next experiment [WM27, WM28]. Default: Prediction first; decision (HD) is an optional last step, to be asked again after the first HA result. If the answer differs: If decision is the goal, move the action prior, guidance and the retrospective loop (documents 06, 08 and 09) to the first milestones and score with decision metrics instead of gene-level error. Affects: docs/00, docs/06, docs/08, docs/09.

> **UQ05**（决策；需要你关注；状态：open）。最终用途是预测转录响应，还是为某个基因型决定给哪种药物和剂量？ 原因：决策质量除预测准确度外，还需要动作先验和回溯式闭环检验（假设 HD）；LabCompass 把世界模型表述为决定下一个实验的工具 [WM27, WM28]。 默认值：预测优先；决策（HD）是可选的最后一步，在得到第一个 HA 结果后再次询问。 若答案不同：若目标是决策，就把动作先验、引导和回溯式闭环（文档 06、08 和 09）提前到首批里程碑，并用决策指标而不是基因层面的误差来评分。 影响范围：docs/00, docs/06, docs/08, docs/09。

**UQ06** (decision; needs your attention; status: open). Is a negative result on HA (genotype adds nothing beyond the baseline state) an acceptable outcome, and what result would end variant-specific modeling? Why: The interaction is a difference of differences and is expected to be small, so a negative result is plausible; a stopping rule prevents effort on a model that cannot be falsified. Default: Yes. Stop variant-specific modeling if, in lineage-matched contrasts with enough lines per arm, adding genotype to a baseline-conditioned model does not reduce interaction-level error beyond the spread across resamples of lines; continue with baseline-conditioned models. If the answer differs: If a negative result is not acceptable, keep modeling with new data (UQ04) or a different target, and rewrite the stopping rule in document 08. Affects: docs/08.

> **UQ06**（决策；需要你关注；状态：open）。在 HA 上得到阴性结果（基因型在基线状态之外没有任何增益）是否可以接受？什么结果会终止针对变异的建模？ 原因：交互项是差值的差值，预计很小，因此阴性结果是可能的；终止规则可避免把精力花在无法证伪的模型上。 默认值：可以。如果在每臂有足够细胞系的、按谱系匹配的对比中，把基因型加入以基线为条件的模型并不能使交互层面的误差降低到超出细胞系重抽样的离散度，就停止针对变异的建模，转而继续使用以基线为条件的模型。 若答案不同：若阴性结果不可接受，就借助新数据（UQ04）或另一个目标继续建模，并改写文档 08 中的终止规则。 影响范围：docs/08。

**UQ08** (decision; needs your attention; status: open). Which variant class and which concrete variants should be modeled first? Why: In Tahoe-100M, TP53 is annotated in 33 of 50 lines, KRAS in 24, CDKN2A in 22 and BRAF in 9 (derived, DS07, Q137), but lineage-matched arms are small (TP53 in lung: 12 mutant versus 3 other lines). Nutlin responses switch with TP53 status [GD45]. Default: Somatic variants with large effects, starting with TP53 status for MDM2-pathway drugs [GD45] and BRAF V600E for MAPK-pathway drugs, on lineage-matched contrasts. If the answer differs: Name the variants and the drug panel; the HA contrast table of document 03 and the milestones of document 08 are rebuilt for them. Affects: docs/03, docs/08.

> **UQ08**（决策；需要你关注；状态：open）。应先对哪一类变异、哪些具体变异建模？ 原因：在 Tahoe-100M 中，50 个系里 TP53 有 33 个被注释，KRAS 有 24 个，CDKN2A 有 22 个，BRAF 有 9 个（推导，DS07，Q137），但按谱系匹配的各臂很小（肺中 TP53：12 个突变系对 3 个其他系）。Nutlin 的响应随 TP53 状态切换 [GD45]。 默认值：效应大的体细胞变异，从 MDM2 通路药物的 TP53 状态 [GD45] 和 MAPK 通路药物的 BRAF V600E 开始，使用按谱系匹配的对比。 若答案不同：指定变异和药物面板；文档 03 的 HA 对比表和文档 08 的里程碑据此重建。 影响范围：docs/03, docs/08。

**UQ10** (decision; needs your attention; status: open). Are non-commercial or conflicting licences acceptable for the models, code and data this project may use? Why: State and Stack weights are non-commercial [MD62, MD65], and Stack says Apache-2.0 in setup.cfg but CC BY-NC-SA 4.0 in the README [MD65]; cellflow says MIT in LICENSE but PolyForm-Noncommercial in pyproject.toml [MD63]; X-Atlas/Orion is CC BY-NC-SA 4.0 [DS24]; the Parse PBMC data are CC BY-NC 4.0 [DS16]; the Systema repository has no LICENSE file [EV36]. Default: Acceptable for non-commercial research only; each asset is flagged, and none is built into the design until the owner confirms the intended use. If the answer differs: If commercial use is intended, replace non-commercial assets with permissive ones (documents 03 and 05) and resolve the conflicting licences with their owners. Affects: docs/03, docs/05, docs/09.

> **UQ10**（决策；需要你关注；状态：open）。对本项目可能使用的模型、代码和数据，非商业许可或相互冲突的许可是否可以接受？ 原因：State 和 Stack 的权重为非商业 [MD62, MD65]，Stack 在 setup.cfg 中写 Apache-2.0，在 README 中却写 CC BY-NC-SA 4.0 [MD65]；cellflow 在 LICENSE 中写 MIT，在 pyproject.toml 中却写 PolyForm-Noncommercial [MD63]；X-Atlas/Orion 为 CC BY-NC-SA 4.0 [DS24]；Parse 的 PBMC 数据为 CC BY-NC 4.0 [DS16]；Systema 仓库没有 LICENSE 文件 [EV36]。 默认值：仅对非商业研究可接受；每项资产都已标注，在所有者确认预期用途之前，不把任何一项纳入设计。 若答案不同：若预期商业使用，就用宽松许可的资产替换非商业资产（文档 03 和 05），并与所有者澄清相互冲突的许可。 影响范围：docs/03, docs/05, docs/09。

**UQ16** (decision; needs your attention; status: open). Should open-ended literature collection stop now so that the HA mediation test on public data begins, or should another search round run first? Why: As of 2026-10-17 the knowledge base holds 246 active sources, and the central uncertainty (does genotype add signal beyond the baseline state?) is empirical rather than a matter of more reading. The stop rule of the search log (two rounds that add fewer than 3 sources) is not met, because the screening of held candidates added 21. Default: Stop open-ended collection; run targeted searches only when an analysis needs a specific fact; design the HA test next. If the answer differs: Plan another search round from the leads in the search log and apply the screening protocol of CLAUDE.md section 10. Affects: docs/08, docs/search-log.

> **UQ16**（决策；需要你关注；状态：open）。是否现在停止开放式的文献收集、开始在公开数据上做 HA 中介检验，还是先再做一轮检索？ 原因：截至 2026-10-17，知识库有 246 条 active 来源，而核心的不确定性（基因型在基线状态之外是否带来信号？）是经验性的，不靠多读文献能解决。检索日志的停止规则（连续两轮新增来源少于 3 条）尚未满足，因为对搁置候选的筛选新增了 21 条。 默认值：停止开放式收集；只有当某项分析需要具体事实时才做针对性检索；下一步设计 HA 检验。 若答案不同：依据检索日志中的线索安排下一轮检索，并应用 CLAUDE.md 第 10 节的筛选协议。 影响范围：docs/08, docs/search-log。

**UQ17** (missing-information; needs your attention; status: open). Do the donors of the large cytokine and drug datasets have genotypes, or can they be genotyped: the 12 donors of the Parse PBMC data [DS16], the 3 donors of OP3 [DS17] and the 40 donors reported for the Stack post-training data [MD42]? Why: Without genotypes these datasets are donor-covariate data, not genotype-by-drug data, and cannot test HA at the germline level. Default: Assume no genotypes; use the datasets for held-out-donor and response-variance tests only. If the answer differs: If genotypes exist, move the datasets to the germline track in document 02 and document 03 and add reQTL-style tests. Affects: docs/02, docs/03.

> **UQ17**（缺失信息；需要你关注；状态：open）。大型细胞因子和药物数据集的供体是否有基因型或能否做基因分型：Parse PBMC 数据的 12 名供体 [DS16]、OP3 的 3 名供体 [DS17]，以及 Stack 后训练数据中报告的 40 名供体 [MD42]？ 原因：没有基因型，这些数据集只是带供体协变量的数据，而不是基因型×药物数据，无法在种系层面检验 HA。 默认值：假定没有基因型；这些数据集只用于留出供体和响应方差的检验。 若答案不同：若有基因型，就在文档 02 和文档 03 中把这些数据集移入种系轨道，并加入 reQTL 式检验。 影响范围：docs/02, docs/03。

**UQ21** (missing-information; needs your attention; status: open). Is wet-lab capacity available for a prospective closed loop (genotype-defined cell lines, drug and dose panels, a transcriptome readout)? Why: Without it, HD can be tested only retrospectively on public data; the LabCompass loops were run on real cultures [DS23] in eight chained loop datasets [WM29]. Default: No wet-lab capacity; only retrospective loops on public data are planned. If the answer differs: Design a prospective loop on the eight-loop structure of the LabCompass data [WM29] and budget it (documents 08 and 09). Affects: docs/08, docs/09.

> **UQ21**（缺失信息；需要你关注；状态：open）。是否有湿实验能力来做前瞻性闭环（基因型明确的细胞系、药物和剂量面板、转录组读出）？ 原因：没有它，HD 只能在公开数据上回溯式检验；LabCompass 的闭环在真实培养物上运行 [DS23]，共有八个相互衔接的闭环数据集 [WM29]。 默认值：没有湿实验能力；只计划在公开数据上做回溯式闭环。 若答案不同：按 LabCompass 数据的八个闭环结构 [WM29] 设计前瞻性闭环并编制预算（文档 08 和 09）。 影响范围：docs/08, docs/09。

**UQ22** (attention; needs your attention; status: open). Do you accept that the drug-target and mechanism labels in Tahoe-100M are model-proposed and vendor-validated, not measured, and therefore not ground truth for drug-class stratification? Why: The dataset card describes the labels as proposed by a model and validated against a vendor catalogue [DS07]. Default: Yes; treat the labels as hints and build the drug-class table from an independent curated source before stratifying. If the answer differs: If the labels are accepted as given, skip the independent mapping and state the limitation in document 03. Affects: docs/03, docs/08.

> **UQ22**（关注事项；需要你关注；状态：open）。你是否接受 Tahoe-100M 中的药物靶点和作用机制标签由模型提出、经厂商验证而非实测，因此不能作为药物类别分层的真值？ 原因：数据集卡片把这些标签描述为由模型提出、对照厂商目录验证 [DS07]。 默认值：接受；把标签当作提示，在分层之前用独立的整理来源建立药物类别表。 若答案不同：若按原样接受这些标签，就跳过独立映射，并在文档 03 中说明这一局限。 影响范围：docs/03, docs/08。

**UQ23** (attention; needs your attention; status: open). Do you accept restricting the HA test to lineage-matched contrasts with small arms, and calling a line non-mutant only for the gene tested? Why: Every Tahoe-100M line has at least one annotated driver, so non-mutant lines are not wild type; in the 12 lineage-matched contrasts computed, the smaller arm holds 1 to 6 lines (TP53 in lung: 12 versus 3), so power is limited (derived, DS07, Q137). Default: Yes; report power and effect sizes with uncertainty. If the answer differs: If more power is required, add datasets with more lines or engineered isogenic data [GD46, GD54] and revisit document 03. Affects: docs/03, docs/08.

> **UQ23**（关注事项；需要你关注；状态：open）。你是否接受把 HA 检验限制在各臂很小的、按谱系匹配的对比上，并且只就被检验的基因把一个系称为非突变系？ 原因：Tahoe-100M 的每个细胞系至少有一个被注释的驱动突变，因此非突变系并非野生型；在已计算的 12 个按谱系匹配的对比中，较小的一臂有 1 至 6 个系（肺中 TP53：12 对 3），因此检验功效有限（推导，DS07，Q137）。 默认值：接受；报告检验功效和带不确定性的效应大小。 若答案不同：若需要更高的检验功效，就加入细胞系更多的数据集或工程化同基因数据 [GD46, GD54]，并重新审视文档 03。 影响范围：docs/03, docs/08。

<!-- questions-attention:end -->

## 3. Other decisions and missing information / 其他决策与缺失信息

<!-- questions-optional:start -->

**UQ02** (decision; optional; status: open). Which drug classes and cell types should the first model cover? Why: Priors and data coverage depend on the choice. Tahoe-100M spans 379 drugs on 50 cell lines [DS07], and every restriction also shrinks the number of lineage-matched mutant-versus-other arms. Default: No restriction; annotate every analysis by drug class and lineage, and use lineage-matched contrasts. If the answer differs: Fix the list of drug classes in document 04 and document 08, restrict the Tahoe-100M slices accordingly, and recount the contrast arms (derived, DS07, Q137). Affects: docs/04, docs/05, docs/08.

> **UQ02**（决策；可选；状态：open）。第一个模型应覆盖哪些药物类别和细胞类型？ 原因：先验和数据覆盖取决于这一选择。Tahoe-100M 涵盖 50 个细胞系上的 379 种药物 [DS07]，而每一项限制也会缩小按谱系匹配的突变株对其他株的各臂规模。 默认值：不设限制；每项分析都按药物类别和谱系标注，并使用按谱系匹配的对比。 若答案不同：在文档 04 和文档 08 中确定药物类别清单，相应限制 Tahoe-100M 的切片，并重新统计对比各臂（推导，DS07，Q137）。 影响范围：docs/04, docs/05, docs/08。

**UQ03** (decision; optional; status: open). Is the operational definition of "world model" recorded in document 06 acceptable as the working definition for this project? Why: The definition decides which tests count as evidence for a world model (hypothesis HC): a model with a persistent state and an action-conditioned transition can be compared with conditional generative and linear baselines. Default: Yes; the definition of document 06 is kept as falsifiable items in document 08. If the answer differs: Rewrite the definition in document 06 and the HC tests in document 08; if the term is dropped, HC becomes a comparison of architectures only. Affects: docs/06, docs/08.

> **UQ03**（决策；可选；状态：open）。文档 06 中记录的“世界模型”操作性定义，是否可以作为本项目的工作定义？ 原因：该定义决定哪些检验可作为世界模型的证据（假设 HC）：带有持久状态和动作条件转移的模型，可以与条件生成模型和线性基线比较。 默认值：可以；文档 06 的定义以可证伪项的形式保存在文档 08 中。 若答案不同：改写文档 06 中的定义和文档 08 中的 HC 检验；若放弃该术语，HC 就只是架构之间的比较。 影响范围：docs/06, docs/08。

**UQ07** (decision; optional; status: open). Is the order HA, HB, HC, HD acceptable, with the world-model test (HC) after the mediation and sparse-shift tests? Why: If genotype adds nothing beyond the baseline state (HA), the later tests are moot. Default: Yes. If the answer differs: Reorder the milestones M0 to M6 in document 08. Affects: docs/08.

> **UQ07**（决策；可选；状态：open）。按 HA、HB、HC、HD 的顺序、把世界模型检验（HC）放在中介和稀疏转变检验之后，是否可以接受？ 原因：如果基因型在基线状态之外没有任何增益（HA），后面的检验就无从谈起。 默认值：可以。 若答案不同：重新排列文档 08 中的里程碑 M0 至 M6。 影响范围：docs/08。

**UQ09** (decision; optional; status: open). Should the labcompass package serve as a baseline implementation (conditional flow-matching forward model with guidance) instead of a reimplementation? Why: The code is BSD-3 and documents a protocol prior and guided inverse design [WM28, WM29], but version 0.0.1 uses synthetic examples, its tests were not read, and no genotype handling appears in the files read. Default: Decide when the first baseline is built (document 08); no dependency before that. If the answer differs: If reuse is chosen now, add the package to the plan and pin its version; if not, reimplement the guidance rule described in document 09. Affects: docs/06, docs/08, docs/09.

> **UQ09**（决策；可选；状态：open）。labcompass 软件包是否应作为基线实现（带引导的条件流匹配前向模型），而不是重新实现？ 原因：代码采用 BSD-3 许可，并记录了方案先验和引导式逆向设计 [WM28, WM29]，但 0.0.1 版本使用合成示例，其测试没有读过，所读文件中也没有基因型处理。 默认值：在构建第一个基线时决定（文档 08）；在此之前不产生依赖。 若答案不同：若现在选择复用，就把该软件包加入计划并固定版本；否则按文档 09 所述重新实现引导规则。 影响范围：docs/06, docs/08, docs/09。

**UQ11** (decision; optional; status: open). Should pharmacokinetic (class 5) gene variants be excluded from the main pharmacodynamic analysis or modeled in a separate branch? Why: PK variants change exposure and confound a pharmacodynamic question, but a separate branch would need exposure data. Default: Tagged class 5 and excluded from the main pharmacodynamic analysis. If the answer differs: Add a PK branch with exposure as a covariate and extend document 01 and the pharmacogenomic rows of document 04. Affects: docs/01, docs/04.

> **UQ11**（决策；可选；状态：open）。药代动力学（类别 5）基因变异应排除在主要药效动力学分析之外，还是在单独的分支中建模？ 原因：PK 变异改变暴露量，会混杂药效动力学问题，但单独的分支需要暴露量数据。 默认值：标记为类别 5，并排除在主要药效动力学分析之外。 若答案不同：加入以暴露量为协变量的 PK 分支，并扩充文档 01 和文档 04 中的药物基因组学条目。 影响范围：docs/01, docs/04。

**UQ12** (decision; optional; status: open). Should the first prior network be restricted to the signaling pathways of the drug classes in scope? Why: A restricted network is smaller and easier to interpret, but it cannot be chosen before the drug classes (UQ02) are fixed. Default: No restriction until the drug classes are chosen (UQ02). If the answer differs: Restrict the prior resources of document 04 to the chosen pathways and rebuild the graph. Affects: docs/04.

> **UQ12**（决策；可选；状态：open）。第一版先验网络是否应限制在所涉药物类别的信号通路上？ 原因：受限的网络更小、更易解释，但在药物类别（UQ02）确定之前无法选定。 默认值：在选定药物类别（UQ02）之前不设限制。 若答案不同：把文档 04 中的先验资源限制在选定的通路上并重建图。 影响范围：docs/04。

**UQ13** (decision; optional; status: open). Should the 2026 Virtual Cell Challenge only be recorded, or also used as an external benchmark? Why: It concerns CRISPRi knockdowns in cell lines, not genotype-by-drug effects [EV07, EV09]. Default: Recorded only; not entered. If the answer differs: Add a benchmark protocol and a milestone to document 07 and document 08. Affects: docs/07, docs/08.

> **UQ13**（决策；可选；状态：open）。2026 年虚拟细胞挑战赛只记录，还是也用作外部基准？ 原因：它涉及细胞系中的 CRISPRi 敲低，而不是基因型×药物效应 [EV07, EV09]。 默认值：只记录；不参赛。 若答案不同：在文档 07 和文档 08 中加入基准协议和里程碑。 影响范围：docs/07, docs/08。

**UQ14** (decision; optional; status: open). Should any retired row be restored, and should the rows retired for unreadable text be screened again if a readable copy appears? Why: Five in-scope rows (GD04, GD05, GD29, GV08, KB03) were retired only because no document cites them. Eight rows (GD24, GD36, GD52, KB11, MD21, WM31, EV06, EV10) were retired because their text was unreadable or secondary, and the primary Cell paper behind GD24 is held for screening. Default: Keep all retired; restore a row only by changing its status to active. If the answer differs: Set the status back to active, refresh the row from a readable copy, and run the validator. Affects: data/sources.csv.

> **UQ14**（决策；可选；状态：open）。是否应恢复某些退役条目？因文本无法阅读而退役的条目，在出现可读副本时是否应重新筛选？ 原因：五个在范围内的条目（GD04、GD05、GD29、GV08、KB03）退役，只是因为没有文档引用它们。八个条目（GD24、GD36、GD52、KB11、MD21、WM31、EV06、EV10）因文本无法阅读或属二手而退役，GD24 背后的 Cell 原始论文被搁置待筛选。 默认值：全部保持退役；只有把 status 改回 active 才恢复一个条目。 若答案不同：把 status 改回 active，依据可读副本更新该条目，并运行校验器。 影响范围：data/sources.csv。

**UQ15** (decision; optional; status: open). Is the five-class variant typology (1 target coding, 2 target regulatory, 3 copy-number or structural, 4 pathway, 5 pharmacokinetic) acceptable? Why: The classes drive the tags in data/sources.csv and the stratified analyses of HA; merging or splitting classes changes both. Default: Keep the five classes. If the answer differs: Re-tag the variant_class column and rewrite document 00 and the stratification of document 08. Affects: docs/00, docs/01, docs/08, data/sources.csv.

> **UQ15**（决策；可选；状态：open）。五类变异类型学（1 靶点编码、2 靶点调控、3 拷贝数或结构、4 通路、5 药代动力学）是否可以接受？ 原因：这些类别决定 data/sources.csv 中的标签和 HA 的分层分析；合并或拆分类别会同时改变两者。 默认值：保留五个类别。 若答案不同：重新标注 variant_class 列，并改写文档 00 和文档 08 中的分层。 影响范围：docs/00, docs/01, docs/08, data/sources.csv。

**UQ18** (missing-information; optional; status: open). Can you supply the text of sources that could not be read, starting with the load-bearing ones among the 57 active rows at tier T2? Why: bioRxiv returns HTTP 429 (Q138) and some publishers are paywalled; 31 of the 63 rows that were abstract-only in the first retrieval pass were bioRxiv (Q134). Claims that rest on them stay unverified until read. Default: They stay at tier T2 and any claim that rests on them is marked unverified. If the answer differs: Provide the text in a session (never in the repository); the next round reads it, re-grades the tier and updates the row. Affects: data/sources.csv (tier T2).

> **UQ18**（缺失信息；可选；状态：open）。能否提供无法阅读的来源的文本，先从 57 条 T2 级 active 条目中承重的那些开始？ 原因：bioRxiv 返回 HTTP 429（Q138），部分出版商需付费；首轮抓取中仅有摘要的 63 行里有 31 行来自 bioRxiv（Q134）。依赖它们的论断在读到之前保持未经核验。 默认值：它们保持在 T2 级，依赖它们的任何论断都标为未经核验。 若答案不同：在会话中提供文本（绝不放入仓库）；下一轮阅读它、重评等级并更新该条目。 影响范围：data/sources.csv (tier T2)。

**UQ19** (missing-information; optional; status: open). Which source defines the genotype of a cell line for the HA test: the dataset's own driver annotation or an independent resource such as DepMap? Why: Every Tahoe-100M line carries at least one annotated driver (derived, DS07, Q137), so a non-mutant line is not wild type, and the annotation may differ from an independent call. Default: Use the dataset annotation first and cross-check against an independent resource when one is accessible. If the answer differs: If an independent resource is primary, add it to the data rows and recompute the contrast arms. Affects: docs/02, docs/03.

> **UQ19**（缺失信息；可选；状态：open）。HA 检验中，细胞系的基因型由哪个来源定义：数据集自带的驱动突变注释，还是 DepMap 之类的独立资源？ 原因：Tahoe-100M 的每个细胞系至少携带一个被注释的驱动突变（推导，DS07，Q137），因此非突变系并非野生型，而且该注释可能与独立的调用结果不同。 默认值：先使用数据集的注释，并在能访问独立资源时与之交叉核对。 若答案不同：若以独立资源为主，就把它加入数据条目并重新计算对比各臂。 影响范围：docs/02, docs/03。

**UQ20** (missing-information; optional; status: open). Can you supply the full text of the LabCompass preprint [WM27]? Why: bioRxiv blocks the fetcher (HTTP 429, Q138); only the abstract (Q140), the code [WM28, WM29], the dataset card [DS23] and a blog [WM32] were read, so the experimental design and results are unverified. Default: Proceed without it; document 09 is limited to what the code and the dataset card show. If the answer differs: Read the text, re-grade WM27 to tier T1, check the blog claims of WM32 and revise document 09. Affects: docs/09, data/sources.csv (WM27, WM32).

> **UQ20**（缺失信息；可选；状态：open）。能否提供 LabCompass 预印本 [WM27] 的全文？ 原因：bioRxiv 阻止了抓取器（HTTP 429，Q138）；只读到了摘要（Q140）、代码 [WM28, WM29]、数据集卡片 [DS23] 和一篇博客 [WM32]，因此实验设计和结果未经核验。 默认值：没有它也继续；文档 09 只限于代码和数据集卡片所显示的内容。 若答案不同：阅读该文本，把 WM27 重评为 T1 级，核对 WM32 中的博客论断，并修订文档 09。 影响范围：docs/09, data/sources.csv (WM27, WM32)。

**UQ24** (attention; optional; status: open). Do you accept that sources whose text sits behind bioRxiv or paywalls stay at tier T2 and that claims resting on them are marked unverified? Why: 57 active rows are at tier T2, 29 of them on bioRxiv and 10 on Cell Press (Q134, Q138); they were read at abstract level. Default: Yes; the caveat of each T2 row says what was not read. If the answer differs: Supply the texts (UQ18) or retire the T2 rows that no analysis needs. Affects: data/sources.csv (tier T2).

> **UQ24**（关注事项；可选；状态：open）。你是否接受文本被 bioRxiv 或付费墙挡住的来源保持在 T2 级，并且依赖它们的论断标为未经核验？ 原因：57 条 active 条目为 T2 级，其中 29 条在 bioRxiv、10 条在 Cell Press（Q134，Q138）；它们只在摘要层面读过。 默认值：接受；每个 T2 条目的注意事项都说明了哪些内容没有读过。 若答案不同：提供文本（UQ18），或让没有任何分析需要的 T2 条目退役。 影响范围：data/sources.csv (tier T2)。

**UQ25** (attention; optional; status: open). Do you accept that tier T1 means the text was read and the key point checked against it, not that results were replicated or code was run, and that performance numbers stay marked self-reported? Why: A T1 repository means that files were read at one commit; no code was run. Default: Yes. If the answer differs: Add a replication field to data/sources.csv and schedule re-execution of the analyses that carry weight. Affects: CLAUDE.md section 3, docs/07.

> **UQ25**（关注事项；可选；状态：open）。你是否接受 T1 级仅表示文本已被阅读且要点已对照核对，并不表示结果已被复现或代码已被运行，并且性能数字继续标为自报？ 原因：T1 级的仓库只表示在某个提交上读过文件；没有运行任何代码。 默认值：接受。 若答案不同：在 data/sources.csv 中加入复现字段，并安排重新运行那些承重的分析。 影响范围：CLAUDE.md section 3, docs/07。

**UQ26** (attention; optional; status: open). Do the length caps (45, 30 and 35 words) and the 55% prose target remove detail that you still want? Why: Condensation keeps only insight (CLAUDE.md section 10); the detail that was removed stays in git history from commit 3d4322f. Default: Keep the caps. If the answer differs: Relax the caps in CLAUDE.md section 10 and restore the detail from history. Affects: CLAUDE.md section 10.

> **UQ26**（关注事项；可选；状态：open）。长度上限（45、30 和 35 词）和 55% 的正文目标是否删去了你仍想保留的细节？ 原因：精简只保留有启示的内容（CLAUDE.md 第 10 节）；被删去的细节仍保存在 git 历史中，起点是提交 3d4322f。 默认值：保留这些上限。 若答案不同：放宽 CLAUDE.md 第 10 节中的上限，并从历史中恢复细节。 影响范围：CLAUDE.md section 10。

**UQ27** (attention; optional; status: open). Do you want a pull request for the branch claude/cool-dijkstra-wrnujs? Why: No pull request was opened because none was requested; the branch is only pushed. Default: No pull request. If the answer differs: Ask for one in a session; it is opened against the default branch. Affects: repository.

> **UQ27**（关注事项；可选；状态：open）。你是否需要为分支 claude/cool-dijkstra-wrnujs 创建 pull request？ 原因：因为没有人要求，所以没有创建 pull request；分支只是被推送。 默认值：不创建 pull request。 若答案不同：在会话中提出要求；它会针对默认分支创建。 影响范围：repository。

**UQ28** (missing-information; optional; status: open). Can you supply text for the nine held candidates (H07, H11, H15, H20, H29, H30, H35, H37, H40)? Why: They were held because no full text was readable (Q141); they are in scope but cannot be judged against the inclusion bar. Default: They stay held and are screened again when a readable copy exists. If the answer differs: Provide the texts; the next round screens them and adds those that pass. Affects: docs/search-log.

> **UQ28**（缺失信息；可选；状态：open）。能否为九个搁置候选（H07、H11、H15、H20、H29、H30、H35、H37、H40）提供文本？ 原因：它们因没有可读的全文而被搁置（Q141）；它们在范围内，但无法对照纳入门槛作出判断。 默认值：它们保持搁置，在出现可读副本时重新筛选。 若答案不同：提供文本；下一轮对其筛选并加入通过者。 影响范围：docs/search-log。

**UQ29** (missing-information; optional; status: open). Do you want to authorize the Wiley, Synapse, Owkin and BioRender connectors of the bio-research plugin? Why: They require an authorization that the assistant cannot start; they might widen access to full texts and datasets, which is untested. Default: No; nothing depends on them. If the answer differs: Authorize them in the connector settings; the next round tests what they can retrieve and logs it. Affects: docs/search-log.

> **UQ29**（缺失信息；可选；状态：open）。你是否要授权 bio-research 插件的 Wiley、Synapse、Owkin 和 BioRender 连接器？ 原因：它们需要助手无法发起的授权；它们可能扩大对全文和数据集的访问，但这尚未经检验。 默认值：不授权；没有任何内容依赖它们。 若答案不同：在连接器设置中授权；下一轮测试它们能取回什么并记入日志。 影响范围：docs/search-log。

<!-- questions-optional:end -->

## 4. Answer register / 回答登记表

The register lists every question with its status and your answer, if any; a row that stays at `open` keeps its default.

> 登记表列出每个问题的状态和你的回答（如有）；保持 `open` 的行沿用其默认值。

<!-- questions-register:start -->
| ID | Type | Priority | Status | Answer | Answered on | Applied on |
|---|---|---|---|---|---|---|
| UQ01 | decision | needs-your-attention | open | — | — | — |
| UQ02 | decision | optional | open | — | — | — |
| UQ03 | decision | optional | open | — | — | — |
| UQ04 | decision | needs-your-attention | open | — | — | — |
| UQ05 | decision | needs-your-attention | open | — | — | — |
| UQ06 | decision | needs-your-attention | open | — | — | — |
| UQ07 | decision | optional | open | — | — | — |
| UQ08 | decision | needs-your-attention | open | — | — | — |
| UQ09 | decision | optional | open | — | — | — |
| UQ10 | decision | needs-your-attention | open | — | — | — |
| UQ11 | decision | optional | open | — | — | — |
| UQ12 | decision | optional | open | — | — | — |
| UQ13 | decision | optional | open | — | — | — |
| UQ14 | decision | optional | open | — | — | — |
| UQ15 | decision | optional | open | — | — | — |
| UQ16 | decision | needs-your-attention | open | — | — | — |
| UQ17 | missing-information | needs-your-attention | open | — | — | — |
| UQ18 | missing-information | optional | open | — | — | — |
| UQ19 | missing-information | optional | open | — | — | — |
| UQ20 | missing-information | optional | open | — | — | — |
| UQ21 | missing-information | needs-your-attention | open | — | — | — |
| UQ22 | attention | needs-your-attention | open | — | — | — |
| UQ23 | attention | needs-your-attention | open | — | — | — |
| UQ24 | attention | optional | open | — | — | — |
| UQ25 | attention | optional | open | — | — | — |
| UQ26 | attention | optional | open | — | — | — |
| UQ27 | attention | optional | open | — | — | — |
| UQ28 | missing-information | optional | open | — | — | — |
| UQ29 | missing-information | optional | open | — | — | — |
<!-- questions-register:end -->

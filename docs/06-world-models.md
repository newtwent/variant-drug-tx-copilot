# 06 World models and virtual cells / 世界模型与虚拟细胞

## 1. Scope / 范围

This document collects what the retrieved sources say about world models in general and about "world models" of the cell: definitions, architectures, claims and critiques. Its purpose is to turn the label into testable requirements, because the end goal of the project is a transcriptome predictor built on a world-model architecture. It does not evaluate any model empirically.

> 本文档汇集检索到的来源对一般世界模型以及细胞“世界模型”的说法：定义、架构、主张和批评。其目的是把这个标签变成可检验的要求，因为本项目的最终目标是以世界模型为架构的转录组预测器。它不对任何模型做实证评估。

## 2. Facts and evidence / 事实与证据

In general machine learning, Dreamer learns behaviors by latent imagination, with a representation model, a transition model and a reward model [WM01]. Surveys cover world models for embodied AI, robotic manipulation and general world simulators [WM02, WM03, WM04, WM05]. One survey describes JEPA as predicting the embedding of a missing or future observation instead of reconstructing it, so no pixel decoder is needed [WM02].

> 在一般机器学习中，Dreamer 通过潜在想象来学习行为，包含表征模型、转移模型和奖励模型 [WM01]。综述涵盖了具身智能、机器人操作和通用世界模拟器的世界模型 [WM02, WM03, WM04, WM05]。一篇综述把 JEPA 描述为预测缺失或未来观测的嵌入而不是重建它，因此不需要像素解码器 [WM02]。

For the cell, an operational definition appears in the search summaries: an encoder into a latent state, an action-conditioned transition operator F that induces trajectories z_{t+1} = F(z_t, a_t), and a decoder back to observables. The summary attributes it to a perspective piece, and whether the exact definition belongs to [WM16] or to [WM17] is unconfirmed. The GenBio AI paper argues that prediction alone is insufficient: a biological world model must support action-conditioned simulation, keep cross-modal consistency and remain stable over multi-step trajectories [WM17].

> 对于细胞，检索摘要中出现了一个操作性定义：编码器把细胞映射到潜在状态，动作条件转移算子 F 产生轨迹 z_{t+1} = F(z_t, a_t)，再由解码器回到可观测量。摘要把它归于一篇观点文章，而这一确切定义究竟属于 [WM16] 还是 [WM17]，尚未确认。GenBio AI 的论文主张仅有预测是不够的：生物世界模型必须支持动作条件的模拟、保持跨模态一致，并在多步轨迹上保持稳定 [WM17]。

A critique holds that action must shape the evolution of the state and not only the output label, and that without an updatable state and a transition operator the claim is representational, not dynamical [WM21]. The same critique is known only from a tier-T3 source. A further paper on world models in biomedical research is known by title only [WM18].

> 一篇批评认为，动作必须塑造状态的演化，而不仅仅是输出标签；如果没有可更新的状态和转移算子，这一主张只是表征性的，而不是动力学的 [WM21]。这一批评只来自 T3 级来源。另一篇关于生物医学研究中世界模型的论文只知道标题 [WM18]。

Works that call themselves world models of the cell are all preprints or repositories, and none has been verified. AlphaCell builds a latent "Virtual Cell Space" from the full protein-coding transcriptome with an encoder, decodes back to genome-wide expression, and treats perturbations as flow-matching vector fields [WM06]. Lingshu-Cell is a masked discrete diffusion model that conditions on cell type or donor identity plus perturbation and self-reports a lead on the Virtual Cell Challenge H1 benchmark [WM10]. CellOS learns cell-state embeddings by multi-view joint-embedding pretraining, and its authors say it does not yet model full cellular dynamics [WM07]. Chreode predicts action-conditioned cell-state transitions through a structured residual transition operator [WM20]. VCWorld, VCLMU, AROMA and CellFluxRL are known by title only [WM08, WM19, WM09, WM23]. The Immune World Model repository describes action-conditioned multi-cell latent dynamics with gene knockouts, drugs and cytokine doses as actions and 4 out-of-distribution splits, and it is a tier-T3 source [WM22].

> 自称细胞世界模型的工作都是预印本或代码仓库，没有一个经过核验。AlphaCell 用编码器从全部蛋白编码转录组构建潜在的“Virtual Cell Space”，再解码回全基因组表达，并把扰动视为流匹配向量场 [WM06]。Lingshu-Cell 是以细胞类型或供体身份加扰动为条件的掩码离散扩散模型，自报在虚拟细胞挑战赛 H1 基准上领先 [WM10]。CellOS 通过多视图联合嵌入预训练学习细胞状态嵌入，其作者称尚未建模完整的细胞动力学 [WM07]。Chreode 通过结构化残差转移算子预测动作条件的细胞状态转移 [WM20]。VCWorld、VCLMU、AROMA 和 CellFluxRL 只知道标题 [WM08, WM19, WM09, WM23]。Immune World Model 仓库描述了以基因敲除、药物和细胞因子剂量为动作的动作条件多细胞潜在动力学，以及 4 种分布外划分，它是 T3 级来源 [WM22]。

JEPA-style latent prediction has reached transcriptomics. GeneJepa predicts latent representations of masked gene sets from visible context, is trained on Tahoe-100M, and reports zero-shot in-silico knockouts by manipulating embeddings with pre-computed perturbation vectors [WM11]. Cell-JEPA trains a student on masked inputs to predict the teacher's embedding of the unmasked cell, together with a gene-level reconstruction loss, and its authors note that the invariance that helps recognize cell states may blunt sensitivity to perturbation-induced shifts, a trade-off between state fidelity and effect-size accuracy [WM12]. BioM-JEPA predicts aggregate representations of graph-connected gene blocks and self-reports the lowest aggregate perturbation-response error among the models it evaluated, using frozen embeddings [WM13]. A JEPA variant exists for DNA models [WM14].

> JEPA 式的潜在预测已进入转录组学。GeneJepa 从可见上下文预测被掩码基因集的潜在表示，在 Tahoe-100M 上训练，并报告通过用预先计算的扰动向量操纵嵌入实现零样本的计算机模拟敲除 [WM11]。Cell-JEPA 训练学生网络在掩码输入上预测教师网络对未掩码细胞的嵌入，并附带基因层面的重建损失，其作者指出，有助于识别细胞状态的不变性可能钝化对扰动引起的偏移的敏感度，这是状态保真度与效应大小准确度之间的权衡 [WM12]。BioM-JEPA 预测由图连接的基因块的聚合表示，自报在其评估的模型中，使用冻结嵌入时扰动响应的综合误差最低 [WM13]。针对 DNA 模型也有一个 JEPA 变体 [WM14]。

The broader vision papers propose an AI virtual cell with universal representations across scales, interpretable in-silico experiments, active learning with biologists in the loop and self-driving laboratories [WM24]. Others discuss the data pillars and closed-loop learning that such a cell needs [WM25], and the role of large language models [WM26].

> 更宏观的愿景论文提出了具有跨尺度通用表示、可解释的计算机模拟实验、有生物学家参与的主动学习和自驱动实验室的 AI 虚拟细胞 [WM24]。另一些论文讨论了这种细胞所需的数据支柱和闭环学习 [WM25]，以及大语言模型的作用 [WM26]。

## 3. A test battery for the "world model" claim / “世界模型”主张的检验清单

| Test | What passes | Data needed | Source IDs | 检验（中文） |
|---|---|---|---|---|
| Multi-step rollout | Predictions at successive doses or times from one starting state stay stable and beat independent one-step predictions on held-out measurements | Dose series or time courses | WM17 | 多步展开：从同一起始状态出发，在连续剂量或时间点上的预测保持稳定，并在留出测量上优于独立的单步预测 |
| State update | A perturbation changes the latent state in a way that alters later predictions, not only the output label | Sequential or combined perturbations | WM21 | 状态更新：扰动会改变潜在状态，从而改变后续预测，而不仅仅是输出标签 |
| Composition | Held-out drug combinations are predicted from single-drug training | Combination data; none retrieved | MD21 (tier T3) | 组合：从单药训练预测留出的药物组合；未检索到组合数据 |
| Counterfactual variant swap | Predicted response of a line with a mutation swapped in or out matches the contrast seen between lineage-matched lines | Lineage-matched mutant and wild-type lines | WM22 (tier T3) | 反事实变异互换：把突变换入或换出后的细胞系的预测响应，与谱系匹配细胞系之间观察到的对比一致 |
| Cross-modal consistency | Predictions agree across modalities | Multi-modal data; not available here | WM17 | 跨模态一致：各模态的预测互相一致；此处没有可用的多模态数据 |

## 4. Judgments / 判断

J6 (confidence: medium). "World model" is currently closer to a narrative label than an established architecture class [WM21]. To justify it, a model must pass the tests in the table above: stable multi-step rollouts along dose or time, generalization to combinations of actions, and counterfactual genotype swaps. Available data support dynamics weakly: I found no dataset with dense time courses crossed with drugs and genotypes, so multi-step tests may be limited to the dose axis.

> J6（置信度：中）。“世界模型”目前更像一个叙事标签，而不是成熟的架构类别 [WM21]。要证明其合理性，模型必须通过上表中的检验：沿剂量或时间的稳定多步展开、对动作组合的泛化，以及反事实的基因型互换。现有数据对动力学的支持较弱：我没有找到密集时间序列同时交叉药物与基因型的数据集，因此多步检验可能只能沿剂量轴进行。

J13 (confidence: medium). A latent-prediction model without a decoder still needs an explicit transcriptome readout to be evaluated at gene level, and the trade-off reported by the Cell-JEPA authors is a warning that such models may under-represent perturbation effect sizes [WM12, WM02].

> J13（置信度：中）。没有解码器的潜在预测模型仍然需要显式的转录组读出才能在基因层面被评估，Cell-JEPA 作者报告的权衡警示这类模型可能低估扰动效应的大小 [WM12, WM02]。

## 5. Recommended actions / 行动建议

Adopt the operational definition and the test battery above before building anything, and record in advance which tests the available data can support [WM17, WM21].

> 在构建任何东西之前，先采用上面的操作性定义和检验清单，并预先记录现有数据能够支持哪些检验 [WM17, WM21]。

Treat self-labelled world models as baselines to be re-evaluated, not as evidence that the architecture works, because all of them are unverified preprints or repositories [WM06, WM10, WM11, WM20].

> 把自称世界模型的工作视为待重新评估的基线，而不是该架构有效的证据，因为它们全部是未经核验的预印本或代码仓库 [WM06, WM10, WM11, WM20]。

If a JEPA-style objective is used, add an explicit transcriptome readout and track effect-size accuracy next to state fidelity [WM12].

> 如果使用 JEPA 式的目标，就加入显式的转录组读出，并在状态保真度之外同时跟踪效应大小的准确度 [WM12]。

Keep the world-model question separate from the performance question: a model can predict well without being a world model, and a world-model design can predict worse than a linear baseline.

> 把世界模型问题与性能问题分开：模型可以预测得很好却不是世界模型，世界模型式的设计也可能预测得比线性基线更差。

## 6. Questions for confirmation / 待确认问题

Is the operational definition above acceptable as the working definition of "world model" for this project? Default: yes (assumption M3 in document 00).

> 上述操作性定义是否可以作为本项目“世界模型”的工作定义？默认：可以（文档 00 中的假设 M3）。

## 7. Evidence gaps / 证据缺口

The details of VCWorld could not be checked because the primary host was unreachable [WM08]. No self-labelled world model was verified, and no source showed a world-model architecture beating a conditional generative model on any benchmark. The primary papers for Dreamer's successors and for JEPA were not retrieved beyond surveys. No dataset with dense time courses crossed with drugs and genotypes was found.

> 由于主要站点无法访问，VCWorld 的细节无法核查 [WM08]。没有任何自称世界模型的工作得到核验，也没有来源显示世界模型架构在任何基准上优于条件生成模型。除综述外，Dreamer 后续版本和 JEPA 的原始论文没有被检索到。未找到密集时间序列同时交叉药物与基因型的数据集。

## 8. Source index (category WM) / 来源索引（类别 WM）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:WM:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| WM01 | T2 | [Dream to Control: Learning Behaviors by Latent Imagination (Dreamer)](<https://arxiv.org/pdf/1912.01603>) | latent imagination with representation, transition and reward models | 含表征、转移和奖励模型的潜在想象 |
| WM02 | T2 | [World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](<https://arxiv.org/pdf/2606.00133>) | — | — |
| WM03 | T2 | [A Survey: Learning Embodied Intelligence from Physical Simulators and World Models](<https://arxiv.org/pdf/2507.00917>) | — | — |
| WM04 | T2 | [Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond](<https://arxiv.org/pdf/2405.03520>) | — | — |
| WM05 | T2 | [A Step Toward World Models: A Survey on Robotic Manipulation](<https://arxiv.org/pdf/2511.02097>) | — | — |
| WM06 | T2 | [Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell](<https://www.biorxiv.org/content/10.64898/2026.03.02.709176v1.full>) | latent Virtual Cell Space from the full protein-coding transcriptome; flow-matching vector fields | 由全部蛋白编码转录组得到的潜在 Virtual Cell Space；流匹配向量场 |
| WM07 | T2 | [CellOS: Learning a World Model of Cellular State through ...](<https://www.biorxiv.org/content/biorxiv/early/2026/06/25/2026.06.18.733163.full.pdf>) | multi-view joint-embedding pretraining; authors say full cellular dynamics are not yet modeled | 多视图联合嵌入预训练；作者称尚未建模完整的细胞动力学 |
| WM08 | T2 | [VCWorld: A Biological World Model for Virtual Cell Simulation](<https://arxiv.org/pdf/2512.00306>) | details unverified (WebFetch failed) | 细节未核验（WebFetch 失败） |
| WM09 | T2 | [AROMA: Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling](<https://arxiv.org/pdf/2604.20263>) | — | — |
| WM10 | T2 | [Lingshu-Cell: A generative cellular world model for transcriptome modeling toward virtual cells](<https://arxiv.org/pdf/2603.25240>) | masked discrete diffusion conditioned on cell type or donor plus perturbation; self-reported lead on the VCC H1 benchmark | 以细胞类型或供体加扰动为条件的掩码离散扩散；自报在 VCC H1 基准上领先 |
| WM11 | T2 | [GeneJepa: A Predictive World Model of the Transcriptome](<https://www.biorxiv.org/content/10.1101/2025.10.14.682378v1.full.pdf>) | predicts latent representations of masked gene sets on Tahoe-100M; zero-shot knockouts by embedding manipulation | 在 Tahoe-100M 上预测被掩码基因集的潜在表示；通过嵌入操纵实现零样本敲除 |
| WM12 | T2 | [Cell-JEPA: Latent Representation Learning for Single-Cell Transcriptomics](<https://arxiv.org/pdf/2602.02093>) | student–teacher on a scGPT backbone; authors note invariance may blunt sensitivity to perturbation shifts | scGPT 骨干上的师生结构；作者指出不变性可能钝化对扰动偏移的敏感度 |
| WM13 | T2 | [BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells](<https://arxiv.org/abs/2608.05928>) | self-reported lowest aggregate perturbation-response error for frozen embeddings | 自报冻结嵌入的扰动响应综合误差最低 |
| WM14 | T2 | [JEPA-DNA: Grounding Genomic Foundation Models through Joint-Embedding Predictive Architectures](<https://arxiv.org/pdf/2602.17162>) | — | — |
| WM15 | T2 | [JEPA-Anything: Learning Predictive Models across Different Worlds](<https://arxiv.org/pdf/2609.20800>) | peripheral | 外围条目 |
| WM16 | T2 | [A world model of the virtual cell](<https://www.sciencedirect.com/science/article/pii/S0092867426010159>) | search summary attributes "encoder + action-conditioned transition F(z_t, a_t) + decoder" to some perspective; not confirmed to be this one (may share a source with WM17) | 检索摘要把“编码器 + 动作条件转移 F(z_t, a_t) + 解码器”归于某篇观点文章；未确认就是本条（可能与 WM17 同源） |
| WM17 | T2 | [A World Model of the Virtual Cell (GenBio AI; Eric Xing and Le Song)](<https://genbio.ai/research/virtual-cell-may-3.pdf>) | argues for action-conditioned simulation, cross-modal consistency and multi-step stability | 主张动作条件模拟、跨模态一致性和多步稳定性 |
| WM18 | T2 | [Towards World Models in Biomedical Research](<https://www.alphaxiv.org/abs/2606.05925>) | — | — |
| WM19 | T2 | [VCLMU: Mechanism-Centric Virtual Cell World Modeling for Perturbation Response](<https://arxiv.org/html/2610.04475>) | — | — |
| WM20 | T2 | [Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction](<https://arxiv.org/html/2605.28111>) | structured residual transition operator | 结构化残差转移算子 |
| WM21 | T3 | [What Makes a Virtual Cell a World Model? Three Gaps, Three Experiments, and a Roadmap](<https://www.researchgate.net/publication/410659566_What_Makes_a_Virtual_Cell_a_World_Model_Three_Gaps_Three_Experiments_and_a_Roadmap>) | critique: without an updatable state and a transition, the claim is representational, not dynamical | 批评：若没有可更新的状态和转移，该主张只是表征性的，不是动力学的 |
| WM22 | T3 | [Immune World Model (GitHub)](<https://github.com/yc9954/immune-world-model>) | action-conditioned multi-cell latent dynamics; 4 OOD splits; code repository | 动作条件的多细胞潜在动力学；4 种分布外划分；代码仓库 |
| WM23 | T2 | [CellFluxRL: Biologically-Constrained Virtual Cell Modeling via Reinforcement Learning](<https://arxiv.org/pdf/2603.21743>) | peripheral | 外围条目 |
| WM24 | T2 | [How to build the virtual cell with artificial intelligence: Priorities and opportunities](<https://www.sciencedirect.com/science/article/pii/S0092867424013321>) | AI virtual cell vision; active learning and self-driving labs | AI 虚拟细胞愿景；主动学习与自驱动实验室 |
| WM25 | T2 | [Grow AI virtual cells: three data pillars and closed-loop learning](<https://www.nature.com/articles/s41422-025-01101-y>) | — | — |
| WM26 | T2 | [Large Language Models Meet Virtual Cell: A Survey](<https://arxiv.org/pdf/2510.07706>) | — | — |
<!-- source-index:WM:end -->

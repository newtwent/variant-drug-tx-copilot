# Variant × Drug → Transcriptional Landscape: Research Knowledge Base / 基因变异 × 药物 → 转录景观：研究知识库

## 1. Purpose / 目的

This repository collects, classifies and critiques public evidence on one research question: how genetic variation in drug targets or signaling pathways changes drug-induced transcriptional landscapes. The end goal is to design a transcriptome-prediction model built on a world-model architecture. The repository holds metadata, key points and judgments only; it does not hold paper full texts or dataset copies.

> 本仓库收集、分类并评述一个研究问题的公开证据：药物靶点或信号通路中的遗传变异如何改变药物诱导的转录景观。最终目标是设计以世界模型为架构的转录组预测模型。仓库只保存元数据、要点和判断，不保存论文全文或数据集副本。

## 2. Status and limits / 状态与限制

On 2026-10-18 the repository holds 292 sources (246 active, 46 retired), 35 datasets, 143 log entries (Q01 to Q143) and 30 open questions. The 246 active sources split into 186 at tier T1, 57 at tier T2 and 3 at tier T3.

> 2026-10-18，仓库共有 292 条来源（246 条 active，46 条 retired）、35 个数据集、143 条日志（Q01 至 Q143）和 30 个待确认问题。246 条 active 来源分为 186 条 T1 级、57 条 T2 级和 3 条 T3 级。

The repository was built on 2026-10-16 in two rounds and audited in a third round between 2026-10-16 and 2026-10-18. The audit retrieved by script the best available text of each of the 232 rows that were active before it and compared every recorded claim with that text; a claim counts as verified only when a script confirmed a literal quote from the text (Q133 to Q143). Of 2,305 claims, 2,094 were verified, 110 unsupported, 71 not checkable and 30 contradicted, and the rows were rewritten to keep only what passed.

> 本仓库于 2026-10-16 分两轮构建，并在 2026-10-16 至 2026-10-18 的第三轮中接受了核查。核查用脚本取回此前处于 active 状态的 232 个条目各自可得的最佳文本，并把每条已记录的论断与该文本比较；只有当脚本确认了文本中的一段逐字引文时，论断才算得到核实（Q133 至 Q143）。2,305 条论断中，2,094 条得到核实，110 条无依据，71 条无法检查，30 条被反驳，条目已据此重写，只保留通过核查的内容。

As a result 152 rows rose to tier T1 (143 from T2 and 9 from T3) and 8 rows were retired. Of the 40 candidates held after the second round, 21 were screened in and 10 rejected, and 9 stay held for lack of text; with the dataset-card row DS24, 22 rows were added (Q141, Q142).

> 因此有 152 条升为 T1 级（143 条来自 T2，9 条来自 T3），8 条被退役。第二轮之后搁置的 40 个候选中，21 个经筛选被纳入，10 个被拒绝，9 个因缺少文本而继续搁置；加上数据集卡片条目 DS24，共新增 22 条（Q141、Q142）。

The audit establishes what a source says, not that it is true. Tier T1 means that the text was read and the key point was checked against it, not that the result was replicated or that code was run. The 57 rows at tier T2 were seen only at abstract level, mostly on bioRxiv, medRxiv or paywalled journal hosts, and bioRxiv answered every full-text request with an HTTP 429 (Q134, Q138); the 3 rows at tier T3 are secondary sources.

> 核查证明的是来源这样说，而不是所说为真。T1 级表示文本已被阅读且要点已对照文本核对，并不表示结果已被复现或代码已被运行。57 条 T2 级条目只见到摘要层面的内容，多数位于 bioRxiv、medRxiv 或付费期刊站点，且 bioRxiv 对每次全文请求都返回 HTTP 429（Q134、Q138）；3 条 T3 级条目是二手来源。

This includes the LabCompass preprint (WM27), of which only the abstract and metadata were read (Q140); the LabCompass facts in this repository come from its two code repositories and its dataset card (WM28, WM29, DS23). In this repository, "not found" means that a limited search did not retrieve it, not that it does not exist.

> 其中包括 LabCompass 预印本（WM27），只读到了摘要和元数据（Q140）；本仓库中的 LabCompass 事实来自它的两个代码仓库和数据集卡片（WM28、WM29、DS23）。在本仓库中，“未找到”意味着有限检索未取回，而不是不存在。

## 3. How to read / 阅读方式

Every conclusion is written in English and is followed immediately by its complete Chinese translation, set as a blockquote. Claims carry source IDs such as [GD06] that resolve to rows of `data/sources.csv`. Numbers marked "self-reported" come from the authors of the method itself, and numbers marked "secondary" come from a summary rather than the primary paper. Facts, judgments, recommended actions and questions are kept in separate sections.

> 每条结论先用英文撰写，紧跟其完整的中文翻译（引用块）。论断带有 [GD06] 这样的来源 ID，对应 `data/sources.csv` 中的行。标注“自报”的数字来自方法作者自己，标注“二手”的数字来自总结而不是原论文。事实、判断、行动建议和问题分在不同的部分。

The "so what" of a row states in at most two sentences what the source offers this project; it is the curator's judgment, not a claim of the source. Retired sources are not cited in the documents, and the source-index tables at the end of documents 01 to 07 list active rows only. Decisions that belong to the owner are collected with their defaults in `docs/10-open-questions.md`; to answer one, edit its row in `data/questions.csv` and commit.

> 一行的“意义”用至多两句话说明该来源能为本项目提供什么；它是整理者的判断，而不是来源本身的论断。退役的来源不在文档中被引用，文档 01 到 07 末尾的来源索引表只列出 active 条目。属于所有者的决策连同其默认值收集在 `docs/10-open-questions.md` 中；要回答某个问题，请编辑 `data/questions.csv` 中对应的行并提交。

## 4. Inclusion bar and retirement / 纳入门槛与退役

A source enters the knowledge base only if all five conditions hold: it fits the topic (the mechanism by which variants in targets or pathways reshape drug-induced transcription, or the modeling of perturbation response and world models); it makes a specific, transferable contribution that fits a "so what" of at most two sentences; it has a verifiable URL and an honest evidence tier; it is not redundant with an existing row unless it adds a distinct angle; and it is a primary source unless the primary one is unreachable, in which case it is flagged as secondary. The rules are in `CLAUDE.md` sections 7, 9 and 10.

> 只有同时满足五个条件，来源才会进入知识库：它契合主题（靶点或通路中的变异重塑药物诱导转录的机理，或扰动响应与世界模型的建模）；它有具体、可迁移的贡献，能写成至多两句话的“意义”；它有可核验的 URL 和诚实的证据等级；除非带来不同的角度，否则与现有条目不冗余；并且是一手来源，除非一手来源无法访问，此时要标注为二手。规则见 `CLAUDE.md` 第 7、9 和 10 节。

A candidate that fails only for lack of information is held, not rejected, so that it can be screened again when the text is readable (Q142). A row that no document cites and that states no transferable contribution may be retired; it stays in `data/sources.csv` with its status set to retired and a retirement note, its ID is never reused, and restoring it means changing one column. The 46 retired rows include the 8 that the third round retired (Q143).

> 仅因信息缺失而未通过的候选会被搁置而不是拒绝，以便在文本可读时重新筛选（Q142）。一个没有被任何文档引用、也没有说明可迁移贡献的条目可以被退役；它仍留在 `data/sources.csv` 中，其 status 设为 retired 并带有退役说明，其 ID 绝不复用，恢复它只需改一列。46 条 retired 条目中包括第三轮退役的 8 条（Q143）。

## 5. Navigation / 导航

Read `docs/08-design-implications.md` for the plan and `docs/10-open-questions.md` for the questions that await an answer; the other documents hold the evidence behind them.

> 计划请读 `docs/08-design-implications.md`，等待回答的问题请读 `docs/10-open-questions.md`；其他文档保存支撑它们的证据。

| Path | Content | 内容 |
|---|---|---|
| `docs/00-problem-framing.md` | Formal statement, tracks and variant typology, assumptions, mistakes, missing information, deeper question, glossary | 形式化陈述、轨道与变异类型学、假设、错误、缺失信息、更深层问题、术语表 |
| `docs/01-genetic-variation-layer.md` | Variants in targets and pathways; variant-to-expression and variant-to-binding models; MR and TWAS | 靶点与通路中的变异；变异到表达、变异到结合的模型；MR 与 TWAS |
| `docs/02-genotype-x-drug-evidence.md` | Response-eQTL, dynamic eQTL, variant functional screens, somatic mutation and drug rewiring; evidence map | 响应型 eQTL、动态 eQTL、变异功能筛选、体细胞突变与药物重编程；证据地图 |
| `docs/03-data-resources.md` | Drug-perturbation, Perturb-seq and eQTL resources; dataset table | 药物扰动、Perturb-seq 与 eQTL 资源；数据集表 |
| `docs/04-prior-knowledge-bases.md` | Signaling-network priors and pharmacogenomics resources | 信号网络先验与药物基因组学资源 |
| `docs/05-perturbation-models.md` | Perturbation-prediction models, mechanism-informed networks, causal representation learning; model table | 扰动预测模型、机制导向网络、因果表示学习；模型表 |
| `docs/06-world-models.md` | Definitions, claims and critiques of world models in biology; test battery for the "world model" claim | 生物学中世界模型的定义、主张与批评；“世界模型”主张的检验清单 |
| `docs/07-evaluation-and-pitfalls.md` | Benchmarks, baseline critiques, metrics, ancestry bias; evaluation checklist | 基准、基线批判、指标、祖源偏倚；评测清单 |
| `docs/08-design-implications.md` | Design principles, three falsifiable hypotheses and one optional extension, candidate architectures, data plan, milestones, risks | 设计原则、三个可证伪假设和一个可选扩展、候选架构、数据计划、里程碑、风险 |
| `docs/09-labcompass-insights.md` | LabCompass facts, component map, insights for the world model, limits of transfer, actions and questions | LabCompass 的事实、组件对照、对世界模型的启示、迁移的局限、行动建议与问题 |
| `docs/10-open-questions.md` | Open questions with defaults and consequences, generated from `data/questions.csv` | 带默认值和后果的待确认问题，由 `data/questions.csv` 生成 |
| `docs/search-log.md` | Every query (Q01 to Q143) with outcome, failures, gaps and screening decisions | 每次查询（Q01 至 Q143）及其结果、失败、缺口和筛选决定 |
| `data/sources.csv` | 292 sources (246 active, 46 retired) with tier, relevance, key points and "so what" (English and Chinese), caveats and status | 292 条来源（246 条 active，46 条 retired），含证据等级、相关性、要点和“意义”（中英文）、注意事项与状态 |
| `data/datasets.csv` | 35 datasets with scale, genotype information and caveats | 35 个数据集，含规模、基因型信息与注意事项 |
| `data/questions.csv` | 30 open questions with default, consequence and an answer column | 30 个待确认问题，含默认值、后果和回答列 |
| `tools/` | Validator (`validate_kb.py`), table generator (`fill_tables.py`) and audit scripts (`audit/`) | 校验器（`validate_kb.py`）、表格生成器（`fill_tables.py`）和核查脚本（`audit/`） |
| `CLAUDE.md` | Conventions for extending the repository: language rule, tiers, inclusion bar, round protocol, open questions | 扩展本仓库的约定：语言规则、等级、纳入门槛、每轮协议、待确认问题 |

## 6. Evidence tiers and category codes / 证据等级与类别代码

| Tier | Meaning | 含义 |
|---|---|---|
| T1 | The full text or the official page (a read repository clone or dataset card counts) was read in a session with network access and the key point was checked against it; this does not mean that the result was replicated or the code run | 在有网络访问的会话中阅读了全文或官方页面（读过的仓库克隆或数据集卡片也算），且要点已对照文本核对；这并不表示结果已被复现或代码已被运行 |
| T2 | Peer-reviewed paper or preprint seen only at title, abstract or excerpt level, including an abstract returned by an API | 同行评议论文或预印本，仅见到标题、摘要或摘录，包括由 API 返回的摘要 |
| T3 | Secondary source: news, blog, social post, third-party summary or talk abstract, even when read in full | 二手来源：新闻、博客、社交媒体帖子、第三方总结或讲座摘要，即使已通读 |

| Code | Category | 类别 |
|---|---|---|
| GV | Genetic variation layer | 遗传变异层 |
| GD | Genotype × drug → transcriptome evidence | 基因型×药物→转录组实证 |
| DS | Datasets | 数据集 |
| KB | Prior-knowledge bases and pharmacogenomics | 先验知识库与药物基因组学 |
| MD | Modeling methods | 建模方法 |
| WM | World models and virtual cells | 世界模型与虚拟细胞 |
| EV | Evaluation, baseline critiques and bias | 评测、基线批判与偏倚 |

| Relevance | Meaning | 含义 |
|---|---|---|
| mechanism | How variants in targets or pathways change drug-induced transcription | 靶点或通路中的变异如何改变药物诱导的转录 |
| modeling | Perturbation-response models, world models and design methods | 扰动响应模型、世界模型与设计方法 |
| data | Datasets and data resources | 数据集与数据资源 |
| evaluation | Benchmarks, metrics and pitfalls | 基准、指标与陷阱 |
| prior | Prior knowledge: networks, regulons, pharmacogenomics | 先验知识：网络、调控子、药物基因组学 |
| context | Framing or commentary that is not itself evidence | 本身不构成证据的框架性表述或评论 |

## 7. Change log / 变更日志

On 2026-10-16 the repository was built for the first time with 191 sources, 20 dataset rows and 44 log rows. Later that day a second round applied the inclusion bar: it added 79 sources and 15 dataset rows, upgraded 10 rows, retired 38 rows, added `docs/09-labcompass-insights.md` and the optional hypothesis HD, and extended the log to Q132, including three spot checks of load-bearing numbers (Q126 to Q132).

> 2026-10-16 首次构建本仓库，含 191 条来源、20 行数据集和 44 行日志。同日稍后第二轮采用了纳入门槛：新增 79 条来源和 15 行数据集，升级 10 条，退役 38 行，新增 `docs/09-labcompass-insights.md` 和可选假设 HD，并把日志扩展到 Q132，其中包括对承重数字的三次抽查（Q126 至 Q132）。

Between 2026-10-16 and 2026-10-18 a third round audited the 232 rows that were active at its start against their texts, re-graded tiers, rescreened the 40 held candidates, added 22 rows, retired 8, and rewrote the 35 dataset rows from the primary pages (Q133 to Q143). It also rewrote `docs/09-labcompass-insights.md` as insight-only, condensed documents 00 to 08, created the open-questions list (`data/questions.csv`, `docs/10-open-questions.md`), installed the scripts under `tools/`, and added the round protocol (section 10) and the open-questions rule (section 11) to `CLAUDE.md`.

> 2026-10-16 至 2026-10-18，第三轮对开始时处于 active 状态的 232 个条目对照其文本做了核查，重评了等级，重新筛选了 40 个搁置候选，新增 22 条、退役 8 条，并依据一手页面重写了 35 行数据集（Q133 至 Q143）。同时把 `docs/09-labcompass-insights.md` 重写为只留启示，精简了文档 00 至 08，创建了待确认问题清单（`data/questions.csv`、`docs/10-open-questions.md`），把脚本安装到 `tools/`，并在 `CLAUDE.md` 中加入了每轮协议（第 10 节）和待确认问题规则（第 11 节）。

The English prose of documents 00 to 09 fell from 16,736 to 12,988 words (counted by `tools/audit/prose_words.py`), a reduction of 22%, because every document also absorbed the audit findings; detail that was removed can be recovered from the git history, and the last commit before the third round is 3d4322f.

> 文档 00 至 09 的英文正文从 16,736 词降到 12,988 词（由 `tools/audit/prose_words.py` 统计），减少了 22%，因为每份文档同时还吸收了核查的发现；被删去的细节可从 git 历史中恢复，第三轮之前的最后一次提交是 3d4322f。

# Variant × Drug → Transcriptional Landscape: Research Knowledge Base / 基因变异 × 药物 → 转录景观：研究知识库

## 1. Purpose / 目的

This repository collects, classifies and critiques public evidence on one research question: how genetic variation in drug targets or signaling pathways changes drug-induced transcriptional landscapes. The end goal is to design a transcriptome-prediction model built on a world-model architecture. The repository holds metadata, key points and judgments only; it does not hold paper full texts or dataset copies.

> 本仓库收集、分类并评述一个研究问题的公开证据：药物靶点或信号通路中的遗传变异如何改变药物诱导的转录景观。最终目标是设计以世界模型为架构的转录组预测模型。仓库只保存元数据、要点和判断，不保存论文全文或数据集副本。

## 2. Status and limits / 状态与限制

The repository was built on 2026-10-16 in two rounds. The first round used 39 completed web searches, and the second round added 74 web searches and 40 page fetches, so `docs/search-log.md` now holds 125 entries (Q01 to Q125). The second round applied an inclusion bar (section 4): it added 78 sources, upgraded 10 rows, retired 39 rows and added a document on LabCompass (`docs/09-labcompass-insights.md`). Of the 269 sources, 231 are active and 38 are retired.

> 本仓库于 2026-10-16 分两轮构建。第一轮使用了 39 次已完成的网络检索，第二轮又增加了 74 次网络检索和 40 次页面抓取，因此 `docs/search-log.md` 现有 125 条记录（Q01 至 Q125）。第二轮采用了纳入门槛（第 4 节）：新增 78 条来源，升级 10 条，退役 39 条，并新增了一篇关于 LabCompass 的文档（`docs/09-labcompass-insights.md`）。269 条来源中，231 条为 active，38 条为 retired。

Tier T1 with verified=Y applies to 11 sources: they are GitHub or PyPI pages that were actually retrieved in the second round, through a fetch tool that returns a model-written answer about the page and not its verbatim text. The other 258 sources are marked verified=N: each was seen only at title, abstract or search-excerpt level, and none of them, including the LabCompass preprint, was checked against its full text, because the build environment could not resolve bioRxiv, PubMed, Europe PMC, Hugging Face and similar hosts and the bio-research literature servers failed to connect. In this repository, "not found" therefore means "not retrieved by a limited search", not "does not exist".

> 有 11 条来源为 T1 级且 verified=Y：它们是第二轮中确实取回过的 GitHub 或 PyPI 页面，所用的抓取工具返回的是模型针对页面所写的回答，而不是页面原文。其余 258 条来源标记为 verified=N：每条都只被看到标题、摘要或检索摘录，包括 LabCompass 预印本在内，没有一条核对过全文，因为构建环境无法解析 bioRxiv、PubMed、Europe PMC、Hugging Face 等站点，且 bio-research 文献服务器连接失败。因此在本仓库中，“未找到”意味着“有限检索未取回”，而不是“不存在”。

## 3. How to read / 阅读方式

Every conclusion is written in English and is followed immediately by its complete Chinese translation, set as a blockquote. Claims carry source IDs such as [GD06]; each ID resolves to a row in `data/sources.csv`. Numbers marked "self-reported" come from the authors of the method itself, and numbers marked "secondary" come from a summary rather than the primary paper. Facts, judgments, recommended actions and questions are kept in separate sections.

> 每条结论先用英文撰写，紧跟其完整的中文翻译（引用块）。论断带有 [GD06] 这样的来源 ID；每个 ID 对应 `data/sources.csv` 中的一行。标注“自报”的数字来自方法作者自己，标注“二手”的数字来自总结而不是原论文。事实、判断、行动建议和问题分在不同的部分。

Each source row can carry a "so what" that states in at most two sentences what the source offers this project. It is the curator's judgment and not a claim of the source, and only the 88 rows that were added or upgraded in the second round have one so far. A retired source is not cited in the documents, and the source-index tables at the end of documents 01 to 07 list active rows only.

> 每条来源可以带有一句“意义”，用至多两句话说明该来源能为本项目提供什么。它是整理者的判断，而不是来源本身的论断，目前只有第二轮新增或升级的 88 条才有。退役的来源不在文档中被引用，文档 01 到 07 末尾的来源索引表只列出 active 条目。

## 4. Inclusion bar and retirement / 纳入门槛与退役

A source enters the knowledge base only if all five conditions hold. It fits the topic, which is either the mechanism by which variants in targets or pathways reshape drug-induced transcription, or the modeling of perturbation response and world models. It makes a specific, transferable contribution that can be stated as a "so what" in at most two sentences. It has a verifiable URL and an honest evidence tier. It is not redundant with an existing row unless it adds a distinct angle. A primary source is preferred, and a secondary one is accepted only when the primary one cannot be reached and is flagged as such. The rule for adding rows is in section 9 of `CLAUDE.md`.

> 只有同时满足五个条件，来源才会进入知识库。它契合主题，即靶点或通路中的变异重塑药物诱导转录的机理，或扰动响应与世界模型的建模。它有具体、可迁移的贡献，能用至多两句话写成“意义”。它有可核验的 URL 和诚实的证据等级。除非带来不同的角度，否则与现有条目不冗余。优先采用一手来源，仅当一手来源无法访问时才接受二手来源，并加以标注。新增条目的规则见 `CLAUDE.md` 的第 9 节。

A candidate that fails only for lack of information is held, not rejected, so that it can be screened again when the full text is readable: 40 candidates (H01 to H40) are held and 5 groups of results are rejected, all listed in `docs/search-log.md`. The same bar was applied to the 191 rows of the first round, and 38 rows that no document cited and that stated no transferable contribution were retired. A retired row stays in `data/sources.csv` with its status set to retired and a retirement note in its caveat columns, its ID is never reused, and restoring it means changing one column. The closest calls, which are the first rows to restore if a broader base is preferred, are listed in section 10 of `docs/search-log.md`.

> 仅因信息缺失而未通过的候选会被搁置而不是拒绝，以便在全文可读时重新筛选：40 条候选（H01 至 H40）被搁置，5 组结果被拒绝，均列于 `docs/search-log.md`。同一门槛也用于第一轮的 191 条来源，其中 38 条没有被任何文档引用、也没有说明可迁移的贡献，因而被退役。退役的条目仍留在 `data/sources.csv` 中，其 status 设为 retired，并在注意事项列中带有退役说明；其 ID 绝不复用，恢复它只需改一列。最难取舍的条目是在偏好更宽的知识库时最先应恢复的，列于 `docs/search-log.md` 的第 10 节。

Four columns of `data/sources.csv` were added for this purpose: `relevance` tags a row as mechanism, modeling, data, evaluation, prior or context; `so_what_en` and `so_what_zh` hold the "so what"; and `status` is active or retired. The `relevance` value of a legacy row was derived from its category code and is a curator default, not a reading of the source.

> 为此在 `data/sources.csv` 中新增了四列：`relevance` 把条目标记为 mechanism、modeling、data、evaluation、prior 或 context；`so_what_en` 和 `so_what_zh` 保存“意义”；`status` 取值为 active 或 retired。旧条目的 `relevance` 由其类别代码推导，是整理者的默认值，不是对来源的阅读结果。

## 5. Navigation / 导航

| Path | Content | 内容 |
|---|---|---|
| `docs/00-problem-framing.md` | Formal statement, tracks, variant typology, assumptions, mistakes, missing information, deeper question, glossary | 形式化陈述、轨道、变异类型学、假设、错误、缺失信息、更深层问题、术语表 |
| `docs/01-genetic-variation-layer.md` | Variants in targets and pathways; variant-to-expression and variant-to-binding models; MR and TWAS | 靶点与通路中的变异；变异到表达、变异到结合的模型；MR 与 TWAS |
| `docs/02-genotype-x-drug-evidence.md` | Response-eQTL, dynamic eQTL, variant functional screens, somatic mutation and drug rewiring | 响应型 eQTL、动态 eQTL、变异功能筛选、体细胞突变与药物重编程 |
| `docs/03-data-resources.md` | Drug-perturbation, Perturb-seq and eQTL resources | 药物扰动、Perturb-seq 与 eQTL 资源 |
| `docs/04-prior-knowledge-bases.md` | Signaling-network priors and pharmacogenomics resources | 信号网络先验与药物基因组学资源 |
| `docs/05-perturbation-models.md` | Perturbation-prediction models, mechanism-informed networks, causal representation learning | 扰动预测模型、机制导向网络、因果表示学习 |
| `docs/06-world-models.md` | Definitions, claims and critiques of world models in biology | 生物学中世界模型的定义、主张与批评 |
| `docs/07-evaluation-and-pitfalls.md` | Benchmarks, baseline critiques, metrics, ancestry bias | 基准、基线批判、指标、祖源偏倚 |
| `docs/08-design-implications.md` | Three falsifiable hypotheses and one optional extension, five candidate architectures, data plan, protocol, milestones | 三个可证伪假设和一个可选扩展、五种候选架构、数据计划、评测协议、里程碑 |
| `docs/09-labcompass-insights.md` | LabCompass facts, component map, insights for the world model, limits of transfer, actions and questions | LabCompass 的事实、组件对照、对世界模型的启示、迁移的局限、行动建议与问题 |
| `docs/search-log.md` | Every query (Q01 to Q125), outcome, failure, gap and verification to-do, plus the held and rejected candidates | 每次查询（Q01 至 Q125）、结果、失败、缺口与核验待办，以及被搁置和被拒绝的候选 |
| `data/sources.csv` | 269 sources (231 active, 38 retired) with tier, relevance, key points and "so what" (English and Chinese), caveats and status | 269 条来源（231 条 active，38 条 retired），含证据等级、相关性、要点和“意义”（中英文）、注意事项与状态 |
| `data/datasets.csv` | 35 datasets with scale, genotype information and caveats | 35 个数据集，含规模、基因型信息与注意事项 |
| `CLAUDE.md` | Conventions for extending the repository, including the inclusion bar | 扩展本仓库的约定，含纳入门槛 |

## 6. Evidence tiers and category codes / 证据等级与类别代码

| Tier | Meaning | 含义 |
|---|---|---|
| T1 | An official page was retrieved and queried in a session with network access, or the full text was read; so far only GitHub and PyPI pages (11 rows), none of them a paper | 在有网络访问的会话中取回并查询了官方页面，或阅读了全文；目前只有 GitHub 和 PyPI 页面（11 行），没有一篇论文 |
| T2 | Peer-reviewed paper or preprint seen only at title, abstract or search-excerpt level | 同行评议论文或预印本，仅见到标题、摘要或检索摘录 |
| T3 | Secondary source: news, blog, social media, third-party summary, talk abstract, or a code repository seen only in a search result | 二手来源：新闻、博客、社交媒体、第三方总结、讲座摘要，或仅在检索结果中见到的代码仓库 |

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

On 2026-10-16 the repository was built for the first time, with 191 sources, 20 datasets and 44 log entries.

> 2026-10-16 首次构建本仓库，含 191 条来源、20 个数据集和 44 条日志条目。

On 2026-10-16 a second round applied the inclusion bar: it added 78 sources, upgraded 10 rows (one of them to tier T1), retired 38 rows, added 15 datasets and updated 2 dataset rows, added `docs/09-labcompass-insights.md` and the optional hypothesis HD, and extended the log to 125 entries (Q45 to Q125). `CLAUDE.md` gained the tier-T1 rule for GitHub and PyPI pages, the new columns and the inclusion bar. The totals are now 269 sources (231 active, 38 retired), 35 datasets and 11 sources at tier T1.

> 2026-10-16 第二轮采用了纳入门槛：新增 78 条来源，升级 10 条（其中 1 条升为 T1 级），退役 38 条，新增 15 个数据集并更新 2 个数据集条目，新增 `docs/09-labcompass-insights.md` 和可选假设 HD，并把日志扩展到 125 条（Q45 至 Q125）。`CLAUDE.md` 增加了 GitHub 与 PyPI 页面的 T1 规则、新列和纳入门槛。当前总计 269 条来源（231 条 active，38 条 retired）、35 个数据集，以及 11 条 T1 级来源。

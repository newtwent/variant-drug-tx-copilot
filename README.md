# Variant × Drug → Transcriptional Landscape: Research Knowledge Base / 基因变异 × 药物 → 转录景观：研究知识库

## 1. Purpose / 目的

This repository collects, classifies and critiques public evidence on one research question: how genetic variation in drug targets or signaling pathways changes drug-induced transcriptional landscapes. The end goal is to design a transcriptome-prediction model built on a world-model architecture. The repository holds metadata, key points and judgments only; it does not hold paper full texts or dataset copies.

> 本仓库收集、分类并评述一个研究问题的公开证据：药物靶点或信号通路中的遗传变异如何改变药物诱导的转录景观。最终目标是设计以世界模型为架构的转录组预测模型。仓库只保存元数据、要点和判断，不保存论文全文或数据集副本。

## 2. Status and limits / 状态与限制

The repository was built on 2026-10-16 from 39 completed web searches (see `docs/search-log.md`). All 191 sources are marked verified=N: each was seen only at title, abstract or search-excerpt level, and none was checked against full text, because the build environment could not resolve the primary hosts and the bio-research literature servers failed to connect. In this repository, "not found" therefore means "not retrieved by a limited search", not "does not exist".

> 本仓库构建于 2026-10-16，基于 39 次已完成的网络检索（见 `docs/search-log.md`）。全部 191 条来源标记为 verified=N：每条都只被看到标题、摘要或检索摘录，没有一条核对过全文，因为构建环境无法解析主要站点，且 bio-research 文献服务器连接失败。因此在本仓库中，“未找到”意味着“有限检索未取回”，而不是“不存在”。

## 3. How to read / 阅读方式

Every conclusion is written in English and is followed immediately by its complete Chinese translation, set as a blockquote. Claims carry source IDs such as [GD06]; each ID resolves to a row in `data/sources.csv`. Numbers marked "self-reported" come from the authors of the method itself, and numbers marked "secondary" come from a summary rather than the primary paper. Facts, judgments, recommended actions and questions are kept in separate sections.

> 每条结论先用英文撰写，紧跟其完整的中文翻译（引用块）。论断带有 [GD06] 这样的来源 ID；每个 ID 对应 `data/sources.csv` 中的一行。标注“自报”的数字来自方法作者自己，标注“二手”的数字来自总结而不是原论文。事实、判断、行动建议和问题分在不同的部分。

## 4. Navigation / 导航

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
| `docs/08-design-implications.md` | Three falsifiable hypotheses, candidate architectures, data plan, protocol, milestones | 三个可证伪假设、候选架构、数据计划、评测协议、里程碑 |
| `docs/search-log.md` | Every query, outcome, failure, gap and verification to-do | 每次查询、结果、失败、缺口与核验待办 |
| `data/sources.csv` | 191 sources with tier, key points (English and Chinese) and caveats | 191 条来源，含证据等级、要点（中英文）与注意事项 |
| `data/datasets.csv` | 20 datasets with scale, genotype information and caveats | 20 个数据集，含规模、基因型信息与注意事项 |
| `CLAUDE.md` | Conventions for extending the repository | 扩展本仓库的约定 |

## 5. Evidence tiers and category codes / 证据等级与类别代码

| Tier | Meaning | 含义 |
|---|---|---|
| T1 | Full text or official page was read and checked (none yet) | 已阅读并核对全文或官方页面（目前没有） |
| T2 | Peer-reviewed paper or preprint seen only at title, abstract or search-excerpt level | 同行评议论文或预印本，仅见到标题、摘要或检索摘录 |
| T3 | Secondary source: news, blog, code repository, social media, third-party summary or talk abstract | 二手来源：新闻、博客、代码仓库、社交媒体、第三方总结或讲座摘要 |

| Code | Category | 类别 |
|---|---|---|
| GV | Genetic variation layer | 遗传变异层 |
| GD | Genotype × drug → transcriptome evidence | 基因型×药物→转录组实证 |
| DS | Datasets | 数据集 |
| KB | Prior-knowledge bases and pharmacogenomics | 先验知识库与药物基因组学 |
| MD | Modeling methods | 建模方法 |
| WM | World models and virtual cells | 世界模型与虚拟细胞 |
| EV | Evaluation, baseline critiques and bias | 评测、基线批判与偏倚 |

## 6. Change log / 变更日志

On 2026-10-16 the repository was built for the first time, with 191 sources, 20 datasets and 44 log entries.

> 2026-10-16 首次构建本仓库，含 191 条来源、20 个数据集和 44 条日志条目。

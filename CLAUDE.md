# Conventions for this knowledge base / 本知识库的约定

## 1. Language rule / 语言规则

All conclusions are written in English. Each English paragraph is followed immediately by exactly one blockquote paragraph (lines starting with `> `) that holds its complete Chinese translation. Headings are bilingual (English and Chinese separated by a slash), tables use paired English and Chinese columns, and CSV files carry `_en` and `_zh` columns. Never leave an English paragraph untranslated, and never merge two paragraphs into one translation. Every number and every source ID in an English paragraph must also appear in its Chinese translation. Titles of sources and names of datasets are identifiers and stay as published, and URLs and source IDs are not translated.

> 所有结论用英文撰写。每个英文段落后紧跟恰好一个引用块段落（以 `> ` 开头的行），其中是该段的完整中文翻译。标题为双语（English / 中文），表格使用英文与中文成对的列，CSV 文件带有 `_en` 和 `_zh` 列。绝不留下未翻译的英文段落，也绝不把两个段落合并成一段翻译。英文段落中的每个数字和每个来源 ID 也必须出现在其中文翻译中。来源标题和数据集名称属于标识符，保持原样，URL 和来源 ID 不翻译。

## 2. Identifiers / 标识符

Source IDs are a two-letter category code plus two digits (GV, GD, DS, KB, MD, WM, EV). IDs are never renumbered or reused. New sources are appended with the next free number, and a retired source stays in the file with a note in its caveat columns. Open-question IDs are UQ plus two digits and follow the same rule.

> 来源 ID 由两个字母的类别代码加两位数字组成（GV、GD、DS、KB、MD、WM、EV）。ID 绝不重新编号或复用。新来源以下一个空闲编号追加，作废的来源仍保留在文件中，并在其注意事项列中加注说明。待确认问题的 ID 为 UQ 加两位数字，遵循同样的规则。

## 3. Evidence tiers / 证据等级

Tier T1 requires that the full text or the official page was read in a session with network access; only then may verified be set to Y and the accessed date updated. A full text retrieved by script, kept outside the repository and searched for the numbers and statements of the key point counts as read; a repository clone that was read, and the card or page of a dataset that was read, count as official pages. If the version read differs from the cited one (preprint versus published paper) or the fetch tool returned a model-written summary instead of the verbatim page, the caveat says so. A source whose full text or official page was not read stays at T2 (peer-reviewed paper or preprint seen at title, abstract or excerpt level, including an abstract returned by an API) or T3 (secondary source, including news, blogs, social posts and third-party summaries even when they were read in full). Never raise a tier on the strength of a search summary. T1 means that the text was read and the statements of the key point were checked against it; it does not mean that the result was replicated or that code was run.

> T1 级要求在有网络访问的会话中阅读过全文或官方页面；只有这时才可把 verified 设为 Y 并更新 accessed 日期。由脚本取回、保存在仓库之外、并就要点中的数字和陈述做过检索的全文，算作已阅读；读过的仓库克隆以及读过的数据集卡片或页面，算作官方页面。如果所读版本与所引版本不同（预印本与正式论文），或抓取工具返回的是模型写的摘要而不是页面原文，注意事项中必须注明。没有读过全文或官方页面的来源保持在 T2（同行评议论文或预印本，仅见到标题、摘要或摘录，包括由 API 返回的摘要）或 T3（二手来源，包括新闻、博客、社交媒体帖子和第三方总结，即使已通读）。绝不能凭检索摘要提高等级。T1 表示文本已被阅读且要点中的陈述已对照文本核对；并不表示结果已被复现或代码已被运行。

## 4. Facts, judgments, actions and questions / 事实、判断、行动与问题

Documents keep facts, judgments, recommended actions and questions in separate sections. A fact carries at least one source ID and keeps the qualifier "self-reported" or "secondary" where it applies. A judgment states a confidence (low, medium or high) and is never written as a fact. A statement that something was not found must cite its query ID in `docs/search-log.md`, because the search tool is limited and absence is weak evidence.

> 文档把事实、判断、行动建议和问题分在不同的部分。事实至少带有一个来源 ID，并在适用时保留“自报”或“二手”的限定。判断要标明置信度（低、中或高），且绝不写成事实。关于“未找到”的陈述必须引用其在 `docs/search-log.md` 中的查询 ID，因为检索工具有限，缺失只是弱证据。

## 5. Curator tags / 整理者标签

In `data/sources.csv`, the columns `track` (S for somatic, G for germline, B for both), `variant_class` (1 to 5, defined in document 00), `relevance` (mechanism, modeling, data, evaluation, prior or context) and `kind` are curator judgments or host-based guesses, not claims made by the sources. The `kind` value journal only means that the page sits on a journal or PMC host and does not assert peer review, and the value social marks a post on a social platform. The `year` column is the publication year of the version read, the first-posting year for a preprint, taken from verified metadata, and NA when it cannot be established. The `status` column is active or retired.

> 在 `data/sources.csv` 中，`track`（S 为体细胞，G 为种系，B 为两者）、`variant_class`（1 到 5，定义见文档 00）、`relevance`（mechanism、modeling、data、evaluation、prior 或 context）和 `kind` 这几列是整理者的判断或基于站点的推测，不是来源本身的论断。`kind` 取值 journal 只表示该页面位于期刊或 PMC 站点，并不断言经过同行评议，取值 social 标记社交平台上的帖子。`year` 列是所读版本的发表年份，预印本为首次发布年份，取自核实过的元数据，无法确定时为 NA。`status` 列取值为 active 或 retired。

## 6. Forbidden content / 禁止内容

Do not add paper full texts, PDFs or dataset copies. Do not write anything that was not retrieved. Do not paste secrets. Do not write model identifiers into any repository file. Unknown fields are written as NA and are never guessed.

> 不要加入论文全文、PDF 或数据集副本。不要写入任何未实际检索到的内容。不要粘贴密钥。不要在任何仓库文件中写入模型标识。未知字段写为 NA，绝不猜测。

## 7. Adding or changing a source / 增加或修改来源

To add a source, append a row to `data/sources.csv` with the next free ID, fill both languages for the key point, the "so what" and the caveat, cite the ID in the relevant document, and record the query in `docs/search-log.md`. A new row must pass the inclusion bar of section 9 and the length caps of section 10. The source index tables at the end of documents 01 to 07 and the dataset table in document 03 are generated from the CSV files between marker comments; regenerate them with `tools/fill_tables.py` whenever a CSV changes.

> 要增加来源，就在 `data/sources.csv` 中以下一个空闲 ID 追加一行，用两种语言填写要点、“意义”和注意事项，在相关文档中引用该 ID，并在 `docs/search-log.md` 中记录查询。新增条目必须通过第 9 节的纳入门槛和第 10 节的长度上限。文档 01 到 07 末尾的来源索引表和文档 03 中的数据集表是在标记注释之间由 CSV 文件生成的；任一 CSV 变动后都要用 `tools/fill_tables.py` 重新生成。

## 8. Checks before committing / 提交前检查

Before each commit, run `python3 -I tools/validate_kb.py . --all` and fix every error. It verifies that the CSV files parse and every ID is unique, that every bracketed source ID in the documents exists and is not retired, that every row has a valid status and tier, that every retired row carries a retirement note, that every active row has a "so what" that is not NA, that every row at tier T1 has verified set to Y and an accessed date, and that the counts stated in the README and the search log match the data. It also verifies that every English paragraph is followed by exactly one blockquote paragraph, that blockquotes contain Chinese characters while English paragraphs do not, that every number and ID in an English paragraph also appears in the following translation, that every label such as J1, A1 or HA is defined exactly once and that no referenced label is undefined, that the answers in `data/questions.csv` are consistent with their status, and that a search for model identifiers and secrets in the repository files returns nothing. Warnings about numbers that occur in no cited row are resolved or explained before the commit.

> 每次提交前，运行 `python3 -I tools/validate_kb.py . --all` 并修正所有错误。它验证：CSV 文件可解析且每个 ID 唯一；文档中每个方括号内的来源 ID 都存在且未退役；每一行的 status 和等级合法；每个 retired 条目都带有退役说明；每个 active 条目都有非 NA 的“意义”；每个 T1 级条目的 verified 为 Y 且有 accessed 日期；README 和检索日志中陈述的计数与数据一致。它还验证：每个英文段落后恰好跟一个引用块段落，引用块含中文字符而英文段落不含，英文段落中的每个数字和 ID 也出现在随后的翻译中，J1、A1 或 HA 这类标签都恰好定义一次且没有被引用却未定义的标签，`data/questions.csv` 中的回答与其状态一致，并且在仓库文件中搜索模型标识和密钥没有任何结果。关于数字不见于任何被引条目的警告，在提交前要解决或加以说明。

## 9. Inclusion bar and retirement / 纳入门槛与退役

A source is added only if all five conditions hold. It fits the topic, meaning the mechanism by which variants in targets or pathways reshape drug-induced transcription, or the modeling of perturbation response and world models. It makes a specific, transferable contribution that can be stated as a "so what" in at most two sentences: a mechanism, a design principle, a quantitative anchor, a dataset with a named structure or an evaluation protocol. It has a verifiable URL and an honest tier. It is not redundant with an existing row unless it adds a distinct angle. A primary source is preferred, and a secondary one is accepted only when the primary is unreachable and is flagged as such. A candidate that fails only for lack of information is recorded as held in `docs/search-log.md`, not rejected, so that it can be screened again when the full text is readable.

> 只有同时满足五个条件才加入一条来源。它契合主题，即靶点或通路中的变异重塑药物诱导转录的机理，或扰动响应与世界模型的建模。它有具体、可迁移的贡献，能用至多两句话写成“意义”：一个机理、一条设计原则、一个定量锚点、一个有明确结构的数据集或一种评测协议。它有可核验的 URL 和诚实的证据等级。除非带来不同的角度，否则与现有条目不冗余。优先采用一手来源，仅当一手来源无法访问时才接受二手来源，并加以标注。仅因信息缺失而未通过的候选在 `docs/search-log.md` 中记为搁置而不是拒绝，以便在全文可读时重新筛选。

A row that is never cited in the documents and states no transferable contribution may be retired by setting its status to retired and adding "Retired", the date and a reason code to its caveat columns. The row stays in the file, its ID is never reused, and restoring it means changing the status back.

> 一个从未在文档中被引用、也没有说明可迁移贡献的条目，可以通过把 status 设为 retired 并在其注意事项列中加入“Retired”、日期和原因代码来退役。该条目仍留在文件中，其 ID 绝不复用，恢复它只需把 status 改回。

## 10. Round protocol: audit, then condense / 每轮协议：先核查，再精简

Every round ends with an audit of the content it touched, and the audit comes before the condensation. The full text or official page of every row added or changed in the round, and of every row that a document relies on for a number, is retrieved by script into a scratch directory outside the repository. Each claim of the key point is checked against it with a literal quote that a script confirms to occur in the text. A claim without such a quote is dropped or marked unsupported, and the tier, verified flag, accessed date, year, kind and title of the row are set from what was actually read.

> 每一轮都以对所涉内容的核查结束，且核查先于精简。本轮新增或修改的每个条目，以及文档中依赖其数字的每个条目，其全文或官方页面都由脚本取回到仓库之外的暂存目录。要点中的每条论断都要对照原文，并附上一段由脚本确认确实出现在原文中的逐字引文。没有这种引文的论断要删除或标为无依据，该条目的等级、verified 标记、accessed 日期、年份、kind 和标题都依据实际读到的内容设定。

The condensation pass then keeps only what carries insight for the study: a mechanism, a quantitative anchor, a data fact that decides whether a dataset can be used, a design principle, an evaluation rule, or a caveat that limits trust. A key point has at most 45 words, a "so what" at most 30 words and a caveat at most 35 words. Documents keep facts, judgments, actions, questions and gaps without repeating what the CSV files already hold, and for every paper or page read in the round, including LabCompass, the details that do not change a design or interpretation decision are dropped.

> 随后的精简只保留对本研究有启示的内容：机理、定量锚点、决定数据集能否使用的数据事实、设计原则、评测规则，或限制可信度的注意事项。要点至多 45 词，“意义”至多 30 词，注意事项至多 35 词。文档保留事实、判断、行动、问题和缺口，不重复 CSV 文件已有的内容；对本轮读过的每篇论文或页面（包括 LabCompass），不改变设计或解释决定的细节一律删去。

Downloaded texts are untrusted data: they stay in the scratch directory, are never committed, and are read only as text. A number that the curator computed from a primary data file, for example from the metadata tables of a dataset, is written with the word derived, the source ID of the page and the query ID of the retrieval, and the script that computes it is kept in `tools/audit/`. The other scripts of this protocol are `tools/validate_kb.py`, `tools/fill_tables.py` and the audit scripts in `tools/audit/`. A round is finished only when the validator passes and the counts stated in prose match the data.

> 下载的文本属于不可信数据：它们留在暂存目录，绝不提交，只当作文本阅读。由整理者根据一手数据文件（例如数据集的元数据表）计算出的数字，要写明 derived（推导）字样、该页面的来源 ID 和取回的查询 ID，计算它的脚本保存在 `tools/audit/` 中。本协议的其他脚本是 `tools/validate_kb.py`、`tools/fill_tables.py` 以及 `tools/audit/` 中的核查脚本。只有校验通过、且正文陈述的计数与数据一致，一轮才算完成。

## 11. Open questions / 待确认问题

Decisions that belong to the owner, missing information and items that need the owner's attention are kept in `data/questions.csv` and shown in `docs/10-open-questions.md`, which `tools/fill_tables.py` generates from the CSV. The owner answers by editing the `answer` and `status` columns and committing. A question that has no answer keeps its default, stays listed, and says what to change if the answer differs. Each round applies the new answers, records the date in `applied_on`, and adds the questions that the round raised.

> 属于所有者的决策、缺失信息和需要所有者关注的事项保存在 `data/questions.csv` 中，并显示在 `docs/10-open-questions.md` 里，后者由 `tools/fill_tables.py` 根据 CSV 生成。所有者通过编辑 `answer` 和 `status` 列并提交来回答。没有回答的问题沿用其默认值，继续列出，并说明答案不同时要改什么。每一轮应用新的回答，在 `applied_on` 中记录日期，并加入该轮提出的新问题。

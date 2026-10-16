# Conventions for this knowledge base / 本知识库的约定

## 1. Language rule / 语言规则

All conclusions are written in English. Each English paragraph is followed immediately by exactly one blockquote paragraph (lines starting with `> `) that holds its complete Chinese translation. Headings are bilingual (English and Chinese separated by a slash), tables use paired English and Chinese columns, and CSV files carry `_en` and `_zh` columns. Never leave an English paragraph untranslated, and never merge two paragraphs into one translation. Every number and every source ID in an English paragraph must also appear in its Chinese translation. Titles of sources and names of datasets are identifiers and stay as published, and URLs and source IDs are not translated.

> 所有结论用英文撰写。每个英文段落后紧跟恰好一个引用块段落（以 `> ` 开头的行），其中是该段的完整中文翻译。标题为双语（English / 中文），表格使用英文与中文成对的列，CSV 文件带有 `_en` 和 `_zh` 列。绝不留下未翻译的英文段落，也绝不把两个段落合并成一段翻译。英文段落中的每个数字和每个来源 ID 也必须出现在其中文翻译中。来源标题和数据集名称属于标识符，保持原样，URL 和来源 ID 不翻译。

## 2. Identifiers / 标识符

Source IDs are a two-letter category code plus two digits (GV, GD, DS, KB, MD, WM, EV). IDs are never renumbered or reused. New sources are appended with the next free number, and a retired source stays in the file with a note in its caveat columns.

> 来源 ID 由两个字母的类别代码加两位数字组成（GV、GD、DS、KB、MD、WM、EV）。ID 绝不重新编号或复用。新来源以下一个空闲编号追加，作废的来源仍保留在文件中，并在其注意事项列中加注说明。

## 3. Evidence tiers / 证据等级

Tier T1 requires that the full text or the official page was read in a session with network access; only then may verified be set to Y and the accessed date updated. A GitHub or PyPI page counts as an official page when it was actually retrieved and not only seen in a search result, and the caveat must say so if the fetch tool returned a model-written summary instead of the verbatim page. A source whose full text or official page was not read stays at T2 (peer-reviewed paper or preprint seen at title, abstract or excerpt level) or T3 (secondary source). Never raise a tier on the strength of a search summary.

> T1 级要求在有网络访问的会话中阅读过全文或官方页面；只有这时才可把 verified 设为 Y 并更新 accessed 日期。GitHub 或 PyPI 页面只有在确实被取回、而不是仅在检索结果中见到时，才算官方页面；如果抓取工具返回的是模型写的摘要而不是页面原文，注意事项中必须注明。没有读过全文或官方页面的来源保持在 T2（同行评议论文或预印本，仅见到标题、摘要或摘录）或 T3（二手来源）。绝不能凭检索摘要提高等级。

## 4. Facts, judgments, actions and questions / 事实、判断、行动与问题

Documents keep facts, judgments, recommended actions and questions in separate sections. A fact carries at least one source ID and keeps the qualifier "self-reported" or "secondary" where it applies. A judgment states a confidence (low, medium or high) and is never written as a fact. A statement that something was not found must cite its query ID in `docs/search-log.md`, because the search tool is limited and absence is weak evidence.

> 文档把事实、判断、行动建议和问题分在不同的部分。事实至少带有一个来源 ID，并在适用时保留“自报”或“二手”的限定。判断要标明置信度（低、中或高），且绝不写成事实。关于“未找到”的陈述必须引用其在 `docs/search-log.md` 中的查询 ID，因为检索工具有限，缺失只是弱证据。

## 5. Curator tags / 整理者标签

In `data/sources.csv`, the columns `track` (S for somatic, G for germline, B for both), `variant_class` (1 to 5, defined in document 00), `relevance` (mechanism, modeling, data, evaluation, prior or context) and `kind` are curator judgments or host-based guesses, not claims made by the sources. The `kind` value journal only means that the page sits on a journal or PMC host and does not assert peer review, and the value social marks a post on a social platform. The `year` column is derived from identifiers such as DOIs, arXiv numbers and publisher codes, is the first-posting year for preprints, and is NA when it cannot be derived. The `status` column is active or retired.

> 在 `data/sources.csv` 中，`track`（S 为体细胞，G 为种系，B 为两者）、`variant_class`（1 到 5，定义见文档 00）、`relevance`（mechanism、modeling、data、evaluation、prior 或 context）和 `kind` 这几列是整理者的判断或基于站点的推测，不是来源本身的论断。`kind` 取值 journal 只表示该页面位于期刊或 PMC 站点，并不断言经过同行评议，取值 social 标记社交平台上的帖子。`year` 列由 DOI、arXiv 编号和出版商代码等标识符推导，对预印本是首次发布年份，无法推导时为 NA。`status` 列取值为 active 或 retired。

## 6. Forbidden content / 禁止内容

Do not add paper full texts, PDFs or dataset copies. Do not write anything that was not retrieved. Do not paste secrets. Do not write model identifiers into any repository file. Unknown fields are written as NA and are never guessed.

> 不要加入论文全文、PDF 或数据集副本。不要写入任何未实际检索到的内容。不要粘贴密钥。不要在任何仓库文件中写入模型标识。未知字段写为 NA，绝不猜测。

## 7. Adding or changing a source / 增加或修改来源

To add a source, append a row to `data/sources.csv` with the next free ID, fill both languages for the key point, the "so what" and the caveat, cite the ID in the relevant document, and record the query in `docs/search-log.md`. A new row must pass the inclusion bar of section 9. The source index tables at the end of documents 01 to 07 were generated from the CSV between marker comments and show active rows only; regenerate them whenever the CSV changes.

> 要增加来源，就在 `data/sources.csv` 中以下一个空闲 ID 追加一行，用两种语言填写要点、“意义”和注意事项，在相关文档中引用该 ID，并在 `docs/search-log.md` 中记录查询。新增条目必须通过第 9 节的纳入门槛。文档 01 到 07 末尾的来源索引表是在标记注释之间由 CSV 生成的，只显示 active 条目；CSV 每次变动后都要重新生成。

## 8. Checks before committing / 提交前检查

Before each commit, verify that the CSV files parse and every ID is unique. Verify that every bracketed source ID in the documents exists in `data/sources.csv`, that the status of every row is active or retired, that every retired row carries a retirement note in its caveat columns, and that every row added since the inclusion bar was introduced has a "so what" that is not NA. Verify that in the documents every English paragraph is followed by exactly one blockquote paragraph, that blockquotes contain Chinese characters while English paragraphs do not, and that every number and ID in an English paragraph also appears in the following translation. Verify that every row at tier T1 has verified set to Y and an accessed date. Finally, verify that a search for model identifiers in the repository files returns nothing.

> 每次提交前，确认 CSV 文件可解析且每个 ID 唯一。确认文档中每个方括号内的来源 ID 都存在于 `data/sources.csv` 中，每一行的 status 为 active 或 retired，每个 retired 条目都在注意事项列中带有退役说明，并且引入纳入门槛之后新增的每一行都有非 NA 的“意义”。确认文档中每个英文段落后恰好跟一个引用块段落，引用块含中文字符而英文段落不含，且英文段落中的每个数字和 ID 也出现在随后的翻译中。确认每个 T1 级条目的 verified 为 Y 且有 accessed 日期。最后确认在仓库文件中搜索模型标识没有任何结果。

## 9. Inclusion bar and retirement / 纳入门槛与退役

A source is added only if all five conditions hold. It fits the topic, meaning the mechanism by which variants in targets or pathways reshape drug-induced transcription, or the modeling of perturbation response and world models. It makes a specific, transferable contribution that can be stated as a "so what" in at most two sentences: a mechanism, a design principle, a quantitative anchor, a dataset with a named structure or an evaluation protocol. It has a verifiable URL and an honest tier. It is not redundant with an existing row unless it adds a distinct angle. A primary source is preferred, and a secondary one is accepted only when the primary is unreachable and is flagged as such. A candidate that fails only for lack of information is recorded as held in `docs/search-log.md`, not rejected, so that it can be screened again when the full text is readable.

> 只有同时满足五个条件才加入一条来源。它契合主题，即靶点或通路中的变异重塑药物诱导转录的机理，或扰动响应与世界模型的建模。它有具体、可迁移的贡献，能用至多两句话写成“意义”：一个机理、一条设计原则、一个定量锚点、一个有明确结构的数据集或一种评测协议。它有可核验的 URL 和诚实的证据等级。除非带来不同的角度，否则与现有条目不冗余。优先采用一手来源，仅当一手来源无法访问时才接受二手来源，并加以标注。仅因信息缺失而未通过的候选在 `docs/search-log.md` 中记为搁置而不是拒绝，以便在全文可读时重新筛选。

A row that is never cited in the documents and states no transferable contribution may be retired by setting its status to retired and adding "Retired", the date and a reason code to its caveat columns. The row stays in the file, its ID is never reused, and restoring it means changing the status back.

> 一个从未在文档中被引用、也没有说明可迁移贡献的条目，可以通过把 status 设为 retired 并在其注意事项列中加入“Retired”、日期和原因代码来退役。该条目仍留在文件中，其 ID 绝不复用，恢复它只需把 status 改回。

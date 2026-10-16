# Conventions for this knowledge base / 本知识库的约定

## 1. Language rule / 语言规则

All conclusions are written in English. Each English paragraph is followed immediately by exactly one blockquote paragraph (lines starting with `> `) that holds its complete Chinese translation. Headings are bilingual (English and Chinese separated by a slash), tables use paired English and Chinese columns, and CSV files carry `_en` and `_zh` columns. Never leave an English paragraph untranslated, and never merge two paragraphs into one translation. Every number and every source ID in an English paragraph must also appear in its Chinese translation.

> 所有结论用英文撰写。每个英文段落后紧跟恰好一个引用块段落（以 `> ` 开头的行），其中是该段的完整中文翻译。标题为双语（English / 中文），表格使用英文与中文成对的列，CSV 文件带有 `_en` 和 `_zh` 列。绝不留下未翻译的英文段落，也绝不把两个段落合并成一段翻译。英文段落中的每个数字和每个来源 ID 也必须出现在其中文翻译中。

## 2. Identifiers / 标识符

Source IDs are a two-letter category code plus two digits (GV, GD, DS, KB, MD, WM, EV). IDs are never renumbered or reused. New sources are appended with the next free number, and a retired source stays in the file with a note in its caveat columns.

> 来源 ID 由两个字母的类别代码加两位数字组成（GV、GD、DS、KB、MD、WM、EV）。ID 绝不重新编号或复用。新来源以下一个空闲编号追加，作废的来源仍保留在文件中，并在其注意事项列中加注说明。

## 3. Evidence tiers / 证据等级

Tier T1 requires that the full text or the official page was read in a session with network access; only then may verified be set to Y and the accessed date updated. Otherwise a source stays at T2 (peer-reviewed paper or preprint seen at title, abstract or excerpt level) or T3 (secondary source). Never raise a tier on the strength of a search summary.

> T1 级要求在有网络访问的会话中阅读过全文或官方页面；只有这时才可把 verified 设为 Y 并更新 accessed 日期。否则来源保持在 T2（同行评议论文或预印本，仅见到标题、摘要或摘录）或 T3（二手来源）。绝不能凭检索摘要提高等级。

## 4. Facts, judgments, actions and questions / 事实、判断、行动与问题

Documents keep facts, judgments, recommended actions and questions in separate sections. A fact carries at least one source ID and keeps the qualifier "self-reported" or "secondary" where it applies. A judgment states a confidence (low, medium or high) and is never written as a fact. A statement that something was not found must cite its query ID in `docs/search-log.md`, because the search tool is limited and absence is weak evidence.

> 文档把事实、判断、行动建议和问题分在不同的部分。事实至少带有一个来源 ID，并在适用时保留“自报”或“二手”的限定。判断要标明置信度（低、中或高），且绝不写成事实。关于“未找到”的陈述必须引用其在 `docs/search-log.md` 中的查询 ID，因为检索工具有限，缺失只是弱证据。

## 5. Curator tags / 整理者标签

In `data/sources.csv`, the columns `track` (S for somatic, G for germline, B for both), `variant_class` (1 to 5, defined in document 00) and `kind` are curator judgments or host-based guesses, not claims made by the sources. The `kind` value journal only means that the page sits on a journal or PMC host and does not assert peer review. The `year` column is derived from identifiers such as DOIs, arXiv numbers and publisher codes, is the first-posting year for preprints, and is NA when it cannot be derived.

> 在 `data/sources.csv` 中，`track`（S 为体细胞，G 为种系，B 为两者）、`variant_class`（1 到 5，定义见文档 00）和 `kind` 这几列是整理者的判断或基于站点的推测，不是来源本身的论断。`kind` 取值 journal 只表示该页面位于期刊或 PMC 站点，并不断言经过同行评议。`year` 列由 DOI、arXiv 编号和出版商代码等标识符推导，对预印本是首次发布年份，无法推导时为 NA。

## 6. Forbidden content / 禁止内容

Do not add paper full texts, PDFs or dataset copies. Do not write anything that was not retrieved. Do not paste secrets. Do not write model identifiers into any repository file. Unknown fields are written as NA and are never guessed.

> 不要加入论文全文、PDF 或数据集副本。不要写入任何未实际检索到的内容。不要粘贴密钥。不要在任何仓库文件中写入模型标识。未知字段写为 NA，绝不猜测。

## 7. Adding or changing a source / 增加或修改来源

To add a source, append a row to `data/sources.csv` with the next free ID, fill both languages for the key point and the caveat, cite the ID in the relevant document, and record the query in `docs/search-log.md`. The source index tables at the end of documents 01 to 07 were generated from the CSV between marker comments; regenerate them whenever the CSV changes.

> 要增加来源，就在 `data/sources.csv` 中以下一个空闲 ID 追加一行，用两种语言填写要点和注意事项，在相关文档中引用该 ID，并在 `docs/search-log.md` 中记录查询。文档 01 到 07 末尾的来源索引表是在标记注释之间由 CSV 生成的；CSV 每次变动后都要重新生成。

## 8. Checks before committing / 提交前检查

Before each commit, verify that the CSV files parse and every ID is unique. Verify that every bracketed source ID in the documents exists in `data/sources.csv`. Verify that in the documents every English paragraph is followed by exactly one blockquote paragraph, that blockquotes contain Chinese characters while English paragraphs do not, and that every number and ID in an English paragraph also appears in the following translation. Finally, verify that a search for model identifiers in the repository files returns nothing.

> 每次提交前，确认 CSV 文件可解析且每个 ID 唯一。确认文档中每个方括号内的来源 ID 都存在于 `data/sources.csv` 中。确认文档中每个英文段落后恰好跟一个引用块段落，引用块含中文字符而英文段落不含，且英文段落中的每个数字和 ID 也出现在随后的翻译中。最后确认在仓库文件中搜索模型标识没有任何结果。

# 04 Prior-knowledge bases and pharmacogenomics / 先验知识库与药物基因组学

## 1. Scope / 范围

This document covers two kinds of prior knowledge that a variant-aware transcriptome model could use: signaling and regulatory networks that encode how drug targets connect to downstream genes, and pharmacogenomics resources that annotate which variants matter for which drugs. It records what the retrieved sources say about their content, scope and disagreements.

> 本文档涵盖变异感知的转录组模型可以使用的两类先验知识：编码药物靶点如何连接到下游基因的信号与调控网络，以及标注哪些变异对哪些药物重要的药物基因组学资源。它记录了检索到的来源关于这些资源的内容、范围和分歧的说法。

## 2. Facts and evidence / 事实与证据

OmniPath is an integrated knowledgebase that began with causal signaling interactions and later added transcription-factor targets, enzyme–post-translational-modification relationships, localization, intercellular communication and complexes, with Python and R clients [KB01]. A 2020 paper counts 34 resources aggregated by OmniPath [KB02].

> OmniPath 是一个整合型知识库，起初收录因果信号相互作用，后来加入了转录因子靶标、酶-翻译后修饰关系、定位、细胞间通讯和复合物，并提供 Python 和 R 客户端 [KB01]。一篇 2020 年的论文统计 OmniPath 聚合了 34 个资源 [KB02]。

SIGNOR is a manually curated, literature-based database of causal interactions in which each edge records activation or inhibition and the mechanism, and its 2025 release puts particular emphasis on phosphorylation data [KB04]. The 2022 update reported roughly 33% proteome coverage [KB05]. STRING stores undirected interactions whereas SIGNOR stores directed ones [KB09].

> SIGNOR 是人工整理的、基于文献的因果相互作用数据库，每条边记录激活或抑制及其机制，其 2025 版特别强调磷酸化数据 [KB04]。2022 年的更新报告了约 33% 的蛋白组覆盖率 [KB05]。STRING 存储无向相互作用，而 SIGNOR 存储有向相互作用 [KB09]。

Open Targets is a platform for target prioritisation that scores target–disease evidence from many sources [KB07]. Its molecular-interactions documentation lists SIGNOR and Reactome among its sources and imports only human–human Reactome interactions, which are directional and signed where possible [KB08]. Pathway footprints such as those of PROGENy are derived from perturbation-response genes [KB10], and could be used as pathway-activity features or readouts, which is a suggestion and not a finding of that paper.

> Open Targets 是一个靶点优先排序平台，对来自多种来源的靶点-疾病证据打分 [KB07]。其分子相互作用文档把 SIGNOR 和 Reactome 列为来源，并且只引入人-人的 Reactome 相互作用，这些相互作用是有方向的，并尽量带符号 [KB08]。PROGENy 这类通路足迹源自扰动响应基因 [KB10]，可以用作通路活性特征或读出，这是一个建议，不是该论文的发现。

A signaling-network recurrent model such as LEMBAS sets its weights to real molecular interactions and zeroes all others [MD12]. Its GPU re-implementation is more than 7-fold faster, and it prunes false edges added to the prior network to a larger extent than edges of the original prior network, provided the L2 regularization is sufficiently large [MD13].

> 像 LEMBAS 这样的信号网络循环模型，把权重设置为真实的分子相互作用，其余全部置零 [MD12]。它的 GPU 重新实现快 7 倍以上，并且对加入先验网络的错误边的剪除程度大于对原始先验网络中边的剪除程度，前提是 L2 正则足够大 [MD13]。

For pharmacogenomics, PharmVar places copy-number variants, hybrid genes and duplications in a structural-variant class [KB11], and CYP2D6 illustrates the problem: about 133 to 137 star alleles are listed depending on the source [KB13], some alleles are specific to ancestry groups such as sub-Saharan African populations [KB15], and some SNPs cause false copy-number-loss calls in common assays [KB16]. A comparison of star-allele callers exists [KB12]. A 3-SNP haplotype model was reported to fit CYP2D6 expression best, but that report comes from a tier-T3 entry whose title was not retrieved [KB14].

> 在药物基因组学方面，PharmVar 把拷贝数变异、杂合基因和重复归入结构变异类别 [KB11]，CYP2D6 说明了这个问题：按来源不同，列出约 133 到 137 个星等位基因 [KB13]，一些等位基因特异于撒哈拉以南非洲人群等祖源群体 [KB15]，而一些 SNP 会在常用检测中造成拷贝数缺失的假阳性调用 [KB16]。星等位基因调用工具的比较已有 [KB12]。有报告称 3-SNP 单倍型模型对 CYP2D6 表达拟合最好，但该报告来自一条标题未取得的 T3 级条目 [KB14]。

The pharmacogenomics resources disagree with each other. The FDA table and CPIC give the same gene–drug association and dosing recommendation for only 5 of 126 drugs, and the FDA publishes two tables, one from CDER and one from CDRH [KB17]. CPIC's actionability grades A to D are not the same as PharmGKB's evidence levels [KB18]. For drugs with a narrow therapeutic index, misimputation of pharmacogenetic variants is risky, and direct genotyping is recommended for established actionable variants [KB19].

> 药物基因组学资源彼此不一致。FDA 表与 CPIC 对同一基因-药物关联和剂量建议一致的药物仅为 126 种中的 5 种，且 FDA 发布两张表，一张来自 CDER，一张来自 CDRH [KB17]。CPIC 的可操作性分级 A 到 D 与 PharmGKB 的证据等级并不相同 [KB18]。对于窄治疗窗药物，药物遗传学变异的误填补有风险，对于已确立的可操作变异，建议直接基因分型 [KB19]。

## 3. Judgments / 判断

J10 (confidence: low). Directed, signed edges (SIGNOR, and Reactome through Open Targets) are the more natural masks for an action-conditioned transition operator than undirected edges (STRING) [KB09, KB04, KB08]. However, in one benchmark of cancer perturbation response, STRING-based encodings were the best for genetic perturbations, so the choice should be tested rather than assumed [EV16].

> J10（置信度：低）。对于动作条件的转移算子，有向、带符号的边（SIGNOR，以及经由 Open Targets 的 Reactome）比无向边（STRING）更自然地可用作掩码 [KB09, KB04, KB08]。然而在一项癌症扰动响应基准中，基于 STRING 的编码对基因扰动效果最好，因此这一选择应经测试而不是想当然 [EV16]。

J14 (confidence: medium). No single pharmacogenomics resource can be treated as ground truth, because the FDA table, CPIC and PharmGKB agree on only a small share of drugs [KB17, KB18].

> J14（置信度：中）。不能把任何单一药物基因组学资源当作真值，因为 FDA 表、CPIC 和 PharmGKB 只在一小部分药物上一致 [KB17, KB18]。

## 4. Recommended actions / 行动建议

Use OmniPath as the aggregator and SIGNOR as the signed, directed core of any prior network, and record the provenance of every edge so that edges from different resources can be ablated separately [KB01, KB04].

> 把 OmniPath 用作聚合器，把 SIGNOR 用作任何先验网络的带符号、有向的核心，并记录每条边的出处，以便可以分别消融来自不同资源的边 [KB01, KB04]。

Keep FDA, CPIC and PharmGKB labels as separate annotation layers and record which layer a label comes from, instead of merging them into one truth [KB17, KB18].

> 把 FDA、CPIC 和 PharmGKB 的标签保留为各自独立的注释层，并记录标签来自哪一层，而不是把它们合并成一个真值 [KB17, KB18]。

Call pharmacogene alleles, including copy-number variants and star alleles, with dedicated callers rather than from array-imputed genotypes [KB12, KB16, KB19].

> 用专门的调用工具来调用药物基因的等位基因（包括拷贝数变异和星等位基因），而不是依赖芯片填补的基因型 [KB12, KB16, KB19]。

Test the choice of prior network empirically, with an ablation of directed-signed against undirected edges, before building it into an architecture [EV16].

> 在把先验网络写入架构之前，通过有向带符号边与无向边的消融，对先验网络的选择做经验检验 [EV16]。

## 5. Questions for confirmation / 待确认问题

Should the first prior network be restricted to the signaling pathways of the drug classes in scope? Default: no restriction until the drug classes are chosen (assumption M2 in document 00).

> 第一版先验网络是否应限制在所涉药物类别的信号通路上？默认：在选定药物类别之前不设限制（文档 00 中的假设 M2）。

## 6. Evidence gaps / 证据缺口

Reactome itself was not retrieved as a source: it appears only through the Open Targets documentation [KB08]. DrugBank, DGIdb and ChEMBL were not retrieved, and the bio-research literature servers that would give structured access failed to connect. No source describing how OmniPath, SIGNOR, Reactome and Open Targets are combined in one pipeline was found (query Q21). No annotation of noncoding regulatory variants under PharmVar was found (query Q22). PharmGKB and CPIC were seen only through resource-level statements and comparison documents (queries Q08 and Q38), not through their raw data.

> Reactome 本身没有作为来源被检索到：它只出现在 Open Targets 文档中 [KB08]。DrugBank、DGIdb 和 ChEMBL 没有被检索到，而能提供结构化访问的 bio-research 文献服务器连接失败。没有找到描述 OmniPath、SIGNOR、Reactome 和 Open Targets 如何在同一管线中组合的来源（查询 Q21）。没有找到 PharmVar 下对非编码调控变异的注释（查询 Q22）。PharmGKB 和 CPIC 只通过资源层面的陈述和对比文档被看到（查询 Q08 和 Q38），而不是通过其原始数据。

## 7. Source index (category KB) / 来源索引（类别 KB）

Generated from `data/sources.csv`; regenerate when the CSV changes.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。

<!-- source-index:KB:start -->
| ID | Tier | Title | Key point | 要点（中文） |
|---|---|---|---|---|
| KB01 | T2 | [OmniPath: integrated knowledgebase for multi-omics analysis](<https://www.biorxiv.org/content/10.1101/2025.09.11.675512v1.full.pdf>) | aggregates signaling, TF targets, enzyme–PTM, localization, intercellular communication, complexes | 聚合信号、TF 靶、酶-PTM、定位、胞间通讯、复合物 |
| KB02 | T2 | [OmniPath resource metadata page](<https://omnipathdb.org/info>) | 34 resources aggregated (per a 2020 paper) | 聚合 34 个资源（据 2020 年论文） |
| KB03 | T2 | [Integrating knowledge and omics to decipher mechanisms via large-scale models of signaling networks](<https://link.springer.com/article/10.15252/msb.202211036>) | — | — |
| KB04 | T2 | [SIGNOR 4.0: the 2025 update with focus on phosphorylation data](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12807704/>) | manually curated directed causal edges (activation or inhibition plus mechanism) | 人工整理的有向因果边（激活或抑制及机制） |
| KB05 | T2 | [SIGNOR 3.0, the SIGnaling network open resource 3.0: 2022 update](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825604/>) | about 33% proteome coverage | 蛋白组覆盖约 33% |
| KB06 | T2 | [SIGNOR 2.0, the SIGnaling Network Open Resource 2.0: 2019 update](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7145695/>) | — | — |
| KB07 | T2 | [Open Targets Platform: supporting systematic drug–target identification and prioritisation](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7779013/>) | — | — |
| KB08 | T2 | [Open Targets documentation: Molecular interactions](<https://platform-docs.opentargets.org/target/molecular-interactions>) | imports SIGNOR and Reactome (human–human, directional, signed where possible) | 引入 SIGNOR 和 Reactome（人-人、有向、尽量带符号） |
| KB09 | T2 | [Large-scale regulatory and signaling network assembly through linked open data](<https://academic.oup.com/database/article/doi/10.1093/database/baaa113/6103765>) | STRING is undirected, SIGNOR directed | STRING 无向，SIGNOR 有向 |
| KB10 | T2 | [Perturbation-response genes reveal signaling footprints in cancer gene expression (PROGENy)](<https://www.nature.com/articles/s41467-017-02391-6>) | pathway-activity signatures usable as features or readouts | 通路活性特征，可用作特征或读数 |
| KB11 | T2 | [PharmVar: Allele Designation Criteria and Evidence Levels](<https://www.pharmvar.org/criteria>) | CNVs, hybrid genes and duplications are a structural-variant class | CNV、杂合基因和重复属于结构变异类 |
| KB12 | T2 | [A systematic comparison of pharmacogene star allele calling bioinformatics algorithms: a focus on CYP2D6 genotyping](<https://www.nature.com/articles/s41525-020-0135-2>) | comparison of star-allele callers | 星等位基因调用工具的比较 |
| KB13 | T2 | [A Review of the Important Role of CYP2D6 in Pharmacogenomics](<https://www.mdpi.com/2073-4425/11/11/1295>) | about 133–137 CYP2D6 star alleles on PharmVar (counts differ by source) | PharmVar 上约 133–137 个 CYP2D6 星等位基因（各来源计数不同） |
| KB14 | T3 | [(title not retrieved) Frontiers in Pharmacology 2023, CYP2D6 expression model](<https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1186540/epub>) | a 3-SNP-haplotype model fit CYP2D6 expression best | 3-SNP 单倍型模型对 CYP2D6 表达拟合最好 |
| KB15 | T2 | [Characterization of Novel CYP2D6 Alleles across Sub-Saharan African Populations](<https://www.mdpi.com/2075-4426/12/10/1575>) | ancestry-specific alleles | 祖源特异的等位基因 |
| KB16 | T2 | [Identification of CYP2D6 Haplotypes that Interfere with Commonly Used Assays for Copy Number Variation Characterization](<https://www.sciencedirect.com/science/article/pii/S1525157821000416>) | some SNPs cause false copy-number-loss calls | 部分 SNP 造成拷贝数缺失的假阳性调用 |
| KB17 | T2 | [FDA vs CPIC (March 2021 comparison PDF)](<https://cpicpgx.org/wp-content/uploads/2021/03/FDA-vs-CPIC-march-2021-c-002.pdf>) | same gene–drug association and dosing recommendation for only 5 of 126 drugs; FDA has a CDER table and a CDRH table | 同一基因-药物关联与剂量建议一致的药物仅为 126 种中的 5 种；FDA 有 CDER 与 CDRH 两张表 |
| KB18 | T2 | [CPIC SOP (2025-05-09)](<https://cpicpgx.org/wp-content/uploads/2025/07/CPIC-SOP-05.09.2025-FINAL.pdf>) | CPIC actionability grades A–D differ from PharmGKB evidence levels | CPIC 可操作性分级 A–D 不同于 PharmGKB 证据等级 |
| KB19 | T2 | [Establishing Best Practices for Clinical GWAS: Tackling Imputation and Data Quality Challenges](<https://doi.org/10.3390/ijms26136397>) | misimputation of pharmacogenetic variants is risky for narrow-therapeutic-index drugs; direct genotyping recommended | 对窄治疗窗药物，药物遗传学变异的误填补有风险；建议直接基因分型 |
<!-- source-index:KB:end -->

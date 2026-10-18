# 04 Prior-knowledge bases and pharmacogenomics / 先验知识库与药物基因组学

## 1. Scope / 范围

This document covers two kinds of prior knowledge that a variant-aware transcriptome model could use: signaling and regulatory networks that encode how drug targets connect to downstream genes, and pharmacogenomics resources that annotate which variants matter for which drugs. It records what the sources say about their content, scope and disagreements.

> 本文档涵盖变异感知转录组模型可以使用的两类先验知识：编码药物靶点如何连接到下游基因的信号网络和调控网络，以及标注哪些变异对哪些药物重要的药物基因组学资源。它记录来源对其内容、范围和分歧的说法。

## 2. Facts and evidence / 事实与证据

Signed, directed networks are available but sparse. OmniPath merges 168 resources, and its interactions domain has 1,419,006 signed, directed records from 115 resources, 22% of them from a single resource, with limited drug–target coverage [KB01]; licences must be checked resource by resource, and DrugBank is CC BY-NC 4.0 [KB02]. SIGNOR 4.0 holds 40,940 curated signed causal edges among 13,768 entities, covering 38% of the human proteome [KB04]; an earlier release left about 70% of proteins without causal links and modeled one abstract cell, so cell-type context must come from expression data [KB05]. In the Open Targets interaction network, Reactome and SIGNOR edges are signed and directional while most IntAct edges are not [KB08], and Open Targets scores 20 evidence sources into 7,282,832 target–disease associations that lack an adequate gold standard [KB07].

> 带符号、有方向的网络已有但很稀疏。OmniPath 整合了 168 个资源，其相互作用域有来自 115 个资源的 1,419,006 条带符号、有方向的记录，其中 22% 仅来自单一资源，药物-靶点覆盖有限 [KB01]；许可必须逐个资源核查，DrugBank 为 CC BY-NC 4.0 [KB02]。SIGNOR 4.0 有 13,768 个实体之间 40,940 条人工整理的带符号因果边，覆盖 38% 的人类蛋白质组 [KB04]；较早的版本中约 70% 的蛋白没有因果联系，并且只建模了一个抽象细胞，所以细胞类型背景必须来自表达数据 [KB05]。在 Open Targets 的相互作用网络中，Reactome 和 SIGNOR 的边带符号且有方向，而大多数 IntAct 的边没有 [KB08]；Open Targets 把 20 个证据来源打分合并为 7,282,832 条靶点-疾病关联，这些关联缺乏足够的金标准 [KB07]。

Prior networks can be built into models. LEMBAS sets signaling-RNN weights only on known interactions, and a GPU re-implementation is 7.1 times faster and tolerates planted false edges when L2 regularization is sufficient, shown on two macrophage ligand datasets and one synthetic set [MD13]. A mechanism-informed network linked genotype to regulators through eQTL and caQTL, but only five of 2,441 type 2 diabetes loci survived [MD12]. PROGENy footprints use 100 responsive genes for each of 11 pathways and recover driver-mutation effects, such as lower p53 scores in TP53-mutant tumors [KB10].

> 先验网络可以内置到模型中。LEMBAS 只在已知相互作用上设置信号 RNN 的权重，其 GPU 重新实现快 7.1 倍，并且在 L2 正则化足够时能容忍植入的错误边，这在两个巨噬细胞配体数据集和一个合成数据集上得到展示 [MD13]。一个机制导向网络通过 eQTL 和 caQTL 把基因型与调控因子联系起来，但 2,441 个 2 型糖尿病位点中只有五个保留下来 [MD12]。PROGENy 足迹对 11 条通路各使用 100 个响应基因，并能恢复驱动突变的效应，例如 TP53 突变肿瘤中较低的 p53 分数 [KB10]。

Transcription-factor regulons give an interpretable readout with limits. CollecTRI regulons (43,175 signed TF–gene interactions for 1,186 TFs) outperformed other TF networks at recovering TF activity changes in KnockTF perturbations (median AUROC 0.73, self-reported) [KB20], but decoupleR with CollecTRI separated perturbed from control cells only modestly in Perturb-seq data (mean AUROC 0.597) [EV39]; neither was validated on drug-induced programmes.

> 转录因子调控子提供有局限的可解释读出。CollecTRI 调控子（1,186 个 TF 的 43,175 条带符号 TF-基因相互作用）在恢复 KnockTF 扰动中的 TF 活性变化方面优于其他 TF 网络（AUROC 中位数 0.73，自报）[KB20]，但在 Perturb-seq 数据中，decoupleR 加 CollecTRI 只能适度地区分被扰动细胞与对照细胞（平均 AUROC 为 0.597）[EV39]；两者都没有在药物诱导的程序上得到验证。

Pharmacogenomic annotation is noisy. CYP2D6 lists 133 star alleles, with one or three gene copies in 12% to 23% of people by population [KB13]; novel alleles on decreased-function backbones are missed by default calling in sub-Saharan African samples [KB15]; common assays give false copy-number-loss calls when rare SNPs sit under probes [KB16]; star-allele callers reached 72% to 89% diplotype concordance on real data and 95% for a two-of-three ensemble (self-reported) [KB12]; and a splicing SNP, rs1058164, cuts full-length CYP2D6 protein by about 50% per allele while extra copies saturate [KB14].

> 药物基因组学注释存在噪声。CYP2D6 列出 133 个星等位基因，按人群不同，有 12% 至 23% 的人带有一个或三个基因拷贝 [KB13]；在撒哈拉以南非洲样本中，位于功能降低骨架上的新等位基因会被默认调用漏掉 [KB15]；常见检测在稀有 SNP 位于探针下方时会给出假的拷贝数丢失调用 [KB16]；星等位基因调用器在真实数据上的二倍型一致性为 72% 至 89%，三取二集成为 95%（自报）[KB12]；一个剪接 SNP rs1058164 使全长 CYP2D6 蛋白每个等位基因减少约 50%，而额外拷贝会饱和 [KB14]。

The pharmacogenomics resources use different categories. CPIC levels A and B carry prescribing actions and are not evidence levels [KB18]; the FDA publishes two tables, 431 CDER biomarker entries that include somatic genes and CDRH associations, against 114 CPIC actionable drugs (secondary slide deck) [KB17]. Direct genotyping is recommended for established actionable variants, and imputation is weaker for rare variants, non-European ancestry and copy-number variants [KB19].

> 药物基因组学资源使用不同的类别。CPIC 的 A 级和 B 级带有处方行动，并不是证据等级 [KB18]；FDA 发布两张表，即包含体细胞基因的 431 条 CDER 生物标志物条目和 CDRH 关联，而 CPIC 有 114 种可行动的药物（二手幻灯片）[KB17]。对已确立的可行动变异推荐直接基因分型，而填补对稀有变异、非欧洲祖源和拷贝数变异较弱 [KB19]。

## 3. Judgments / 判断

J10 (confidence: low). Directed, signed edges (SIGNOR, and Reactome through Open Targets) are the more natural masks for an action-conditioned transition operator than undirected edges [KB04, KB08]. However, in one benchmark of cancer perturbation response, STRING-based encodings were the best for genetic perturbations, so the choice should be tested rather than assumed [EV16].

> J10（置信度：低）。有方向、带符号的边（SIGNOR，以及经由 Open Targets 的 Reactome）比无方向的边更适合作为动作条件转移算子的掩码 [KB04, KB08]。不过，在一项癌症扰动响应基准中，基于 STRING 的编码对遗传扰动效果最好，所以这一选择应当检验而不是假定 [EV16]。

J14 (confidence: medium). No single pharmacogenomics resource can be treated as ground truth, because FDA, CPIC and PharmGKB use different categories rather than one evidence scale [KB17, KB18].

> J14（置信度：中）。没有哪一个药物基因组学资源可以被当作真值，因为 FDA、CPIC 和 PharmGKB 使用的是不同的类别，而不是同一个证据尺度 [KB17, KB18]。

J22 (confidence: low-medium). Transcription-factor activities derived from CollecTRI regulons are a candidate space in which to state mechanism-level objectives, for example whether a programme stays off in a mutant context, and to score them with a mechanism-fidelity measure [KB20, EV33]. This is a proposal, because the regulons were validated on TF perturbations and separated perturbed cells only modestly [EV39].

> J22（置信度：低中）。由 CollecTRI 调控子推导的转录因子活性，是陈述机制层面目标的候选空间，例如某个程序在突变背景中是否保持关闭，并可用机制保真度度量来评分 [KB20, EV33]。这是一项提议，因为这些调控子是在 TF 扰动上得到验证的，并且只能适度地区分被扰动细胞 [EV39]。

## 4. Recommended actions / 行动建议

Use OmniPath as the aggregator and SIGNOR as the signed, directed core of any prior network, and record the provenance of every edge so that edges from different resources can be ablated separately [KB01, KB04].

> 以 OmniPath 作为整合者、以 SIGNOR 作为任何先验网络中带符号、有方向的核心，并记录每条边的来源，以便不同资源的边可以分别消融 [KB01, KB04]。

Keep FDA, CPIC and PharmGKB labels as separate annotation layers and record which layer a label comes from, instead of merging them into one truth [KB17, KB18].

> 把 FDA、CPIC 和 PharmGKB 的标签作为各自独立的注释层，并记录标签来自哪一层，而不是把它们合并成一个真值 [KB17, KB18]。

Call pharmacogene alleles, including copy-number variants and star alleles, with dedicated callers rather than from array-imputed genotypes [KB12, KB16, KB19].

> 用专门的调用器而不是芯片填补的基因型来调用药物基因的等位基因，包括拷贝数变异和星等位基因 [KB12, KB16, KB19]。

Test the choice of prior network empirically, with an ablation of directed-signed against undirected edges, before building it into an architecture [EV16].

> 在把先验网络内置到架构之前，用有方向且带符号的边对无方向的边做消融，以经验方式检验先验网络的选择 [EV16]。

Add CollecTRI transcription-factor activities as an interpretable readout beside gene-level metrics and compare them with PROGENy pathway footprints, before using them to state design objectives [KB20, KB10].

> 在用来陈述设计目标之前，把 CollecTRI 转录因子活性作为可解释的读出加到基因层面指标旁边，并与 PROGENy 通路足迹比较 [KB20, KB10]。

## 5. Questions for confirmation / 待确认问题

Open decisions for this topic are kept in `data/questions.csv` and listed in `docs/10-open-questions.md`: UQ12 (whether the first prior network is restricted to the pathways of the drug classes in scope).

> 本主题的待决事项保存在 `data/questions.csv` 中，并列在 `docs/10-open-questions.md` 里：UQ12（第一版先验网络是否限制在所涉药物类别的通路上）。

## 6. Evidence gaps / 证据缺口

Reactome itself was not retrieved as a source and appears only through the Open Targets documentation [KB08]; DrugBank, DGIdb and ChEMBL were not retrieved. No source describing how OmniPath, SIGNOR, Reactome and Open Targets are combined in one pipeline was found (Q21), no annotation of non-coding regulatory variants under PharmVar was found (Q22), and no benchmark of footprint-based pathway-activity scoring on drug-induced perturbations was found (Q101). PharmGKB and CPIC were seen only through resource-level statements and comparison documents (Q08, Q38).

> Reactome 本身没有作为来源被取回，只出现在 Open Targets 文档中 [KB08]；DrugBank、DGIdb 和 ChEMBL 没有被取回。没有找到描述 OmniPath、SIGNOR、Reactome 和 Open Targets 如何合并成一条流程的来源（Q21），没有找到 PharmVar 下对非编码调控变异的注释（Q22），也没有找到基于足迹的通路活性评分在药物诱导扰动上的基准（Q101）。PharmGKB 和 CPIC 只通过资源层面的陈述和比较文档见到（Q08、Q38）。

## 7. Source index (category KB) / 来源索引（类别 KB）

Generated from `data/sources.csv`; regenerate when the CSV changes. Rows whose status is retired are omitted, and each key point is followed by its "so what" where one was written.

> 由 `data/sources.csv` 生成；CSV 变动后需重新生成。状态为 retired 的条目被省略，写有“意义”的条目在要点之后附上意义。

<!-- source-index:KB:start -->
| ID | Tier | Source | So what | 意义（中文） |
|---|---|---|---|---|
| KB01 | T1 | [OmniPath: integrated knowledgebase for multi-omics analysis](<https://www.biorxiv.org/content/10.1101/2025.09.11.675512v1.full.pdf>) | Ready-made signed, directed signaling and TF–target prior for propagating a target or pathway variant toward transcription; drug–target coverage is limited, so a separate drug-target source is needed. | 现成的带符号、有方向的信号通路与 TF–target 先验，可把靶点或通路变异向转录层面传导；药物–靶点覆盖有限，需另配药物靶点来源。 |
| KB02 | T1 | [Metadata about resources in OmniPath and pypath](<https://omnipathdb.org/info>) | Check licences resource by resource before redistributing any OmniPath-derived prior; non-commercial (DrugBank) and unlicensed resources need filtering, and curation category can tag edges for provenance ablation. | 在分享任何源自 OmniPath 的先验之前，应逐个资源核对许可；DrugBank 这类非商业资源和无许可资源需要过滤，整理类别还可用来标记边的出处以便消融。 |
| KB04 | T1 | [SIGNOR 4.0: the 2025 update with focus on phosphorylation data](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12807704/>) | Residue-level phosphosite nodes let a coding variant at a mapped site be placed in a signed graph; with only 38% proteome coverage and binary edges, expect gaps. | 残基层面的磷酸化位点节点使位于已映射位点的编码变异可以放进带符号的图中；蛋白组覆盖率仅 38%且边为二元关系，应预期存在缺口。 |
| KB05 | T1 | [SIGNOR 3.0, the SIGnaling network open resource 3.0: 2022 update](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825604/>) | Sparsity anchor for a signed-edge prior: about 70% of proteins lack causal links and the graph is context-free by default, so cell-type context must come from the expression data. | 带符号边先验的稀疏性锚点：约 70% 的蛋白缺少因果连接，且该图默认不含细胞背景，因此细胞类型背景必须来自表达数据。 |
| KB07 | T1 | [Open Targets Platform: supporting systematic drug–target identification and prioritisation](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7779013/>) | Open source of drug mechanisms and variant-to-gene links for the action prior and germline track; evidence scores are not ground truth, as the authors report no adequate gold standards. | 可作为药物机制和变异到基因连接的开放来源，用于动作先验和种系轨道；证据分数不是真值，因为作者承认缺少合适的金标准。 |
| KB08 | T1 | [Molecular interactions \| Open Targets Platform Documentation](<https://platform-docs.opentargets.org/target/molecular-interactions>) | Reactome and SIGNOR edges here are signed and directional, which suits a signed action mask; most IntAct edges are neither, and their scores can reflect study bias. | 这里 Reactome 和 SIGNOR 的边带符号且有方向，适合作为带符号的动作掩码；多数 IntAct 的边两者皆无，其分数还可能反映研究偏倚。 |
| KB09 | T2 | [Large-scale regulatory and signaling network assembly through linked open data](<https://academic.oup.com/database/article/doi/10.1093/database/baaa113/6103765>) | Precedent for automating prior-network assembly from linked open data; the abstract names the difficulty of recovering logical flows but not which sources or edge semantics are used. | 自动从关联开放数据组装先验网络的先例；摘要提到恢复逻辑流的困难，但没有说明使用哪些来源或边的语义。 |
| KB10 | T1 | [Perturbation-response genes reveal signaling footprints in cancer gene expression](<https://www.nature.com/articles/s41467-017-02391-6>) | Candidate low-dimensional readout for scoring variant-driven pathway shifts: footprint genes barely overlap the pathway's own signaling genes, so the variant gene's expression is a poor proxy. | 可作为低维读出来评分变异驱动的通路变化：足迹基因与该通路自身的信号基因几乎不重叠，因此变异基因自身的表达是较差的替代指标。 |
| KB12 | T1 | [A systematic comparison of pharmacogene star allele calling bioinformatics algorithms: a focus on CYP2D6 genotyping](<https://www.nature.com/articles/s41525-020-0135-2>) | Upstream genotype calls are noisy for structural variants and differ by caller and by benchmark; a genotype-aware model should carry call uncertainty or use a consensus call. | 上游基因型调用在结构变异上噪声较大，且随调用工具和基准而异；感知基因型的模型应携带调用的不确定性，或使用共识调用。 |
| KB13 | T1 | [A Review of the Important Role of CYP2D6 in Pharmacogenomics](<https://www.mdpi.com/2073-4425/11/11/1295>) | Encode PK genotype as activity score plus copy number, treat co-medication as a separate input, and avoid inferring germline PK genotype from tumor-derived sequence. | 把药代动力学基因型编码为活性评分加拷贝数，把合并用药作为单独输入，并避免从源自肿瘤的序列推断种系药代基因型。 |
| KB14 | T1 | [A frequent CYP2D6 variant promotes skipping of exon 3 and reduces CYP2D6 protein expression in human liver samples](<https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1186540/epub>) | Splicing and enhancer SNPs in a PK gene reshape expression beyond star-allele scores, and extra copies saturate, so genotype encodings should not assume linear dosage. | 药代基因中的剪接和增强子 SNP 在星等位基因评分之外还会改变表达，额外的拷贝会饱和，因此基因型编码不应假定线性剂量。 |
| KB15 | T1 | [Characterization of Novel CYP2D6 Alleles across Sub-Saharan African Populations](<https://www.mdpi.com/2075-4426/12/10/1575>) | Rare alleles on decreased-function backbones can be missed by standard panels, and in-silico predictors underperform on pharmacogenetic variants, so genotype encodings should carry allele uncertainty, especially in under-represented ancestries. | 位于功能降低骨架上的罕见等位基因可能被标准检测板漏掉，且计算机预测工具在药物遗传学变异上表现不佳，因此基因型编码应携带等位基因的不确定性，尤其是在代表性不足的祖源中。 |
| KB16 | T2 | [Identification of CYP2D6 Haplotypes that Interfere with Commonly Used Assays for Copy Number Variation Characterization](<https://www.sciencedirect.com/science/article/pii/S1525157821000416>) | Probe-based assays can give false copy-number-loss calls when rare SNPs sit under probe sites, here nearly all in people of African descent; treat copy number as an uncertain input. | 当罕见 SNP 位于探针位点之下时，基于探针的检测可能给出假的拷贝数缺失调用，本研究中几乎都发生在非洲裔人群；应把拷贝数视为不确定的输入。 |
| KB17 | T3 | [FDA vs CPIC (March 2021 comparison PDF)](<https://cpicpgx.org/wp-content/uploads/2021/03/FDA-vs-CPIC-march-2021-c-002.pdf>) | Treat FDA, CPIC and PharmGKB labels as separate annotation layers with different meanings; scale anchors are 114 CPIC actionable drugs and 431 FDA biomarker entries. | 把 FDA、CPIC 和 PharmGKB 的标签视为含义各异的独立注释层；规模锚点为 114 个 CPIC 可操作药物和 431 条 FDA 生物标志物条目。 |
| KB18 | T1 | [Clinical Practice Guideline Standard Operating Procedure](<https://cpicpgx.org/wp-content/uploads/2025/07/CPIC-SOP-05.09.2025-FINAL.pdf>) | Use level A and B pairs as the actionable subset and diplotype-to-phenotype groups as conditioning labels; the cross-population assumption is a default to test by ancestry, not a finding. | 把 A 和 B 级配对用作可操作子集，把双倍型到表型的分组用作条件标签；跨人群假设只是需按祖源检验的默认设定，而不是发现。 |
| KB19 | T1 | [Establishing Best Practices for Clinical GWAS: Tackling Imputation and Data Quality Challenges](<https://doi.org/10.3390/ijms26136397>) | Take germline PK genotypes from direct genotyping or sequencing, not imputation; if imputed, carry INFO quality, and expect weak copy-number and non-European calls. | 种系药代基因型应来自直接基因分型或测序而非填补；若为填补，应携带 INFO 质量，并预期拷贝数和非欧洲人群的调用较弱。 |
| KB20 | T1 | [Expanding the coverage of regulons from high-confidence prior knowledge for accurate estimation of transcription factor activities](<https://academic.oup.com/nar/article/51/20/10934/7318114>) | Signed TF regulons give an interpretable readout, validated on TF knockdown and knockout data, not drug-induced programmes; check it per TF, since perturbed-only comparisons were comparable across networks. | 带符号的 TF 调控子提供可解释的读出，验证基于 TF 敲低和敲除数据，而非药物诱导的程序；应逐个 TF 检验，因为仅看被扰动 TF 时各网络表现相当。 |
<!-- source-index:KB:end -->

# Search log / 检索日志

## 1. Scope / 范围

This log records every query, tool attempt and outcome behind the repository, including failures, so that every claim of absence can be traced to a query ID. It also lists the topics that returned nothing, the failures, the status of the load-bearing claims, the leads for later rounds and the screening decisions.

> 本日志记录仓库背后的每次查询、工具尝试和结果，包括失败，使每一条“未找到”的陈述都能追溯到查询 ID。它还列出没有返回结果的主题、失败、承重主张的状态、后续轮次的线索和筛选决定。

## 2. Legend and totals / 图例与总数

Mode E is the extended web search and mode S the standard one; "EMPTY" means that the topic returned no relevant hits. Q01 to Q44 hold 39 completed searches (34 extended, 5 standard), 2 searches that the user interrupted and that were re-run in modified form, and 3 attempts that failed or were blocked. Q45 to Q132 hold 78 searches (71 extended, 7 standard), 46 page fetches grouped as Q119 to Q124 and Q130 to Q132 (35 succeeded, 11 failed) and one note on unavailable tools (Q125); Q126 to Q132 are verification checks. Q133 to Q143 are the third round, an audit that ran no web searches: 11 scripted retrievals, connector calls and checks, of which 10 completed and 1 failed (Q138). Query texts are verbatim and outcomes are the curator's summary of what came back.

> 模式 E 是扩展网络检索，模式 S 是标准检索；“EMPTY”表示该主题没有返回相关命中。Q01 至 Q44 包含 39 次已完成的检索（34 次扩展、5 次标准）、2 次被用户中断并以改写形式重跑的检索，以及 3 次失败或被拦截的尝试。Q45 至 Q132 包含 78 次检索（71 次扩展、7 次标准）、按 Q119 至 Q124 和 Q130 至 Q132 分组的 46 次页面抓取（35 次成功、11 次失败）以及一条关于不可用工具的说明（Q125）；Q126 至 Q132 是核验检查。Q133 至 Q143 是第三轮，是没有进行网络检索的稽查：11 个脚本抓取、连接器调用和检查，其中 10 个完成、1 个失败（Q138）。查询文本为原文，结果是整理者对返回内容的概括。

## 3. Log / 日志

<!-- search-table:start -->
| ID | Mode | Query or attempt | Outcome | 结果（中文） |
|---|---|---|---|---|
| Q01 | E | genetic variation drug target affects drug-induced transcriptional response response-eQTL | ok | 正常 |
| Q02 | E | world model architecture virtual cell transcriptome perturbation prediction 2025 2026 | ok | 正常 |
| Q03 | E | Arc Institute Virtual Cell Challenge 2025 results STATE model Tahoe-100M | ok; STATE ranking and Tahoe results in the challenge not found | 正常；挑战赛中 STATE 排名和 Tahoe 结果未找到 |
| Q04 | E | single-cell eQTL context-specific dynamic eQTL drug stimulation sc-eQTLGen consortium | drug-stimulation-specific results EMPTY | 药物刺激特异的结果为空 |
| Q05 | E | Perturb-seq base editing variant-to-function transcriptomic readout coding variants screen | ok | 正常 |
| Q06 | E | AlphaGenome Enformer Borzoi regulatory variant effect prediction personal genome expression | ok; whole-expression application to a personal genome not found | 正常；未找到对个人基因组整体表达的应用 |
| Q07 | E | chemCPA CPA GEARS scGPT drug perturbation prediction deep learning linear baseline critique benchmark | ok; chemCPA-specific critique thin | 正常；针对 chemCPA 的批评较少 |
| Q08 | E | Mendelian randomization genetically proxied drug target validation pharmacogenomics PharmGKB CPIC drug target variant database | MR ok; PharmGKB / CPIC EMPTY (filled by Q38) | MR 部分正常；PharmGKB / CPIC 为空（由 Q38 补上） |
| Q09 | S | world model latent dynamics Dreamer JEPA action-conditioned prediction architecture survey | ok | 正常 |
| Q10 | E | biologically informed neural network signaling pathway CellBox LEMBAS visible neural network P-NET mechanistic hybrid model | CellBox EMPTY | CellBox 为空 |
| Q11 | E | Tahoe-100M sci-Plex drug perturbation single-cell atlas cell line genotype context dependence LINCS L1000 | direct Tahoe versus LINCS comparison EMPTY | Tahoe 与 LINCS 的直接比较为空 |
| Q12 | E | genotype-aware perturbation response prediction model donor iPSC panel drug response variation transcriptome | EMPTY; nearest hits pertTF and P³ | 为空；最接近的命中是 pertTF 和 P³ |
| Q13 | E | resistance mutation EGFR BRAF kinase inhibitor transcriptional reprogramming adaptive signaling rewiring signature | ok | 正常 |
| Q14 | — | WebFetch of the arXiv abstract page for VCWorld | FAILED: DNS ENOTFOUND | 失败：DNS 解析失败（ENOTFOUND） |
| Q15 | — | Bash: query agent-proxy status with curl | BLOCKED by the permission classifier; not retried | 被权限分类器拦截；未重试 |
| Q16 | — | WebFetch of the Arc VCC 2025 wrap-up page | FAILED: DNS ENOTFOUND | 失败：DNS 解析失败（ENOTFOUND） |
| Q17 | E | gene-environment interaction eQTL treatment response glucocorticoid statin genotype by treatment interaction transcriptome | statin EMPTY | 他汀为空 |
| Q18 | E | Virtual Cell Challenge 2026 zero-shot generalization cellular contexts Cell paper benchmark design | ok | 正常 |
| Q19 | E | causal representation learning perturbation identifiability counterfactual single-cell interventions theory | counterfactual queries partly EMPTY | 反事实查询部分为空 |
| Q20 | E | DepMap GDSC PRISM cell line mutation drug sensitivity prediction transcriptome machine learning benchmark | ok | 正常 |
| Q21 | E | Open Targets OmniPath SIGNOR Reactome signaling network prior knowledge drug target pathway resource integration | joint pipeline of the four EMPTY | 四者联合管线为空 |
| Q22 | E | pharmacogenomic variants noncoding regulatory CYP2D6 star allele expression drug metabolism PharmVar annotation | noncoding regulatory annotation EMPTY | 非编码调控注释为空 |
| Q23 | E | "AI virtual cell" position paper Bunne Cell 2024 how to build virtual cell with AI roadmap universal representation | ok | 正常 |
| Q24 | E | transcriptome-wide association study drug response TWAS pharmacogenomics imputed expression clinical outcome | ok | 正常 |
| Q25 | E | CellFlow optimal transport flow matching cell state perturbation model single-cell trajectory | ok | 正常 |
| Q26 | E | mutation-conditioned genotype encoding perturbation response prediction cancer cell line encodings benchmark 2026 | ok | 正常 |
| Q27 | E | in silico perturbation variant aware foundation model drug target mutation predict expression change genotype conditioning | interrupted by the user; re-run in modified form as Q31 | 被用户中断；以改写形式作为 Q31 重跑 |
| Q28 | E | scPerturBench PerturBench evaluation metrics perturbation prediction pitfalls distribution shift E-distance | interrupted by the user; re-run in modified form as Q32 | 被用户中断；以改写形式作为 Q32 重跑 |
| Q29 | E | personal gene expression prediction from DNA sequence deep learning fails individual variation Enformer Basenji2 Sasse Huang Nature Genetics 2023 | ok; the author attribution in the query (Sasse, Huang) was not confirmed by the results | 正常；查询中的作者归属（Sasse、Huang）未被结果确认 |
| Q30 | E | response QTL drug exposure iPSC cardiomyocytes doxorubicin anthracycline statin lymphoblastoid cell lines gene expression response genotype | statin and lymphoblastoid-line hits EMPTY | 他汀与淋巴母细胞系的命中为空 |
| Q31 | E | genotype-conditioned single-cell foundation model variant effect cell-type-specific expression donor genotype input | EMPTY; nearest hit PertAdapt | 为空；最接近的命中是 PertAdapt |
| Q32 | S | PerturBench benchmark perturbation prediction evaluation metrics rank metrics mean baseline pitfalls | ok | 正常 |
| Q33 | E | Perturb-seq across genetically diverse donors iPSC lines genetic background modifies perturbation effect variant by perturbation interaction | human data EMPTY; yeast only | 人类数据为空；仅有酵母 |
| Q34 | E | predicting mutation effect on drug binding affinity resistance deep learning AlphaFold3 Boltz-2 protein-ligand variant | AF3 versus Boltz-2 head-to-head on resistance mutations EMPTY | AF3 与 Boltz-2 在耐药突变上的直接对比为空 |
| Q35 | S | LINCS L1000 connectivity map dataset size cell lines perturbagens Subramanian 2017 CMap | ok; exact cell-line count of the 2017 release not found | 正常；2017 年版本的确切细胞系数未找到 |
| Q36 | E | JEPA joint embedding predictive architecture single-cell gene expression perturbation latent prediction | ok | 正常 |
| Q37 | E | dynamic eQTL iPSC differentiation single-cell genetic effects change along trajectory Cuomo Jerber Strober | ok; involvement of Jerber and Strober (named in the query) not confirmed by the results | 正常；查询中提到的 Jerber 和 Strober 的参与未被结果确认 |
| Q38 | S | PharmGKB CPIC guidelines gene-drug pairs clinical annotations FDA table of pharmacogenomic biomarkers drug labeling | ok | 正常 |
| Q39 | S | AlphaMissense ESM1b EVE missense variant effect prediction benchmark deep mutational scanning ClinVar | EVE comparison EMPTY | 与 EVE 的比较为空 |
| Q40 | E | Arc Institute State model state transition embedding architecture perturbation prediction unseen cell contexts | ok | 正常 |
| Q41 | E | world model for biology perspective definition action-conditioned latent dynamics cell state counterfactual virtual cell versus conditional generative model | ok | 正常 |
| Q42 | E | ancestry bias eQTL reference panels European gene expression prediction portability diverse populations pharmacogenomics | pharmacogenomics angle EMPTY | 药物基因组学角度为空 |
| Q43 | E | drug-induced transcriptional response depends on mutation status BRAF KRAS TP53 cell lines pharmacotranscriptomics genotype-specific response | joint BRAF / KRAS / TP53 stratified study EMPTY | 联合 BRAF / KRAS / TP53 分层的研究为空 |
| Q44 | E | PRnet TranSiGen scGen predict transcriptional response unseen compounds L1000 generative model chemical structure | ok | 正常 |
| Q45 | E | LabCompass Fabian Theis | ok; the preprint, an X post and LinkedIn profile pages | 正常；预印本、一条 X 帖子和 LinkedIn 主页 |
| Q46 | E | LabCompass lab-in-the-loop perturbation experiment design virtual cell Theis Helmholtz Munich | ok; preprint abstract text and LinkedIn profile pages | 正常；预印本摘要文字和 LinkedIn 主页 |
| Q47 | E | Theis lab world model cell perturbation 2026 preprint | EMPTY for a Theis-lab world-model preprint; hits were other groups' work (AlphaCell, Chreode, Diversity by Design) | 未找到 Theis 实验室的世界模型预印本；命中的是其他团队的工作（AlphaCell、Chreode、Diversity by Design） |
| Q48 | E | Generative inverse design steers human hematopoietic cell fate in vitro flow matching forward surrogate experimental design | ok; the preprint and a newsletter summary | 正常；预印本和一份通讯摘要 |
| Q49 | E | LabCompass 78 million cells spectral flow cytometry CD34+ cytokines small molecules four lab-in-the-loop rounds | ok; the GitHub reproducibility repository and the 78-million-cell figure | 正常；GitHub 可复现仓库及 7,800 万细胞的数字 |
| Q50 | E | LabCompass viral infection single-cell transcriptomic inverse design not tied to a particular virtual cell model | ok; one LinkedIn post (author attribution unverified) mentions viral-infection transcriptomics, no details | 正常；一则 LinkedIn 帖子（作者归属未核实）提到病毒感染转录组，没有细节 |
| Q51 | E | theislab Hugging Face LabCompass dataset repository inverse design | ok; dataset listed on the Hugging Face organization page, dataset card not readable | 正常；数据集列在 Hugging Face 组织页面上，数据集卡片读不到 |
| Q52 | E | Fabian Theis cellular world models decide what experiment to do next generative inverse design LinkedIn X post | ok; the X post excerpt; no LinkedIn post in these results | 正常；X 帖子摘录；这些结果中没有 LinkedIn 帖子 |
| Q53 | E | Large Perturbation Model LPM in silico biological discovery perturbation readout context disentangled architecture | ok | 正常 |
| Q54 | E | TxPert transcriptional response prediction biological knowledge graphs unseen perturbations experimental reproducibility benchmark | ok; a later work's claim of a higher score under Systema noted | 正常；记下了后续工作在 Systema 下得分更高的说法 |
| Q55 | E | inverse design of perturbations to reach a target cell state generative model guidance single-cell reprogramming | ok; U-Pert, PerturbGen, MolGene-E and a PNAS reprogramming-design paper | 正常；U-Pert、PerturbGen、MolGene-E 以及一篇 PNAS 细胞重编程设计论文 |
| Q56 | E | active learning Bayesian optimal experimental design Perturb-seq perturbation selection virtual cell lab-in-the-loop | ok; IterPert found; no closed-loop virtual-cell system found | 正常；找到 IterPert；没有找到闭环虚拟细胞系统 |
| Q57 | E | chemical-genetic Perturb-seq CRISPR knockout combined with drug treatment single-cell gene-drug interaction transcriptional response | thin; PerturbNet and multiome Perturb-seq hits, no single-cell gene-by-drug study among the links shown | 较少；PerturbNet 和多组学 Perturb-seq，所示链接中没有单细胞基因×药物研究 |
| Q58 | E | Parse Biosciences 10 million PBMC cytokine perturbation 12 donors donor-specific response single-cell atlas | ok; dataset page, poster, Stack, PULSAR | 正常；数据集页面、海报、Stack、PULSAR |
| Q59 | E | Open Problems single-cell perturbation prediction PBMC donors 144 compounds dataset cell type donor generalization | ok; GSE279945 (OP3) and benchmark pages | 正常；GSE279945（OP3）和基准页面 |
| Q60 | E | pooled iPSC lines village in a dish drug exposure single-cell RNA-seq genetic variation response heterogeneity donors | ok; village-in-a-dish papers; no drug-exposure village study found | 正常；村落类论文；没有找到药物暴露的村落研究 |
| Q61 | E | isogenic cell lines oncogenic mutations panel drug response transcriptional signature mutation-specific signaling rewiring RNA-seq | ok; MIX-Seq and a chemical–genetic interaction map | 正常；MIX-Seq 和化学–遗传相互作用图谱 |
| Q62 | E | drug target resistance mutation changes transcriptional response to inhibitor EGFR C797S BCR-ABL T315I RNA-seq signature bypass pathway | EMPTY for transcriptional-response comparisons between target-mutant and wild-type cells; hits were resistance-mechanism papers | 目标突变与野生型细胞之间转录响应比较为空；命中的是耐药机制论文 |
| Q63 | E | Systema evaluation framework systematic variation genetic perturbation response prediction beyond baseline shift | ok | 正常 |
| Q64 | E | scPerturb harmonized single-cell perturbation data E-distance Peidli Nature Methods | ok | 正常 |
| Q65 | E | sci-Plex massively multiplex chemical transcriptomics single-cell Srivatsan dose response 188 compounds | ok | 正常 |
| Q66 | E | dose-response aware single-cell perturbation model continuous dose conditioning transcriptional response prediction | ok; no dedicated continuous-dose model beyond CPA-style covariates and a 2023 Patterns paper | 正常；除 CPA 式协变量和一篇 2023 年 Patterns 论文外，没有专门的连续剂量模型 |
| Q67 | E | drug combination single-cell transcriptomic response prediction combinatorial perturbation dataset synergy transcriptome model | ok; scDFM and several single-cell drug-response predictors; no new dataset | 正常；scDFM 和若干单细胞药物响应预测器；没有新数据集 |
| Q68 | E | Eduati logic models signaling cancer cell lines mutation-specific parameters drug combinations prior knowledge network | ok; 2017, 2020 and later logic-model papers; no exact mutation-specific match | 正常；2017 年、2020 年及后续的逻辑模型论文；没有完全匹配的突变特异论文 |
| Q69 | E | Stack in-context learning single-cell biology foundation model unseen donors cytokines | ok; no detailed unseen-donor numbers in the results | 正常；结果中没有详细的未见供体数字 |
| Q70 | E | PerturbGen perturbations reshape cellular trajectories generative foundation model time dynamics | ok | 正常 |
| Q71 | E | X-Cell Xaira scaling causal perturbation prediction X-Atlas Orion genome-wide Perturb-seq million cells | ok; X-Cell evidence rests on company announcements | 正常；X-Cell 的证据来自公司公告 |
| Q72 | E | GEARS Roohani predicting transcriptional outcomes of novel multigene perturbations gene ontology knowledge graph Nature Biotechnology | ok | 正常 |
| Q73 | E | compositional perturbation autoencoder CPA Lotfollahi predicting cellular responses to complex perturbations covariates dose combinations Molecular Systems Biology 2023 | ok | 正常 |
| Q74 | E | Replogle genome-scale Perturb-seq K562 RPE1 mapping information-rich genotype-phenotype landscapes | ok | 正常 |
| Q75 | E | Unbalanced Perturbation Dynamics For Cell Fate Design U-Pert unbalanced optimal transport cell number changes inverse design | ok; no independent evaluation found | 正常；未找到独立评估 |
| Q76 | E | genetic background aware perturbation response prediction donor genotype covariate single-cell deep learning inherited variants modulate response | EMPTY for donor-genotype covariates; nearest hits PerturbNet, scLAMBDA, PertAdapt, scRGP | 供体基因型协变量为空；最接近的命中是 PerturbNet、scLAMBDA、PertAdapt、scRGP |
| Q77 | E | Tahoe-x1 Tahoe Therapeutics single-cell foundation model billion parameters perturbation context 2026 | ok; no 2026-specific update found | 正常；未找到 2026 年的更新 |
| Q78 | E | Diversity by Design mode collapse scRNA-seq perturbation modeling well-calibrated metrics | ok; abstract and secondary-citation level | 正常；摘要和二手引用层面 |
| Q79 | E | Mechanisms Matter: Transportability of Cellular Perturbation Effects bioRxiv 2026 | ok; abstract and third-party summary | 正常；摘要和第三方摘要 |
| Q80 | E | Evaluating Single-Cell Perturbation Response Models Is Far from Straightforward bioRxiv 2026 | ok; related evaluation papers listed | 正常；列出了相关的评测论文 |
| Q81 | E | PerturbNet missense mutations amino acid sequence embedding predicted cell state distribution TP53 KRAS variants Perturb-seq Yu Welch | ok; the authors named in the query (Yu, Welch) not confirmed by the results | 正常；查询中提到的作者（Yu、Welch）未被结果确认 |
| Q82 | E | Modelling drug-induced cellular perturbation responses with a biologically informed dual-branch transformer Nature Machine Intelligence | ok; XPert found, with a follow-up (MAP) | 正常；找到 XPert 及其后续工作（MAP） |
| Q83 | E | Predicting and interpreting cell-type-specific drug responses in the small-data regime using inductive priors Nature Machine Intelligence | ok; PrePR-CT found | 正常；找到 PrePR-CT |
| Q84 | E | scooby modeling multi-modal genomic profiles from DNA sequence at single-cell resolution Borzoi Gagneur Theis variant effect cell-type specific | ok; variant-effect scoring mentioned in the abstract only | 正常；变异效应打分只在摘要中提到 |
| Q85 | E | mechanism-annotated benchmark limited fidelity drug-response signatures single-cell perturbation models | ok | 正常 |
| Q86 | E | PerturbRx treatment-conditioned latent transitions patient drug response prediction | ok | 正常 |
| Q87 | E | time-resolved single-cell RNA-seq metabolic labeling drug perturbation transcriptional kinetics new RNA scNT-seq sci-FATE dataset | ok for scNT-seq and Well-TEMP-seq; sci-FATE paper or dataset EMPTY | scNT-seq 与 Well-TEMP-seq 正常；sci-FATE 论文或数据集为空 |
| Q88 | E | CellBox interpretable machine learning perturbation biology neural ordinary differential equation Sorger cell response | ok; a link between CellBox and Sorger not found (the name appears only in a citation) | 正常；未找到 CellBox 与 Sorger 的关联（该名字只出现在一条参考文献中） |
| Q89 | E | CausalBench large-scale benchmark network inference single-cell perturbation data GSK | ok | 正常 |
| Q90 | E | model-based reinforcement learning cell state control reprogramming latent dynamics world model planning single-cell | ok; DiRL found; no latent-planning benchmark for reprogramming found | 正常；找到 DiRL；没有找到针对重编程的潜空间规划基准 |
| Q91 | E | temporal perturbation single-cell time course CRISPR perturbation dynamics model predict trajectories under intervention neural SDE | ok; scDiffEq, PRESCIENT, ARTEMIS, Chreode | 正常；scDiffEq、PRESCIENT、ARTEMIS、Chreode |
| Q92 | E | deep mutational scanning drug target variants resistance map kinase inhibitor ABL1 imatinib saturation mutagenesis drug sensitivity | ok; BCR-ABL1 saturation, base-editing and combined computational–experimental studies | 正常；BCR-ABL1 饱和突变、碱基编辑以及计算与实验结合的研究 |
| Q93 | E | massively parallel reporter assay regulatory variants under drug or hormone stimulation context-dependent allelic effects glucocorticoid treatment | thin; one drug-response MPRA (caffeine); glucocorticoid MPRA EMPTY | 较少；只有一项药物响应 MPRA（咖啡因）；糖皮质激素 MPRA 为空 |
| Q94 | E | Randolph genetic ancestry effects on response to viral infection pervasive cell type specific single-cell PBMC influenza | ok | 正常 |
| Q95 | E | rare cell variability and drug-induced reprogramming mode of cancer drug resistance Shaffer pre-existing transcriptional states predict resistance | ok | 正常 |
| Q96 | E | lineage barcoding drug tolerance pre-existing states transitions non-genetic determinants of clonal fitness single-cell Goyal Fennell | ok; mostly reviews of drug-tolerant persisters | 正常；多数是耐药持留细胞的综述 |
| Q97 | E | machine learning closed-loop optimization of directed differentiation protocol cytokines Bayesian optimization stem cell fate active learning | thin; no transcriptomic closed-loop differentiation-protocol system found, held items only | 较少；没有找到转录组层面的闭环分化方案优化系统，只有搁置条目 |
| Q98 | E | Drug Response Prediction Provides a Biologically Relevant Benchmark for Perturbation Response Models | ok; abstract and figure-legend level | 正常；摘要和图注层面 |
| Q99 | E | Morris discovery of target genes and pathways at GWAS loci by pooled single-cell CRISPR screens Science 2023 | ok; locus counts differ between versions (124 cis targets of 91 loci versus 134 elements) | 正常；各版本的位点数不同（91 个位点的 124 个 cis 靶基因，对比 134 个元件） |
| Q100 | E | DrugCell visible neural network interpretable deep learning drug response cancer cell line mutations Gene Ontology hierarchy Kuenzi Cancer Cell 2020 | ok; Gene Ontology not confirmed in the results | 正常；结果中未确认基因本体 |
| Q101 | E | decoupleR CollecTRI transcription factor activity inference benchmark perturbation experiments footprint pathway activity | ok; no footprint-based pathway-activity benchmark found | 正常；没有找到基于足迹法的通路活性基准 |
| Q102 | E | Alessandro Palma Theis flow matching experimental design generative model protocol optimization single-cell inverse problem | ok; CellFlow and CFGen; no other flow-matching protocol-optimization paper surfaced (weak evidence) | 正常；CellFlow 和 CFGen；没有出现其他流匹配方案优化论文（弱证据） |
| Q103 | S | DCell deep learning hierarchical structure and function of a cell Ma Nature Methods 2018 genotype to phenotype | ok; abstract only | 正常；仅摘要 |
| Q104 | E | Goettgens lab spectral flow cytometry hematopoietic CD34+ cytokine screen Theis generative design collaboration preprint authors | EMPTY for the preprint through this query; the collaboration is stated in the repository description found by Q49 and Q51 | 此查询未找到该预印本；合作关系见 Q49 和 Q51 找到的仓库描述 |
| Q105 | E | Disease-associated loci share properties with response eQTLs under common environmental exposures ethanol caffeine nicotine | ok; the number of individuals differs across sources (51 versus 53) | 正常；各来源的个体数不同（51 对 53） |
| Q106 | E | What Makes a Representation Good for Single-Cell Perturbation Prediction? arXiv 2605.19343 findings | ok | 正常 |
| Q107 | E | Allele-specific expression reveals interactions between genetic variation and environment cis-regulatory GxE treatment ASE method | ok; EAGLE identified | 正常；找到 EAGLE |
| Q108 | E | Frohlich efficient parameter estimation enables prediction of drug response using a mechanistic pan-cancer pathway model Cell Systems | ok | 正常 |
| Q109 | E | training-free guidance flow matching differentiating through the flow controlled generation D-Flow diffusion posterior sampling Diffuser planning with diffusion | ok; OC-Flow and general guidance papers; no D-Flow link returned (fixed by Q118) | 正常；OC-Flow 和一般性的引导论文；未返回 D-Flow 链接（由 Q118 补上） |
| Q110 | E | V-JEPA 2 action-conditioned latent world model planning model predictive control zero-shot robot | ok; the primary arXiv number named, only secondary descriptions seen | 正常；给出了原始 arXiv 编号，只见到二手描述 |
| Q111 | E | donor-specific perturbation effects prediction unseen donors cytokine response single-cell model donor heterogeneity generalization | ok; CellFlow tutorial, PULSAR, Stack and benchmark papers | 正常；CellFlow 教程、PULSAR、Stack 和基准论文 |
| Q112 | E | "inverse modeling framework" optimizes experimental designs toward candidates expected to produce specified target cell states flow-matching forward surrogate hematopoietic | ok; the preprint abstract again, plus unrelated engineering papers | 正常；再次找到预印本摘要，另有无关的工程论文 |
| Q113 | E | Benchmarking virtual cell models for in-the-wild perturbation response arXiv 2604.27646 unseen contexts unseen perturbations unseen patients | ok; the unseen-patient scenario is not confirmed in the abstract | 正常；摘要中未确认“未见患者”场景 |
| Q114 | E | PULSAR foundation model multi-scale multi-cellular biology donor embedding cytokine perturbed embedding unseen donors | ok; unseen-donor perturbation results not shown | 正常；未显示未见供体的扰动结果 |
| Q115 | S | Combination treatment optimization using a pan-cancer pathway model Frohlich PLOS Computational Biology 2021 mutation-specific | ok; mutation-specific optimization not mentioned | 正常；未提到针对突变的优化 |
| Q116 | E | single-cell CRISPR screen under drug treatment gene-by-drug interaction transcriptional readout knockout modifies drug response Perturb-seq with compound | EMPTY for single-cell gene-by-drug Perturb-seq; nearest hit is a pooled-growth CRISPR-drug map | 单细胞基因×药物 Perturb-seq 为空；最接近的是混池生长读出的 CRISPR–药物图谱 |
| Q117 | E | CFTR variant patient-derived organoids forskolin-induced swelling predicts clinical response to CFTR modulators ivacaftor variant-specific drug response | ok; supportive and mixed evidence for organoid swelling | 正常；类器官肿胀的支持性与混合证据 |
| Q118 | S | D-Flow: Differentiating through Flows for Controlled Generation Ben-Hamu | ok; arXiv and PMLR links (run while finalizing this plan) | 正常；arXiv 和 PMLR 链接（在定稿本计划时运行） |
| Q119 | — | WebFetch of 19 GitHub pages and raw files of theislab/LabCompass and theislab/LabCompass-reproducibility (repository, directory and README pages, source files, LICENSE, pyproject.toml) | all 19 ok | 全部 19 次正常 |
| Q120 | — | WebFetch of the github.com/theislab organization page and an api.github.com repository search for labcompass | ok; the organization page lists only 10 of 276 repositories, the search returned 12 repositories | 正常；组织页面只列出 276 个仓库中的 10 个，搜索返回 12 个仓库 |
| Q121 | — | WebFetch of the PyPI JSON record for cellflow-tools | ok | 正常 |
| Q122 | — | WebFetch of nine GitHub repository pages (ArcInstitute/state, theislab/cellflow, theislab/CPA, Lotfollahi-lab/Perturbgen, ArcInstitute/stack, Genentech/iterative-perturb-seq, gagneurlab/scooby, bm2-lab/scPerturBench, theislab/ReconEval) | all 9 ok | 全部 9 次正常 |
| Q123 | — | WebFetch of seven hosts (www.biorxiv.org, huggingface.co, behindthebioinformatics.substack.com, europepmc.org, pubmed.ncbi.nlm.nih.gov, zenodo.org, openreview.net), one page each | FAILED: DNS ENOTFOUND, 7 of 7 | 失败：DNS 解析失败（ENOTFOUND），7 次全部失败 |
| Q124 | — | WebFetch of the GitHub tree API for the two LabCompass repositories | FAILED: HTTP 403, 2 of 2; worked around with HTML directory pages (Q119) | 失败：HTTP 403，2 次全部失败；改用 HTML 目录页面绕过（Q119） |
| Q125 | — | MCP servers biorender, biorxiv, c-trials, chembl, consensus, ot, owkin, pubmed, synapse and wiley of the bio-research plugin | not callable: the harness reported failed connections (proxy refused the tunnel with 403); no call was attempted | 不可调用：运行环境报告连接失败（代理以 403 拒绝建立隧道）；未尝试调用 |
| Q126 | S | response eQTL nicotine caffeine ethanol 51 individuals single-cell RNA-seq 1.4 million cells response eQTLs per cell type eGenes | ok; the 51 individuals and about 1.4 million cells were confirmed, but the response-eQTL counts per cell type and the eGene counts were not returned | 正常；51 名个体和约 1.4 million（140 万）个细胞得到确认，但每种细胞类型的响应 eQTL 计数和 eGene 计数没有返回 |
| Q127 | S | Disease-associated loci share properties with response eQTLs under common environmental exposures 31 to 110 response eQTLs per cell type 380 336 276 eGenes ethanol caffeine nicotine | ok; the same paper, two PMC versions and a 2025 bioRxiv preprint with the same title were found; the counts 31 to 110 and 380, 336 and 276 were not returned again | 正常；找到同一篇论文、其两个 PMC 版本以及标题相同的 2025 年 bioRxiv 预印本；31 至 110 以及 380、336 和 276 这些计数再次没有返回 |
| Q128 | S | caffeine response regulatory variants vascular endothelial cells massively parallel reporter assay 665 allelic effects 6 variants altered response to caffeine | ok; 665 variants with allelic effects and 6 caffeine-response (GxE) variants at a false discovery rate below 5% were confirmed for the published eLife version (2024); the first eLife version and the bioRxiv preprint report 29 GxE variants at a false discovery rate below 10% | 正常；已发表的 eLife 版本（2024 年）确认了 665 个有等位基因效应的变异，以及在 FDR 低于 5% 时的 6 个咖啡因响应（GxE）变异；eLife 第一版和 bioRxiv 预印本报告在 FDR 低于 10% 时有 29 个 GxE 变异 |
| Q129 | S | Systema framework evaluating genetic perturbation response prediction beyond systematic variation perturbed centroid reference average treatment effect baseline Nature Biotechnology | ok; the Nature Biotechnology 2025 publication, ten datasets and the finding that simple baselines score comparably were confirmed; the perturbed-centroid reference and the average-treatment-effect baseline were not returned | 正常；确认了 2025 年 Nature Biotechnology 的发表、十个数据集，以及简单基线得分相当的发现；扰动后质心参照和平均处理效应基线没有返回 |
| Q130 | — | WebFetch of the PMC page of the response-eQTL paper (www.ncbi.nlm.nih.gov) | FAILED: DNS ENOTFOUND | 失败：DNS 解析失败（ENOTFOUND） |
| Q131 | — | WebFetch of the github.com/mlbio-epfl/systema page (two prompts), its raw README and its raw LICENSE file | page and README ok; the LICENSE file returned HTTP 404 and the page shows no licence | 页面和 README 正常；LICENSE 文件返回 HTTP 404，页面也没有显示许可 |
| Q132 | — | WebFetch of an api.github.com repository search for the Systema evaluation code | EMPTY: zero repositories returned (the repository was found by its direct URL, Q131) | 为空：返回 0 个仓库（该仓库是通过直接 URL 找到的，见 Q131） |
| Q133 | — | Script (kbaudit.py ids and meta): parse DOI, arXiv, PubMed and PMC identifiers from the URLs of the 270 rows, fetch metadata from the Crossref, arXiv, Europe PMC, OpenAlex and bioRxiv APIs, then a second pass through Crossref and Europe PMC for rows without an abstract | ok; an abstract for all 270 rows | 正常；270 行都有摘要 |
| Q134 | — | Script (kbaudit.py text): fetch the best available full text of each of the 270 rows by identifier from open-access sources (arXiv, PubMed Central and Europe PMC, publisher pages through the DOI, GitHub); the Bioconductor package vignette for DS04 and the arXiv page for WM38 then replaced two secondary pages | first pass: 207 of 270 rows with a full text and 63 abstract-only (31 bioRxiv, 9 Cell Press, 4 ScienceDirect, 3 Science and 16 others); texts are kept outside the repository | 首轮抓取：270 行中 207 行取得全文，63 行仅有摘要（bioRxiv 31 行、Cell Press 9 行、ScienceDirect 4 行、Science 3 行、其他 16 行）；文本保存在仓库之外 |
| Q135 | — | Shallow git clones of 15 repositories (README, licence, project file and key source files): scooby, iterative-perturb-seq, CPA, Perturbgen, state, cellflow, stack, ReconEval, immune-world-model, LabCompass, LabCompass-reproducibility, scPerturBench, virtual-cell-generalization, Systema and a Bioconductor package mirror | ok; 15 of 15 read | 正常；15 个中的 15 个均已读取 |
| Q136 | — | Dataset pages: Hugging Face API records and cards for Tahoe-100M, X-Atlas/Orion and LabCompass, the GEO series pages GSE92742 and GSE279945, the Zenodo record 5000833, and the Parse Biosciences, Virtual Cell Challenge and Arc Institute pages | ok, except the Virtual Cell Challenge evaluation page, which is rendered by script and returned 33 bytes | 正常，但 Virtual Cell Challenge 评测页面由脚本渲染，只返回了 33 字节 |
| Q137 | — | HTTP range reads of the Tahoe-100M metadata tables on Hugging Face (the cell line, drug and sample tables in full; the cell_name, pass_filter and plate columns of obs_metadata) | ok; derived by the curator: 100,648,790 cells, 50 cell lines, 379 drugs at 3 doses, 14 plates and per-line driver annotations (see DS07 and the dataset table) | 正常；整理者推导：100,648,790 个细胞、50 个细胞系、379 种药物 × 3 个剂量、14 块板和逐系驱动突变注释（见 DS07 和数据集表） |
| Q138 | — | bioRxiv: JATS XML and PDF requests at least 100 s apart (biorxiv_fetch.py) and HEAD requests, for the LabCompass preprint and other bioRxiv rows | FAILED: HTTP 429 from Cloudflare on every attempt; the fetcher was stopped, and no full text was read from www.biorxiv.org | 失败：每次尝试都收到 Cloudflare 的 HTTP 429；抓取器已停止，没有从 www.biorxiv.org 读到任何全文 |
| Q139 | — | PubMed connector of the bio-research plugin: three title searches (the GD52, GD46 and GD36 papers), one citation lookup (Cancer Discov 2015;5:154 for GD46 and Cancer Discov 2014;4:OF17 for GD36) and metadata for PMID 38485147 and PMID 25501949 | ok; the abstract of GD46 (PMID 25501949) was read; GD52 has only a research letter without an abstract and GD36 only a news item, so both were retired | 正常；读到了 GD46 的摘要（PMID 25501949）；GD52 只有无摘要的研究快报，GD36 只有新闻条目，二者均已退役 |
| Q140 | — | bioRxiv connector of the bio-research plugin: get_preprint for DOI 10.64898/2026.10.07.756550 (the LabCompass preprint, WM27) | ok; metadata and abstract only: corresponding author Fabian J. Theis, 4 loops, a 78-million-cell dataset; no full text | 正常；只有元数据和摘要：通讯作者 Fabian J. Theis、4 轮闭环、78 百万（7,800 万）细胞的数据集；没有全文 |
| Q141 | — | Script (fetch_holds.py): metadata and full texts for the 40 held candidates H01 to H40 | 31 of 40 with a full text; 9 abstract-only or empty (H07, H11, H15, H20, H29, H30, H35, H37, H40) | 40 个候选中 31 个取得全文；9 个仅有摘要或为空（H07、H11、H15、H20、H29、H30、H35、H37、H40） |
| Q142 | — | Screening of the 40 held candidates against the five-condition inclusion bar, from the texts of Q141 (every number kept in a new row is backed by a verbatim quote that a script matched against the stored text) | 21 accepted and added as MD68 to MD74, GD54, GD55, GV32, GV33, WM41 to WM47 and EV37 to EV39; 10 rejected (H02, H03, H06, H08, H13, H16, H17, H24, H28, H36); 9 held for lack of text | 21 个被接受并加入为 MD68 至 MD74、GD54、GD55、GV32、GV33、WM41 至 WM47 和 EV37 至 EV39；10 个被拒绝（H02、H03、H06、H08、H13、H16、H17、H24、H28、H36）；9 个因缺少文本而搁置 |
| Q143 | — | Claim audit of the 232 rows that were active before this round: agents compared each recorded key point, "so what" and caveat with the stored text and wrote verdicts with verbatim quotes, and a script checked every quote as a literal substring of the stored text | 2,305 claims checked: 2,094 verified, 110 unsupported, 71 not checkable and 30 contradicted; tiers re-graded (143 rows T2 to T1, 9 rows T3 to T1, 8 rows retired) | 检查了 2,305 条论断：2,094 条得到核实、110 条无依据、71 条无法检查、30 条被反驳；等级重评（143 行 T2 升为 T1、9 行 T3 升为 T1、8 行退役） |
<!-- search-table:end -->

## 4. Unmapped claims (F18) / 无法映射的主张（F18）

Three claims in first-round search summaries could not be tied to a URL. One was resolved in the second round: the 51-person study of ethanol, caffeine and nicotine exposure with treatment-specific eQTLs is [GD10] (query Q105). Item b, that drug-response agreement between GDSC, CTRP and CCLE on one side and PRISM on the other stays low, is supported only in a narrower form by [EV18], which reports a cross-study label reproducibility of 0.220 (self-reported); [EV19] does not support it. Item c, a KRAS G12C mechanism in which a co-occurring PIK3CA mutation enables bypass signaling, remains unmapped and is not a fact.

> 第一轮检索摘要中的三项主张无法对应到 URL。其中一项在第二轮得到解决：涉及 51 人、关于乙醇、咖啡因和尼古丁暴露并报告处理特异 eQTL 的研究就是 [GD10]（查询 Q105）。b 项，即 GDSC、CTRP 和 CCLE 与 PRISM 之间药物响应一致性仍然较低，只有 [EV18] 以更窄的形式支持，它报告跨研究的标签可重复性为 0.220（自报）；[EV19] 不支持该说法。c 项，即一个 KRAS G12C 机制，其中共存的 PIK3CA 突变使旁路信号成为可能，仍未映射，不是事实。

## 5. Topics that returned nothing / 没有返回结果的主题

The following topics returned no relevant hits, which is weak evidence of absence because the search tool is limited: drug-stimulation-specific single-cell eQTLs (Q04); statin studies in lymphoblastoid lines or hepatocytes (Q17, Q30); human Perturb-seq across several donor genotypes with drugs (Q12, Q33); a model that takes inherited donor genotype as input (Q12, Q31); a direct comparison of Tahoe-100M with L1000 (Q11); counterfactual queries in causal representation learning (Q19); a joint pipeline of OmniPath, SIGNOR, Reactome and Open Targets (Q21); noncoding regulatory annotation under PharmVar (Q22); a head-to-head comparison of AlphaFold 3 and Boltz-2 on resistance mutations (Q34); an EVE comparison with AlphaMissense and ESM1b (Q39); a pharmacogenomics-specific view of ancestry bias (Q42); and a joint BRAF, KRAS and TP53 stratified pharmacotranscriptomic study (Q43).

> 下列主题没有返回相关命中，这只是缺失的弱证据，因为检索工具有限：药物刺激特异的单细胞 eQTL（Q04）；淋巴母细胞系或肝细胞中的他汀研究（Q17、Q30）；带药物的、跨多个供体基因型的人类 Perturb-seq（Q12、Q33）；以遗传性供体基因型为输入的模型（Q12、Q31）；Tahoe-100M 与 L1000 的直接比较（Q11）；因果表示学习中的反事实查询（Q19）；OmniPath、SIGNOR、Reactome 和 Open Targets 的联合管线（Q21）；PharmVar 下的非编码调控注释（Q22）；AlphaFold 3 与 Boltz-2 在耐药突变上的直接对比（Q34）；EVE 与 AlphaMissense 和 ESM1b 的比较（Q39）；祖源偏倚的药物基因组学视角（Q42）；以及 BRAF、KRAS 和 TP53 联合分层的药物转录组研究（Q43）。

The second round added the following: a Theis-lab world-model preprint (Q47); transcriptional-response comparisons between target-mutant and wild-type cells under the same drug (Q62); donor-genotype covariates in perturbation models (Q76); a sci-FATE publication or dataset (Q87); glucocorticoid-stimulated reporter assays (Q93); transcriptome-level closed-loop systems for differentiation protocols (Q97); and single-cell gene-by-drug Perturb-seq (Q116). Two further queries returned nothing but the targets were found by other queries: CellBox (Q10; found in Q88) and the LabCompass preprint through a Göttgens-lab query (Q104; found in Q45, Q48 and Q112).

> 第二轮增加了下列主题：Theis 实验室的世界模型预印本（Q47）；同一药物下目标突变细胞与野生型细胞之间的转录响应比较（Q62）；扰动模型中的供体基因型协变量（Q76）；sci-FATE 的论文或数据集（Q87）；糖皮质激素刺激的报告基因实验（Q93）；转录组层面的分化方案闭环系统（Q97）；以及单细胞基因×药物 Perturb-seq（Q116）。另有两个查询一无所获，但目标被其他查询找到：CellBox（Q10；在 Q88 中找到）和通过 Göttgens 实验室查询找 LabCompass 预印本（Q104；在 Q45、Q48 和 Q112 中找到）。

## 6. Failures and refusals / 失败与拒绝

In the first round, the hosts arxiv.org and arcinstitute.org could not be resolved (Q14, Q16), a shell command that queried the agent proxy status was blocked by the permission classifier and was not retried (Q15), and the bio-research literature servers failed to connect with proxy 403 errors, so no structured literature or target-database query was possible. Two searches were interrupted by the user (Q27, Q28) and re-run in modified form as Q31 and Q32.

> 在第一轮中，arxiv.org 和 arcinstitute.org 这两个主机无法解析（Q14、Q16），一条查询代理状态的 shell 命令被权限分类器拦截且未重试（Q15），bio-research 文献服务器因代理 403 错误连接失败，因此无法进行结构化的文献或靶点数据库查询。两次检索被用户中断（Q27、Q28），并以改写形式重跑为 Q31 和 Q32。

In the second round, seven further hosts could not be resolved (www.biorxiv.org, huggingface.co, behindthebioinformatics.substack.com, europepmc.org, pubmed.ncbi.nlm.nih.gov, zenodo.org and openreview.net; Q123), the GitHub tree API returned HTTP 403 for the two LabCompass repositories (Q124), the bio-research plugin servers failed again with a proxy 403 (Q125), www.ncbi.nlm.nih.gov could not be resolved (Q130) and the LICENSE file of the Systema repository returned HTTP 404 (Q131). Only GitHub pages, raw GitHub files, the GitHub search API and pypi.org could be fetched, so repositories could be read directly and papers could not.

> 在第二轮中，另有七个主机无法解析（www.biorxiv.org、huggingface.co、behindthebioinformatics.substack.com、europepmc.org、pubmed.ncbi.nlm.nih.gov、zenodo.org 和 openreview.net；Q123），GitHub 目录树 API 对两个 LabCompass 仓库返回 HTTP 403（Q124），bio-research 插件服务器再次因代理 403 而失败（Q125），www.ncbi.nlm.nih.gov 无法解析（Q130），Systema 仓库的 LICENSE 文件返回 HTTP 404（Q131）。只有 GitHub 页面、GitHub 原始文件、GitHub 搜索 API 和 pypi.org 能抓取，因此仓库可以直接阅读，而论文不能。

In the third round the network was open, but www.biorxiv.org answered every JATS XML, PDF and HEAD request with an HTTP 429 from Cloudflare (Q138), so no bioRxiv full text was read, including that of the LabCompass preprint [WM27]. The evaluation page of the Virtual Cell Challenge is rendered by script and returned 33 bytes (Q136), and the PubMed connector found only a research letter without an abstract for one row and a news item for another (Q139).

> 在第三轮中网络是开放的，但 www.biorxiv.org 对每一次 JATS XML、PDF 和 HEAD 请求都返回来自 Cloudflare 的 HTTP 429（Q138），因此没有读到任何 bioRxiv 全文，包括 LabCompass 预印本 [WM27]。Virtual Cell Challenge 的评测页面由脚本渲染，只返回了 33 字节（Q136），而 PubMed 连接器对一个条目只找到没有摘要的研究快报，对另一个只找到一条新闻（Q139）。

## 7. Status of the load-bearing claims / 承重主张的状态

The load-bearing rows named in earlier versions of this section were audited against their texts in the third round (Q143). Those still at abstract level are [GD01, DS05, EV07, MD06, WM06, EV16, EV19, WM27, WM35, WM36] at tier T2 and [KB17] at tier T3, so any statement that rests only on them should be read as unverified. The Tahoe-100M counts in this repository were derived from the metadata tables of the dataset itself (Q137, [DS07]) and not read from the preprint [DS05].

> 本节早期版本点名的承重条目已在第三轮对照其文本做了核查（Q143）。仍停留在摘要层面的是 T2 级的 [GD01, DS05, EV07, MD06, WM06, EV16, EV19, WM27, WM35, WM36] 和 T3 级的 [KB17]，因此任何仅依赖它们的陈述都应视为未核实。本仓库中的 Tahoe-100M 计数是由数据集自身的元数据表推导出来的（Q137，[DS07]），而不是从预印本 [DS05] 读到的。

## 8. Leads and stop rule / 线索与停止规则

Seeds for the next round, in the order of expected value, are transcriptome-level closed-loop or lab-in-the-loop design papers, multi-donor drug or cytokine single-cell data with genotype, knowledge-graph priors for variant-affected pathways, time-resolved drug single-cell data, mechanism-level benchmarks, stimulus-response eQTL studies in immune cells, statin-treated lymphoblastoid-line eQTL studies, donor-pooled single-cell RNA-seq with a stimulus, and a re-screen of the 9 held candidates once their full text is readable. These seeds come from background knowledge and are not evidence.

> 下一轮的种子，按预期价值排序，是转录组层面的闭环或实验室闭环设计论文、带基因型的多供体药物或细胞因子单细胞数据、受变异影响通路的知识图谱先验、时间分辨的药物单细胞数据、机制层面的基准、免疫细胞中的刺激-响应 eQTL 研究、他汀处理淋巴母细胞系的 eQTL 研究、带刺激的供体混合单细胞 RNA-seq，以及在全文可读之后对 9 个搁置候选的重新筛选。这些种子来自背景知识，不是证据。

The stop rule is two consecutive rounds that add fewer than 3 sources. The second round added 79 and the third round 22, so the rule has not been triggered; whether to stop collecting now is the open question UQ16.

> 停止规则是连续两轮新增来源少于 3 条。第二轮新增了 79 条，第三轮新增了 22 条，因此该规则尚未触发；现在是否停止收集是待确认问题 UQ16。

## 9. Screening decisions / 筛选决定

In the second round 79 results were added to `data/sources.csv`, 10 existing rows were upgraded, 38 older rows were retired, 40 candidates were held and 5 groups of results were rejected. In the third round the 40 held candidates were screened against the five conditions of the inclusion bar from their retrieved texts (Q141, Q142): 21 were accepted, 10 were rejected, and 9 stay held because only an abstract or nothing could be read. A held candidate looked relevant but too little was retrieved to state a "so what"; it is not a negative judgment.

> 第二轮中有 79 条结果被加入 `data/sources.csv`，10 条现有条目被升级，38 条旧条目被退役，40 个候选被搁置，5 组结果被拒绝。第三轮依据取回的文本，对照纳入门槛的五个条件筛选了这 40 个搁置候选（Q141、Q142）：21 个被接受，10 个被拒绝，9 个继续搁置，因为只能读到摘要或什么也读不到。被搁置的候选看起来相关，但取回的内容太少而无法写出“意义”；这不是否定性判断。

The accepted candidates became new rows: H01 as MD68, H04 as MD69, H05 as GD54, H09 as GV32, H10 as GV33, H12 as WM41, H14 as GD55, H18 as MD70, H19 as MD71, H21 as MD72, H22 as EV37, H23 as MD73, H25 as MD74, H26 as WM42, H27 as WM43, H31 as WM44, H32 as WM45, H33 as WM46, H34 as WM47, H38 as EV38 and H39 as EV39.

> 被接受的候选成为新条目：H01 记为 MD68，H04 记为 MD69，H05 记为 GD54，H09 记为 GV32，H10 记为 GV33，H12 记为 WM41，H14 记为 GD55，H18 记为 MD70，H19 记为 MD71，H21 记为 MD72，H22 记为 EV37，H23 记为 MD73，H25 记为 MD74，H26 记为 WM42，H27 记为 WM43，H31 记为 WM44，H32 记为 WM45，H33 记为 WM46，H34 记为 WM47，H38 记为 EV38，H39 记为 EV39。

The retirement codes are R1 (marked peripheral in iteration 1 and never cited), R2 (review, perspective, news or blog item, never cited), R3 (narrow scope: mouse, protocol only or title only), R4 (duplicate or superseded by another row), R5 (redundant inside a cluster that is already covered), R6 (off the aim) and R7 (third round: the text could not be read, or the item adds nothing beyond a row that covers it). The closest calls are GD04, GD05, GD29, GV08 and KB03, which concern in-scope topics and are retired only because no document uses them; restoring a row means changing its status column.

> 退役代码为 R1（在第 1 轮中被标为边缘且从未被引用）、R2（综述、观点、新闻或博客条目，从未被引用）、R3（范围狭窄：小鼠、仅方案或仅标题）、R4（与另一条目重复或已被取代）、R5（位于已被覆盖的簇内而冗余）、R6（偏离研究目标）和 R7（第三轮：文本无法读取，或该条目没有提供超出已涵盖它的条目的内容）。最难取舍的是 GD04、GD05、GD29、GV08 和 KB03，它们涉及范围内的主题，之所以退役，只是因为没有文档使用它们；恢复一个条目只需改它的 status 列。

### 9.1 Rejected candidates (10) / 被拒绝的候选（10）

| ID | Title (as published; truncated where the search result was) | URL | Reason (EN) | 原因（中文） |
|---|---|---|---|---|
| H02 | Multiome Perturb-seq unlocks scalable discovery of integrated perturbation effects on the transcriptome and epigenome | https://www.biorxiv.org/content/10.1101/2024.07.26.605307.full.pdf | A guide-capture method with a small pilot of 13 chromatin-remodeler targets; no drug, dose or genotype axis, so nothing transfers to a genotype-aware drug-response model | 一种引导 RNA 捕获方法加一个涉及 13 个染色质重塑因子靶点的小型先导实验；没有药物、剂量或基因型维度，因此没有内容可迁移到基因型感知的药物响应模型 |
| H03 | CFM-GP: Unified Conditional Flow Matching to Learn Gene Perturbation Across Cell Types | https://arxiv.org/pdf/2508.08312 | Conditional flow matching from control to perturbed profiles adds no design principle beyond MD05 and MD09, and the text reports no mean or linear baseline | 从对照到扰动谱的条件流匹配没有提供超出 MD05 和 MD09 的设计原则，且文中没有报告均值或线性基线 |
| H06 | Gene isoforms as expression-based biomarkers predictive of drug response in vitro | https://www.nature.com/articles/s41467-017-01153-8 | Baseline isoform expression as univariate biomarkers of growth sensitivity; no drug-induced transcription, perturbation-response model or variant mechanism, and its lessons on label inconsistency are covered by EV15 to EV17 | 把基线异构体表达作为生长敏感性的单变量生物标志物；没有药物诱导转录、扰动响应模型或变异机理，其关于标签不一致的教训已由 EV15 至 EV17 涵盖 |
| H08 | GPX1 confers resistance to metabolic stress in BCR/ABL-T315I mutant chronic myeloid leukemia cells | https://www.nature.com/articles/s41420-025-02502-z | Association-level evidence from 3 versus 3 bone-marrow RNA-seq samples with no data accession; the GPX1 therapeutic angle does not transfer to transcription prediction | 关联层面的证据，来自 3 对 3 个骨髓 RNA-seq 样本，没有数据登录号；GPX1 的治疗角度不能迁移到转录预测 |
| H13 | Drug-tolerant persister cells in cancer: bridging the gaps between bench and bedside | https://www.nature.com/articles/s41467-025-66376-6 | A qualitative perspective with no data or number of its own; its main points are carried by GD51, GD33 and GD34 | 一篇没有自己的数据或数字的定性观点文章；其要点已由 GD51、GD33 和 GD34 承载 |
| H16 | Multi-objective optimization reveals time- and dose-dependent inflammatory cytokine-mediated regulation of human stem cell derived T-cell development | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8795204/ | Culture-protocol optimization of stem-cell-derived T-cell development with flow-cytometry counts and a few qPCR genes; no transcriptome, drug or genotype | 干细胞来源 T 细胞发育的培养方案优化，读数为流式细胞计数和少数 qPCR 基因；没有转录组、药物或基因型 |
| H17 | Accelerating cell culture media development using Bayesian optimization-based iterative experimental design | https://www.nature.com/articles/s41467-025-61113-5 | Bayesian optimization of culture media with viability and titer readouts; no transcriptome, variant or perturbation-response model, and closer closed-loop anchors exist (MD48, WM27) | 对培养基的贝叶斯优化，读数为存活率和滴度；没有转录组、变异或扰动响应模型，且存在更贴近的闭环锚点（MD48、WM27） |
| H24 | DeMixPert: Decomposed Response Modeling with Gaussian Mixtures for OOD Single-Cell Perturbation Prediction | https://arxiv.org/pdf/2608.23114 | Redundant: its decomposition, conditional-generation and distribution-modeling ideas overlap MD40, MD18, MD39 and MD09, its motivation is EV29, and its gains are self-reported on four small CRISPR sets with unreleased code | 冗余：其分解、条件生成和分布建模思路与 MD40、MD18、MD39 和 MD09 重叠，动机来自 EV29，其增益是在四个小型 CRISPR 数据集上自报的，代码未发布 |
| H28 | Escaping Local Optima in the Waddington Landscape: A Two-Stage TRPO–PPO Approach for Single-Cell Perturbation Analysis | https://arxiv.org/html/2510.13018v1 | A generic policy-optimization warm start (TRPO step, then PPO) compared only with vanilla PPO on a random split, so no unseen-perturbation generalization; no transferable mechanism, data or protocol | 通用的策略优化热启动（先 TRPO 再 PPO），只与原始 PPO 在随机拆分上比较，因此没有对未见扰动的泛化；没有可迁移的机理、数据或方案 |
| H36 | Molecular causality in the advent of foundation models | https://arxiv.org/pdf/2401.09558 | A perspective with no data, benchmark or protocol of its own; its message that prior knowledge and hybrid models help when data are scarce is covered by MD12, MD13, MD14 and KB10 | 一篇没有自己的数据、基准或方案的观点文章；其关于数据稀缺时先验知识和混合模型有帮助的观点已由 MD12、MD13、MD14 和 KB10 涵盖 |

### 9.2 Candidates still held (9) / 仍被搁置的候选（9）

| ID | Title (as published; truncated where the search result was) | URL | Reason (EN) | 原因（中文） |
|---|---|---|---|---|
| H07 | The Allelic Context of the C797S Mutation Acq... (title truncated) | https://aacrjournals.org/clincancerres/article/21/17/3924/117742/The-Allelic-Context-of-the-C797S-Mutation-Acq | No text or abstract could be retrieved (the OpenAlex lookup answered HTTP 429), so none of the five conditions can be judged | 没有取回任何文本或摘要（OpenAlex 查询返回 HTTP 429），因此五个条件都无法判断 |
| H11 | Variability within rare cell states enables multiple paths towards drug resistance | https://www.biorxiv.org/content/10.1101/2020.03.18.996660v2.full | Abstract only: rare drug-naive precursors of resistance in BRAF V600E melanoma overlap GD51; whether the lineage-barcoding result adds a checkable anchor needs the full text | 仅有摘要：BRAF V600E 黑色素瘤中罕见的药物初治耐药前体与 GD51 重叠；谱系条形码的结果能否增加可核对的锚点需要全文 |
| H15 | Machine-guided cell-fate engineering | https://www.biorxiv.org/content/10.1101/2022.10.14.512279.full.pdf | Abstract only: it does not show whether the pipeline learns a perturbation-effect model or an iterative design loop with quantified gains; the Methods and results are needed | 仅有摘要：摘要没有说明该流程学习的是扰动效应模型，还是带有量化增益的迭代设计循环；需要方法和结果部分 |
| H20 | SCREP: Towards Single-Cell Drug Response Prediction by Pharmacogenomic Embedding Enhanced Meta-Pretraining and Few-Shot Transfer Learning | https://www.biorxiv.org/content/10.1101/2024.04.25.591050.full.pdf | Abstract only: it does not say whether the genomic input is mutation or expression, whether the output is a sensitivity label or a transcriptome, or which baselines and splits give the reported gains of 4.58% and 20% | 仅有摘要：摘要没有说明基因组输入是突变还是表达，输出是敏感性标签还是转录组，也没有说明报告的 4.58% 和 20% 增益来自哪些基线和拆分 |
| H29 | Optimizing sequential gene expression modulation for cellular reprogramming - Coupled Boolean modeling and Reinforcement Learning based method | https://www.biorxiv.org/content/10.1101/2024.03.19.585672v1.full | Abstract only: a Boolean model constrains the state space for a reinforcement-learning policy over sequences of modulations, with demonstrations on a 4-gene toy network and a 15-gene network, so transferable scale looks limited | 仅有摘要：布尔模型约束强化学习策略在调控序列上的状态空间，演示是一个 4 基因玩具网络和一个 15 基因网络，因此可迁移的规模看来有限 |
| H30 | Generative Inverse Design with Abstention via Diagonal Flow Matching | https://www.researchgate.net/publication/402612678_Generative_Inverse_Design_with_Abstention_via_Diagonal_Flow_Matching | No text or abstract could be retrieved (the OpenAlex lookup answered HTTP 429); re-screen when an arXiv, journal or full-text page is readable | 没有取回任何文本或摘要（OpenAlex 查询返回 HTTP 429）；待 arXiv、期刊或全文页面可读时重新筛选 |
| H35 | In Vivo Time-Resolved Single-Cell RNA-Seq Reveals Chemotherapy-Induced Transcriptional Dynamics in Tumor Infiltrating Lymphocytes | https://pubs.acs.org/doi/10.1021/acs.analchem.4c05648 | Abstract only (not open access): an in vivo 4sU time-resolved method with qualitative cisplatin effects in mouse tumor-infiltrating lymphocytes, without counts, time points, doses or data access | 仅有摘要（非开放获取）：一种体内 4sU 时间分辨方法，报告了小鼠肿瘤浸润淋巴细胞中定性的顺铂效应，没有计数、时间点、剂量或数据获取方式 |
| H37 | Tracking biological hallucinations in single-cell perturbation predictions using scArchon, a comprehensive benchmarking platform | https://www.biorxiv.org/content/10.1101/2025.06.23.661046.full.pdf | Abstract only: it names the tools and a finding that good quantitative scores can hide lost biological signatures but gives no datasets, splits, metrics or numbers, and it overlaps EV20, EV33 and EV01 | 仅有摘要：摘要点出了工具，以及良好的定量得分可能掩盖生物学特征丢失的发现，但没有给出数据集、拆分、指标或数字，并且与 EV20、EV33 和 EV01 重叠 |
| H40 | Uncertainty-aware transcription factor activity and perturbation inference without additional training | https://www.biorxiv.org/content/10.1101/2025.10.05.680506.full.pdf | Abstract only: TFActProfiler (signed TF-mRNA effect map, confidence score, training-free perturbation prediction) could matter for uncertainty, but no datasets, metrics or numbers are given and the comparison with KB20 cannot be checked | 仅有摘要：TFActProfiler（带符号的 TF–mRNA 效应图、置信度得分、无需训练的扰动预测）可能对不确定性有意义，但没有给出数据集、指标或数字，与 KB20 的比较无法核对 |

Judgment (confidence: low): of the 9 held candidates, H15 (machine-guided cell-fate engineering), H30 (abstention in inverse design) and H07 (allelic context of a resistance mutation) are the most likely to change the design if their full text becomes readable, because each bears on insights I2, I6 or I9 of document 09.

> 判断（置信度：低）：在 9 个搁置候选中，H15（机器引导的细胞命运工程）、H30（逆向设计中的弃权）和 H07（耐药突变的等位基因背景）在全文可读后最有可能改变设计，因为它们各自关系到文档 09 的启示 I2、I6 或 I9。

### 9.3 Rejected result groups (5) / 被拒绝的结果组（5）

| Group | Examples seen | Queries | Reason (EN) | 原因（中文） |
|---|---|---|---|---|
| G1 | Dflow-SUR (aerodynamics), Conditional Flow Matching for ML-Based Inverse Design Problems, How well do generative models solve inverse problems? A benchmark study, surrogate models for blood flow and implosions | Q48, Q112 | not about cells, drugs or genetic variation; the guidance ideas reach this project through the included papers (WM28, WM39, WM40) | 与细胞、药物或遗传变异无关；引导思想通过已纳入的论文（WM28、WM39、WM40）到达本项目 |
| G2 | patent documents on BCR-ABL mutations, CD34+ expansion media and SF3B1 splice variants | Q61, Q62, Q104 | no peer-reviewed content; claims cannot be verified | 没有同行评议内容；主张无法核实 |
| G3 | CD34+ cell enumeration by flow cytometry, label-free CD34+ identification, CD44 knockout in CD34+ cells | Q49, Q104 | shared keywords only; no link to design or genotype | 只是关键词相同；与设计或基因型无关 |
| G4 | massively parallel reporter assays of cortical-structure regulatory activity and general MPRA reviews | Q93 | no drug, hormone or other perturbation arm, so no genotype-by-treatment content | 没有药物、激素或其他扰动组，因此没有基因型×处理的内容 |
| G5 | Medium, EmergentMind, LearnOpenCV, Pith and ResearchGate copies, and X summaries other than WM30 | Q53, Q110, Q113 | secondary copies of papers that are already ledgered or cited through the primary page | 已入账或通过一手页面引用的论文的二手副本 |

Rejected groups are results that share keywords with the topic but carry no mechanism or modeling content for it.

> 被拒绝的组是与主题共享关键词、但对其不含机理或建模内容的结果。

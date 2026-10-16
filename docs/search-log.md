# Search log / 检索日志

## 1. Scope / 范围

This log records every query, tool attempt and outcome behind the repository, including failures and refusals, so that absence claims in the documents can be traced to a query ID. It also lists the unmapped claims, the topics that returned nothing, the claims to verify first, the leads for later search rounds and the screening decisions of the second round.

> 本日志记录仓库背后的每次查询、工具尝试和结果，包括失败和拒绝，使文档中的“缺失”论断都能追溯到查询 ID。它还列出无法映射的主张、没有返回任何结果的主题、需要优先核验的主张、后续检索轮次的线索，以及第二轮的筛选决定。

## 2. Legend and totals / 图例与总数

Mode E is the extended web search and mode S is the standard web search. "EMPTY" means the target topic returned no relevant hits. In total, 34 extended and 5 standard searches completed, 2 more were interrupted by the user and re-run in modified form, and 3 non-search attempts failed or were blocked: two page fetches that could not resolve their hosts and one shell command blocked by the permission classifier. The second round (Q45 to Q132) added 78 searches (71 extended and 7 standard, Q45 to Q118 and Q126 to Q129), 46 page fetches grouped as Q119 to Q124 and Q130 to Q132 (35 succeeded and 11 failed) and one note on unavailable tools (Q125); query texts are verbatim and outcomes are my summary of what came back. Q126 to Q132 are verification checks that were run after the first commit of the second round.

> 模式 E 是扩展网络检索，模式 S 是标准网络检索。“EMPTY”表示目标主题没有返回相关命中。总计完成 34 次扩展检索和 5 次标准检索，另有 2 次被用户中断并以改写形式重跑，还有 3 次非检索尝试失败或被拦截：两次因无法解析主机而失败的页面抓取，以及一条被权限分类器拦截的 shell 命令。第二轮（Q45 至 Q132）增加了 78 次检索（71 次扩展、7 次标准，Q45 至 Q118 以及 Q126 至 Q129）、按 Q119 至 Q124 和 Q130 至 Q132 分组的 46 次页面抓取（35 次成功、11 次失败）以及一条关于不可用工具的说明（Q125）；查询文本为原文，结果是我对返回内容的概括。Q126 至 Q132 是在第二轮第一次提交之后进行的核验检查。

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
<!-- search-table:end -->

## 4. Unmapped claims (F18) / 无法映射的主张（F18）

Three claims in search summaries could not be tied to a specific URL in the first round and were therefore not recorded as facts. Item a, a 51-person study of ethanol, caffeine and nicotine exposure that reported treatment-specific and temporally dynamic eQTLs, was resolved in the second round: it is the response-eQTL paper recorded as [GD10] (query Q105). Item b is the statement that drug-response agreement between GDSC, CTRP and CCLE on one side and PRISM on the other stays low. Item c is a KRAS G12C mechanism in which a co-occurring PIK3CA mutation enables bypass signaling. Candidate sources for item b are [EV18, EV19], whose titles were truncated.

> 检索摘要中的三项主张在第一轮无法对应到具体 URL，因此没有记为事实。a 项是一项涉及 51 人、关于乙醇、咖啡因和尼古丁暴露的研究，报告了处理特异且随时间动态变化的 eQTL，它在第二轮得到解决：就是记为 [GD10] 的响应 eQTL 论文（查询 Q105）。b 项是关于 GDSC、CTRP 和 CCLE 与 PRISM 之间药物响应一致性仍然较低的说法。c 项是一个 KRAS G12C 机制，其中共存的 PIK3CA 突变使旁路信号成为可能。b 项的候选来源是 [EV18, EV19]，它们的标题被截断。

## 5. Topics that returned nothing / 没有返回结果的主题

The following topics returned no relevant hits, which is weak evidence of absence because the search tool is limited. Drug-stimulation-specific single-cell eQTLs (Q04). Statin studies in lymphoblastoid lines or hepatocytes (Q17, Q30). Human Perturb-seq across several donor genotypes with drugs (Q12, Q33). A model that takes inherited donor genotype as input (Q12, Q31). A direct comparison of Tahoe-100M with L1000 (Q11). CellBox (Q10; found later in Q88). Counterfactual queries in causal representation learning (Q19). A joint pipeline of OmniPath, SIGNOR, Reactome and Open Targets (Q21). Noncoding regulatory annotation under PharmVar (Q22). A head-to-head comparison of AlphaFold 3 and Boltz-2 on resistance mutations (Q34). An EVE comparison with AlphaMissense and ESM1b (Q39). A pharmacogenomics-specific view of ancestry bias (Q42). A joint BRAF, KRAS and TP53 stratified pharmacotranscriptomic study (Q43).

> 下列主题没有返回相关命中，这只是缺失的弱证据，因为检索工具有限。药物刺激特异的单细胞 eQTL（Q04）。淋巴母细胞系或肝细胞中的他汀研究（Q17、Q30）。带药物的、跨多个供体基因型的人类 Perturb-seq（Q12、Q33）。以遗传性供体基因型为输入的模型（Q12、Q31）。Tahoe-100M 与 L1000 的直接比较（Q11）。CellBox（Q10；后来在 Q88 中找到）。因果表示学习中的反事实查询（Q19）。OmniPath、SIGNOR、Reactome 和 Open Targets 的联合管线（Q21）。PharmVar 下的非编码调控注释（Q22）。AlphaFold 3 与 Boltz-2 在耐药突变上的直接对比（Q34）。EVE 与 AlphaMissense 和 ESM1b 的比较（Q39）。祖源偏倚的药物基因组学视角（Q42）。BRAF、KRAS 和 TP53 联合分层的药物转录组研究（Q43）。

In the second round the following topics again returned nothing relevant, which is weak evidence of absence. A Theis-lab world-model preprint (Q47). Transcriptional-response comparisons between target-mutant and wild-type cells under the same drug (Q62). Donor-genotype covariates in perturbation models (Q76). A sci-FATE publication or dataset (Q87). Glucocorticoid-stimulated reporter assays (Q93). Transcriptome-level closed-loop systems for differentiation protocols (Q97). Single-cell gene-by-drug Perturb-seq (Q116). The LabCompass preprint through a Göttgens-lab query (Q104), although the preprint was found by other queries (Q45, Q48 and Q112).

> 在第二轮中，下列主题再次没有返回相关结果，这只是缺失的弱证据。Theis 实验室的世界模型预印本（Q47）。同一药物下目标突变细胞与野生型细胞之间的转录响应比较（Q62）。扰动模型中的供体基因型协变量（Q76）。sci-FATE 的论文或数据集（Q87）。糖皮质激素刺激的报告基因实验（Q93）。转录组层面的分化方案闭环系统（Q97）。单细胞基因×药物 Perturb-seq（Q116）。通过 Göttgens 实验室查询找 LabCompass 预印本（Q104）一无所获，尽管该预印本被其他查询找到了（Q45、Q48 和 Q112）。

## 6. Failures and refusals / 失败与拒绝

Two page fetches failed because the hosts arxiv.org and arcinstitute.org could not be resolved (Q14, Q16), so the abstract of VCWorld and the Arc challenge wrap-up could not be read directly. One shell command that queried the agent proxy status was blocked by the permission classifier and was not retried (Q15). All bio-research literature servers (PubMed, bioRxiv, ChEMBL, Open Targets, Consensus and others) failed to connect with proxy 403 errors, so no structured literature or target-database query was possible. Two searches were interrupted by the user (Q27, Q28) and were re-run in modified form as Q31 and Q32.

> 两次页面抓取失败，因为无法解析 arxiv.org 和 arcinstitute.org 这两个主机（Q14、Q16），所以无法直接阅读 VCWorld 的摘要和 Arc 挑战赛总结。一条查询代理状态的 shell 命令被权限分类器拦截，未重试（Q15）。所有 bio-research 文献服务器（PubMed、bioRxiv、ChEMBL、Open Targets、Consensus 等）因代理 403 错误连接失败，因此无法进行结构化的文献或靶点数据库查询。两次检索被用户中断（Q27、Q28），并以改写形式重跑为 Q31 和 Q32。

In the second round, seven further hosts could not be resolved (www.biorxiv.org, huggingface.co, behindthebioinformatics.substack.com, europepmc.org, pubmed.ncbi.nlm.nih.gov, zenodo.org and openreview.net; Q123), the GitHub tree API returned HTTP 403 for the two LabCompass repositories (Q124), and the bio-research plugin servers (biorender, biorxiv, c-trials, chembl, consensus, ot, owkin, pubmed, synapse and wiley) were again reported as failed to connect with a proxy 403 (Q125). Only GitHub pages, raw GitHub files, the GitHub search API and pypi.org could be fetched, so repositories and packages could be read directly and papers could not. After the first commit of the second round, a fetch of www.ncbi.nlm.nih.gov also failed to resolve (Q130), and the LICENSE file of the Systema repository returned HTTP 404 (Q131).

> 在第二轮中，另有七个主机无法解析（www.biorxiv.org、huggingface.co、behindthebioinformatics.substack.com、europepmc.org、pubmed.ncbi.nlm.nih.gov、zenodo.org 和 openreview.net；Q123），GitHub 目录树 API 对两个 LabCompass 仓库返回 HTTP 403（Q124），bio-research 插件服务器（biorender、biorxiv、c-trials、chembl、consensus、ot、owkin、pubmed、synapse 和 wiley）再次被报告因代理 403 而连接失败（Q125）。只有 GitHub 页面、GitHub 原始文件、GitHub 搜索 API 和 pypi.org 能抓取，因此仓库和软件包可以直接阅读，而论文不能。在第二轮第一次提交之后，对 www.ncbi.nlm.nih.gov 的一次抓取也因无法解析而失败（Q130），Systema 仓库的 LICENSE 文件返回 HTTP 404（Q131）。

## 7. Claims to verify first / 需要优先核验的主张

When full-text access is available, read the primary sources for the load-bearing claims first: [EV01, EV05, GV05, GV06, GV02, GD06, GD01, GD08, DS05, EV07, EV08, EV09, EV10, EV11, MD06, WM06, WM10, GV19, EV16, KB17]. For DS05, check the Tahoe-100M counts; for EV07 to EV11, check the 2026 challenge dates.

> 当可以获取全文时，首先阅读承重主张的原始来源：[EV01, EV05, GV05, GV06, GV02, GD06, GD01, GD08, DS05, EV07, EV08, EV09, EV10, EV11, MD06, WM06, WM10, GV19, EV16, KB17]。对于 DS05，核对 Tahoe-100M 的计数；对于 EV07 至 EV11，核对 2026 年挑战赛的日期。

Entries whose titles were truncated or whose metadata are missing, and which are flagged in the caveat columns of `data/sources.csv`, are [GD13, GD27, EV14, EV18, EV19, KB14].

> 标题被截断或元数据缺失、并在 `data/sources.csv` 的注意事项列中标注的条目是 [GD13, GD27, EV14, EV18, EV19, KB14]。

After the second round, the additional load-bearing claims to read first are: the LabCompass full text [WM27]; the response-eQTL counts [GD10]; the reporter-assay ratio of 6 of 665 [GD50]; the Systema reference shift [EV29]; the genotype-demultiplexed TP53 result [GD45]; the donor counts and the genotyping status of the large cytokine datasets [DS16, MD42]; and the reproducibility claim of TxPert [MD37]. Titles truncated in the second round are those of [MD53, WM34, WM35, WM36, WM37]. The twelve tier-T1 rows are repository or package pages retrieved through a summarizing fetch tool, so statements of absence in them are that tool's report: [GV27, MD49, MD58, MD59, MD62, MD63, MD65, MD66, WM28, WM29, EV03, EV36].

> 第二轮之后，另需优先阅读的承重主张是：LabCompass 全文 [WM27]；响应 eQTL 的计数 [GD10]；报告基因实验的比例 665 个中的 6 个 [GD50]；Systema 的参照重设 [EV29]；按基因型解复用的 TP53 结果 [GD45]；大型细胞因子数据集的供体数和基因分型状态 [DS16, MD42]；以及 TxPert 的可重复性主张 [MD37]。第二轮中标题被截断的是 [MD53, WM34, WM35, WM36, WM37]。12 个 T1 级条目是通过带摘要功能的抓取工具取回的仓库或软件包页面，因此其中关于“没有某内容”的陈述是该工具的报告：[GV27, MD49, MD58, MD59, MD62, MD63, MD65, MD66, WM28, WM29, EV03, EV36]。

Spot checks run after the first commit of the second round (Q126 to Q132) changed three of these load-bearing claims. For [GD10], the 51 individuals and the about 1.4 million cells were reconfirmed, but the per-cell-type counts (31 to 110) and the eGene counts (380, 336 and 276) were not returned in two searches and stay unconfirmed. For [GD50], the 6 of 665 variants were confirmed for the published version at a false discovery rate below 5%, whereas the first version and the preprint report 29 variants at a false discovery rate below 10%, so the interaction fraction depends on the version and the threshold. For [EV29], the perturbed-cell-centroid reference was confirmed in the authors' repository [EV36], whereas the statements that scores drop substantially and that systematic variation is a cosine similarity remain at search-summary level.

> 第二轮第一次提交之后进行的抽查（Q126 至 Q132）改变了其中三项承重主张的状态。对 [GD10]，51 名个体和约 1.4 million（140 万）个细胞得到再次确认，但每种细胞类型的计数（31 至 110）和 eGene 计数（380、336 和 276）在两次检索中都没有返回，仍未确认。对 [GD50]，已发表版本在 FDR 低于 5% 时 665 个变异中的 6 个得到确认，而第一版和预印本报告在 FDR 低于 10% 时有 29 个变异，因此交互比例取决于版本和阈值。对 [EV29]，扰动后细胞质心参照在作者的仓库中得到确认 [EV36]，而得分大幅下降以及系统性变异为余弦相似度的说法仍处于检索摘要层面。

To enable full-text checking, the environment's network policy must allow outbound access: open the environment menu, choose Edit, go to Network access, and either pick a broader level or add the hosts under Allowed domains while leaving "Allow package managers" ticked. Suggested hosts are arxiv.org, biorxiv.org, nature.com, ncbi.nlm.nih.gov, cell.com, sciencedirect.com, elifesciences.org, journals.plos.org, github.com, arcinstitute.org, huggingface.co and virtualcellchallenge.org. The steps are at https://code.claude.com/docs/en/cloud-environments#network-access.

> 要启用全文核查，环境的网络策略必须允许出站访问：打开环境菜单，选择 Edit，进入 Network access，然后选择更宽的级别，或把这些主机加入 Allowed domains 并保持勾选 “Allow package managers”。建议的主机是 arxiv.org、biorxiv.org、nature.com、ncbi.nlm.nih.gov、cell.com、sciencedirect.com、elifesciences.org、journals.plos.org、github.com、arcinstitute.org、huggingface.co 和 virtualcellchallenge.org。步骤见 https://code.claude.com/docs/en/cloud-environments#network-access。

## 8. Leads for a second search round / 第二轮检索的线索

These leads come from background knowledge and were NOT retrieved in this session. They are unverified and must not be cited until they have been checked. Stimulus-response eQTL studies in immune cells (Fairfax 2014 in monocytes, Lee 2014 in dendritic cells, Kim-Hellmuth 2017, Alasoo 2018 in macrophages). A statin-treated lymphoblastoid-line eQTL study (Mangravite 2013). Multiplexed, donor-pooled single-cell RNA-seq with a stimulus (Kang 2018, interferon-beta in blood cells). Data details of GTEx, the eQTL Catalogue and OneK1K. Genome-scale Perturb-seq atlases (Replogle 2022 and later). DrugBank, DGIdb and ChEMBL. The primary JEPA papers. CellBox. The raw data of PharmGKB and CPIC. Multi-line work from the IGVF consortium.

> 这些线索来自背景知识，本次会话并未检索到。它们未经核验，在核实之前不得引用。免疫细胞中的刺激-响应 eQTL 研究（Fairfax 2014 单核细胞，Lee 2014 树突状细胞，Kim-Hellmuth 2017，Alasoo 2018 巨噬细胞）。他汀处理淋巴母细胞系的 eQTL 研究（Mangravite 2013）。带刺激的多路复用、供体混合单细胞 RNA-seq（Kang 2018，血细胞中的干扰素 β）。GTEx、eQTL Catalogue 和 OneK1K 的数据细节。基因组规模 Perturb-seq 图谱（Replogle 2022 及之后）。DrugBank、DGIdb 和 ChEMBL。JEPA 的原始论文。CellBox。PharmGKB 和 CPIC 的原始数据。IGVF 联盟的多细胞系工作。

The second round has been run (Q45 to Q132). Of these leads, the Replogle genome-scale atlas (as [DS19]) and CellBox (as [MD50]) were retrieved; the others remain open and still must not be cited from background knowledge.

> 第二轮已经运行（Q45 至 Q132）。在这些线索中，Replogle 基因组规模图谱（即 [DS19]）和 CellBox（即 [MD50]）已被检索到；其余线索仍未解决，仍不得凭背景知识引用。

## 9. Leads for a third round / 第三轮检索的线索

Seeds for a third round, in the order of expected value: transcriptome-level closed-loop or lab-in-the-loop design papers; multi-donor drug or cytokine single-cell data with genotype; knowledge-graph priors for variant-affected pathways; time-resolved drug single-cell data; mechanism-level benchmarks; and a re-screen of the held candidates in Section 10 once full text is readable. The stop rule is two consecutive rounds that add fewer than 3 sources, and the second round added 79.

> 第三轮的种子，按预期价值排序：转录组层面的闭环或实验室闭环设计论文；带基因型的多供体药物或细胞因子单细胞数据；受变异影响通路的知识图谱先验；时间分辨的药物单细胞数据；机制层面的基准；以及在全文可读之后对第 10 节中被搁置候选的重新筛选。停止规则是连续两轮新增来源少于 3 条，而第二轮新增了 79 条。

## 10. Screening decisions of the second round / 第二轮的筛选决定

Of the results screened in the second round, 79 were added to `data/sources.csv`, 10 existing rows were upgraded, 40 candidates are held and 5 groups of results are rejected; 38 older rows were retired by setting their status to retired, with a reason code in the caveat columns. A held candidate looked relevant, but too little was retrieved to state a "so what"; it is not a negative judgment. Codes for the held list: M1 means title or snippet only, M2 means it overlaps an included row and would be added only if the full text shows a distinct angle, and M3 means a plausible link to the aim that the retrieved text does not state.

> 在第二轮被筛选的结果中，79 条被加入 `data/sources.csv`，10 条现有条目被升级，40 条候选被搁置，5 组结果被拒绝；另有 38 条旧条目通过把状态设为 retired 而退役，并在注意事项列中给出原因代码。被搁置的候选看起来相关，但取回的内容太少而无法写出“意义”；这不是否定性判断。搁置清单的代码：M1 表示仅有标题或片段，M2 表示与已纳入条目重叠、只有全文显示出不同角度才会加入，M3 表示与研究目标可能有关，但取回的文字没有说明。

The retirement codes are R1 (marked peripheral in iteration 1 and never cited), R2 (review, perspective, news or blog item, never cited), R3 (narrow scope: mouse, protocol only or title only), R4 (duplicate or superseded by another row), R5 (redundant inside a cluster that is already covered) and R6 (off the aim). The closest calls are GD04, GD05, GD29, GV08 and KB03, which concern in-scope topics and are retired only because no document uses them; restoring a row means changing its status column. GD15, which was on the original list of closest calls, was first retired and then restored when the validation run found that `data/datasets.csv` cites it.

> 退役代码为 R1（在第 1 轮中被标为边缘且从未被引用）、R2（综述、观点、新闻或博客条目，从未被引用）、R3（范围狭窄：小鼠、仅方案或仅标题）、R4（与另一条目重复或已被取代）、R5（位于已被覆盖的簇内而冗余）和 R6（偏离研究目标）。最难取舍的是 GD04、GD05、GD29、GV08 和 KB03，它们涉及范围内的主题，之所以退役，只是因为没有文档使用它们；恢复一个条目只需改它的 status 列。原本在最难取舍名单上的 GD15 起初被退役，后来在校验中发现 `data/datasets.csv` 引用了它，于是被恢复。

### 10.1 Held candidates (40) / 被搁置的候选（40）

<!-- hold-table:start -->
| ID | Code | Title | URL | Query |
|---|---|---|---|---|
| H01 | M1 | Decoding heterogeneous single-cell perturbation responses | https://www.nature.com/articles/s41556-025-01626-9 | Q57 |
| H02 | M3 | Multiome Perturb-seq unlocks scalable discovery of integrated perturbation eff... (title truncated) | https://www.biorxiv.org/content/10.1101/2024.07.26.605307.full.pdf | Q57 |
| H03 | M2 | CFM-GP: Unified Conditional Flow Matching to Learn Gene Perturbation Across Ce... (title truncated) | https://arxiv.org/pdf/2508.08312 | Q57 |
| H04 | M2 | PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling | https://arxiv.org/pdf/2602.19685 | Q58 |
| H05 | M3 | An isogenic cell line panel for sequence-based screening of targeted anticancer... (title truncated) | https://www.cell.com/iscience/fulltext/S2589-0042(22)00708-8 | Q61 |
| H06 | M3 | Gene isoforms as expression-based biomarkers predictive of drug response in vi... (title truncated) | https://www.nature.com/articles/s41467-017-01153-8 | Q61 |
| H07 | M1 | The Allelic Context of the C797S Mutation Acq... (title truncated) | https://aacrjournals.org/clincancerres/article/21/17/3924/117742/The-Allelic-Context-of-the-C797S-Mutation-Acq | Q62 |
| H08 | M1 | GPX1 confers resistance to metabolic stress in BCR/ABL-T315I mutant chronic my... (title truncated) | https://www.nature.com/articles/s41420-025-02502-z | Q62 |
| H09 | M2 | Deep Mutational Scanning Reveals EGFR Mutations Conferring Resistance to the 4... (title truncated) | https://www.biorxiv.org/content/10.1101/2025.03.31.646429.full.pdf | Q92 |
| H10 | M2 | Saturation mutagenesis identifies activating and resistance-inducing FGFR kina... (title truncated) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12807871/ | Q92 |
| H11 | M1 | Variability within rare cell states enables multiple paths towards drug resist... (title truncated) | https://www.biorxiv.org/content/10.1101/2020.03.18.996660v2.full | Q95 |
| H12 | M1 | Optimal dosing of anti-cancer treatment under drug-induced plasticity | https://arxiv.org/pdf/2412.16391 | Q95 |
| H13 | M2 | Drug-tolerant persister cells in cancer: bridging the gaps between bench and b... (title truncated) | https://www.nature.com/articles/s41467-025-66376-6 | Q96 |
| H14 | M1 | Clonal dynamics shaped by diverse drug-tolerant persister states in melanoma r... (title truncated) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12458950/ | Q96 |
| H15 | M1 | Machine-guided cell-fate engineering | https://www.biorxiv.org/content/10.1101/2022.10.14.512279.full.pdf | Q97 |
| H16 | M1 | Multi-objective optimization reveals time- and dose-dependent inflammatory cytokine-mediated regulation of human stem cell derived cardiomyocyte... (title truncated) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8795204/ | Q97 |
| H17 | M3 | Accelerating cell culture media development using Bayesian optimization-based... (title truncated) | https://www.nature.com/articles/s41467-025-61113-5 | Q97 |
| H18 | M2 | Generative modeling of single-cell gene expression for dose-dependent chemical... (title truncated) | https://www.cell.com/patterns/fulltext/S2666-3899(23)00186-1 | Q66 |
| H19 | M1 | STRAND: Sequence-Conditioned Transport for Single-Cell Perturbations | https://arxiv.org/pdf/2602.10156 | Q64 |
| H20 | M3 | SCREP: Towards Single-Cell Drug Response Prediction by Pharmacogenomic Embeddi... (title truncated) | https://www.biorxiv.org/content/10.1101/2024.04.25.591050.full.pdf | Q67 |
| H21 | M1 | A knowledge-driven framework for predicting single-cell responses for unprofiled drugs (MAP; title truncated in the result) | https://www.nature.com/articles/s42256-026-01286-w | Q82 |
| H22 | M1 | Chem2Gen-Bench: Benchmarking Chemical-to-Genetic Translation in Perturbation... (title truncated) | https://arxiv.org/pdf/2606.21109 | Q85 |
| H23 | M2 | PRiMeFlow: Capturing Complex Expression Heterogeneity in Perturbation Response Modelling | https://arxiv.org/pdf/2604.13986 | Q47 |
| H24 | M2 | DeMixPert: Decomposed Response Modeling with Gaussian Mixtures for OOD Single-cell... (title truncated) | https://arxiv.org/pdf/2608.23114 | Q111 |
| H25 | M2 | CellRFT: Reinforcement Fine-Tuning for Single-Cell Perturbation Modeling | https://arxiv.org/pdf/2609.19970 | Q47 |
| H26 | M1 | CellxPert: Inference-Time MCMC Steering of a Multi-Omics Single-Cell Foundation Model for In-Silico Perturbation | https://arxiv.org/pdf/2605.00930 | Q46 |
| H27 | M3 | Cell reprogramming design by transfer learning of functional transcriptional networks | https://www.pnas.org/doi/10.1073/pnas.2312942121 | Q55 |
| H28 | M1 | Escaping Local Optima in the Waddington Landscape: A Multi-Stage TRPO–... (title truncated) | https://arxiv.org/html/2510.13018v1 | Q90 |
| H29 | M1 | Optimizing sequential gene expression modulation for cellular reprogra... (title truncated) | https://www.biorxiv.org/content/10.1101/2024.03.19.585672v1.full | Q90 |
| H30 | M1 | Generative Inverse Design with Abstention via Diagonal Flow Matching | https://www.researchgate.net/publication/402612678_Generative_Inverse_Design_with_Abstention_via_Diagonal_Flow_Matching | Q48 |
| H31 | M1 | Getting Your Guidance Weights Right in diffusion and flow-matching posterior sampling | https://arxiv.org/abs/2610.03503 | Q109 |
| H32 | M1 | On the Guidance of Flow Matching | https://arxiv.org/abs/2502.02150 | Q109 |
| H33 | M1 | ESS-Flow: Training-free guidance of flow-based models as inference in source space | https://arxiv.org/html/2510.05849 | Q109 |
| H34 | M1 | ParetoTransport: Generative Optimization by Mass Transport Toward The Paret... (title truncated) | https://arxiv.org/pdf/2609.07706 | Q109 |
| H35 | M2 | In Vivo Time-Resolved Single-Cell RNA-Seq Reveals Chemotherapy-Induced... (title truncated) | https://pubs.acs.org/doi/10.1021/acs.analchem.4c05648 | Q87 |
| H36 | M3 | Molecular causality in the advent of foundation models | https://arxiv.org/pdf/2401.09558 | Q88 |
| H37 | M1 | Tracking biological hallucinations in single-cell perturbation predictions | https://www.biorxiv.org/content/10.1101/2025.06.23.661046.full.pdf | Q98 |
| H38 | M2 | The Metric Picks the Winner: Evaluation Choice Flips Model Rankings fo... (title truncated) | https://arxiv.org/pdf/2606.12639 | Q80 |
| H39 | M3 | Benchmarking methods for inferring single-cell transcription factor activity usi... (title truncated) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13584069/ | Q101 |
| H40 | M1 | Uncertainty-aware transcription factor activity and perturbation inference witho... (title truncated) | https://www.biorxiv.org/content/10.1101/2025.10.05.680506.full.pdf | Q101 |
<!-- hold-table:end -->

The held items most likely to change the design if their full text were readable are H15 (machine-guided cell-fate engineering), H26 (inference-time steering), H30 (abstention in inverse design), H34 (multi-objective transport, relevant to selective killing) and H07 (allelic context of a resistance mutation), because each bears directly on insights I2, I6 or I9 of document 09.

> 如果全文可读，最可能改变设计的被搁置条目是 H15（机器引导的细胞命运工程）、H26（推理时引导）、H30（逆向设计中的弃权）、H34（多目标传输，与选择性杀伤相关）和 H07（耐药突变的等位基因背景），因为它们各自直接关系到文档 09 的启示 I2、I6 或 I9。

### 10.2 Rejected groups (5) / 被拒绝的结果组（5）

<!-- reject-table:start -->
| Group | Examples seen | Queries | Reason (EN) | 原因（中文） |
|---|---|---|---|---|
| G1 | Dflow-SUR (aerodynamics), Conditional Flow Matching for ML-Based Inverse Design Problems, How well do generative models solve inverse problems? A benchmark study, surrogate models for blood flow and implosions | Q48, Q112 | not about cells, drugs or genetic variation; the guidance ideas reach this project through the included papers (WM28, WM39, WM40) | 与细胞、药物或遗传变异无关；引导思想通过已纳入的论文（WM28、WM39、WM40）到达本项目 |
| G2 | patent documents on BCR-ABL mutations, CD34+ expansion media and SF3B1 splice variants | Q61, Q62, Q104 | no peer-reviewed content; claims cannot be verified | 没有同行评议内容；主张无法核实 |
| G3 | CD34+ cell enumeration by flow cytometry, label-free CD34+ identification, CD44 knockout in CD34+ cells | Q49, Q104 | shared keywords only; no link to design or genotype | 只是关键词相同；与设计或基因型无关 |
| G4 | massively parallel reporter assays of cortical-structure regulatory activity and general MPRA reviews | Q93 | no drug, hormone or other perturbation arm, so no genotype-by-treatment content | 没有药物、激素或其他扰动组，因此没有基因型×处理的内容 |
| G5 | Medium, EmergentMind, LearnOpenCV, Pith and ResearchGate copies, and X summaries other than WM30 | Q53, Q110, Q113 | secondary copies of papers that are already ledgered or cited through the primary page | 已入账或通过一手页面引用的论文的二手副本 |
<!-- reject-table:end -->

Rejected groups are results that share keywords with the topic but carry no mechanism or modeling content for it.

> 被拒绝的组是与主题共享关键词、但对其不含机理或建模内容的结果。

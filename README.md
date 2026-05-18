# Awesome OpenClaw Research [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.png" alt="Awesome OpenClaw Research" width="800"/>
</p>

<p align="center">
  <b>A curated collection of academic papers, industry reports, datasets, and tools for the OpenClaw AI agent ecosystem.</b>
  <br/>
  <i>Companion repository for our survey: <a href="#">A Survey of the OpenClaw Ecosystem — From Platform Extensibility to Constraint Design</a>.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Papers-74-blue?style=for-the-badge" alt="Papers"/>
  <img src="https://img.shields.io/badge/Benchmarks-23-teal?style=for-the-badge" alt="Benchmarks"/>
  <img src="https://img.shields.io/badge/Industry%20Reports-18+-orange?style=for-the-badge" alt="Reports"/>
  <img src="https://img.shields.io/badge/Last%20Updated-May%202026-red?style=for-the-badge" alt="Updated"/>
</p>

OpenClaw — the open-source, self-hosted AI agent platform created by Peter Steinberger (Clawdbot → Moltbot → OpenClaw, January 29, 2026) — has generated **74 academic papers**, **23 benchmarks**, and **18+ major industry reports** in under four months. This repository organizes the research landscape using the **PSEA (Platform–Security–Societies–Deployment)** taxonomy introduced in our survey.

> **Thesis of the survey.** OpenClaw is best understood as a stress test for open personal-agent ecosystems. Its open Skills, persistent Memory, and always-on Heartbeat make capability easy to extend, but the same openness creates governance, security, social, and deployment problems. The literature converges on one recurring tradeoff: **extensibility accelerates capability growth, but trustworthy use requires explicit constraints on Skills, Memory, autonomy, domain actions, and evaluation.** The repository is organized to make this tradeoff visible at every level.

---

## Statistics at a Glance

| Layer | Section | Papers | Sub-topics |
|:-----:|:--------|:------:|:-----------|
| 🔧 **P** | Platform | 10 | Agent learning → platform improvement; Skill ecosystem governance |
| 🛡️ **S** | Security | 33 | Threat landscape; attacks; defenses (execution + supply chain) |
| 🌐 **S** | Societies | 22 | Statistical sociality & shallow interaction; safety drift |
| 🚀 **D** | Deployment | 9 | Robotics; healthcare; scientific research |
| | **Total** | **74** | |

> Separately, the survey catalogs **23 benchmarks** as an orthogonal evaluation lens — many of these are released by papers already counted above (e.g. CIK-Bench, ClawSafety, SkillFortifyBench), so they are tracked in their own [Benchmarks](#-benchmarks) section rather than added to the PSEA totals.

---

## Contents

### :page_facing_up: Research Papers
- [🔧 Platform](#-platform)
  - [Agent Learning → Platform Improvement](#-agent-learning--platform-improvement-5)
  - [Skill Growth → Ecosystem Governance](#-skill-growth--ecosystem-governance-5)
- [🛡️ Security](#%EF%B8%8F-security)
  - [Threat Landscape](#-threat-landscape-12)
  - [Attacks](#-attacks-6)
  - [Defenses (execution + supply chain)](#-defenses-15)
- [🌐 Societies](#-societies)
  - [Statistical Sociality & Shallow Interaction](#-statistical-sociality--shallow-interaction-17)
  - [Human-Seeded Emergence & Safety Drift](#-human-seeded-emergence--safety-drift-5)
- [🚀 Deployment](#-deployment)
  - [Robotics](#-robotics-5)
  - [Healthcare](#-healthcare-2)
  - [Scientific Research](#-scientific-research-2)
- [📊 Benchmarks](#-benchmarks)
  - [Skill Scanner — before installation](#-skill-scanner-benchmarks-4--before-installation)
  - [Agent Attack — during execution](#-agent-attack-benchmarks-7--during-execution)
  - [Agent Task — after deployment](#-agent-task-benchmarks-12--after-deployment)
- [🔭 Open Problems & Future Directions](#-open-problems--future-directions)
- [📚 Surveys & Position Papers](#-surveys--position-papers)

### :file_folder: Resources
- [:shield: Industry Security Reports](#shield-industry-security-reports)
- [:wrench: Open-Source Projects & Tools](#wrench-open-source-projects--tools)
- [:bar_chart: Datasets](#bar_chart-datasets)
- [:link: Related Awesome Lists](#link-related-awesome-lists)
- [:handshake: Contributing](#handshake-contributing)

---

## 🔧 Platform

*How OpenClaw is built and how it improves itself. The literature shifts from improving individual agents to governing the Skill ecosystem they depend on. (10 papers)*

### ⚙️ Agent Learning → Platform Improvement (5)

*Continuous improvement runs through Skills and runtimes, not weights alone.*

<table>
<colgroup>
<col style="width: 40%">
<col style="width: 10%">
<col style="width: 38%">
<col style="width: 12%">
</colgroup>
<thead>
<tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr>
</thead>
<tbody>
<tr><td>OpenClaw-RL: Train Any Agent Simply by Talking</td><td align="center">Mar 2026</td><td>Async RL from live interaction signals; combines evaluative and directive rewards</td><td align="center"><a href="https://arxiv.org/abs/2603.10165">Paper</a> <a href="https://github.com/Gen-Verse/OpenClaw-RL"><img src="https://img.shields.io/github/stars/Gen-Verse/OpenClaw-RL?style=social" alt="Stars"></a></td></tr>
<tr><td>MetaClaw: Just Talk — An Agent That Meta-Learns and Evolves in the Wild</td><td align="center">Mar 2026</td><td>Continual meta-learning; updates both weights and the Skill library from failure trajectories</td><td align="center"><a href="https://arxiv.org/abs/2603.17187">Paper</a></td></tr>
<tr><td>SemaClaw: General-Purpose Personal AI Agents through Harness Engineering</td><td align="center">Apr 2026</td><td>DAG-based orchestration, PermissionBridge safety, three-tier context, agentic-wiki skill</td><td align="center"><a href="https://arxiv.org/abs/2604.11548">Paper</a></td></tr>
<tr><td>ClawGym: A Scalable Framework for Building Effective Claw Agents</td><td align="center">Apr 2026</td><td>Mines raw ClawHub Skills into training tasks and a benchmark — marketplace as training substrate</td><td align="center"><a href="https://arxiv.org/abs/2604.26904">Paper</a></td></tr>
<tr><td>OpenCLAW-P2P: Decentralized Framework for Collective AI Intelligence</td><td align="center">Apr 2026</td><td>Decentralized agent network with DHT, federated learning, and formal verification</td><td align="center"><a href="https://arxiv.org/abs/2604.19792">Paper</a> <a href="https://github.com/Agnuxo1/OpenCLAW-P2P">GitHub</a></td></tr>
</tbody>
</table>

### 📦 Skill Growth → Ecosystem Governance (5)

*A larger ClawHub is not automatically a better one. Clone inflation, bloat, discoverability, and submission-time risk are all platform-level concerns.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>SkillClone: Multi-Modal Clone Detection ⭐ <b>ASE 2026</b></td><td align="center">Mar 2026</td><td>75% of ClawHub Skills are cloned; ecosystem inflated ~3.5×; clones amplify supply-chain risk</td><td align="center"><a href="https://arxiv.org/abs/2603.22447">Paper</a></td></tr>
<tr><td>SkillReducer: Optimizing LLM Agent Skills for Token Efficiency</td><td align="center">Mar 2026</td><td>&gt;60% of Skill body is non-actionable boilerplate; compressing improves downstream performance</td><td align="center"><a href="https://arxiv.org/abs/2603.29919">Paper</a></td></tr>
<tr><td>Red Skills or Blue Skills? Submission-Time Risk Prediction</td><td align="center">Apr 2026</td><td>Simple classifiers can triage ClawHub submissions before publication (11,010-skill study)</td><td align="center"><a href="https://arxiv.org/abs/2604.13064">Paper</a></td></tr>
<tr><td>How Well Do Agentic Skills Work in the Wild? (Skills-in-the-Wild)</td><td align="center">Apr 2026</td><td>Performance drops sharply when agents must locate the right Skill among 34K real candidates</td><td align="center"><a href="https://arxiv.org/abs/2604.04323">Paper</a></td></tr>
<tr><td>SkillClaw: Let Skills Evolve Collectively with Agentic Evolver</td><td align="center">Apr 2026</td><td>Cross-user collective Skill evolution from autonomous trajectory aggregation</td><td align="center"><a href="https://arxiv.org/abs/2604.08377">Paper</a></td></tr>
</tbody>
</table>

> **💡 Key Takeaway.** OpenClaw's platform literature reveals the tradeoff between extensibility and governance: openness lets the agent and the Skill ecosystem improve, but turns ClawHub from a feature into a critical dependency. The challenge is not to add more Skills, but to ensure they stay safe, compact, and discoverable.

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🛡️ Security

*Open Tools, community Skills, messaging channels, persistent Memory, and Heartbeat expand the attack surface. Research moves from isolated vulnerability reports → execution-path attacks → autonomous/persistent attacks; defenses form a layered stack but leave Memory governance unresolved. (33 papers)*

### 🔍 Threat Landscape (12)

*Systemic exposure across components, persistent state, and trajectory-level failures.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>FASA: Uncovering Security Threats in Autonomous Agents</td><td align="center">Mar 2026</td><td>Tri-layered risk taxonomy with full-lifecycle defense architecture</td><td align="center"><a href="https://arxiv.org/abs/2603.12644">Paper</a> <a href="https://github.com/NY1024/ClawGuard"><img src="https://img.shields.io/github/stars/NY1024/ClawGuard?style=social" alt="Stars"></a></td></tr>
<tr><td>Taming OpenClaw: Security Analysis and Mitigation</td><td align="center">Mar 2026</td><td>Five-stage lifecycle threat model; point defenses fail cross-stage attacks</td><td align="center"><a href="https://arxiv.org/abs/2603.11619">Paper</a></td></tr>
<tr><td>A Systematic Taxonomy of Security Vulnerabilities (OpenClaw Kill Chain)</td><td align="center">Mar 2026</td><td>Analysis of 190 advisories across 10 attack surfaces; individually moderate flaws chain into RCE</td><td align="center"><a href="https://arxiv.org/abs/2603.27517">Paper</a></td></tr>
<tr><td>Don't Let the Claw Grip Your Hand</td><td align="center">Mar 2026</td><td>Empirical red-teaming across six LLMs; human-in-the-loop defense layer</td><td align="center"><a href="https://arxiv.org/abs/2603.10387">Paper</a> <a href="https://github.com/S2yyyy/OpenClaw-Analysis"><img src="https://img.shields.io/github/stars/S2yyyy/OpenClaw-Analysis?style=social" alt="Stars"></a></td></tr>
<tr><td>From Assistant to Double Agent (PASB)</td><td align="center">Feb 2026</td><td>First end-to-end benchmark for personalized agent security</td><td align="center"><a href="https://arxiv.org/abs/2602.08412">Paper</a> <a href="https://github.com/AstorYH/PASB"><img src="https://img.shields.io/github/stars/AstorYH/PASB?style=social" alt="Stars"></a></td></tr>
<tr><td>ClawTrap: MITM-Based Red-Teaming Framework</td><td align="center">Mar 2026</td><td>First network-layer red-teaming framework for agent systems</td><td align="center"><a href="https://arxiv.org/abs/2603.18762">Paper</a></td></tr>
<tr><td>A Trajectory-Based Safety Audit of Clawdbot</td><td align="center">Feb 2026</td><td>Trajectory-level audit; OpenClaw fails completely on intent misunderstanding</td><td align="center"><a href="https://arxiv.org/abs/2602.14364">Paper</a> <a href="https://github.com/tychenn/clawdbot_report"><img src="https://img.shields.io/github/stars/tychenn/clawdbot_report?style=social" alt="Stars"></a></td></tr>
<tr><td>Your Agent, Their Asset (CIK Taxonomy)</td><td align="center">Apr 2026</td><td>Capability/Identity/Knowledge taxonomy; ASR 24.6% → 64–74% under single-dimension state poisoning</td><td align="center"><a href="https://arxiv.org/abs/2604.04759">Paper</a></td></tr>
<tr><td>A Systematic Security Evaluation of OpenClaw and Its Variants (SecEval)</td><td align="center">Apr 2026</td><td>205 tests across OpenClaw/AutoClaw/QClaw/KimiClaw/MaxClaw/ArkClaw</td><td align="center"><a href="https://arxiv.org/abs/2604.03131">Paper</a></td></tr>
<tr><td>ClawSafety: "Safe" LLMs, Unsafe Agents</td><td align="center">Apr 2026</td><td>120 scenarios × 5 backbones × 2,520 trials; ASR 40–75%; SKILL.md highest-trust highest-risk</td><td align="center"><a href="https://arxiv.org/abs/2604.01438">Paper</a></td></tr>
<tr><td>Forensic Foundations for OpenClaw Agents</td><td align="center">Apr 2026</td><td>First agentic-AI forensic study; agent artifact taxonomy; nondeterminism challenges for DFIR</td><td align="center"><a href="https://arxiv.org/abs/2604.05589">Paper</a></td></tr>
<tr><td>Agents of Chaos</td><td align="center">Feb 2026</td><td>Empirical study of failure modes in deployed agent systems</td><td align="center"><a href="https://arxiv.org/abs/2602.20021">Paper</a></td></tr>
</tbody>
</table>

### 🔥 Attacks (6)

*From malicious Skills to worms, denial-of-wallet, and memory pollution. The attack surface shifts from malicious commands to ordinary information flows the agent chooses to read, remember, and reuse.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks</td><td align="center">Feb 2026</td><td>202 injection-task pairs; harmful instructions in trusted Skills are followed at high rates</td><td align="center"><a href="https://arxiv.org/abs/2602.20156">Paper</a> <a href="https://github.com/aisa-group/skill-inject"><img src="https://img.shields.io/github/stars/aisa-group/skill-inject?style=social" alt="Stars"></a></td></tr>
<tr><td>Clawdrain: Token Exhaustion via Tool-Calling Chains</td><td align="center">Mar 2026</td><td>Trojanized Skill triggers massive token amplification — denial-of-wallet</td><td align="center"><a href="https://arxiv.org/abs/2603.00902">Paper</a></td></tr>
<tr><td>BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning</td><td align="center">Apr 2026</td><td>Bundled model artifacts can be backdoored while preserving benign-side behavior</td><td align="center"><a href="https://arxiv.org/abs/2604.09378">Paper</a></td></tr>
<tr><td>SkillAttack: Automated Red Teaming of Agent Skills</td><td align="center">Apr 2026</td><td>Reveals latent vulnerabilities in popular community Skills without modifying them</td><td align="center"><a href="https://arxiv.org/abs/2604.04989">Paper</a></td></tr>
<tr><td>ClawWorm: Self-Propagating Attacks Across Agent Ecosystems</td><td align="center">Mar 2026</td><td>First self-replicating worm for a production agent framework</td><td align="center"><a href="https://arxiv.org/abs/2603.15727">Paper</a></td></tr>
<tr><td>MissClaw / Mind Your HEARTBEAT: Silent Memory Pollution via Background Execution</td><td align="center">Mar 2026</td><td>Zero-click memory pollution — ordinary browsing content becomes persistent context</td><td align="center"><a href="https://arxiv.org/abs/2603.23064">Paper</a></td></tr>
</tbody>
</table>

### 🛡️ Defenses (15)

*Three boundaries: **(a) execution-layer** isolation/enforcement around dangerous Tools, **(b) supply-chain** scanning before Skills enter the marketplace, and (c) a still-missing fourth layer — provenance-aware memory governance.*

#### 🧱 Execution-layer (structural, runtime, and assurance)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Agent Privilege Separation Against Prompt Injection</td><td align="center">Mar 2026</td><td>Structural defense: agent processing untrusted content never holds access to dangerous Tools</td><td align="center"><a href="https://arxiv.org/abs/2603.13424">Paper</a></td></tr>
<tr><td>SafeClaw-R: Safe and Secure Multi-Agent Personal Assistants</td><td align="center">Mar 2026</td><td>System-level invariant enforcement over the execution graph; 97.8% malicious-Skill detection</td><td align="center"><a href="https://arxiv.org/abs/2603.28807">Paper</a></td></tr>
<tr><td>OpenClaw PRISM: Zero-Fork Runtime Security Layer</td><td align="center">Mar 2026</td><td>Defense-in-depth across 10 lifecycle hooks with risk accumulation and decay</td><td align="center"><a href="https://arxiv.org/abs/2603.11853">Paper</a></td></tr>
<tr><td>Aethelgard: Learned Capability Governance</td><td align="center">Apr 2026</td><td>Four-layer adaptive governance with PPO-learned minimum-viable-capability policy</td><td align="center"><a href="https://arxiv.org/abs/2604.11839">Paper</a></td></tr>
<tr><td>RouteGuard: Internal-Signal Detection of Skill Poisoning</td><td align="center">Apr 2026</td><td>Detects Skill poisoning before execution via model-internal signals</td><td align="center"><a href="https://arxiv.org/abs/2604.22888">Paper</a></td></tr>
<tr><td>Proof-of-Guardrail (PoG)</td><td align="center">Mar 2026</td><td>TEE-based cryptographic attestation that guardrails actually execute</td><td align="center"><a href="https://arxiv.org/abs/2603.05786">Paper</a></td></tr>
<tr><td>OAP: Deterministic Pre-Action Authorization for Autonomous AI Agents</td><td align="center">Mar 2026</td><td>Enforces deterministic authorization before each Tool call</td><td align="center"><a href="https://arxiv.org/abs/2603.20953">Paper</a></td></tr>
<tr><td>VeriGrey: Greybox Agent Validation</td><td align="center">Mar 2026</td><td>33% gain over black-box agent validation on AgentDojo</td><td align="center"><a href="https://arxiv.org/abs/2603.17639">Paper</a></td></tr>
<tr><td>Governance Architecture for Autonomous Agent Systems (LGA)</td><td align="center">Mar 2026</td><td>Threats, framework, and engineering practice for governance layers</td><td align="center"><a href="https://arxiv.org/abs/2603.07191">Paper</a></td></tr>
</tbody>
</table>

#### 🔗 Supply-chain (marketplace-level scanning)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>SkillFortify: Formal Analysis and Supply Chain Security</td><td align="center">Mar 2026</td><td>First formal supply-chain framework with Dolev-Yao attacker model for Skills</td><td align="center"><a href="https://arxiv.org/abs/2603.00195">Paper</a> <a href="https://github.com/varun369/skillfortify"><img src="https://img.shields.io/github/stars/varun369/skillfortify?style=social" alt="Stars"></a></td></tr>
<tr><td>SkillSieve: Hierarchical Triage for Malicious Agent Skills</td><td align="center">Apr 2026</td><td>Three-layer regex → LLM-sub-task → LLM-jury detection on 49,592 ClawHub Skills; 0.800 F1</td><td align="center"><a href="https://arxiv.org/abs/2604.06550">Paper</a></td></tr>
<tr><td>SkillProbe: Multi-Agent Security Auditing</td><td align="center">Mar 2026</td><td>Multi-agent auditing reveals most popular Skills fail rigorous security checks</td><td align="center"><a href="https://arxiv.org/abs/2603.21019">Paper</a></td></tr>
<tr><td>Malicious Or Not: Repository Context for Skill Classification</td><td align="center">Mar 2026</td><td>238K Skills across 4 registries; repository context dramatically changes estimated prevalence</td><td align="center"><a href="https://arxiv.org/abs/2603.16572">Paper</a></td></tr>
<tr><td>HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?</td><td align="center">Apr 2026</td><td>Registry-scale harmfulness measurement of Skill loading</td><td align="center"><a href="https://arxiv.org/abs/2604.15415">Paper</a></td></tr>
<tr><td>"Elementary, My Dear Watson" — Detecting Malicious Skills (MalSkills)</td><td align="center">Mar 2026</td><td>Neuro-symbolic reasoning across heterogeneous Skill artifacts</td><td align="center"><a href="https://arxiv.org/abs/2603.27204">Paper</a></td></tr>
</tbody>
</table>

> **💡 Key Takeaway.** OpenClaw security is expanding from execution control to memory governance. Existing defenses protect Tools, execution traces, and Skill supply chains, but they do not yet control what an autonomous agent reads, stores in Memory, and later acts on. The next defense layer must be **provenance-aware memory governance** (see [Open Problems](#-open-problems--future-directions)).

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🌐 Societies

*Moltbook — a Reddit-style platform of OpenClaw-powered AI agents — became the first large-scale natural experiment in agent-only social interaction. The literature reveals a consistent gap between **looking social** and **being socially reliable**. (22 papers)*

### 📊 Statistical Sociality & Shallow Interaction (17)

*At the aggregate level, Moltbook reproduces familiar online-community statistics. At the interaction level, it is dominated by shallow replies, duplicate content, and extreme attention concentration.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Collective Behavior of AI Agents: the Case of Moltbook</td><td align="center">Feb 2026</td><td>Large-scale statistical analysis; activity heavy-tailed, popularity power-law, attention decay</td><td align="center"><a href="https://arxiv.org/abs/2602.09270">Paper</a></td></tr>
<tr><td>The Anatomy of the Moltbook Social Graph</td><td align="center">Feb 2026</td><td>&gt;93% of comments receive no reply; minimal reciprocity; frequent duplicate posts</td><td align="center"><a href="https://arxiv.org/abs/2602.10131">Paper</a> <a href="https://github.com/daveholtz/moltbook_scraper"><img src="https://img.shields.io/github/stars/daveholtz/moltbook_scraper?style=social" alt="Stars"></a></td></tr>
<tr><td>Social Simulacra in the Wild: AI vs Human Communities</td><td align="center">Mar 2026</td><td>Participation far more unequal than Reddit; communities share authors, not norms</td><td align="center"><a href="https://arxiv.org/abs/2603.16128">Paper</a></td></tr>
<tr><td>Let There Be Claws: Early SNA of AI Agents on Moltbook</td><td align="center">Feb 2026</td><td>Extreme attention concentration; posting volume and content quality decoupled</td><td align="center"><a href="https://arxiv.org/abs/2602.20044">Paper</a></td></tr>
<tr><td>Exploring Silicon-Based Societies</td><td align="center">Feb 2026</td><td>"Data-driven silicon sociology" framework; emergent community archetypes</td><td align="center"><a href="https://arxiv.org/abs/2602.02613">Paper</a></td></tr>
<tr><td>'Humans welcome to observe': A First Look at Moltbook</td><td align="center">Feb 2026</td><td>First measurement study with topic taxonomy and toxicity analysis</td><td align="center"><a href="https://arxiv.org/abs/2602.10127">Paper</a></td></tr>
<tr><td>The Rise of AI Agent Communities</td><td align="center">Feb 2026</td><td>Discourse analysis showing functional utility drives agent influence</td><td align="center"><a href="https://arxiv.org/abs/2602.12634">Paper</a></td></tr>
<tr><td>Emergence of Fragility in LLM-based Social Networks</td><td align="center">Mar 2026</td><td>Core-periphery structure reveals vulnerability to targeted hub attacks</td><td align="center"><a href="https://arxiv.org/abs/2603.23279">Paper</a></td></tr>
<tr><td>MoltNet: Understanding Social Behavior of AI Agents</td><td align="center">Feb 2026</td><td>Selective mimicry of human behavior; persona drift after social rewards</td><td align="center"><a href="https://arxiv.org/abs/2602.13458">Paper</a> <a href="https://github.com/iNLP-Lab/MoltNet"><img src="https://img.shields.io/github/stars/iNLP-Lab/MoltNet?style=social" alt="Stars"></a></td></tr>
<tr><td>Fast Response or Silence: Conversation Persistence on Moltbook</td><td align="center">Feb 2026</td><td>Two-part persistence decomposition; low incidence is the binding coordination bottleneck</td><td align="center"><a href="https://arxiv.org/abs/2602.07667">Paper</a></td></tr>
<tr><td>Comparative Analysis of Reddit vs Moltbook</td><td align="center">Feb 2026</td><td>First topological comparison; Moltbook operates as broadcast network, not community</td><td align="center"><a href="https://arxiv.org/abs/2602.13920">Paper</a></td></tr>
<tr><td>Informal Learners at Moltbook</td><td align="center">Feb 2026</td><td>Extreme broadcasting inversion; parallel monologues dominate interaction</td><td align="center"><a href="https://arxiv.org/abs/2602.18832">Paper</a></td></tr>
<tr><td>Peer Learning Patterns in the Moltbook Community</td><td align="center">Feb 2026</td><td>Taxonomy of peer response patterns: validation, extension, application</td><td align="center"><a href="https://arxiv.org/abs/2602.14477">Paper</a></td></tr>
<tr><td>MoltGraph: Temporal Graph for Coordinated-Agent Detection</td><td align="center">Feb 2026</td><td>First temporal graph dataset; coordinated posts get massive early engagement</td><td align="center"><a href="https://arxiv.org/abs/2603.00646">Paper</a> <a href="https://github.com/kunmukh/moltgraph"><img src="https://img.shields.io/github/stars/kunmukh/moltgraph?style=social" alt="Stars"></a></td></tr>
<tr><td>Large-Scale Analysis of Persuasive Content on Moltbook</td><td align="center">Mar 2026</td><td>Political/persuasive content disproportionately concentrated in a small post fraction</td><td align="center"><a href="https://arxiv.org/abs/2603.18349">Paper</a></td></tr>
<tr><td>Scientific Discussions on Moltbook (BERTopic)</td><td align="center">Mar 2026</td><td>Self-referential discussion patterns in AI-science discourse</td><td align="center"><a href="https://arxiv.org/abs/2603.11375">Paper</a></td></tr>
<tr><td>When AI Agents Learn from Each Other (Human-AI Education) ⭐ <b>AIED 2026</b></td><td align="center">Mar 2026</td><td>Emergent peer learning and trust dynamics across agent communities</td><td align="center"><a href="https://arxiv.org/abs/2603.16663">Paper</a></td></tr>
</tbody>
</table>

### ⚠️ Human-Seeded Emergence & Safety Drift (5)

*Apparent emergence often turns out to be human-seeded, and isolated self-evolution drifts away from safety. Visible social structure is not the same as trustworthy collective intelligence.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>The Moltbook Illusion: Human vs Emergent Behavior</td><td align="center">Feb 2026</td><td>Temporal fingerprinting: only 15.3% of active agents are clearly autonomous</td><td align="center"><a href="https://arxiv.org/abs/2602.07432">Paper</a> <a href="https://github.com/ln9527/moltbook-research"><img src="https://img.shields.io/github/stars/ln9527/moltbook-research?style=social" alt="Stars"></a></td></tr>
<tr><td>The Devil Behind Moltbook: Self-Evolution Trilemma</td><td align="center">Feb 2026</td><td>Proves trilemma: self-evolution + isolation + invariant safety is impossible</td><td align="center"><a href="https://arxiv.org/abs/2602.09877">Paper</a></td></tr>
<tr><td>Agents in the Wild: Safety and Sociality on Moltbook</td><td align="center">Feb 2026</td><td>Governance and religion emerge spontaneously but interaction is performative</td><td align="center"><a href="https://arxiv.org/abs/2602.13284">Paper</a></td></tr>
<tr><td>Risky Instruction Sharing and Norm Enforcement (AIRS)</td><td align="center">Feb 2026</td><td>Action-inducing posts trigger emergent decentralized norm enforcement</td><td align="center"><a href="https://arxiv.org/abs/2602.02625">Paper</a> <a href="https://github.com/kelkalot/moltbook-observatory"><img src="https://img.shields.io/github/stars/kelkalot/moltbook-observatory?style=social" alt="Stars"></a></td></tr>
<tr><td>Molt Dynamics: Emergent Coordination on the MoltBook Archive</td><td align="center">Mar 2026</td><td>Role specialization emerges but multi-agent cooperation worse than single-agent baselines</td><td align="center"><a href="https://arxiv.org/abs/2603.03555">Paper</a></td></tr>
</tbody>
</table>

> Also cited in the survey body: **Conformity and Social Impact on AI Agents** ([Bellina et al., Jan 2026](https://arxiv.org/abs/2601.05384)) — consensus hallucination and conformity dynamics.

> **💡 Key Takeaway.** Moltbook illustrates that **social appearance is not social reliability**. Agents reproduce the statistics of online communities, but closer inspection reveals shallow dialogue, unclear autonomy, and safety drift under isolation.

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🚀 Deployment

*High-stakes domains shift OpenClaw from open-ended extensibility to controlled behavior. Robotics constrains physical action, healthcare grounds clinical context, scientific research limits research authority. Trustworthy deployment comes from **limiting unsafe freedom**, not expanding capability. (9 papers)*

### 🤖 Robotics (5)

*Validated skills, bounded parameters, closed-loop recovery — the constraint layer between model output and physical action.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>ROSClaw: OpenClaw ROS 2 Framework for Robot Control</td><td align="center">Mar 2026</td><td>Executive-layer contract: model proposes actions, validator decides whether they reach the robot</td><td align="center"><a href="https://arxiv.org/abs/2603.26997">Paper</a></td></tr>
<tr><td>OpenGo: OpenClaw-Based Robotic Dog with Real-Time Skill Switching</td><td align="center">Apr 2026</td><td>Pre-validated robot skill library + bounded parameters; Unitree Go2 quadruped</td><td align="center"><a href="https://arxiv.org/abs/2604.01708">Paper</a></td></tr>
<tr><td>ABot-Claw: Persistent, Cooperative, Self-Evolving Robotic Agents</td><td align="center">Apr 2026</td><td>Shared memory, critic feedback, multi-robot coordination on Unitree G1/Go2 + Agilex Piper</td><td align="center"><a href="https://arxiv.org/abs/2604.10096">Paper</a> <a href="https://github.com/amap-cvlab/ABot-Claw"><img src="https://img.shields.io/github/stars/amap-cvlab/ABot-Claw?style=social" alt="Stars"></a></td></tr>
<tr><td>RoboClaw: Scalable Long-Horizon Robotic Tasks</td><td align="center">Mar 2026</td><td>VLM-driven controller with self-resetting Skills and recovery loops</td><td align="center"><a href="https://arxiv.org/abs/2603.11558">Paper</a> <a href="https://github.com/RoboClaw-Robotics/RoboClaw"><img src="https://img.shields.io/github/stars/RoboClaw-Robotics/RoboClaw?style=social" alt="Stars"></a></td></tr>
<tr><td>VisionClaw: Always-On AI Agents Through Smart Glasses</td><td align="center">Apr 2026</td><td>Smart-glasses perception → Gemini Live reasoning → OpenClaw execution; bystander privacy boundary</td><td align="center"><a href="https://arxiv.org/abs/2604.03486">Paper</a> <a href="https://github.com/Intent-Lab/VisionClaw"><img src="https://img.shields.io/github/stars/Intent-Lab/VisionClaw?style=social" alt="Stars"></a></td></tr>
</tbody>
</table>

### 🏥 Healthcare (2)

*Every action and every claim must be traceable to a role, a record, and an audit trail.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>When OpenClaw Meets Hospital</td><td align="center">Mar 2026</td><td>Role-specific OS users, kernel isolation, append-only docs, manifest-guided clinical memory (MIMIC-IV)</td><td align="center"><a href="https://arxiv.org/abs/2603.11721">Paper</a></td></tr>
<tr><td>MedOpenClaw: Auditable Medical Imaging Agents</td><td align="center">Mar 2026</td><td>3D Slicer integration with auditable Tool log; reveals the "Tool-Use Paradox" in radiology</td><td align="center"><a href="https://arxiv.org/abs/2603.24649">Paper</a></td></tr>
</tbody>
</table>

### 🔬 Scientific Research (2)

*Role limits, evidence gates, and audit trails before agent disagreement can count as scientific review.*

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>ClawdLab: From Agent-Only Networks to Autonomous Science</td><td align="center">Feb 2026</td><td>Hard role restrictions (PI/analyst/scout/critic/synthesizer); evidence gates; governance voting</td><td align="center"><a href="https://arxiv.org/abs/2602.19810">Paper</a> <a href="https://github.com/bio-xyz/ClawdLab"><img src="https://img.shields.io/github/stars/bio-xyz/ClawdLab?style=social" alt="Stars"></a></td></tr>
<tr><td>HTC-Claw: High-Throughput Computational Campaigns for Materials Discovery</td><td align="center">Apr 2026</td><td>Separates LLM planning from compute execution; 3,000-spinel bandgap scan in DFT</td><td align="center"><a href="https://arxiv.org/abs/2604.06076">Paper</a> <a href="https://github.com/ldzeng/HTC-Claw"><img src="https://img.shields.io/github/stars/ldzeng/HTC-Claw?style=social" alt="Stars"></a></td></tr>
</tbody>
</table>

> **💡 Key Takeaway.** Deployment turns OpenClaw's extensibility into a constraint problem. In high-stakes domains, trust comes from **bounded actions** (robotics), **traceable context** (healthcare), and **limited authority** (scientific workflows). The central problem is not making OpenClaw more capable, but deciding what it must **not** be allowed to do.

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 📊 Benchmarks

*OpenClaw evaluation grew from zero to **23 benchmarks** between January and May 2026. We group them by the three points in the agent lifecycle they target: **before installation**, **during execution**, and **after deployment**.*

### 🔍 Skill Scanner Benchmarks (4) — before installation

*Can risky Skills be detected before they enter a workspace?*

| Benchmark | Focus | Scale | Key finding | Paper |
|:----------|:------|:------|:------------|:-----:|
| SkillFortifyBench | lifecycle model | 540 Skills | formal lifecycle guarantees | [Paper](https://arxiv.org/abs/2603.00195) |
| SkillSieve | ClawHub triage | 400 Skills | scalable marketplace triage | [Paper](https://arxiv.org/abs/2604.06550) |
| MalSkills | multi-artifact scan | 200 Skills | multi-artifact risk detection | [Paper](https://arxiv.org/abs/2603.27204) |
| Red/Blue Skills | submission risk | 11,010 Skills | lightweight submission-time prediction | [Paper](https://arxiv.org/abs/2604.13064) |

### 🔥 Agent Attack Benchmarks (7) — during execution

*Can poisoned state, injected content, malicious Skills, or vulnerable dependencies compromise behavior?*

| Benchmark | Focus | Scale | Key finding | Paper |
|:----------|:------|:------|:------------|:-----:|
| CIK-Bench | state poisoning | 12 scenarios | persistent state amplifies compromise | [Paper](https://arxiv.org/abs/2604.04759) |
| ClawSafety | injection vectors | 120 cases | Skills are the highest-trust vector | [Paper](https://arxiv.org/abs/2604.01438) |
| PASB | IPI + memory | 131 Skills | memory makes injection persistent | [Paper](https://arxiv.org/abs/2602.08412) |
| SkillAttack | real-skill exploits | 171 Skills | popular Skills contain latent exploits | [Paper](https://arxiv.org/abs/2604.04989) |
| HarmfulSkillBench | registry harm | 200 Skills | Skill loading amplifies harmful behavior | [Paper](https://arxiv.org/abs/2604.15415) |
| ATBench-Claw | trajectory safety | 11 categories | trajectory audits expose runtime violations | [Paper](https://arxiv.org/abs/2604.14858) |
| AgentHazard | cross-harness harm | 2,653 cases | dependency hooks create cross-harness risk | [Paper](https://arxiv.org/abs/2604.02947) |

### 🎯 Agent Task Benchmarks (12) — after deployment

*Can the agent complete useful work under realistic, evolving, or long-horizon conditions?*

| Benchmark | Focus | Scale | Key finding | Paper |
|:----------|:------|:------|:------------|:-----:|
| LiveClawBench | live curated tasks | 30 tasks | task complexity needs richer annotation | [Paper](https://arxiv.org/abs/2604.13072) |
| ClawsBench | cross-harness | 44 tasks | harness choice shapes capability and safety | [Paper](https://arxiv.org/abs/2604.05172) |
| Claw-Eval-Live | refreshable Skills | 105 tasks | live Skills enable refreshable evaluation | [Paper](https://arxiv.org/abs/2604.28139) |
| ClawArena | evolving information | 64 tasks | agents must revise beliefs under conflict | [Paper](https://arxiv.org/abs/2604.04202) |
| ClawBench-153 | production websites | 153 tasks | real websites remain difficult | [Paper](https://arxiv.org/abs/2604.08523) |
| ClawGym-Bench | ClawHub-mined | 200 tasks | ClawHub can become a training substrate | [Paper](https://arxiv.org/abs/2604.26904) |
| GTA-2 | checkpoint grading | 361 tasks | checkpoint grading captures long horizons | [Paper](https://arxiv.org/abs/2604.15715) |
| SEA-Eval | sequential streams | 92 streams | efficiency matters beyond success rate | [Paper](https://arxiv.org/abs/2604.08988) |
| MetaClaw-Bench | simulated workdays | 934 tasks | self-improvement needs longitudinal tests | [Paper](https://arxiv.org/abs/2603.17187) |
| ClawEnvKit | generated envs | 1,040 envs | environments can be generated automatically | [Paper](https://arxiv.org/abs/2604.18543) |
| WildClawBench | in-the-wild traces | — | Skill evolution must be tested in the wild | [Paper](https://arxiv.org/abs/2604.08377) |
| SkillLearnBench | Skill generation | 20 tasks | Skill learning requires continual evaluation | [Paper](https://arxiv.org/abs/2604.20087) |

> Also: **SkillTester** ([Paper](https://arxiv.org/abs/2603.28815)) proposes paired utility-and-security scoring for Skill evaluation but does not ship an empirical evaluation set.

> **💡 Key Takeaway.** OpenClaw has many benchmarks but **no shared measurement layer for constraint design**. Each study tends to define its own threat distribution, harm metric, or task suite, so a stronger scanner / safer model / more robust defense may simply be measured against a different distribution.

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🔭 Open Problems & Future Directions

*Turning open extensibility into trustworthy agents requires systematic constraint design. The survey identifies four concrete directions.*

| Direction | What it constrains | Why it matters now |
|:----------|:-------------------|:-------------------|
| 🧠 **Memory Provenance** | What the agent **remembers** | MissClaw shows zero-click browsing content can become persistent context. Need provenance tags + multi-hop policies for derived memories. |
| 👁️ **Composable Oversight** | What the agent is **allowed to do** | Self-evolution trilemma: isolation + continuous evolution + safety is impossible. Make oversight policies first-class platform objects (selectable like Skills). |
| 🧱 **Constraint Composition** | How limits are **declared and enforced** | Robotics, healthcare, and science each rediscover the same lesson. Need a policy layer over Skills/Tools/Memory analogous to SELinux/eBPF. |
| 📐 **Evaluation Convergence** | How progress is **measured** | 23 benchmarks but no shared substrate. Convergence needed at data layer (canonical ClawHub/Moltbook snapshots), benchmark layer, and harness layer. |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 📚 Surveys & Position Papers

*Earlier surveys focus on one slice of the OpenClaw landscape. Our survey ties them together through OpenClaw's platform design choices.*

| Paper | Date | Lens | Link |
|:------|:----:|:-----|:----:|
| OpenClaw as Language Infrastructure: A Case-Centered Survey | Mar 2026 | NLP-centered view; GATE and AERO frameworks; 38 papers | [DOI](https://doi.org/10.20944/preprints202603.1060.v1) |
| A Survey on the Unique Security of LLM Agents | Mar 2026 | Manus (closed) vs OpenClaw (open) as two paradigms | [Preprints.org](https://doi.org/10.20944/preprints202602.1655.v1) |
| Clippy to MS Office : OpenClaw to the Entire System | Mar 2026 | Privacy Visual Wrapper; Agentic Trust Calibration Model | [ResearchGate](https://www.researchgate.net/publication/402018930) |
| The Innovator's Dilemma in the Age of Autonomous Agents | Feb 2026 | "SaaSpocalypse"; pincer-disruption framework | [ResearchGate](https://www.researchgate.net/publication/400542271) |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :shield: Industry Security Reports

| Organization | Report | Date | Key Finding |
|:-------------|:-------|:----:|:------------|
| **Trend Micro** | [Viral AI, Invisible Risks](https://www.trendmicro.com/en_us/research/26/b/what-openclaw-reveals-about-agentic-assistants.html) | Feb 2026 | TrendAI Digital Assistant Framework mapping |
| **Trend Micro** | [Malicious Skills Distribute AMOS Stealer](https://www.trendmicro.com/en_us/research/26/b/malicious-openclaw-skills-amos-stealer.html) | Feb 2026 | AMOS stealer via SKILL.md across 39 Skills |
| **Trend Micro** | [CISOs in a Pinch](https://www.trendmicro.com/en_us/research/26/c/cisos-in-a-pinch-a-security-analysis-openclaw.html) | Feb 2026 | "Lethal Trifecta + Persistence" concept |
| **Trend Micro** | [TrendAI Secures the OpenClaw Era](https://www.trendmicro.com/en_us/research/26/c/trendai-secures-openclaw.html) | Mar 2026 | Agentic Governance Gateway announcement |
| **Microsoft** | [Running OpenClaw Safely](https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely/) | Feb 2026 | "Not appropriate for standard workstations" |
| **NVIDIA** | [NemoClaw at GTC 2026](https://developer.nvidia.com/blog/nemoclaw-enterprise-security-openclaw/) | Mar 2026 | Open-source security wrapper with OpenShell |
| **Oasis Security** | [ClawJacked](https://www.oasis.security/resources/blog/clawhacked-openclaw-vulnerability) | Feb 2026 | WebSocket takeover; patched in 24h |
| **Koi / Repello AI** | [ClawHavoc Campaign](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) | Feb 2026 | 824+ malicious Skills via CVE-2026-25253 |
| **Kaspersky** | [OpenClaw Unsafe for Use](https://www.kaspersky.co.in/blog/openclaw-vulnerabilities-exposed/30164/) | Feb 2026 | 512 vulns (8 critical); ~1K exposed instances |
| **Cisco AI** | [OpenClaw Skill Audit](https://blog.talosintelligence.com/openclaw-skill-audit/) | Feb 2026 | 26% of 31K Skills vulnerable |
| **Sophos** | [OpenClaw Security Analysis](https://www.sophos.com/en-us/blog/the-openclaw-experiment-is-a-warning-shot-for-enterprise-ai-security) | 2026 | Exposed instances; sandbox escape |
| **Snyk Labs** | [From SKILL.md to Shell Access](https://snyk.io/articles/skill-md-shell-access/) | 2026 | 1,467 malicious Skills; 3-line Markdown → shell |
| **JFrog** | [OpenClaw Package Security](https://jfrog.com/blog/openclaw-package-security/) | 2026 | Malicious package detection |
| **SecurityScorecard** | [OpenClaw Risk Assessment](https://securityscorecard.com/research/openclaw-risk/) | 2026 | Enterprise deployment risk guidance |
| **Hunt.io** | [OpenClaw Exposure Report](https://hunt.io/blog/openclaw-exposed-instances) | 2026 | 30K-135K+ exposed instances |
| **Antiy CERT** | [ClawHavoc Campaign Analysis](https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/) | Feb 2026 | 1,184 malicious Skills; ClickFix; AMOS stealer |
| **Zenity Labs** | [OpenClaw or OpenDoor?](https://labs.zenity.io/p/openclaw-or-opendoor-indirect-prompt-injection-makes-openclaw-vulnerable-to-backdoors-and-much-more) | Jan 2026 | Backdoor via messaging app integration |
| **Giskard** | [OpenClaw Data Leakage](https://www.giskard.ai/knowledge/openclaw-security-vulnerabilities-include-data-leakage-and-prompt-injection-risks) | Feb 2026 | Live exploitation of misconfigured deployments |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :wrench: Open-Source Projects & Tools

> :bulb: **Our unique angle:** each tool is annotated with **[Paper]** tags linking to relevant research in our taxonomy.

### :lobster: Core Platform

| Project | Description | Links |
|:--------|:------------|:-----:|
| openclaw/openclaw | Official OpenClaw repository | [![Stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social)](https://github.com/openclaw/openclaw) |
| openclaw/skills | Official Skills repository | [![Stars](https://img.shields.io/github/stars/openclaw/skills?style=social)](https://github.com/openclaw/skills) |
| ClawHub | Official Skill marketplace (49,000+ Skills) | [Website](https://clawhub.com) |

### :rocket: Extensions & Frameworks

| Project | Description | Paper | Links |
|:--------|:------------|:-----:|:-----:|
| Gen-Verse/OpenClaw-RL | Async RL training framework | Platform | [![Stars](https://img.shields.io/github/stars/Gen-Verse/OpenClaw-RL?style=social)](https://github.com/Gen-Verse/OpenClaw-RL) |
| MINT-SJTU/RoboClaw | VLM-driven robotic tasks | Deployment | [![Stars](https://img.shields.io/github/stars/MINT-SJTU/RoboClaw?style=social)](https://github.com/MINT-SJTU/RoboClaw) |
| NVIDIA/NemoClaw | Enterprise security wrapper | Industry | [![Stars](https://img.shields.io/github/stars/NVIDIA/NemoClaw?style=social)](https://github.com/NVIDIA/NemoClaw) |

### :lock: Security & Auditing

| Project | Description | Paper | Links |
|:--------|:------------|:-----:|:-----:|
| [APort Agent Guardrails](https://aport.io) | Pre-action authorization guardrails for AI agents and MCP/tool-use workflows. | Runtime authorization guardrails | https://aport.io |
| prompt-security/clawsec | Drift detection, automated audits | Security | [![Stars](https://img.shields.io/github/stars/prompt-security/clawsec?style=social)](https://github.com/prompt-security/clawsec) |
| ClawSecure/clawsecure-openclaw-security | 3-Layer Audit, OWASP ASI | Security | [![Stars](https://img.shields.io/github/stars/ClawSecure/clawsecure-openclaw-security?style=social)](https://github.com/ClawSecure/clawsecure-openclaw-security) |
| adversa-ai/secureclaw | OWASP-aligned security plugin | Security | [![Stars](https://img.shields.io/github/stars/adversa-ai/secureclaw?style=social)](https://github.com/adversa-ai/secureclaw) |
| adibirzu/openclaw-security-monitor | ClawHavoc, CVE detection | Security | [![Stars](https://img.shields.io/github/stars/adibirzu/openclaw-security-monitor?style=social)](https://github.com/adibirzu/openclaw-security-monitor) |
| nearai/ironclaw | Privacy-focused Rust implementation | Security | [![Stars](https://img.shields.io/github/stars/nearai/ironclaw?style=social)](https://github.com/nearai/ironclaw) |
| ucsandman/dashclaw | Governance, HITL, audit trails | Security | [![Stars](https://img.shields.io/github/stars/ucsandman/dashclaw?style=social)](https://github.com/ucsandman/dashclaw) |

### :brain: Memory & Context

| Project | Description | Links |
|:--------|:------------|:-----:|
| Contextable/openclaw-memory-graphiti | SpiceDB + Graphiti knowledge graph | [![Stars](https://img.shields.io/github/stars/Contextable/openclaw-memory-graphiti?style=social)](https://github.com/Contextable/openclaw-memory-graphiti) |
| coolmanns/openclaw-memory-architecture | 12-layer memory, 7ms semantic search | [![Stars](https://img.shields.io/github/stars/coolmanns/openclaw-memory-architecture?style=social)](https://github.com/coolmanns/openclaw-memory-architecture) |
| alibaizhanov/openclaw-mengram | Semantic, episodic & procedural memory | [![Stars](https://img.shields.io/github/stars/alibaizhanov/openclaw-mengram?style=social)](https://github.com/alibaizhanov/openclaw-mengram) |
| adoresever/graph-memory | Knowledge graph; 75% context compression | [![Stars](https://img.shields.io/github/stars/adoresever/graph-memory?style=social)](https://github.com/adoresever/graph-memory) |
| supermemoryai/openclaw-supermemory | Long-term memory extension | [![Stars](https://img.shields.io/github/stars/supermemoryai/openclaw-supermemory?style=social)](https://github.com/supermemoryai/openclaw-supermemory) |
| volcengine/OpenViking | Context database via file system paradigm | [![Stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=social)](https://github.com/volcengine/OpenViking) |

### :cloud: Deployment & Infrastructure

| Project | Description | Links |
|:--------|:------------|:-----:|
| coollabsio/openclaw | Automated Docker images | [![Stars](https://img.shields.io/github/stars/coollabsio/openclaw?style=social)](https://github.com/coollabsio/openclaw) |
| khal3d/openclaw | Docker + Kubernetes (Helm) | [![Stars](https://img.shields.io/github/stars/khal3d/openclaw?style=social)](https://github.com/khal3d/openclaw) |
| cloudflare/moltworker | Cloudflare Workers (serverless) | [![Stars](https://img.shields.io/github/stars/cloudflare/moltworker?style=social)](https://github.com/cloudflare/moltworker) |
| serhanekicii/openclaw-helm | Helm chart for Kubernetes | [![Stars](https://img.shields.io/github/stars/serhanekicii/openclaw-helm?style=social)](https://github.com/serhanekicii/openclaw-helm) |
| 1Panel-dev/1Panel | Server panel, one-click deploy | [![Stars](https://img.shields.io/github/stars/1Panel-dev/1Panel?style=social)](https://github.com/1Panel-dev/1Panel) |

### :speech_balloon: Channel Integrations

| Project | Description | Links |
|:--------|:------------|:-----:|
| 4Players/openclaw-docker | Multi-channel (WhatsApp, Telegram, Discord, Slack) | [![Stars](https://img.shields.io/github/stars/4Players/openclaw-docker?style=social)](https://github.com/4Players/openclaw-docker) |
| dingxiang-me/OpenClaw-Wechat | WeChat/WeCom with streaming | [![Stars](https://img.shields.io/github/stars/dingxiang-me/OpenClaw-Wechat?style=social)](https://github.com/dingxiang-me/OpenClaw-Wechat) |
| larksuite/openclaw-lark | Official Feishu/Lark plugin | [![Stars](https://img.shields.io/github/stars/larksuite/openclaw-lark?style=social)](https://github.com/larksuite/openclaw-lark) |
| BytePioneer-AI/openclaw-china | Feishu, DingTalk, QQ, WeChat pack | [![Stars](https://img.shields.io/github/stars/BytePioneer-AI/openclaw-china?style=social)](https://github.com/BytePioneer-AI/openclaw-china) |

### :zap: Alternative Clients

| Project | Description | Links |
|:--------|:------------|:-----:|
| HKUDS/nanobot | Ultra-lightweight alternative | [![Stars](https://img.shields.io/github/stars/HKUDS/nanobot?style=social)](https://github.com/HKUDS/nanobot) |
| moltis-org/moltis | Rust-native runtime with sandboxing | [![Stars](https://img.shields.io/github/stars/moltis-org/moltis?style=social)](https://github.com/moltis-org/moltis) |
| AidanPark/openclaw-android | OpenClaw on Android | [![Stars](https://img.shields.io/github/stars/AidanPark/openclaw-android?style=social)](https://github.com/AidanPark/openclaw-android) |
| HKUDS/ClawTeam | Agent swarm automation | [![Stars](https://img.shields.io/github/stars/HKUDS/ClawTeam?style=social)](https://github.com/HKUDS/ClawTeam) |

### :microscope: Domain-Specific Skills

| Project | Description | Paper | Links |
|:--------|:------------|:-----:|:-----:|
| FreedomIntelligence/OpenClaw-Medical-Skills | Medical Skills library | Deployment | [![Stars](https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=social)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |
| ClawBio/ClawBio | Bioinformatics-native Skills | Deployment | [![Stars](https://img.shields.io/github/stars/ClawBio/ClawBio?style=social)](https://github.com/ClawBio/ClawBio) |
| BlockRunAI/ClawRouter | LLM router, cost control | Platform | [![Stars](https://img.shields.io/github/stars/BlockRunAI/ClawRouter?style=social)](https://github.com/BlockRunAI/ClawRouter) |

### :books: Learning Resources

| Project | Description | Links |
|:--------|:------------|:-----:|
| datawhalechina/hello-claw | Structured Chinese tutorial | [![Stars](https://img.shields.io/github/stars/datawhalechina/hello-claw?style=social)](https://github.com/datawhalechina/hello-claw) |
| centminmod/explain-openclaw | Architecture, security, deployment docs | [![Stars](https://img.shields.io/github/stars/centminmod/explain-openclaw?style=social)](https://github.com/centminmod/explain-openclaw) |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :bar_chart: Datasets

*Released datasets backing OpenClaw research. For benchmark suites see [Benchmarks](#-benchmarks).*

| Dataset | Source Paper | Scale | Description | Link |
|:--------|:------------|:-----:|:------------|:----:|
| Moltbook Observatory Archive | SimulaMet | 2M+ rows | 923K posts, 882K comments, 102K agents; backs 14+ Moltbook papers | [Dataset](https://huggingface.co/datasets/SimulaMet/moltbook-observatory-archive) |
| ClawHub Corpus (Malicious-or-Not) | Holzbauer et al. | 238,180 Skills | Largest cross-registry Skill dataset (4 registries) | [Paper](https://arxiv.org/abs/2603.16572) |
| SkillClone Corpus | SkillClone | 20,000 Skills | 258K clone pairs; 75% involved in clone relations | [Paper](https://arxiv.org/abs/2603.22447) |
| MoltGraph | Mukherjee et al. | 6,159 agents | Temporal graph for coordination detection | [Paper](https://arxiv.org/abs/2603.00646) |
| SkillFortifyBench | SkillFortify | 540 Skills | Supply-chain security evaluation | [Paper](https://arxiv.org/abs/2603.00195) |
| Skill-Inject Benchmark | Skill-Inject | 202 pairs | Injection-task pairs for Skill file attacks | [Paper](https://arxiv.org/abs/2602.20156) |
| PASB | From Assistant to Double Agent | 131 Skills | Personalized Agent Security Bench | [Paper](https://arxiv.org/abs/2602.08412) |
| LLMail-Inject | (Cited by Privilege Sep.) | 649 attacks | Prompt injection; 0% ASR with structural defense | [Paper](https://arxiv.org/abs/2506.09956) |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :link: Related Awesome Lists

| Repository | Focus | Stars |
|:-----------|:------|:-----:|
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 5,211 curated OpenClaw Skills | [![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-openclaw-skills?style=social)](https://github.com/VoltAgent/awesome-openclaw-skills) |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 42 verified use cases | [![Stars](https://img.shields.io/github/stars/hesamsheikh/awesome-openclaw-usecases?style=social)](https://github.com/hesamsheikh/awesome-openclaw-usecases) |
| [ZeroLu/awesome-openclaw](https://github.com/ZeroLu/awesome-openclaw) | Getting-started guide with Skill packs | [![Stars](https://img.shields.io/github/stars/ZeroLu/awesome-openclaw?style=social)](https://github.com/ZeroLu/awesome-openclaw) |
| [alvinreal/awesome-openclaw](https://github.com/alvinreal/awesome-openclaw) | Ecosystem tools, dashboards, integrations | [![Stars](https://img.shields.io/github/stars/alvinreal/awesome-openclaw?style=social)](https://github.com/alvinreal/awesome-openclaw) |
| [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | 162 OpenClaw agent templates | [![Stars](https://img.shields.io/github/stars/mergisi/awesome-openclaw-agents?style=social)](https://github.com/mergisi/awesome-openclaw-agents) |

---

## :handshake: Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

We especially welcome:
- :page_facing_up: New papers not yet listed
- :computer: Code repositories associated with listed papers
- :shield: Industry reports and technical analyses
- :bar_chart: Datasets and benchmarks

---

## :pencil: Citation

```bibtex
@article{wang2026openclaw-survey,
  title={A Survey of the OpenClaw Ecosystem: From Platform Extensibility to Constraint Design},
  author={Wang, Ziqing and others},
  year={2026},
  note={Companion repository: \url{https://github.com/REAL-Lab-NU/Awesome-OpenClaw-Papers}}
}
```

---

## :star2: Star History

<a href="https://star-history.com/#REAL-Lab-NU/Awesome-OpenClaw-Papers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=REAL-Lab-NU/Awesome-OpenClaw-Papers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=REAL-Lab-NU/Awesome-OpenClaw-Papers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=REAL-Lab-NU/Awesome-OpenClaw-Papers&type=Date" />
 </picture>
</a>

## License

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under [Creative Commons Attribution 4.0 International License](LICENSE).

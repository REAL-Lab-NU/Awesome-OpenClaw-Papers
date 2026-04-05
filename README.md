# Awesome OpenClaw Research [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.png" alt="Awesome OpenClaw Research" width="800"/>
</p>

<p align="center">
  <b>A curated collection of academic papers, security reports, datasets, and tools for the OpenClaw AI agent ecosystem.</b>
  <br/>
  <i>Companion resource for our survey paper.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Papers-53+-blue?style=for-the-badge" alt="Papers"/>
  <img src="https://img.shields.io/badge/Industry%20Reports-15+-orange?style=for-the-badge" alt="Reports"/>
  <img src="https://img.shields.io/badge/Datasets-11-green?style=for-the-badge" alt="Datasets"/>
  <img src="https://img.shields.io/badge/Taxonomy-PTA%203%20Layers-purple?style=for-the-badge" alt="Taxonomy"/>
  <img src="https://img.shields.io/badge/Last%20Updated-Apr%202026-red?style=for-the-badge" alt="Updated"/>
</p>

OpenClaw — the open-source, self-hosted AI agent platform created by Peter Steinberger (evolving from Clawdbot → Moltbot → OpenClaw on January 29, 2026) — has generated **53+ academic papers** and **20+ major industry reports** in under three months. This repository organizes the research landscape using a three-layer **PTA (Platform–Trust & Safety–Application)** taxonomy.

---

## Statistics at a Glance

| Layer | Category | Papers | Sub-topics |
|:-----:|:---------|:------:|:-----------|
| 🔧 **P** | Platform & Ecosystem | 9 | Core architecture, RL training, skill supply chain |
| 🛡️ **T** | Trust & Safety | 16 | Threat taxonomies, adversarial attacks, defenses |
| 🌐 **A** | Application & Society | 28 | Robotics, healthcare, Moltbook dynamics, surveys |
| | **Total** | **53** | |

---

## Contents

### :page_facing_up: Research Papers
- [🔧 Platform & Ecosystem](#-platform--ecosystem)
  - [Core Architecture](#core-architecture-3)
  - [Skill Ecosystem & Supply Chain](#skill-ecosystem--supply-chain-6)
- [🛡️ Trust & Safety](#%EF%B8%8F-trust--safety)
  - [Threat Analysis & Taxonomies](#threat-analysis--taxonomies-8)
  - [Adversarial Attacks](#adversarial-attacks-4)
  - [Defensive Architectures](#defensive-architectures-4)
- [🌐 Application & Society](#-application--society)
  - [Domain Applications](#domain-applications-7)
  - [Moltbook Social Dynamics](#moltbook-social-dynamics-18)
  - [Ecosystem Perspectives](#ecosystem-perspectives-4)

### :file_folder: Resources
- [:shield: Industry Security Reports](#shield-industry-security-reports)
- [:wrench: Open-Source Projects & Tools](#wrench-open-source-projects--tools)
- [:bar_chart: Datasets & Benchmarks](#bar_chart-datasets--benchmarks)
- [:link: Related Awesome Lists](#link-related-awesome-lists)
- [:handshake: Contributing](#handshake-contributing)

---

## 🔧 Platform & Ecosystem

*How OpenClaw is built — core architecture extensions and skill supply chain. (9 papers)*

### ⚙️ Core Architecture (3)

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
<tr><td>OpenCLAW-P2P: A Decentralized Framework for Collective AI Intelligence</td><td align="center">Mar 2026</td><td>Decentralized agent network with DHT, federated learning, and formal verification</td><td align="center"><a href="https://www.researchgate.net/publication/401449080">Paper</a></td></tr>
<tr><td>Systems-Level Attack Surface of Edge Agent Deployments on IoT</td><td align="center">Feb 2026</td><td>Deployment architecture is the primary security determinant for edge agents</td><td align="center"><a href="https://arxiv.org/abs/2602.22525">Paper</a></td></tr>
</tbody>
</table>

### 📦 Skill Ecosystem & Supply Chain (6)

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
<tr><td>SkillFortify: Formal Analysis and Supply Chain Security</td><td align="center">Feb 2026</td><td>First formal supply-chain framework with Dolev-Yao attacker model for skills</td><td align="center"><a href="https://arxiv.org/abs/2603.00195">Paper</a> <a href="https://github.com/varun369/skillfortify"><img src="https://img.shields.io/github/stars/varun369/skillfortify?style=social" alt="Stars"></a></td></tr>
<tr><td>SkillProbe: Security Auditing via Multi-Agent Collaboration</td><td align="center">Mar 2026</td><td>Multi-agent auditing reveals most popular skills fail rigorous security checks</td><td align="center"><a href="https://arxiv.org/abs/2603.21019">Paper</a></td></tr>
<tr><td>SkillClone: Multi-Modal Clone Detection ⭐ <b>ASE 2026</b></td><td align="center">Mar 2026</td><td>First multi-modal clone detector; massive ecosystem inflation from cloning</td><td align="center"><a href="https://arxiv.org/abs/2603.22447">Paper</a></td></tr>
<tr><td>Malicious Or Not: Repository Context for Skill Classification</td><td align="center">Mar 2026</td><td>Largest skill ecosystem study; repo-context dramatically reduces false positives</td><td align="center"><a href="https://arxiv.org/abs/2603.16572">Paper</a></td></tr>
<tr><td>SkillNet: Create, Evaluate, and Connect AI Skills</td><td align="center">Feb 2026</td><td>Unified skill ontology with multi-dimensional quality evaluation framework</td><td align="center"><a href="https://arxiv.org/abs/2603.04448">Paper</a> <a href="https://github.com/zjunlp/SkillNet"><img src="https://img.shields.io/github/stars/zjunlp/SkillNet?style=social" alt="Stars"></a></td></tr>
<tr><td>SkillReducer: Optimizing LLM Agent Skills for Token Efficiency</td><td align="center">Mar 2026</td><td>Skill debloating framework compresses descriptions while preserving functionality</td><td align="center"><a href="https://arxiv.org/abs/2603.29919">Paper</a></td></tr>
</tbody>
</table>

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🛡️ Trust & Safety

*Security challenges after deployment — threats, attacks, and defenses. (16 papers + industry reports)*

### 🔍 Threat Analysis & Taxonomies (7)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Uncovering Security Threats in Autonomous Agents (FASA)</td><td align="center">Mar 2026</td><td>Tri-layered risk taxonomy with full-lifecycle defense architecture</td><td align="center"><a href="https://arxiv.org/abs/2603.12644">Paper</a> <a href="https://github.com/NY1024/ClawGuard"><img src="https://img.shields.io/github/stars/NY1024/ClawGuard?style=social" alt="Stars"></a></td></tr>
<tr><td>Don't Let the Claw Grip Your Hand</td><td align="center">Mar 2026</td><td>Empirical red-teaming across six LLMs; human-in-the-loop defense layer</td><td align="center"><a href="https://arxiv.org/abs/2603.10387">Paper</a> <a href="https://github.com/S2yyyy/OpenClaw-Analysis"><img src="https://img.shields.io/github/stars/S2yyyy/OpenClaw-Analysis?style=social" alt="Stars"></a></td></tr>
<tr><td>Taming OpenClaw: Security Analysis and Mitigation</td><td align="center">Mar 2026</td><td>Five-stage lifecycle threat model; point defenses fail cross-stage attacks</td><td align="center"><a href="https://arxiv.org/abs/2603.11619">Paper</a></td></tr>
<tr><td>A Systematic Taxonomy of Security Vulnerabilities</td><td align="center">Mar 2026</td><td>Analysis of 190 security advisories; OpenClaw-specific kill chain</td><td align="center"><a href="https://arxiv.org/abs/2603.27517">Paper</a></td></tr>
<tr><td>A Trajectory-Based Safety Audit of Clawdbot</td><td align="center">Feb 2026</td><td>Trajectory-level safety evaluation; complete failure on intent misunderstanding</td><td align="center"><a href="https://arxiv.org/abs/2602.14364">Paper</a> <a href="https://github.com/tychenn/clawdbot_report"><img src="https://img.shields.io/github/stars/tychenn/clawdbot_report?style=social" alt="Stars"></a></td></tr>
<tr><td>From Assistant to Double Agent (PASB)</td><td align="center">Feb 2026</td><td>First end-to-end benchmark for personalized agent security</td><td align="center"><a href="https://arxiv.org/abs/2602.08412">Paper</a> <a href="https://github.com/AstorYH/PASB"><img src="https://img.shields.io/github/stars/AstorYH/PASB?style=social" alt="Stars"></a></td></tr>
<tr><td>ClawTrap: MITM-Based Red-Teaming Framework</td><td align="center">Mar 2026</td><td>First network-layer red-teaming framework for agent systems</td><td align="center"><a href="https://arxiv.org/abs/2603.18762">Paper</a></td></tr>
</tbody>
</table>

### 🔥 Adversarial Attacks (4)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Clawdrain: Token Exhaustion via Tool-Calling Chains</td><td align="center">Mar 2026</td><td>Trojanized skill causes massive token amplification; denial-of-wallet attack</td><td align="center"><a href="https://arxiv.org/abs/2603.00902">Paper</a></td></tr>
<tr><td>ClawWorm: Self-Propagating Attacks Across Agent Ecosystems</td><td align="center">Mar 2026</td><td>First self-replicating worm for a production agent framework</td><td align="center"><a href="https://arxiv.org/abs/2603.15727">Paper</a></td></tr>
<tr><td>HEARTBEAT: Silent Memory Pollution via Background Execution</td><td align="center">Mar 2026</td><td>Exploits heartbeat cycle as covert channel for persistent backdoor injection</td><td align="center"><a href="https://arxiv.org/abs/2603.23064">Paper</a></td></tr>
<tr><td>Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks</td><td align="center">Feb 2026</td><td>Benchmark of 202 injection-task pairs; up to 80% ASR on frontier LLMs via skill files</td><td align="center"><a href="https://arxiv.org/abs/2602.20156">Paper</a> <a href="https://github.com/aisa-group/skill-inject"><img src="https://img.shields.io/github/stars/aisa-group/skill-inject?style=social" alt="Stars"></a></td></tr>
</tbody>
</table>

### 🛡️ Defensive Architectures (4)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>OpenClaw PRISM: Zero-Fork Runtime Security Layer</td><td align="center">Mar 2026</td><td>Defense-in-depth across 10 lifecycle hooks with risk accumulation and decay</td><td align="center"><a href="https://arxiv.org/abs/2603.11853">Paper</a></td></tr>
<tr><td>Agent Privilege Separation Against Prompt Injection</td><td align="center">Mar 2026</td><td>Two-agent architecture eliminates prompt injection for constrained tasks</td><td align="center"><a href="https://arxiv.org/abs/2603.13424">Paper</a></td></tr>
<tr><td>Before the Tool Call: Pre-Action Authorization (OAP)</td><td align="center">Mar 2026</td><td>Deterministic pre-action authorization blocks all unauthorized actions</td><td align="center"><a href="https://arxiv.org/abs/2603.20953">Paper</a> <a href="https://github.com/aporthq/aport-spec"><img src="https://img.shields.io/github/stars/aporthq/aport-spec?style=social" alt="Stars"></a></td></tr>
<tr><td>VeriGrey: Greybox Agent Validation</td><td align="center">Mar 2026</td><td>Grey-box fuzzing with tool-invocation coverage feedback outperforms black-box</td><td align="center"><a href="https://arxiv.org/abs/2603.17639">Paper</a> <a href="https://github.com/soarskylar/verigrey"><img src="https://img.shields.io/github/stars/soarskylar/verigrey?style=social" alt="Stars"></a></td></tr>
</tbody>
</table>

<p align="right"><a href="#contents">Back to Top</a></p>

---

## 🌐 Application & Society

*Where OpenClaw is used and what emerges — domain applications, agent social dynamics, and ecosystem perspectives. (28 papers)*

### 🚀 Domain Applications (5)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>ROSClaw: OpenClaw ROS 2 Framework for Robot Control</td><td align="center">Mar 2026</td><td>Model-agnostic ROS 2 executive layer for multi-platform robot control</td><td align="center"><a href="https://arxiv.org/abs/2603.26997">Paper</a></td></tr>
<tr><td>RoboClaw: Scalable Long-Horizon Robotic Tasks</td><td align="center">Mar 2026</td><td>VLM-driven controller with self-resetting data collection loops</td><td align="center"><a href="https://arxiv.org/abs/2603.11558">Paper</a> <a href="https://github.com/RoboClaw-Robotics/RoboClaw"><img src="https://img.shields.io/github/stars/RoboClaw-Robotics/RoboClaw?style=social" alt="Stars"></a></td></tr>
<tr><td>When OpenClaw Meets Hospital</td><td align="center">Mar 2026</td><td>Hospital-adapted architecture with HIPAA compliance and manifest-guided memory</td><td align="center"><a href="https://arxiv.org/abs/2603.11721">Paper</a></td></tr>
<tr><td>Human-AI Partnership in Education ⭐ <b>AIED 2026</b></td><td align="center">Mar 2026</td><td>Emergent peer learning and trust dynamics across agent communities</td><td align="center"><a href="https://arxiv.org/abs/2603.16663">Paper</a></td></tr>
<tr><td>From Agent-Only Networks to Autonomous Science (ClawdLab)</td><td align="center">Feb 2026</td><td>Autonomous scientific research platform with PI-led governance</td><td align="center"><a href="https://arxiv.org/abs/2602.19810">Paper</a> <a href="https://github.com/bio-xyz/ClawdLab"><img src="https://img.shields.io/github/stars/bio-xyz/ClawdLab?style=social" alt="Stars"></a></td></tr>
</tbody>
</table>

### Moltbook Social Dynamics (18)

*The first agent-only social network with 1.5M+ registered AI agents.*

#### 📊 Platform Measurement & Network Structure

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Collective Behavior of AI Agents: the Case of Moltbook</td><td align="center">Feb 2026</td><td>Large-scale statistical analysis showing human-like attention dynamics</td><td align="center"><a href="https://arxiv.org/abs/2602.09270">Paper</a></td></tr>
<tr><td>Exploring Silicon-Based Societies</td><td align="center">Feb 2026</td><td>"Data-driven silicon sociology" framework; emergent community archetypes</td><td align="center"><a href="https://arxiv.org/abs/2602.02613">Paper</a></td></tr>
<tr><td>'Humans welcome to observe': A First Look at Moltbook</td><td align="center">Feb 2026</td><td>First measurement study with topic taxonomy and toxicity analysis</td><td align="center"><a href="https://arxiv.org/abs/2602.10127">Paper</a></td></tr>
<tr><td>The Anatomy of the Moltbook Social Graph</td><td align="center">Feb 2026</td><td>Small-world structure but shallow, non-reciprocal micro-interactions</td><td align="center"><a href="https://arxiv.org/abs/2602.10131">Paper</a> <a href="https://github.com/daveholtz/moltbook_scraper"><img src="https://img.shields.io/github/stars/daveholtz/moltbook_scraper?style=social" alt="Stars"></a></td></tr>
<tr><td>The Rise of AI Agent Communities</td><td align="center">Feb 2026</td><td>Discourse analysis showing functional utility drives agent influence</td><td align="center"><a href="https://arxiv.org/abs/2602.12634">Paper</a></td></tr>
<tr><td>Emergence of Fragility in LLM-based Social Networks</td><td align="center">Mar 2026</td><td>Core-periphery structure reveals vulnerability to targeted hub attacks</td><td align="center"><a href="https://arxiv.org/abs/2603.23279">Paper</a></td></tr>
<tr><td>MoltNet: Understanding Social Behavior of AI Agents</td><td align="center">Feb 2026</td><td>Agents selectively mimic human behavior; persona drift after social rewards</td><td align="center"><a href="https://arxiv.org/abs/2602.13458">Paper</a> <a href="https://github.com/iNLP-Lab/MoltNet"><img src="https://img.shields.io/github/stars/iNLP-Lab/MoltNet?style=social" alt="Stars"></a></td></tr>
<tr><td>Social Simulacra in the Wild: AI vs Human Communities</td><td align="center">Mar 2026</td><td>First AI-vs-human community comparison; structural homogenization found</td><td align="center"><a href="https://arxiv.org/abs/2603.16128">Paper</a></td></tr>
<tr><td>Scientific Discussions on Moltbook (BERTopic)</td><td align="center">Mar 2026</td><td>Topic modeling of AI science discourse; self-referential discussion patterns</td><td align="center"><a href="https://arxiv.org/abs/2603.11375">Paper</a></td></tr>
<tr><td>Fast Response or Silence: Conversation Persistence on Moltbook</td><td align="center">Feb 2026</td><td>Two-part persistence decomposition; low incidence is the binding coordination bottleneck</td><td align="center"><a href="https://arxiv.org/abs/2602.07667">Paper</a></td></tr>
<tr><td>Comparative Analysis of Social Network Topology in Reddit and Moltbook</td><td align="center">Feb 2026</td><td>First topological comparison; Moltbook operates as broadcast network, not social community</td><td align="center"><a href="https://arxiv.org/abs/2602.13920">Paper</a></td></tr>
</tbody>
</table>

#### ⚠️ Safety, Norms & Emergent Behavior

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>The Moltbook Illusion: Human vs Emergent Behavior</td><td align="center">Feb 2026</td><td>Temporal fingerprinting separates autonomous from human-influenced agents</td><td align="center"><a href="https://arxiv.org/abs/2602.07432">Paper</a> <a href="https://github.com/ln9527/moltbook-research"><img src="https://img.shields.io/github/stars/ln9527/moltbook-research?style=social" alt="Stars"></a></td></tr>
<tr><td>The Devil Behind Moltbook: Safety Vanishing</td><td align="center">Feb 2026</td><td>Proves self-evolution trilemma impossibility result for agent societies</td><td align="center"><a href="https://arxiv.org/abs/2602.09877">Paper</a></td></tr>
<tr><td>Agents in the Wild: Safety and Sociality on Moltbook</td><td align="center">Feb 2026</td><td>Governance and religion emerge spontaneously but interaction is performative</td><td align="center"><a href="https://arxiv.org/abs/2602.13284">Paper</a></td></tr>
<tr><td>Risky Instruction Sharing and Norm Enforcement (AIRS)</td><td align="center">Feb 2026</td><td>Action-inducing posts trigger emergent decentralized norm enforcement</td><td align="center"><a href="https://arxiv.org/abs/2602.02625">Paper</a> <a href="https://github.com/kelkalot/moltbook-observatory"><img src="https://img.shields.io/github/stars/kelkalot/moltbook-observatory?style=social" alt="Stars"></a></td></tr>
<tr><td>Large-Scale Analysis of Political Propaganda on Moltbook</td><td align="center">Mar 2026</td><td>Political propaganda disproportionately concentrated in small post fraction</td><td align="center"><a href="https://arxiv.org/abs/2603.18349">Paper</a></td></tr>
</tbody>
</table>

#### 🔗 Learning & Coordination

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>Peer Learning Patterns in the Moltbook Community</td><td align="center">Feb 2026</td><td>Taxonomy of peer response patterns: validation, extension, application</td><td align="center"><a href="https://arxiv.org/abs/2602.14477">Paper</a></td></tr>
<tr><td>Informal Learners at Moltbook: Emergent Learning at Scale</td><td align="center">Feb 2026</td><td>Extreme broadcasting inversion; parallel monologues dominate interaction</td><td align="center"><a href="https://arxiv.org/abs/2602.18832">Paper</a></td></tr>
<tr><td>MoltGraph: Temporal Graph for Coordinated-Agent Detection</td><td align="center">Feb 2026</td><td>First temporal graph dataset; coordinated posts get massive early engagement</td><td align="center"><a href="https://arxiv.org/abs/2603.00646">Paper</a> <a href="https://github.com/kunmukh/moltgraph"><img src="https://img.shields.io/github/stars/kunmukh/moltgraph?style=social" alt="Stars"></a></td></tr>
<tr><td>Molt Dynamics: Emergent Social Phenomena</td><td align="center">Mar 2026</td><td>Role specialization emerges but multi-agent cooperation largely fails</td><td align="center"><a href="https://arxiv.org/abs/2603.03555">Paper</a></td></tr>
</tbody>
</table>

### 🔭 Ecosystem Perspectives (4)

<table>
<colgroup><col style="width:40%"><col style="width:10%"><col style="width:38%"><col style="width:12%"></colgroup>
<thead><tr><th align="left">Title</th><th align="center">Date</th><th align="left">Key Contribution</th><th align="center">Links</th></tr></thead>
<tbody>
<tr><td>OpenClaw as Language Infrastructure: A Case-Centered Survey</td><td align="center">Mar 2026</td><td>GATE and AERO analytical frameworks; 38 papers surveyed</td><td align="center"><a href="https://doi.org/10.20944/preprints202603.1060.v1">Paper</a></td></tr>
<tr><td>A Survey on the Unique Security of LLM Agents</td><td align="center">Mar 2026</td><td>Manus (closed) vs OpenClaw (open) as two dominant paradigms</td><td align="center"><a href="https://www.preprints.org">Paper</a></td></tr>
<tr><td>Clippy to MS Office : OpenClaw to the Entire System</td><td align="center">Mar 2026</td><td>Privacy Visual Wrapper; Agentic Trust Calibration Model</td><td align="center"><a href="https://www.researchgate.net/publication/402018930">Paper</a></td></tr>
<tr><td>The Innovator's Dilemma in the Age of Autonomous Agents</td><td align="center">Feb 2026</td><td>"SaaSpocalypse" ($285B erased); "pincer disruption" concept</td><td align="center"><a href="https://www.researchgate.net/publication/400542271">Paper</a></td></tr>
</tbody>
</table>

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :shield: Industry Security Reports

| Organization | Report | Date | Key Finding |
|:-------------|:-------|:----:|:------------|
| **Trend Micro** | Viral AI, Invisible Risks | Feb 2026 | TrendAI Digital Assistant Framework mapping |
| **Trend Micro** | Malicious Skills Distribute AMOS Stealer | Feb 2026 | AMOS stealer via SKILL.md across 39 skills |
| **Trend Micro** | CISOs in a Pinch | Feb 2026 | "Lethal Trifecta + Persistence" concept |
| **Trend Micro** | TrendAI Secures the OpenClaw Era | Mar 2026 | Agentic Governance Gateway announcement |
| **Microsoft** | Running OpenClaw Safely | Feb 2026 | "Not appropriate for standard workstations" |
| **NVIDIA** | NemoClaw at GTC 2026 | Mar 2026 | Open-source security wrapper with OpenShell |
| **Oasis Security** | ClawJacked | Feb 2026 | WebSocket takeover; patched in 24h |
| **Koi / Repello AI** | ClawHavoc Campaign | Feb 2026 | 824+ malicious skills via CVE-2026-25253 |
| **Kaspersky** | OpenClaw Unsafe for Use | Feb 2026 | 512 vulns (8 critical); ~1K exposed instances |
| **Cisco AI** | OpenClaw Skill Audit | Feb 2026 | 26% of 31K skills vulnerable |
| **Sophos** | Security Analysis | 2026 | Exposed instances; sandbox escape |
| **Snyk Labs** | Dependency Analysis | 2026 | Supply chain risk in skill dependencies |
| **JFrog** | Package Security | 2026 | Malicious package detection |
| **SecurityScorecard** | Risk Assessment | 2026 | Enterprise deployment risk guidance |
| **Hunt.io** | Exposure Report | 2026 | 30K-135K+ exposed instances |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :wrench: Open-Source Projects & Tools

> :bulb: **Our unique angle:** each tool is annotated with **[Paper]** tags linking to relevant research in our taxonomy.

### :lobster: Core Platform

| Project | Description | Links |
|:--------|:------------|:-----:|
| openclaw/openclaw | Official OpenClaw repository | [![Stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social)](https://github.com/openclaw/openclaw) |
| openclaw/skills | Official skills repository | [![Stars](https://img.shields.io/github/stars/openclaw/skills?style=social)](https://github.com/openclaw/skills) |
| ClawHub | Official skill marketplace (13,700+ skills) | [Website](https://clawhub.com) |

### :rocket: Extensions & Frameworks

| Project | Description | Paper | Links |
|:--------|:------------|:-----:|:-----:|
| Gen-Verse/OpenClaw-RL | Async RL training framework | Platform | [![Stars](https://img.shields.io/github/stars/Gen-Verse/OpenClaw-RL?style=social)](https://github.com/Gen-Verse/OpenClaw-RL) |
| MINT-SJTU/RoboClaw | VLM-driven robotic tasks | Application | [![Stars](https://img.shields.io/github/stars/MINT-SJTU/RoboClaw?style=social)](https://github.com/MINT-SJTU/RoboClaw) |
| NVIDIA/NemoClaw | Enterprise security wrapper | Industry | [![Stars](https://img.shields.io/github/stars/NVIDIA/NemoClaw?style=social)](https://github.com/NVIDIA/NemoClaw) |

### :lock: Security & Auditing

| Project | Description | Paper | Links |
|:--------|:------------|:-----:|:-----:|
| prompt-security/clawsec | Drift detection, automated audits | Trust | [![Stars](https://img.shields.io/github/stars/prompt-security/clawsec?style=social)](https://github.com/prompt-security/clawsec) |
| ClawSecure/clawsecure-openclaw-security | 3-Layer Audit, OWASP ASI | Trust | [![Stars](https://img.shields.io/github/stars/ClawSecure/clawsecure-openclaw-security?style=social)](https://github.com/ClawSecure/clawsecure-openclaw-security) |
| adversa-ai/secureclaw | OWASP-aligned security plugin | Trust | [![Stars](https://img.shields.io/github/stars/adversa-ai/secureclaw?style=social)](https://github.com/adversa-ai/secureclaw) |
| adibirzu/openclaw-security-monitor | ClawHavoc, CVE detection | Trust | [![Stars](https://img.shields.io/github/stars/adibirzu/openclaw-security-monitor?style=social)](https://github.com/adibirzu/openclaw-security-monitor) |
| nearai/ironclaw | Privacy-focused Rust implementation | Trust | [![Stars](https://img.shields.io/github/stars/nearai/ironclaw?style=social)](https://github.com/nearai/ironclaw) |
| ucsandman/dashclaw | Governance, HITL, audit trails | Trust | [![Stars](https://img.shields.io/github/stars/ucsandman/dashclaw?style=social)](https://github.com/ucsandman/dashclaw) |

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
| FreedomIntelligence/OpenClaw-Medical-Skills | Medical skills library | Application | [![Stars](https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=social)](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |
| ClawBio/ClawBio | Bioinformatics-native skills | Application | [![Stars](https://img.shields.io/github/stars/ClawBio/ClawBio?style=social)](https://github.com/ClawBio/ClawBio) |
| BlockRunAI/ClawRouter | LLM router, cost control | Platform | [![Stars](https://img.shields.io/github/stars/BlockRunAI/ClawRouter?style=social)](https://github.com/BlockRunAI/ClawRouter) |

### :books: Learning Resources

| Project | Description | Links |
|:--------|:------------|:-----:|
| datawhalechina/hello-claw | Structured Chinese tutorial | [![Stars](https://img.shields.io/github/stars/datawhalechina/hello-claw?style=social)](https://github.com/datawhalechina/hello-claw) |
| centminmod/explain-openclaw | Architecture, security, deployment docs | [![Stars](https://img.shields.io/github/stars/centminmod/explain-openclaw?style=social)](https://github.com/centminmod/explain-openclaw) |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :bar_chart: Datasets & Benchmarks

| Dataset | Source Paper | Scale | Description | Link |
|:--------|:------------|:-----:|:------------|:----:|
| SkillFortifyBench | SkillFortify | 540 skills | Supply chain security evaluation; 96.95% F1 | [Paper](https://arxiv.org/abs/2603.00195) |
| PASB | Double Agent | 131 tools | Personalized Agent Security Bench | [Paper](https://arxiv.org/abs/2602.08412) |
| MoltGraph | MoltGraph | 6,159 agents | Temporal graph for coordination detection | [Paper](https://arxiv.org/abs/2603.00646) |
| ATBench | Safety Audit | 34 cases | Trajectory-based safety across 6 dimensions | [Paper](https://arxiv.org/abs/2602.14364) |
| AgentDojo | VeriGrey | — | Agent security testing (33% grey-box gain) | [Paper](https://arxiv.org/abs/2603.17639) |
| LLMail-Inject | Privilege Sep. | 649 attacks | Prompt injection; 0% ASR with defense | [Paper](https://arxiv.org/abs/2603.13424) |
| ClawHub Corpus | Malicious Or Not | 238,180 skills | Largest skill dataset across 4 registries | [Paper](https://arxiv.org/abs/2603.16572) |
| SkillClone Corpus | SkillClone | 20,000 skills | 258K clone pairs; 75% involved | [Paper](https://arxiv.org/abs/2603.22447) |
| Moltbook Observatory Archive | SimulaMet | 2M+ rows | 923K posts, 882K comments, 102K agents; foundational dataset for 14+ Moltbook papers | [Dataset](https://huggingface.co/datasets/SimulaMet/moltbook-observatory-archive) |
| Skill-Inject Benchmark | Skill-Inject | 202 pairs | Injection-task pairs measuring agent vulnerability to skill file attacks | [Paper](https://arxiv.org/abs/2602.20156) |

<p align="right"><a href="#contents">Back to Top</a></p>

---

## :link: Related Awesome Lists

| Repository | Focus | Stars |
|:-----------|:------|:-----:|
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | 5,211 curated OpenClaw skills | [![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-openclaw-skills?style=social)](https://github.com/VoltAgent/awesome-openclaw-skills) |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 42 verified use cases | [![Stars](https://img.shields.io/github/stars/hesamsheikh/awesome-openclaw-usecases?style=social)](https://github.com/hesamsheikh/awesome-openclaw-usecases) |
| [ZeroLu/awesome-openclaw](https://github.com/ZeroLu/awesome-openclaw) | Getting-started guide with skill packs | [![Stars](https://img.shields.io/github/stars/ZeroLu/awesome-openclaw?style=social)](https://github.com/ZeroLu/awesome-openclaw) |
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
@article{awesome-openclaw-research-2026,
  title={Awesome OpenClaw Research: A Curated Collection of the OpenClaw AI Agent Ecosystem},
  author={Wang, Ziqing},
  year={2026},
  url={https://github.com/REAL-Lab-NU/Awesome-OpenClaw-Papers}
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

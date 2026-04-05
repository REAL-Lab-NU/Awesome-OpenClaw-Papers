# OpenClaw: A Comprehensive Survey of the Open-Source AI Agent Ecosystem

## Detailed Survey Paper Outline

**Target venue:** Top-tier conference or journal (S&P, CCS, USENIX Security, ACL, NeurIPS, or TIFS/TDSC)
**Language:** English
**Scope:** 48+ academic papers + 20+ industry reports (as of April 2026)

---

## 1. Introduction (~1.5 pages)

**Narrative arc:** The emergence of OpenClaw represents a unique case study — an open-source AI agent platform that generated an entire research ecosystem in under three months.

**Key points:**
- OpenClaw's genesis and naming evolution (Clawdbot → Moltbot → OpenClaw, Jan 29, 2026)
- Explosive research response: 48+ papers in ~10 weeks (unprecedented for any single AI system)
- The "preprint phenomenon": almost entire body of work remains unreviewed (exception: SkillClone at ASE 2026)
- Gap in existing literature: V1 survey covers 38 papers as of Mar 10; we cover significantly more with a different analytical lens

**Our contributions:**
1. A six-layer architecture-aligned taxonomy organizing the full research landscape
2. The first comprehensive survey covering all research streams (security, social dynamics, architecture, applications)
3. Cross-layer analysis revealing systemic patterns and dependencies
4. Identification of open research problems and future directions
5. A curated, maintained companion repository (Awesome OpenClaw Research)

**Papers referenced:** V1, V2

---

## 2. Background & Timeline (~2 pages)

### 2.1 OpenClaw Architecture Overview
- Core components: LLM backbone, Skill system, Memory mechanism, Tool execution pipeline
- The SKILL.md specification and skill lifecycle
- Heartbeat-driven background execution model
- Gateway and authentication architecture

### 2.2 Key Timeline
```
Jan 29, 2026  — OpenClaw released (renamed from Moltbot)
Late Jan      — Moltbook platform launched; explosive agent growth
Early Feb     — First academic papers appear (S6, S7, A3, M-series)
Feb 3-4       — "SaaSpocalypse" ($285B market cap erased)
Feb 6         — Trend Micro first industry report
Feb 19        — Microsoft Security advisory
Mid Feb       — CVE-2026-25253 disclosed
Late Feb      — ClawHavoc campaign (824+ malicious skills)
Feb 25        — ClawJacked vulnerability patched
Mar 2026      — Security paper surge (S1-S5, A1-A2, A4, D1-D4)
Mar 16        — NVIDIA NemoClaw announced at GTC 2026
Late Mar      — Supply chain papers (E2-E4, E6)
Apr 2026      — 48+ papers, 20+ industry reports
```

### 2.3 Positioning in the Agent Landscape
- OpenClaw (open-source, self-hosted) vs. Manus (closed-source, commercial) — the two dominant paradigms [V2]
- Comparison with AutoGPT, LangChain, CrewAI and other agent frameworks
- What makes OpenClaw unique: first agent platform to spawn a social network (Moltbook)

**Papers referenced:** V1, V2, C2, S4 (naming history), M5 (lineage)

---

## 3. Core Platform & Architecture (L1) (~2 pages)

### 3.1 Platform Design Philosophy
- Self-hosted, privacy-first architecture
- Skill-based extensibility model
- Multi-LLM backend support

### 3.2 Reinforcement Learning Extensions
- OpenClaw-RL: asynchronous RL with Hindsight-Guided OPD [X1]
- Four decoupled loops for personal agent improvement
- Implications for agent self-improvement

### 3.3 Robotics Integration
- ROSClaw: model-agnostic ROS 2 executive layer [X2]
- Dynamic capability discovery and multimodal observation normalization
- Safety validation across robot platforms (up to 4.8x variation in out-of-policy rates)

### 3.4 Decentralized & Edge Deployment
- OpenCLAW-P2P: Kademlia DHT + federated learning + BFT voting [C3]
- Edge deployment security: deployment architecture as primary risk determinant [I1]
- 40,000+ exposed gateway instances [I1]

### 3.5 Autonomous Science
- ClawdLab: PI-led governance with structured adversarial critique [X3]
- Five recurring architectural failure modes identified

**Papers:** X1, X2, X3, C3, I1

---

## 4. Skill Ecosystem & Supply Chain (L2) (~2.5 pages)

### 4.1 Ecosystem Overview
- ClawHub marketplace: 13,700+ registered skills
- Growth trajectory and composition
- The SKILL.md specification as attack surface

### 4.2 Formal Security Analysis
- DY-Skill attacker model (Dolev-Yao adaptation) [E1]
- Capability-based sandboxing and trust score algebra
- Agent Dependency Graph with SAT-based resolution
- ClawHavoc campaign: 1,200+ malicious skills [E1]

### 4.3 Clone Detection & Ecosystem Inflation
- Multi-modal clone detection across YAML, NL, and code [E3]
- 258,000 clone pairs; 75% of skills involved; ecosystem inflated 3.5x
- 141 security-relevant skills propagating to 1,100+ clones
- **Only peer-reviewed paper in ecosystem (ASE 2026)**

### 4.4 Marketplace Auditing
- SkillProbe: multi-agent "Skills-for-Skills" auditing [E2]
- 90%+ of high-popularity skills fail rigorous auditing
- Giant connected component of high-risk skills (systemic cascading risk)

### 4.5 Large-Scale Classification
- 238,180 unique skills analyzed across four registries [E4]
- Repository-context analysis reduces false positives to 0.52%
- Challenge to earlier high malicious-classification rates

### 4.6 Skill Optimization
- 26.4% lack routing descriptions; 60%+ non-actionable content [E6]
- Two-stage optimization for token efficiency

### 4.7 Skill Infrastructure at Scale
- SkillNet: unified ontology with 200,000+ skills [E5]
- Multi-dimensional evaluation (Safety, Completeness, Executability, Maintainability, Cost-awareness)

**Papers:** E1-E6

---

## 5. Security & Trust (L3) (~4 pages)

### 5.1 Threat Analysis & Taxonomies

#### 5.1.1 Multi-Dimensional Taxonomies
- Tri-layered taxonomy: AI Cognitive × Software Execution × Information System [S1]
- Five-layer lifecycle model: initialization → input → inference → decision → execution [S3]
- OpenClaw-specific kill chain with "Context Manipulation" stage [S4]
- Four risk classes with pipeline-oriented threat model [S5]
- **Comparative analysis** of taxonomy approaches across S1-S5

#### 5.1.2 Empirical Security Evaluation
- 47 adversarial scenarios: only 17% average defense rate [S2]
- Near-zero resilience to sandbox escape [S2]
- Trajectory audit: 58.9% overall pass, 0% on intent-misunderstanding [S6]
- 190 security advisories analyzed [S4]

#### 5.1.3 Benchmarking Personalized Agents
- PASB benchmark: 131 threatening tools [S7]
- Attack propagation under long-horizon interactions
- User prompt processing, external content, tool invocation, memory retrieval attack vectors

**Papers:** S1-S7

### 5.2 Adversarial Attacks

#### 5.2.1 Resource Exhaustion
- Clawdrain: "Segmented Verification Protocol" causing 6-7x token amplification [A1]
- Denial-of-wallet implications for API-cost-bearing deployments
- Deployed against production OpenClaw v2026.2.9 with Gemini 2.5 Pro

#### 5.2.2 Self-Propagating Worms
- ClawWorm: first self-replicating worm for production agent framework [A2]
- Full autonomous infection cycle: hijack → persist → propagate
- Across 40,000+ active instances

#### 5.2.3 Agent-to-Agent Jailbreaking
- SLINGSHOT: RL-trained "Tag-Along Attacks" [A3]
- 67.0% success on Qwen2.5-32B (1.7% baseline)
- Zero-shot transfer to closed-source models (Gemini 2.5 Flash: 56.0%)
- Only 156 A100 GPU-hours, no human demonstrations

#### 5.2.4 Memory Pollution
- HEARTBEAT: exploiting background execution for silent memory pollution [A4]
- Heartbeat cycle as covert channel for persistent backdoor injection
- Connection to temporal fingerprinting in Moltbook studies [M6]

**Papers:** A1-A4

### 5.3 Defensive Architectures

#### 5.3.1 Runtime Security
- PRISM: zero-fork defense-in-depth across 10 lifecycle hooks [D1]
- Hybrid heuristic + LLM scanning pipeline
- Session-scoped risk accumulation with TTL-based decay

#### 5.3.2 Privilege Separation
- Two-agent pipeline with tool partitioning [D2]
- 0% attack success rate on LLMail-Inject (649 attacks)
- Demonstrates architectural elimination of prompt injection for constrained tasks

#### 5.3.3 Pre-Action Authorization
- Open Agent Passport (OAP) specification [D3]
- 53ms median enforcement latency
- Social engineering: 7% model success → 0% with OAP

#### 5.3.4 Grey-Box Testing
- VeriGrey: tool invocation sequences as coverage feedback [D4]
- 33% improvement over black-box on AgentDojo
- 100% vulnerability discovery on Kimi-K2.5, 90% on Opus 4.6

**Papers:** D1-D4

---

## 6. Agent Social Dynamics — Moltbook (L4) (~3.5 pages)

### 6.1 Platform Measurement & Network Structure

#### 6.1.1 Scale and Growth
- Explosive growth: 46,690 agents → 1,500,000+ in days [M1, M10]
- Heavy-tailed distributions and power-law scaling [M1]
- Rapid topical diversification [M8]

#### 6.1.2 Network Properties
- Small-world connectivity (avg path length 2.91) [M9]
- Extremely shallow conversations (mean depth 1.07) [M9]
- Low reciprocity (0.197) [M9]
- Heavy-tailed degree distributions with core-periphery structure [M14]
- 0.9% of nodes form structural core [M14]

#### 6.1.3 Content Analysis
- Six thematic domains [M10]
- 9-category topic taxonomy [M8]
- Knowledge-driven (not interest-driven) behavior [M12]
- 34.1% exact duplicate viral templates [M9]

**Papers:** M1, M5, M8, M9, M10, M12, M14

### 6.2 Safety, Norms & Emergent Behavior

#### 6.2.1 Human vs. AI Attribution
- Temporal fingerprinting via heartbeat cycle [M6]
- 15.3% autonomous, 54.8% human-influenced
- No viral phenomenon from clearly autonomous agents

#### 6.2.2 Safety Decay
- Self-evolution trilemma (impossibility result) [M7]
- Three failure modes: Cognitive Degeneration, Alignment Failure, Communication Collapse
- 28.7% of content is safety-related [M11]
- Social engineering outperforms prompt injection 31.9% vs 3.7% [M11]

#### 6.2.3 Emergent Social Structures
- Governance, economies, religion emerge in 3-5 days [M11]
- "Crustafarianism" — viral religion among agents [M7]
- Performative identity paradox: 4.1% reciprocity [M11]
- Selective norm enforcement via AIRS [M2]

**Papers:** M2, M6, M7, M11

### 6.3 Learning & Coordination

#### 6.3.1 Peer Learning
- Response taxonomy: validation (22%), knowledge extension (18%), application (12%) [M3]
- "Broadcasting inversion": 8.9:1 statement-to-question ratio [M4]
- 93% parallel monologues [M4]
- Extreme participation inequality (Gini = 0.889) [M4]

#### 6.3.2 Coordination Detection
- MoltGraph: temporal heterogeneous graph dataset [M13]
- Bursty coordination episodes (98.33% under 24h)
- 506.35% higher early interaction rates for coordinated posts
- Hub formation acceleration

**Papers:** M3, M4, M13

---

## 7. Applications & Domains (L5) (~1.5 pages)

### 7.1 Healthcare
- Hospital-adapted architecture with HIPAA compliance [P1]
- Document-centric interaction, page-indexed memory
- Composable medical skills library

### 7.2 Finance
- "Delegation Gap" formalization [P2]
- Survivability-Aware Execution middleware
- 93.1% drawdown reduction on Binance data

### 7.3 Education
- Bidirectional scaffolding and emergent peer learning [Ed1]
- "Learn by Teaching Your AI Agent Teammate" curriculum
- Observations across 167,000+ agents on three platforms

### 7.4 General Assistance & Comparison
- IronEngine: systematic comparison across five platforms [P3]
- IronClaw variant for hardware/embedded scenarios
- Three-phase pipeline (Discussion, Model Switch, Execution)

**Papers:** P1, P2, P3, Ed1

---

## 8. Discussion (~3 pages)

### 8.1 Industry Response Synthesis
- Timeline of industry security reports
- Convergent findings: exposed instances (30K-135K+), skill contamination, sandbox escape
- Divergent recommendations: isolation (Microsoft) vs. wrapping (NVIDIA NemoClaw) vs. governance (Trend Micro)

### 8.2 Cross-Layer Analysis
- **L2→L3 dependency**: Skill supply chain vulnerabilities enable attack vectors (ClawHavoc → Clawdrain, ClawWorm)
- **L3→L4 interaction**: Security mechanisms interact with social dynamics (heartbeat exploitation spans both)
- **L1→L5 gap**: Architecture extensions not yet integrated with domain applications
- **Measurement challenges**: Moltbook studies (L4) rely on different datasets with overlapping but non-identical timeframes

### 8.3 Open Research Problems

1. **Formal verification of agent behavior** — moving beyond empirical testing to provable safety guarantees
2. **Scalable skill auditing** — automating the review of 13,700+ skills with acceptable false positive rates
3. **Cross-agent trust establishment** — protocols for agent-to-agent trust in decentralized deployments
4. **Temporal dynamics of agent communities** — longitudinal studies beyond Moltbook's first weeks
5. **Domain-specific safety frameworks** — HIPAA-grade guarantees for healthcare, financial compliance for trading
6. **Human-AI attribution at scale** — improving on the 30.2% unclassified rate in temporal fingerprinting [M6]
7. **Worm containment** — defense mechanisms against self-propagating agent attacks [A2]
8. **Ecosystem governance** — balancing openness with security in skill marketplaces

### 8.4 Limitations of Current Literature
- Nearly all preprints (1 peer-reviewed exception: ASE 2026)
- Potential for duplicated or contradictory findings without peer review
- Moltbook studies cluster in a narrow time window (first 2-3 weeks)
- Limited reproducibility: many studies rely on proprietary model backends
- Geographic concentration of research teams

---

## 9. Conclusion (~0.5 pages)

- Summary of the six-layer taxonomy and key findings per layer
- The OpenClaw case as a template for future open-source agent ecosystem analysis
- Call for peer-reviewed research and longitudinal studies

---

## Appendix

### A. Complete Paper Mapping Table
Full mapping of all 48+ papers to our taxonomy layers with venue, date, and citation counts.

### B. Industry Report Timeline
Chronological listing of all industry security reports with key findings.

### C. Alias Mapping
Complete mapping of platform names: OpenClaw, Clawdbot, Clawd, Moltbot, Moltbook, ClawHub, ClawdLab, etc.

---

## Estimated Length
- Main body: ~18 pages (single column) or ~12 pages (double column)
- References: ~100 entries
- Suitable for: S&P/CCS/USENIX Security (security focus), ACL/EMNLP (NLP/language infrastructure angle), or a comprehensive journal submission (TIFS, TDSC, ACM Computing Surveys)

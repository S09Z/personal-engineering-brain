# NEWS_REGISTRY.md

## Purpose

Canonical registry for what the Personal Engineering Brain monitors.

Defines:

- Themes
- Topics
- Keywords
- Priority
- Preferred sources
- Collection frequency
- Retention rules

Do not create new Themes automatically.

New Topics may be suggested but should be reviewed before becoming canonical.

---

# Priority Levels

## P0 — Critical

Actively monitor.

Examples:

- security incidents
- breaking API changes
- major market events
- important model releases
- breaking infrastructure changes

## P1 — High

Include in daily discovery.

## P2 — Normal

Include when meaningful developments occur.

## P3 — Background

Mostly useful for weekly synthesis.

---

# THEME: Markets

id: markets

priority: P0

## Topic: NASDAQ

id: nasdaq

priority: P0

keywords:

- NASDAQ
- Nasdaq Composite
- Nasdaq 100
- NDX
- QQQ
- technology stocks
- semiconductor stocks

track:

- major daily movements
- earnings impact
- technology-sector rotation
- AI-related market movement
- index composition changes
- volatility
- major macro impact

preferred_sources:

- Nasdaq
- SEC
- company investor relations
- Reuters
- Bloomberg
- Financial Times

cadence: daily

## Topic: S&P 500

id: sp500

priority: P0

keywords:

- S&P 500
- SPX
- SPY
- US equities
- US stock market

track:

- major index movements
- sector rotation
- market breadth
- earnings impact
- major macroeconomic impact
- index composition changes

preferred_sources:

- S&P Global
- SEC
- company investor relations
- Reuters
- Bloomberg
- Financial Times

cadence: daily

## Topic: SET50

id: set50

priority: P0

keywords:

- SET50
- SET Index
- SET
- Thai stocks
- Thailand equities

track:

- major index movements
- SET50 constituents
- corporate earnings
- index changes
- Thailand macro events affecting equities
- major sector movements

preferred_sources:

- Stock Exchange of Thailand
- SEC Thailand
- company investor relations
- Bank of Thailand
- reputable Thai financial news

cadence: daily

## Topic: Technology Equities

id: technology-equities

priority: P1

keywords:

- NVIDIA
- Microsoft
- Apple
- Alphabet
- Amazon
- Meta
- AMD
- Broadcom
- TSMC
- semiconductor
- AI stocks

track:

- earnings
- AI capex
- datacenter demand
- GPU demand
- cloud growth
- major product announcements
- guidance changes

cadence: daily

---

# THEME: Software Engineering

id: software-engineering

priority: P0

## Topic: Developer Tooling

id: developer-tooling

priority: P1

keywords:

- IDE
- coding agent
- developer tools
- CLI
- SDK
- compiler
- debugger

track:

- major releases
- productivity changes
- breaking changes
- new engineering workflows

## Topic: AI Coding Agents

id: ai-coding-agents

priority: P0

keywords:

- Claude Code
- Codex
- coding agent
- agentic coding
- GitHub Copilot
- Cursor
- Gemini CLI
- MCP

subtopics:

- Claude Code
- Codex
- GitHub Copilot
- Cursor
- Gemini CLI
- MCP

track:

- model changes
- agent capability
- IDE integration
- terminal agents
- MCP
- code review
- autonomous development
- benchmarks
- pricing changes

cadence: daily

## Topic: Web Engineering

id: web-engineering

priority: P1

keywords:

- Node.js
- Bun
- TypeScript
- JavaScript
- Next.js
- React
- Vite
- pnpm

track:

- releases
- breaking changes
- security
- build performance
- deployment

## Topic: Software Architecture

id: software-architecture

priority: P2

keywords:

- distributed systems
- event driven
- microservices
- modular monolith
- API design
- caching
- reliability patterns

cadence: weekly

---

# THEME: AI Engineering

id: ai-engineering

priority: P0

## Topic: AI Infrastructure

id: ai-infrastructure

priority: P1

keywords:

- inference
- GPU serving
- vLLM
- TensorRT
- Triton
- inference server
- AI infrastructure

track:

- inference performance
- serving frameworks
- GPU utilization
- deployment
- cost optimization

## Topic: Agent Engineering

id: agent-engineering

priority: P0

keywords:

- AI agents
- agent framework
- tool use
- MCP
- memory
- computer use
- agent evaluation

track:

- architecture
- tool use
- memory
- planning
- evaluation
- production patterns

## Topic: RAG

id: rag

priority: P1

keywords:

- RAG
- retrieval augmented generation
- embeddings
- reranking
- semantic search
- vector database

track:

- retrieval architecture
- evaluation
- reranking
- hybrid search
- production lessons

---

# THEME: Data Engineering

id: data-engineering

priority: P1

## Topic: Data Platforms

id: data-platforms

priority: P1

keywords:

- Apache Spark
- Flink
- Kafka
- Airflow
- dbt
- DuckDB
- Iceberg
- Delta Lake
- Snowflake
- Databricks

track:

- major releases
- architecture changes
- performance
- open table formats
- streaming
- orchestration

cadence: daily

## Topic: Databases

id: databases

priority: P0

keywords:

- PostgreSQL
- MySQL
- Redis
- MongoDB
- ClickHouse
- DuckDB
- vector database

subtopics:

- PostgreSQL
- Redis
- ClickHouse
- DuckDB

track:

- releases
- performance
- security
- query capabilities
- replication
- AI/vector support

---

# THEME: Data Science

id: data-science

priority: P1

## Topic: Machine Learning

id: machine-learning

priority: P1

keywords:

- XGBoost
- LightGBM
- scikit-learn
- forecasting
- classification
- regression
- anomaly detection

track:

- practical techniques
- benchmarks
- production methods
- important releases

## Topic: Computer Vision

id: computer-vision

priority: P1

keywords:

- vision model
- object detection
- segmentation
- tracking
- multimodal vision
- diffusion
- image generation

cadence: weekly

---

# THEME: MLOps

id: mlops

priority: P0

## Topic: Model Deployment

id: model-deployment

priority: P0

keywords:

- model serving
- inference
- deployment
- Kubernetes AI
- Triton
- vLLM
- Ray Serve

track:

- production architecture
- performance
- autoscaling
- GPU scheduling

## Topic: ML Observability

id: ml-observability

priority: P1

keywords:

- model monitoring
- drift
- evaluation
- observability
- ML metrics

track:

- drift detection
- monitoring
- evaluation
- production incidents

## Topic: ML Lifecycle

id: ml-lifecycle

priority: P1

keywords:

- MLflow
- Kubeflow
- feature store
- experiment tracking
- model registry

cadence: weekly

---

# THEME: LLM

id: llm

priority: P0

## Topic: Foundation Models

id: foundation-models

priority: P0

keywords:

- GPT
- Claude
- Gemini
- Llama
- Qwen
- DeepSeek
- Mistral

track:

- new models
- benchmark results
- context
- reasoning
- multimodal
- tool use
- pricing
- API changes

cadence: daily

## Topic: Local LLM

id: local-llm

priority: P1

keywords:

- Ollama
- LM Studio
- llama.cpp
- GGUF
- quantization
- local inference

track:

- inference performance
- new models
- quantization
- GPU compatibility
- context performance

## Topic: LLM Evaluation

id: llm-evaluation

priority: P1

keywords:

- LLM eval
- benchmark
- hallucination
- agent eval
- SWE-bench

track:

- evaluation methods
- benchmark methodology
- contamination
- reliability

---

# THEME: AI Research

id: ai-research

priority: P0

## Topic: Model Architecture

id: model-architecture

priority: P1

keywords:

- transformer
- state space model
- MoE
- attention
- architecture
- scaling

track:

- important architectural changes
- efficiency
- scaling
- long context

## Topic: Training

id: model-training

priority: P1

keywords:

- pretraining
- post-training
- RLHF
- reinforcement learning
- distillation
- synthetic data
- fine-tuning

track:

- training methods
- data
- alignment
- post-training
- efficiency

## Topic: Reasoning

id: reasoning-research

priority: P0

keywords:

- reasoning model
- chain of thought
- test-time compute
- reinforcement learning
- verifier

track:

- new techniques
- benchmark improvements
- limitations
- inference-time methods

## Topic: Multimodal AI

id: multimodal-ai

priority: P1

keywords:

- vision language model
- multimodal
- audio model
- video model
- world model

track:

- architecture
- capability
- benchmarks
- applications

## Topic: AI Papers

id: ai-papers

priority: P1

preferred_sources:

- arXiv
- conference proceedings
- official research labs
- author repositories

conferences:

- NeurIPS
- ICML
- ICLR
- ACL
- EMNLP
- CVPR
- ICCV
- ECCV

cadence: daily

---

# Daily Brief Registry

Daily brief priority:

1. Markets
2. AI Coding Agents
3. Foundation Models
4. AI Research
5. Software Engineering
6. MLOps
7. Data Engineering
8. Data Science

Target:

5–10 retained items per day.

Avoid producing dozens of low-value stories.

---

# Daily Market Snapshot

Include:

- NASDAQ
- S&P 500
- SET50

For each:

- direction
- notable movement
- major driver
- important company/event
- source

Do not add speculative trading advice.

---

# Story Labels

ACTION

Affects tools, projects, security, compatibility, or operational decisions.

IMPORTANT

Meaningful development worth retaining.

INTERESTING

Useful context but no immediate impact.

IGNORE

Marketing, duplicate, low-signal, or irrelevant.

---

# My Stack

Tools the owner actually runs or depends on:

- Next.js / Node.js / TypeScript
- Claude Code and other coding agents
- PostgreSQL
- self-hosted inference (vLLM and similar)

A story is ACTION only when it requires doing something on this stack:

- a security fix to apply
- a breaking change to handle before upgrading
- a setting or config that must change

The same kind of story about a tool outside this list is IMPORTANT at most.

---

# Promotion Rules

ACTION:
- Create News note
- Update Topic note after human review of the News note

IMPORTANT:
- Create News note
- Link Topic

INTERESTING:
- Daily/weekly summary only by default

IGNORE:
- Do not retain

---

# Suggested Retention

Routine daily market movement:
- retain primarily in Daily summaries

Major market regime/event:
- permanent News note

Product release:
- retain if meaningful

Minor product announcement:
- weekly summary only

Security issue:
- retain

Breaking API/deprecation:
- retain

Major research paper:
- retain

Minor benchmark improvement:
- weekly summary unless strategically relevant

Community speculation:
- do not promote without verification

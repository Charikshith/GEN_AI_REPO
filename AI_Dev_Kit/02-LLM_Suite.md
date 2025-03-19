## 2. LLM-Suite

| LLM             | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|


| SLM             | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| [gemma3](https://ai.google.dev/gemma) | Gemma is a family of lightweight, state-of-the-art open models built by Google DeepMind and Google. They are designed for best-in-class performance and responsibility, prioritizing rigorous testing and safety evaluations. Gemma models are available in two sizes: Gemma 2B and Gemma 7B, with both pretrained and instruction-tuned variants. They are based on the same research and technology used to create Gemini models. |
| [mistralsmall3.1](https://mistral.ai/news/mistral-small-3-1) | Mistral Small is a performant language model for reasoning and specialized use-cases. Mistral Small is on par with Mixtral 8x7B and optimized for latency and cost. |


This section focuses on libraries, tools, and techniques specifically designed for working with Large Language Models (LLMs). It covers aspects such as training, fine-tuning, application development, RAG, inference, deployment, security, and more.

### 2.1 LLM Training and Fine-Tuning

This section lists libraries that facilitate the training and fine-tuning of Large Language Models (LLMs), allowing you to customize pre-trained models for specific tasks and datasets.

| Library             | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| [unsloth](https://github.com/unslothai/unsloth)            | Fine-tune LLMs faster with less memory.                                                          |
| [PEFT](https://github.com/huggingface/peft)                | State-of-the-art Parameter-Efficient Fine-Tuning library.                                       |
| [TRL](https://github.com/huggingface/trl)                 | Train transformer language models with reinforcement learning.                                  |
| [Transformers](https://github.com/huggingface/transformers)       | Transformers provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio. |
| [Axolotl](https://github.com/axolotl-ai-cloud/axolotl/)           | Tool designed to streamline post-training for various AI models.                                 |
| [LLMBox](https://github.com/RUCAIBox/LLMBox)             | A comprehensive library for implementing LLMs, including a unified training pipeline and comprehensive model evaluation. |
| [LitGPT](https://github.com/Lightning-AI/litgpt)             | Train and fine-tune LLM lightning fast.                                                          |
| [Mergoo](https://github.com/Leeroo-AI/mergoo)            | A library for easily merging multiple LLM experts, and efficiently train the merged LLM.         |
| [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory)      | Easy and efficient LLM fine-tuning.                                                              |
| [Ludwig](https://github.com/ludwig-ai/ludwig)            | Low-code framework for building custom LLMs, neural networks, and other AI models.               |
| [Txtinstruct](https://github.com/neuml/txtinstruct)       | A framework for training instruction-tuned models.                                               |
| [Lamini](https://github.com/lamini-ai/lamini)            | An integrated LLM inference and tuning platform.                                                 |
| [XTuring](https://github.com/stochasticai/xTuring)           | xTuring provides fast, efficient and simple fine-tuning of open-source LLMs, such as Mistral, LLaMA, GPT-J, and more. |
| [RL4LMs](https://github.com/allenai/RL4LMs)            | A modular RL library to fine-tune language models to human preferences.                          |
| [DeepSpeed](https://github.com/deepspeedai/DeepSpeed)         | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. |
| [torchtune](https://github.com/pytorch/torchtune)         | A PyTorch-native library specifically designed for fine-tuning LLMs.                             |
| [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning) | A library that offers a high-level interface for pretraining and fine-tuning LLMs.               |

### 2.2 LLM Application Development

This section features frameworks, libraries, and tools designed for building applications powered by Large Language Models (LLMs).

#### 2.2.1 Frameworks

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [LangChain](https://github.com/langchain-ai/langchain)    | LangChain is a framework for developing applications powered by large language models (LLMs).          |
| [Llama Index](https://github.com/run-llama/llama_index)  | LlamaIndex is a data framework for your LLM applications.                                              |
| [HayStack](https://github.com/deepset-ai/haystack)     | Haystack is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. |
| [Prompt flow](https://github.com/microsoft/promptflow)  | A suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications. |
| [Griptape](https://github.com/griptape-ai/griptape)     | A modular Python framework for building AI-powered applications.                                        |
| [Weave](https://github.com/wandb/weave)        | Weave is a toolkit for developing Generative AI applications.                                          |
| [Llama Stack](https://github.com/meta-llama/llama-stack)  | Build Llama Apps.                                                                                      |

#### 2.2.2 Multi API Access

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [LiteLLM](https://github.com/BerriAI/litellm)      | Library to call 100+ LLM APIs in OpenAI format.                                                        |
| [AI Gateway](https://github.com/Portkey-AI/gateway)   | A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.                                                 |

#### 2.2.3 Routers

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [RouteLLM](https://github.com/lm-sys/RouteLLM)     | Framework for serving and evaluating LLM routers - save LLM costs without compromising quality. Drop-in replacement for OpenAI's client to route simpler queries to cheaper models.                                                      |

#### 2.2.4 Memory

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [mem0](https://github.com/mem0ai/mem0)         | The Memory layer for your AI apps.                                                                     |
| [Memoripy](https://github.com/caspianmoon/memoripy)     | An AI memory layer with short- and long-term storage, semantic clustering, and optional memory decay for context-aware applications. |

#### 2.2.5 Interface

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [Streamlit](https://github.com/streamlit/streamlit)    | A faster way to build and share data apps. Streamlit lets you transform Python scripts into interactive web apps in minutes                                                             |
| [Gradio](https://github.com/gradio-app/gradio)       | Build and share delightful machine learning apps, all in Python.                                       |
| [AI SDK UI](https://sdk.vercel.ai/docs/introduction)    | Build chat and generative user interfaces.                                                             |
| [AI-Gradio](https://github.com/AK391/ai-gradio)    | Create AI apps powered by various AI providers.                                                        |
| [Simpleaichat](https://github.com/minimaxir/simpleaichat) | Python package for easily interfacing with chat apps, with robust features and minimal code complexity. |
| [Chainlit](https://github.com/Chainlit/chainlit)     | Build production-ready Conversational AI applications in minutes.                                      |

#### 2.2.6 Low Code

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [LangFlow](https://github.com/langflow-ai/langflow)     | LangFlow is a low-code app builder for RAG and multi-agent AI applications. It’s Python-based and agnostic to any model, API, or database.                           |
| [n8n](https://github.com/n8n-io/n8n)          | n8n is a low-code automation tool that allows users to create complex workflows by connecting various applications and services. It offers both self-hosted and cloud-hosted options, with a visual interface.                           |

#### 2.2.7 Cache

| Library        | Description                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------|
| [GPTCache](https://github.com/zilliztech/gptcache)     | A Library for Creating Semantic Cache for LLM Queries. Slash Your LLM API Costs by 10x 💰, Boost Speed by 100x. Fully integrated with LangChain and LlamaIndex.                               |

### 2.3 LLM Retrieval Augmented Generation (RAG)

This section presents libraries focused on Retrieval Augmented Generation (RAG), a technique for enhancing LLMs with external knowledge sources for more accurate and context-aware responses.

| Library         | Description                                                                                                      |
|---------------|----------------------------------------------------------------------------------------------------------------|
| [FastGraph RAG](https://github.com/circlemind-ai/fast-graphrag) | Streamlined and promptable Fast GraphRAG framework designed for interpretable, high-precision, agent-driven retrieval workflows. |
| [Chonkie](https://github.com/chonkie-ai/chonkie)       | RAG chunking library that is lightweight, lightning-fast, and easy to use.                                      |
| [RAGChecker](https://github.com/amazon-science/RAGChecker)    | A Fine-grained Framework For Diagnosing RAG.                                                                   |
| [RAG to Riches](https://github.com/SciPhi-AI/R2R) | Build, scale, and deploy state-of-the-art Retrieval-Augmented Generation applications.                         |
| [BeyondLLM](https://github.com/aiplanethub/beyondllm)     | Beyond LLM offers an all-in-one toolkit for experimentation, evaluation, and deployment of Retrieval-Augmented Generation (RAG) systems. |
| [SQLite-Vec](https://github.com/asg017/sqlite-vec)    | A vector search SQLite extension that runs anywhere!                                                           |
| [fastRAG](https://github.com/IntelLabs/fastRAG)       | fastRAG is a research framework for efficient and optimized retrieval-augmented generative pipelines, incorporating state-of-the-art LLMs and Information Retrieval. |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG)      | A Python Toolkit for Efficient RAG Research.                                                                   |
| [Llmware](https://github.com/llmware-ai/llmware)       | Unified framework for building enterprise RAG pipelines with small, specialized models.                        |
| [Rerankers](https://github.com/AnswerDotAI/rerankers)     | A lightweight unified API for various reranking models.                                                        |
| [Vectara](https://vectara.github.io/py-vectara-agentic/latest/)       | Build Agentic RAG applications.                                                                                |

### 2.4 LLM Vector Stores

This section lists databases relevant to LLM applications, including specialized vector stores for embedding similarity search and general-purpose databases that may be used for storing LLM-related data or metadata.

| Library      | Description                                                                                                                                   | Deployment     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [Pinecone](https://www.pinecone.io/)      | A managed vector database optimized for similarity search, enabling efficient retrieval of data based on vector embeddings.                  | Cloud (Managed)   |
| [Weaviate](https://www.weaviate.io/)      | An open-source vector search engine that allows you to store and search data based on vector embeddings.                                       | Self-Hosted/Cloud |
| [ChromaDB](https://www.trychroma.com/)      | An open-source embedding database. Chroma makes it easy to build LLM apps by making knowledge, facts, and skills pluggable for LLMs.                                                        | Self-Hosted        |
| [Milvus](https://milvus.io/)         | Open-source vector database for embedding similarity search and AI applications.                                                                   | Self-Hosted/Cloud |
| [Qdrant](https://qdrant.tech/)        | An open-source vector database and search engine designed for high-performance similarity search and neural network-based solutions.        | Self-Hosted/Cloud |
| [FAISS](https://github.com/facebookresearch/faiss)         | A library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM.  | Library (Self-Implemented) |
| [PostgreSQL](https://www.postgresql.org/)    | A powerful, open-source relational database management system.  Can be used to store LLM data or metadata, but not optimized for vector search without extensions. | Self-Hosted/Cloud |
| [MySQL](https://www.mysql.com/)         | A popular open-source relational database management system. Can be used to store LLM data or metadata. | Self-Hosted/Cloud |
| [MongoDB](https://www.mongodb.com/)       | A NoSQL document database, providing flexibility and scalability for handling unstructured and semi-structured data.                         | Self-Hosted/Cloud |

**Comments:**

*   **Pinecone:** Excellent for a managed solution, ease of use, and production-ready scalability. Use when you want to focus on building your application rather than managing infrastructure. Offers a proprietary API for vector similarity search.
*   **Weaviate:** Good choice if you want an open-source solution with GraphQL and strong semantic search capabilities. Supports both GraphQL and vector similarity search for querying. Can be self-hosted or used with Weaviate Cloud Service (WCS).
*   **ChromaDB:** Designed for simplicity and ease of use, great for local development and quick prototyping. Good Python integration. Offers a proprietary API for vector similarity search.
*   **Milvus:** A powerful, scalable vector database designed for large-scale deployments. More complex to set up and manage but offers high performance. Uses Vector Similarity Search as its query logic.
*   **Qdrant:** Provides a good balance of performance, scalability, and ease of use. Offers a flexible deployment and rich feature set. Uses Vector Similarity Search as its query logic.
*   **FAISS:** Best suited when you need a library to build custom indexes and have more control over the implementation. Excellent if you are memory-constrained. Offers Vector Similarity Search (Library). Requires self-implementation for deployment.
*   **PostgreSQL:** A robust and reliable relational database. Primarily uses SQL for querying. Consider for storing structured LLM data, but requires extensions (e.g., pgvector) for efficient vector similarity search. Available for self-hosting or on various cloud platforms.
*   **MySQL:** A widely used relational database. Primarily uses SQL for querying. Consider for storing structured LLM data. Available for self-hosting or on various cloud platforms.
*   **MongoDB:** A flexible NoSQL database. Uses MongoDB Query Language (MQL). Consider for storing unstructured or semi-structured LLM data and metadata. Available for self-hosting or through MongoDB Atlas on various cloud platforms.

**Key for "Deployment" Column:**

*   **Cloud (Managed):** Primarily offered as a managed service, where the provider handles infrastructure and maintenance.
*   **Self-Hosted:** Designed to be deployed and managed on your own infrastructure.
*   **Self-Hosted/Cloud:** Available for self-hosting but also offered as a managed service on a cloud platform.
*   **Library (Self-Implemented):** Requires you to implement and deploy the solution yourself using the library.                                                              |                                                                       |                                                                                       |


### 2.5 LLM Inference

| Library         | Description                                                                                               |
|---------------|------------------------------------------------------------------------------------------------------|
| [LLM Compressor](https://github.com/vllm-project/llm-compressor) | Transformers-compatible library for applying various compression algorithms to LLMs for optimized deployment. |
| [LightLLM](https://github.com/ModelTC/lightllm)      | Python-based LLM inference and serving framework, notable for its lightweight design, easy scalability, and high-speed performance. |
| [vLLM](https://github.com/vllm-project/vllm)         | High-throughput and memory-efficient inference and serving engine for LLMs.                            |
| [torchchat](https://github.com/pytorch/torchchat)     | Run PyTorch LLMs locally on servers, desktop, and mobile.                                              |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)  | TensorRT-LLM is a library for optimizing Large Language Model (LLM) inference.                        |
| [WebLLM](https://github.com/mlc-ai/web-llm)        | High-performance In-browser LLM Inference Engine.                                                     |

### 2.6 LLM Serving

| Library   | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| [Langcorn](https://github.com/msoedov/langcorn)  | Serving LangChain LLM apps and agents automagically with FastAPI.       |
| [LitServe](https://github.com/Lightning-AI/LitServe)  | Lightning-fast serving engine for any AI model of any size. It augments FastAPI with features like batching, streaming, and GPU autoscaling.           |

### 2.7 LLM Data Handling (Extraction & Generation)

#### 2.7.1 LLM Data Extraction

| Library         | Description                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [Crawl4AI](https://github.com/unclecode/crawl4ai)       | Open-source LLM Friendly Web Crawler & Scraper.                                                                                      |
| [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai)  | A web scraping Python library that uses LLM and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.). |
| [Docling](https://github.com/DS4SD/docling)        | Docling parses documents and exports them to the desired format with ease and speed.                                                  |
| [smol-docling](https://github.com/smol-rs/smol-docling) | A lightweight documentation generator for Rust and other languages. It's designed to be simple, fast, and customizable, inspired by `rustdoc` but more flexible and language-agnostic. It supports Markdown, code highlighting, and custom themes to create beautiful and easy-to-read documentation. |
| [Llama Parse](https://github.com/run-llama/llama_cloud_services)    | GenAI-native document parser that can parse complex document data for any downstream LLM use case (RAG, agents).                     |
| [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)    | PyMuPDF4LLM library makes it easier to extract PDF content in the format you need for LLM & RAG environments.                        |
| [Crawlee](https://github.com/apify/crawlee-python)        | A web scraping and browser automation library.                                                                                         |
| [MegaParse](https://github.com/quivrhq/megaparse)      | Parser for every type of document.                                                                                                    |
| [ExtractThinker](https://github.com/enoch3712/ExtractThinker) | Document Intelligence library for LLMs.                                                                                               |


#### 2.7.2 LLM Data Generation

| Library       | Description                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------|
| [DataDreamer](https://github.com/datadreamer-dev/DataDreamer)  | DataDreamer is a powerful open-source Python library for prompting, synthetic data generation, and training workflows. |
| [fabricator](https://github.com/flairNLP/fabricator)   | A flexible open-source framework to generate datasets with large language models.                   |
| [Promptwright](https://github.com/stacklok/promptwright) | Synthetic Dataset Generation Library.                                                               |
| [EasyInstruct](https://github.com/zjunlp/EasyInstruct) | An Easy-to-use Instruction Processing Framework for Large Language Models.                          |
| [Text Machina](https://github.com/Genaios/TextMachina) | A modular and extensible Python framework, designed to aid in the creation of high-quality, unbiased datasets to build robust models for MGT-related tasks such as detection, attribution, and boundary detection. |


### 2.8 LLM Agents

| Library         | Description                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------|
| [CrewAI](https://github.com/crewAIInc/crewAI)        | Framework for orchestrating role-playing, autonomous AI agents.                                          |
| [LangGraph](https://github.com/langchain-ai/langgraph)     | Build resilient language agents as graphs.                                                               |
| [Agno](https://github.com/agno-agi/agno)          | Build AI Agents with memory, knowledge, tools, and reasoning. Chat with them using a beautiful Agent UI.  |
| [AutoGen](https://github.com/microsoft/autogen)       | An open-source framework for building AI agent systems.                                                  |
| [Smolagents](https://github.com/huggingface/smolagents)    | Library to build powerful agents in a few lines of code.                                                 |
| [Pydantic AI](https://ai.pydantic.dev/) | Python agent framework to build production grade applications with Generative AI. |
| [gradio-tools](https://github.com/freddyaboulton/gradio-tools)  | A Python library for converting Gradio apps into tools that can be leveraged by an LLM-based agent to complete its task. |
| [Composio](https://github.com/ComposioHQ/composio)      | Production Ready Toolset for AI Agents.                                                                  |
| [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents) | Building AI agents, atomically.                                                                         |
| [Memary](https://github.com/kingjulio8238/Memary)        | Open Source Memory Layer For Autonomous Agents.                                                          |
| [Browser Use](https://github.com/browser-use/browser-use)   | Make websites accessible for AI agents.                                                                 |
| [OpenWebAgent](https://github.com/THUDM/OpenWebAgent/)   | An Open Toolkit to Enable Web Agents on Large Language Models.                                           |
| [Lagent](https://github.com/InternLM/lagent)        | A lightweight framework for building LLM-based agents.                                                   |
| [LazyLLM](https://github.com/LazyAGI/LazyLLM)       | A Low-code Development Tool For Building Multi-agent LLMs Applications.                                  |
| [Swarms](https://github.com/kyegomez/swarms)        | The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework.                               |
| [ChatArena](https://github.com/Farama-Foundation/chatarena)     | ChatArena is a library that provides multi-agent language game environments and facilitates research about autonomous LLM agents and their social interactions. |
| [Swarm](https://github.com/openai/swarm)         | Educational framework exploring ergonomic, lightweight multi-agent orchestration.                        |
| [AgentStack](https://github.com/AgentOps-AI/AgentStack)    | The fastest way to build robust AI agents.                                                               |
| [Archgw](https://github.com/katanemo/archgw)        | Intelligent gateway for Agents.                                                                          |
| [Flow](https://github.com/lmnr-ai/flow)          | A lightweight task engine for building AI agents.                                                        |
| [AgentOps](https://github.com/AgentOps-AI/agentops)      | Python SDK for AI agent monitoring.                                                                      |
| [Langroid](https://github.com/langroid/langroid)      | Multi-Agent framework.                                                                                   |
| [Agentarium](https://github.com/Thytu/Agentarium)    | Framework for creating and managing simulations populated with AI-powered agents.                        |
| [Upsonic](https://github.com/upsonic/upsonic)       | Reliable AI agent framework that supports MCP.                                                          |

### 2.9 LLM Evaluation

| Library     | Description                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------|
| [Ragas](https://github.com/explodinggradients/ragas)      | Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications.            |
| [Giskard](https://github.com/Giskard-AI/giskard)    | Open-Source Evaluation & Testing for ML & LLM systems.                                                           |
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM Evaluation Framework |
| [Lighteval](https://github.com/huggingface/lighteval)  | All-in-one toolkit for evaluating LLMs.                                                                         |
| [Trulens](https://github.com/truera/trulens) | Evaluation and Tracking for LLM Experiments |
| [PromptBench](https://github.com/microsoft/promptbench) | A unified evaluation framework for large language models.                                                        |
| [LangTest](https://github.com/JohnSnowLabs/langtest)   | Deliver Safe & Effective Language Models. 60+ Test Types for Comparing LLM & NLP Models on Accuracy, Bias, Fairness, Robustness & More. |
| [EvalPlus](https://github.com/evalplus/evalplus)   | A rigorous evaluation framework for LLM4Code.                                                                    |
| [FastChat](https://github.com/lm-sys/FastChat)   | An open platform for training, serving, and evaluating large language model-based chatbots.                      |
| [judges](https://github.com/quotient-ai/judges)     | A small library of LLM judges.                                                                                   |
| [Evals](https://github.com/openai/evals)      | Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks.            |
| [AgentEvals](https://github.com/langchain-ai/agentevals) | Evaluators and utilities for evaluating the performance of your agents.                                         |
| [LLMBox](https://github.com/RUCAIBox/LLMBox)     | A comprehensive library for implementing LLMs, including a unified training pipeline and comprehensive model evaluation. |
| [Opik](https://github.com/comet-ml/opik)       | An open-source end-to-end LLM Development Platform which also includes LLM evaluation.                           |
| [pandas-ai](https://github.com/Sinaptik-AI/pandas-ai)   | Chat with your database (SQL, CSV, pandas, polars, MongoDB, NoSQL, etc.). |

### 2.10 LLM Monitoring

| Library              | Description                                                                                       |
|----------------------|-------------------------------------------------------------------------------------------------|
| [Opik](https://github.com/comet-ml/opik)                | An open-source end-to-end LLM Development Platform which also includes LLM monitoring.          |
| [LangSmith](https://github.com/langchain-ai/langsmith-sdk)           | Provides tools for logging, monitoring, and improving your LLM applications.                     |
| [Weights & Biases](https://github.com/wandb) (W&B) | W&B provides features for tracking LLM performance.                                          |
| [Helicone](https://github.com/Helicone/helicone)            | Open source LLM-Observability Platform for Developers. One-line integration for monitoring, metrics, evals, agent tracing, prompt management, playground, etc. |
| [Evidently](https://github.com/evidentlyai/evidently)          | An open-source ML and LLM observability framework.                                                |
| [Phoenix](https://github.com/Arize-ai/phoenix)            | An open-source AI observability platform designed for experimentation, evaluation, and troubleshooting. |
| [Observers](https://github.com/cfahlgren1/observers)          | A Lightweight Library for AI Observability.                                                       |

### 2.11 LLM Prompt Engineering

| Library             | Description                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| [PCToolkit](https://github.com/3DAgentWorld/Toolkit-for-Prompt-Compression)          | A Unified Plug-and-Play Prompt Compression Toolkit of Large Language Models.                                   |
| [Selective Context](https://pypi.org/project/selective-context/)  | Selective Context compresses your prompt and context to allow LLMs (such as ChatGPT) to process 2x more content. |
| [LLMLingua](https://github.com/microsoft/LLMLingua)          | Library for compressing prompts to accelerate LLM inference.                                                  |
| [betterprompt](https://github.com/stjordanis/betterprompt)       | Test suite for LLM prompts before pushing them to production.                                                 |
| [Promptify](https://github.com/promptslab/Promptify)         | Solve NLP Problems with LLMs & easily generate different NLP Task prompts for popular generative models like GPT, PaLM, and more with Promptify. |
| [PromptSource](https://pypi.org/project/promptsource/)      | PromptSource is a toolkit for creating, sharing, and using natural language prompts.                          |
| [DSPy](https://github.com/stanfordnlp/dspy)              | DSPy is the open-source framework for programming—rather than prompting—language models.                      |
| [Py-priompt](https://github.com/zenbase-ai/py-priompt)        | Prompt design library.                                                                                        |
| [Promptimizer](https://github.com/hinthornw/promptimizer)      | Prompt optimization library.                                                                                  |

### 2.12 LLM Structured Output Generation

| Library |	Description |
|------------|--------------------------------------------------------|
| [Instructor](https://github.com/instructor-ai/instructor) |	Python library for working with structured outputs from large language models (LLMs). Built on top of Pydantic, it provides a simple, transparent, and user-friendly API. |
| [XGrammar](https://github.com/mlc-ai/xgrammar)   | An open-source library for efficient, flexible, and portable structured generation. |
| [Outlines](https://github.com/dottxt-ai/outlines)   | Robust (structured) text generation |
| [Guidance](https://github.com/guidance-ai/guidance)   | Guidance is an efficient programming paradigm for steering language models. |
| [LMQL](https://github.com/eth-sri/lmql)      | A language for constraint-guided and efficient LLM programming. |
| [Jsonformer](https://github.com/1rgs/jsonformer) | A Bulletproof Way to Generate Structured JSON from Language Models. |

### 2.13 LLM Safety and Security

| Library         | Description  |
|---------------|-----------------------------------------------------------|
| [JailbreakEval](https://github.com/ThuCCSLab/JailbreakEval) | A collection of automated evaluators for assessing jailbreak attempts. |
| [EasyJailbreak](https://github.com/EasyJailbreak/EasyJailbreak) | An easy-to-use Python framework to generate adversarial jailbreak prompts. |
| [Guardrails](https://github.com/guardrails-ai/guardrails)    | Adding guardrails to large language models. |
| [LLM Guard](https://github.com/protectai/llm-guard)     | The Security Toolkit for LLM Interactions. |
| [AuditNLG](https://github.com/salesforce/AuditNLG)      | AuditNLG is an open-source library that can help reduce the risks associated with using generative AI systems for language. |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems. |
| [Garak](https://github.com/NVIDIA/garak)        | LLM vulnerability scanner |

### 2.14 LLM Embedding Models

| Library                   | Description                                         |
|---------------------------|-----------------------------------------------------|
| [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers)     | State-of-the-Art Text Embeddings                   |
| [Model2Vec](https://github.com/MinishLab/model2vec)                | Fast State-of-the-Art Static Embeddings             |
| [Text Embedding Inference](https://github.com/huggingface/text-embeddings-inference) | A blazing fast inference solution for text embeddings models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. |


### 2.15 LLM Learning Resources and Tutorials

This section provides a curated list of resources for learning about Large Language Models (LLMs), covering various topics from fundamental concepts to advanced techniques.

| Title | Topic |
| :--- | :---: |
| [GenAI HuggingFace - Fine Tuning](https://github.com/huggingface/smol-course) | Fine Tuning |
| [NLP + GENAI HuggingFace - All topics](https://huggingface.co/learn/nlp-course/en/chapter1/1?fw=pt) | All topics |
| [GenAI Groq - AI Agents](https://github.com/neural-maze/agentic_patterns) | AI Agents |
| [GenAI Parlance - RAG Evals Finetuning- Videos](https://parlance-labs.com/education/) | RAG Evals Finetuning- Videos |
| [Data Science Interview Questions & Answers](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers) | Data Science |
| [The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=high_level_overview) |  |
| [vLLM](https://github.com/vllm-project/vllm) |  |
| [Unsloth.ai](https://www.unsloth.ai/introducing) |  |

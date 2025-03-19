# AI-Dev-Kit

A curated collection of tools, libraries, and resources for building AI applications. This includes a focus on Large Language Models (LLMs) and related technologies.


**Quick Navigation**

||||
|---|---|---|
| [🚀 Core AI Development](#1-core-ai-development) | [🤖 LLM-Specific Tools, Resources, and Techniques](#2-llm-specific-tools-resources-and-techniques) | [💾 Data Management and Processing](#data-management-and-processing) |
| [☁️ Deployment and Infrastructure](#deployment-and-infrastructure)| [👁️‍🗨️ Monitoring, Evaluation, and Observability](#monitoring-evaluation-and-observability) |


## 1. Core AI Development

This section provides essential resources for building and deploying AI solutions. It includes fundamental frameworks, libraries, and tools for tasks such as machine learning, data science, computer vision, and natural language processing.

### 1.1 Machine Learning Frameworks

This section lists popular and widely used machine learning frameworks that provide the core tools and functionalities for building and training various AI models. These frameworks offer optimized numerical computation, automatic differentiation, and model building capabilities.

| Framework     | Description                                                                                                                                   | Link                                            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| TensorFlow    | An open-source machine learning framework developed by Google, known for its flexibility, scalability, and support for both CPU and GPU computation. | [Link](https://www.tensorflow.org/)           |
| PyTorch       | An open-source machine learning framework developed by Facebook, known for its dynamic computation graph, ease of use, and strong community support.    | [Link](https://pytorch.org/)                 |
| Scikit-learn  | A simple and efficient library for machine learning in Python, providing a wide range of algorithms for classification, regression, clustering, and dimensionality reduction. | [Link](https://scikit-learn.org/stable/)        |
| JAX           | A high-performance numerical computation library with automatic differentiation, designed for machine learning research and high-performance applications. | [Link](https://jax.readthedocs.io/en/latest/)   |
| Keras         | A high-level API for building and training neural networks. It can run on top of TensorFlow, Theano, or CNTK. Often considered easier to use than raw TensorFlow. | [Link](https://keras.io/)                    |
| XGBoost       | An optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. | [Link](https://xgboost.readthedocs.io/en/stable/) |
| LightGBM      | A gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with faster training speed and higher efficiency. | [Link](https://lightgbm.readthedocs.io/en/latest/) |
| CatBoost      | A gradient boosting library from Yandex. Excellent for handling categorical features directly.                                                                  | [Link](https://catboost.ai/)                 |

### 1.2 Data Science Libraries

This section highlights essential Python libraries used for data manipulation, analysis, visualization, and general data science tasks. These libraries provide powerful tools for working with structured and unstructured data, performing statistical analysis, and creating insightful visualizations.

| Library     | Description                                                                                                                               | Link                                        |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| Pandas        | A powerful library for data manipulation and analysis, providing data structures like DataFrames for working with tabular data.               | [Link](https://pandas.pydata.org/)          |
| NumPy         | The fundamental package for numerical computation in Python, providing support for arrays, matrices, and mathematical functions.              | [Link](https://numpy.org/)                 |
| Matplotlib    | A comprehensive library for creating static, interactive, and animated visualizations in Python.                                            | [Link](https://matplotlib.org/)            |
| Seaborn       | A high-level data visualization library based on Matplotlib, providing a more aesthetically pleasing and informative interface for statistical graphics. | [Link](https://seaborn.pydata.org/)           |
| Scikit-learn  | While listed as a Machine Learning Framework, it also provides a wealth of tools for data preprocessing, feature selection, and model evaluation crucial for data science.  | [Link](https://scikit-learn.org/stable/)      |
| SciPy         | A library for scientific computing and technical computing, providing algorithms for optimization, integration, interpolation, linear algebra, and more. | [Link](https://scipy.org/)                  |
| Statsmodels   | A library for estimating and testing statistical models, providing tools for regression analysis, time series analysis, and hypothesis testing.  | [Link](https://www.statsmodels.org/stable/) |
| Plotly        | An interactive visualization library that allows users to create web-based plots and dashboards.                                         | [Link](https://plotly.com/)                 |
| Bokeh         | Another interactive visualization library that focuses on creating web-based applications and dashboards.                                     | [Link](https://bokeh.org/)                  |
| Datatable     | A fast and memory-efficient library for large datasets, designed to handle data manipulation and analysis with speed and scalability.       | [Link](https://datatable.readthedocs.io/)    |
| Vaex          | A library for lazy, out-of-core dataframes to visualize and explore large tabular datasets.                                                  | [Link](https://vaex.io/)                     |

### 1.3 Optimization Libraries

This section features libraries designed to optimize machine learning models and training processes. These libraries offer functionalities like hyperparameter tuning, distributed training, and efficient resource utilization, helping to improve model performance and reduce training time.

| Library     | Description                                                                                                                                   | Link                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Optuna        | An automatic hyperparameter optimization framework, featuring define-by-run API and efficient search algorithms.                             | [Link](https://optuna.org/)                  |
| Ray Tune      | A scalable hyperparameter tuning framework built on Ray, supporting distributed training and various optimization algorithms.                   | [Link](https://www.ray.io/tune)              |
| Hyperopt      | A Python library for serial and parallel optimization over awkward search spaces (including real-valued, discrete, and conditional dimensions). | [Link](http://hyperopt.github.io/hyperopt/)     |
| Scikit-optimize| Sequential model-based optimization with a `scikit-learn` interface. Great for optimizing machine learning hyperparameters.                   | [Link](https://scikit-optimize.github.io/stable/) |
| Ax            | A platform for understanding and improving the performance of any system through adaptive experimentation.  Good for bandit optimization and A/B testing. | [Link](https://ax.dev/)                        |
| Nevergrad     | A gradient-free optimization platform.                                                                                                   | [Link](https://facebookresearch.github.io/nevergrad/) |
| PySOT         | Python Surrogate Optimization Toolbox:  A collection of derivative-free optimization algorithms.                                           | [Link](https://py-sot.readthedocs.io/en/latest/)  |

### 1.4 Computer Vision

This section showcases libraries and tools for developing computer vision applications. These libraries provide functionalities for image processing, object detection, image segmentation, image generation, and other computer vision tasks.

| Library           | Description                                                                                                                                   | Link                                                |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| OpenCV            | A comprehensive library for real-time computer vision, image processing, and video analysis, providing a wide range of algorithms and functionalities. | [Link](https://opencv.org/)                        |
| PyTorch Vision    | A part of the PyTorch ecosystem, providing datasets, model architectures, and image transformations for computer vision tasks.                    | [Link](https://pytorch.org/vision/stable/index.html)  |
| TensorFlow Graphics | A library for computer graphics in TensorFlow, enabling differentiable rendering, 3D object manipulation, and other graphics-related tasks.    | [Link](https://www.tensorflow.org/graphics)          |
| SimpleCV          | An open source framework that gives computer vision superpowers to Python, with a clean, simple interface to CV libraries such as OpenCV.   | [Link](http://simplecv.org/)                       |
| Scikit-image      | A collection of algorithms for image processing, providing tools for image filtering, segmentation, feature extraction, and more.        | [Link](https://scikit-image.org/)                  |
| Detectron2        | Facebook AI Research's next-generation library that provides state-of-the-art detection and segmentation algorithms.                              | [Link](https://github.com/facebookresearch/detectron2) |
| Kornia            | A differentiable computer vision library for PyTorch.                                                                                           | [Link](https://kornia.readthedocs.io/en/latest/)     |
| Albumentations  | Fast image augmentation library and easy to use wrapper around other libraries.                                                                | [Link](https://albumentations.ai/)                |

### 1.5 Natural Language Processing (General)

This section lists general-purpose libraries for Natural Language Processing (NLP). These libraries provide tools for tasks like text processing, tokenization, part-of-speech tagging, named entity recognition, and general-purpose language understanding, forming the foundation for more specialized NLP applications.

| Library       | Description                                                                                                                                   | Link                                            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| spaCy         | A library for advanced Natural Language Processing in Python, designed for production use. Provides fast and accurate tokenization, POS tagging, NER, and more. | [Link](https://spacy.io/)                     |
| NLTK          | The Natural Language Toolkit, a leading platform for building Python programs to work with human language data. Provides easy-to-use interfaces to over 50 corpora and lexical resources. | [Link](https://www.nltk.org/)                  |
| Gensim        | A library for topic modeling, document indexing, and similarity retrieval with large text corpora. Good for unsupervised text analysis.     | [Link](https://radimrehurek.com/gensim/)        |
| Transformers  | While this also goes in the LLM section, the Transformers library provides core NLP components for tasks like tokenization, model loading, and sequence processing that are relevant even outside of just LLMs. | [Link](https://huggingface.co/transformers/)    |
| TextBlob      | A Python library for processing textual data. It provides a simple API for diving into common NLP tasks.   Often used for prototyping and educational purposes. | [Link](https://textblob.readthedocs.io/en/dev/) |
| CoreNLP      | Stanford CoreNLP provides a set of human language technology tools.    Offers a lot of linguistic analysis, but is Java-based (with Python wrappers). | [Link](https://stanfordnlp.github.io/CoreNLP/) |
| AllenNLP      | An NLP research library, built on PyTorch, designed to be modular and extensible, making it suitable for prototyping and experimenting with new NLP models. | [Link](https://allennlp.org/)                  |
| Hugging Face Tokenizers | Provides fast tokenizers, written in Rust. | [Link](https://github.com/huggingface/tokenizers) |

## 2. LLM-Specific Tools, Resources, and Techniques

This section focuses on libraries, tools, and techniques specifically designed for working with Large Language Models (LLMs). It covers aspects such as training, fine-tuning, application development, RAG, inference, deployment, security, and more.

### 2.1 LLM Training and Fine-Tuning

This section lists libraries that facilitate the training and fine-tuning of Large Language Models (LLMs), allowing you to customize pre-trained models for specific tasks and datasets.

| Library             | Description                                                                                     | Link |
|---------------------|-------------------------------------------------------------------------------------------------|------|
| unsloth            | Fine-tune LLMs faster with less memory.                                                          | [Link](https://github.com/unslothai/unsloth) |
| PEFT                | State-of-the-art Parameter-Efficient Fine-Tuning library.                                       | [Link](https://github.com/huggingface/peft) |
| TRL                 | Train transformer language models with reinforcement learning.                                  | [Link](https://github.com/huggingface/trl) |
| Transformers       | Transformers provides thousands of pretrained models to perform tasks on different modalities such as text, vision, and audio. | [Link](https://github.com/huggingface/transformers) |
| Axolotl           | Tool designed to streamline post-training for various AI models.                                 | [Link](https://github.com/axolotl-ai-cloud/axolotl/) |
| LLMBox             | A comprehensive library for implementing LLMs, including a unified training pipeline and comprehensive model evaluation. | [Link](https://github.com/RUCAIBox/LLMBox) |
| LitGPT             | Train and fine-tune LLM lightning fast.                                                          | [Link](https://github.com/Lightning-AI/litgpt) |
| Mergoo            | A library for easily merging multiple LLM experts, and efficiently train the merged LLM.         | [Link](https://github.com/Leeroo-AI/mergoo) |
| Llama-Factory      | Easy and efficient LLM fine-tuning.                                                              | [Link](https://github.com/hiyouga/LLaMA-Factory) |
| Ludwig            | Low-code framework for building custom LLMs, neural networks, and other AI models.               | [Link](https://github.com/ludwig-ai/ludwig) |
| Txtinstruct       | A framework for training instruction-tuned models.                                               | [Link](https://github.com/neuml/txtinstruct) |
| Lamini            | An integrated LLM inference and tuning platform.                                                 | [Link](https://github.com/lamini-ai/lamini) |
| XTuring           | xTuring provides fast, efficient and simple fine-tuning of open-source LLMs, such as Mistral, LLaMA, GPT-J, and more. | [Link](https://github.com/stochasticai/xTuring) |
| RL4LMs            | A modular RL library to fine-tune language models to human preferences.                          | [Link](https://github.com/allenai/RL4LMs) |
| DeepSpeed         | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. | [Link](https://github.com/deepspeedai/DeepSpeed) |
| torchtune         | A PyTorch-native library specifically designed for fine-tuning LLMs.                             | [Link](https://github.com/pytorch/torchtune) |
| PyTorch Lightning | A library that offers a high-level interface for pretraining and fine-tuning LLMs.               | [Link](https://github.com/Lightning-AI/pytorch-lightning) |

### 2.2 LLM Application Development

This section features frameworks, libraries, and tools designed for building applications powered by Large Language Models (LLMs).

#### 2.2.1 Frameworks

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| LangChain    | LangChain is a framework for developing applications powered by large language models (LLMs).          | [Link](https://github.com/langchain-ai/langchain) |
| Llama Index  | LlamaIndex is a data framework for your LLM applications.                                              | [Link](https://github.com/run-llama/llama_index) |
| HayStack     | Haystack is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. | [Link](https://github.com/deepset-ai/haystack) |
| Prompt flow  | A suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications. | [Link](https://github.com/microsoft/promptflow) |
| Griptape     | A modular Python framework for building AI-powered applications.                                        | [Link](https://github.com/griptape-ai/griptape) |
| Weave        | Weave is a toolkit for developing Generative AI applications.                                          | [Link](https://github.com/wandb/weave) |
| Llama Stack  | Build Llama Apps.                                                                                      | [Link](https://github.com/meta-llama/llama-stack) |

#### 2.2.2 Multi API Access

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| LiteLLM      | Library to call 100+ LLM APIs in OpenAI format.                                                        | [Link](https://github.com/BerriAI/litellm) |
| AI Gateway   | A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.                                                 | [Link](https://github.com/Portkey-AI/gateway) |

#### 2.2.3 Routers

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| RouteLLM     | Framework for serving and evaluating LLM routers - save LLM costs without compromising quality. Drop-in replacement for OpenAI's client to route simpler queries to cheaper models.                                                      | [Link](https://github.com/lm-sys/RouteLLM) |

#### 2.2.4 Memory

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| mem0         | The Memory layer for your AI apps.                                                                     | [Link](https://github.com/mem0ai/mem0) |
| Memoripy     | An AI memory layer with short- and long-term storage, semantic clustering, and optional memory decay for context-aware applications. | [Link](https://github.com/caspianmoon/memoripy) |

#### 2.2.5 Interface

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| Streamlit    | A faster way to build and share data apps. Streamlit lets you transform Python scripts into interactive web apps in minutes                                                             | [Link](https://github.com/streamlit/streamlit) |
| Gradio       | Build and share delightful machine learning apps, all in Python.                                       | [Link](https://github.com/gradio-app/gradio) |
| AI SDK UI    | Build chat and generative user interfaces.                                                             | [Link](https://sdk.vercel.ai/docs/introduction) |
| AI-Gradio    | Create AI apps powered by various AI providers.                                                        | [Link](https://github.com/AK391/ai-gradio) |
| Simpleaichat | Python package for easily interfacing with chat apps, with robust features and minimal code complexity. | [Link](https://github.com/minimaxir/simpleaichat) |
| Chainlit     | Build production-ready Conversational AI applications in minutes.                                      | [Link](https://github.com/Chainlit/chainlit) |

#### 2.2.6 Low Code

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| LangFlow     | LangFlow is a low-code app builder for RAG and multi-agent AI applications. It’s Python-based and agnostic to any model, API, or database.                           | [Link](https://github.com/langflow-ai/langflow) |
| n8n          | n8n is a low-code automation tool that allows users to create complex workflows by connecting various applications and services. It offers both self-hosted and cloud-hosted options, with a visual interface.                           | [Link](https://github.com/n8n-io/n8n) |

#### 2.2.7 Cache

| Library        | Description                                                                                               | Link  |
|--------------|------------------------------------------------------------------------------------------------------|-------|
| GPTCache     | A Library for Creating Semantic Cache for LLM Queries. Slash Your LLM API Costs by 10x 💰, Boost Speed by 100x. Fully integrated with LangChain and LlamaIndex.                               | [Link](https://github.com/zilliztech/gptcache) |

### 2.3 LLM Retrieval Augmented Generation (RAG)

This section presents libraries focused on Retrieval Augmented Generation (RAG), a technique for enhancing LLMs with external knowledge sources for more accurate and context-aware responses.

| Library         | Description                                                                                                      | Link  |
|---------------|----------------------------------------------------------------------------------------------------------------|-------|
| FastGraph RAG | Streamlined and promptable Fast GraphRAG framework designed for interpretable, high-precision, agent-driven retrieval workflows. | [Link](https://github.com/circlemind-ai/fast-graphrag) |
| Chonkie       | RAG chunking library that is lightweight, lightning-fast, and easy to use.                                      | [Link](https://github.com/chonkie-ai/chonkie) |
| RAGChecker    | A Fine-grained Framework For Diagnosing RAG.                                                                   | [Link](https://github.com/amazon-science/RAGChecker) |
| RAG to Riches | Build, scale, and deploy state-of-the-art Retrieval-Augmented Generation applications.                         | [Link](https://github.com/SciPhi-AI/R2R) |
| BeyondLLM     | Beyond LLM offers an all-in-one toolkit for experimentation, evaluation, and deployment of Retrieval-Augmented Generation (RAG) systems. | [Link](https://github.com/aiplanethub/beyondllm) |
| SQLite-Vec    | A vector search SQLite extension that runs anywhere!                                                           | [Link](https://github.com/asg017/sqlite-vec) |
| fastRAG       | fastRAG is a research framework for efficient and optimized retrieval-augmented generative pipelines, incorporating state-of-the-art LLMs and Information Retrieval. | [Link](https://github.com/IntelLabs/fastRAG) |
| FlashRAG      | A Python Toolkit for Efficient RAG Research.                                                                   | [Link](https://github.com/RUC-NLPIR/FlashRAG) |
| Llmware       | Unified framework for building enterprise RAG pipelines with small, specialized models.                        | [Link](https://github.com/llmware-ai/llmware) |
| Rerankers     | A lightweight unified API for various reranking models.                                                        | [Link](https://github.com/AnswerDotAI/rerankers) |
| Vectara       | Build Agentic RAG applications.                                                                                | [Link](https://vectara.github.io/py-vectara-agentic/latest/) |

### 2.4 LLM Vector Stores

This section lists databases relevant to LLM applications, including specialized vector stores for embedding similarity search and general-purpose databases that may be used for storing LLM-related data or metadata.

| Library      | Description                                                                                                                                   | Deployment     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [Pinecone](https://www.pinecone.io/)      | A managed vector database optimized for similarity search, enabling efficient retrieval of data based on vector embeddings.                  | Cloud (Managed)   |
| [Weaviate](https://weaviate.io/)      | An open-source vector search engine that allows you to store and search data based on vector embeddings.                                       | Self-Hosted/Cloud |
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
*   **Milvus:** A powerful, scalable vector database designed for large-scale deployments. More complex to set up and manage but offers high performance. Can be self-hosted or used via Zilliz Cloud. Uses Vector Similarity Search as its query logic.
*   **Qdrant:** Provides a good balance of performance, scalability, and ease of use. Offers a flexible deployment and rich feature set. Can be self-hosted or used with Qdrant Cloud. Uses Vector Similarity Search as its query logic.
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

This section presents libraries for optimizing the inference process of Large Language Models (LLMs), aiming for faster performance and efficient resource utilization.

| Library         | Description                                                                                               | Link  |
|---------------|------------------------------------------------------------------------------------------------------|-------|
| LLM Compressor | Transformers-compatible library for applying various compression algorithms to LLMs for optimized deployment. | [Link](https://github.com/vllm-project/llm-compressor) |
| LightLLM      | Python-based LLM inference and serving framework, notable for its lightweight design, easy scalability, and high-speed performance. | [Link](https://github.com/ModelTC/lightllm) |
| vLLM         | High-throughput and memory-efficient inference and serving engine for LLMs.                            | [Link](https://github.com/vllm-project/vllm) |
| torchchat     | Run PyTorch LLMs locally on servers, desktop, and mobile.                                              | [Link](https://github.com/pytorch/torchchat) |
| TensorRT-LLM  | TensorRT-LLM is a library for optimizing Large Language Model (LLM) inference.                        | [Link](https://github.com/NVIDIA/TensorRT-LLM) |
| WebLLM        | High-performance In-browser LLM Inference Engine.                                                     | [Link](https://github.com/mlc-ai/web-llm) |

### 2.6 LLM Serving

This section highlights libraries for serving Large Language Models (LLMs) in a production environment, enabling you to deploy and manage LLMs for real-world applications.

| Library   | Description                                                              | Link  |
|-----------|--------------------------------------------------------------------------|-------|
| Langcorn  | Serving LangChain LLM apps and agents automagically with FastAPI.       | [Link](https://github.com/msoedov/langcorn) |
| LitServe  | Lightning-fast serving engine for any AI model of any size. It augments FastAPI with features like batching, streaming, and GPU autoscaling.           | [Link](https://github.com/Lightning-AI/LitServe) |

### 2.7 LLM Data Handling (Extraction & Generation)

This section combines tools for both extracting data to feed into LLMs and generating new data using LLMs.

#### 2.7.1 LLM Data Extraction

This section provides libraries for extracting data from various sources (web pages, documents, etc.) to be used as input for Large Language Models (LLMs).

| Library         | Description                                                                                                                           | Link  |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|-------|
| Crawl4AI       | Open-source LLM Friendly Web Crawler & Scraper.                                                                                      | [Link](https://github.com/unclecode/crawl4ai) |
| ScrapeGraphAI  | A web scraping Python library that uses LLM and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.). | [Link](https://github.com/ScrapeGraphAI/Scrapegraph-ai) |
| Docling        | Docling parses documents and exports them to the desired format with ease and speed.                                                  | [Link](https://github.com/DS4SD/docling) |
| Llama Parse    | GenAI-native document parser that can parse complex document data for any downstream LLM use case (RAG, agents).                     | [Link](https://github.com/run-llama/llama_cloud_services) |
| PyMuPDF4LLM    | PyMuPDF4LLM library makes it easier to extract PDF content in the format you need for LLM & RAG environments.                        | [Link](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) |
| Crawlee        | A web scraping and browser automation library.                                                                                         | [Link](https://github.com/apify/crawlee-python) |
| MegaParse      | Parser for every type of document.                                                                                                    | [Link](https://github.com/quivrhq/megaparse) |
| ExtractThinker | Document Intelligence library for LLMs.                                                                                               | [Link](https://github.com/enoch3712/ExtractThinker) |

#### 2.7.2 LLM Data Generation

This section features libraries for generating synthetic data or augmenting existing datasets using Large Language Models (LLMs).

| Library       | Description                                                                                          | Link  |
|--------------|--------------------------------------------------------------------------------------------------|-------|
| DataDreamer  | DataDreamer is a powerful open-source Python library for prompting, synthetic data generation, and training workflows. | [Link](https://github.com/datadreamer-dev/DataDreamer) |
| fabricator   | A flexible open-source framework to generate datasets with large language models.                   | [Link](https://github.com/flairNLP/fabricator) |
| Promptwright | Synthetic Dataset Generation Library.                                                               | [Link](https://github.com/stacklok/promptwright) |
| EasyInstruct | An Easy-to-use Instruction Processing Framework for Large Language Models.                          | [Link](https://github.com/zjunlp/EasyInstruct) |
| Text Machina| A modular and extensible Python framework, designed to aid in the creation of high-quality, unbiased datasets to build robust models for MGT-related tasks such as detection, attribution, and boundary detection. | [Link](https://github.com/Genaios/TextMachina) |

### 2.8 LLM Agents

This section showcases libraries for building autonomous agents powered by Large Language Models (LLMs), enabling them to perform complex tasks and interact with their environment.

| Library         | Description                                                                                                 | Link  |
|----------------|---------------------------------------------------------------------------------------------------------|-------|
| CrewAI        | Framework for orchestrating role-playing, autonomous AI agents.                                          | [Link](https://github.com/crewAIInc/crewAI) |
| LangGraph     | Build resilient language agents as graphs.                                                               | [Link](https://github.com/langchain-ai/langgraph) |
| Agno          | Build AI Agents with memory, knowledge, tools, and reasoning. Chat with them using a beautiful Agent UI.  | [Link](https://github.com/agno-agi/agno) |
| AutoGen       | An open-source framework for building AI agent systems.                                                  | [Link](https://github.com/microsoft/autogen) |
| Smolagents    | Library to build powerful agents in a few lines of code.                                                 | [Link](https://github.com/huggingface/smolagents) |
| Pydantic AI | Python agent framework to build production grade applications with Generative AI. | [Link](https://ai.pydantic.dev/) |
| gradio-tools  | A Python library for converting Gradio apps into tools that can be leveraged by an LLM-based agent to complete its task. | [Link](https://github.com/freddyaboulton/gradio-tools) |
| Composio      | Production Ready Toolset for AI Agents.                                                                  | [Link](https://github.com/ComposioHQ/composio) |
| Atomic Agents | Building AI agents, atomically.                                                                         | [Link](https://github.com/BrainBlend-AI/atomic-agents) |
| Memary        | Open Source Memory Layer For Autonomous Agents.                                                          | [Link](https://github.com/kingjulio8238/Memary) |
| Browser Use   | Make websites accessible for AI agents.                                                                 | [Link](https://github.com/browser-use/browser-use) |
| OpenWebAgent   | An Open Toolkit to Enable Web Agents on Large Language Models.                                           | [Link](https://github.com/THUDM/OpenWebAgent/) |
| Lagent        | A lightweight framework for building LLM-based agents.                                                   | [Link](https://github.com/InternLM/lagent) |
| LazyLLM       | A Low-code Development Tool For Building Multi-agent LLMs Applications.                                  | [Link](https://github.com/LazyAGI/LazyLLM) |
| Swarms        | The Enterprise-Grade Production-Ready Multi-Agent Orchestration Framework.                               | [Link](https://github.com/kyegomez/swarms) |
| ChatArena     | ChatArena is a library that provides multi-agent language game environments and facilitates research about autonomous LLM agents and their social interactions. | [Link](https://github.com/Farama-Foundation/chatarena) |
| Swarm         | Educational framework exploring ergonomic, lightweight multi-agent orchestration.                        | [Link](https://github.com/openai/swarm) |
| AgentStack    | The fastest way to build robust AI agents.                                                               | [Link](https://github.com/AgentOps-AI/AgentStack) |
| Archgw        | Intelligent gateway for Agents.                                                                          | [Link](https://github.com/katanemo/archgw) |
| Flow          | A lightweight task engine for building AI agents.                                                        | [Link](https://github.com/lmnr-ai/flow) |
| AgentOps      | Python SDK for AI agent monitoring.                                                                      | [Link](https://github.com/AgentOps-AI/agentops) |
| Langroid      | Multi-Agent framework.                                                                                   | [Link](https://github.com/langroid/langroid) |
| Agentarium    | Framework for creating and managing simulations populated with AI-powered agents.                        | [Link](https://github.com/Thytu/Agentarium) |
| Upsonic       | Reliable AI agent framework that supports MCP.                                                          | [Link](https://github.com/upsonic/upsonic) |

### 2.9 LLM Evaluation

This section lists libraries and tools for evaluating the performance and quality of Large Language Models (LLMs).

| Library     | Description                                                                                                         | Link  |
|------------|-----------------------------------------------------------------------------------------------------------------|-------|
| Ragas      | Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications.            | [Link](https://github.com/explodinggradients/ragas) |
| Giskard    | Open-Source Evaluation & Testing for ML & LLM systems.                                                           | [Link](https://github.com/Giskard-AI/giskard) |
| DeepEval | LLM Evaluation Framework | [Link](https://github.com/confident-ai/deepeval) |
| Lighteval  | All-in-one toolkit for evaluating LLMs.                                                                         | [Link](https://github.com/huggingface/lighteval) |
| Trulens | Evaluation and Tracking for LLM Experiments | [Link](https://github.com/truera/trulens) |
| PromptBench | A unified evaluation framework for large language models.                                                        | [Link](https://github.com/microsoft/promptbench) |
| LangTest   | Deliver Safe & Effective Language Models. 60+ Test Types for Comparing LLM & NLP Models on Accuracy, Bias, Fairness, Robustness & More. | [Link](https://github.com/JohnSnowLabs/langtest) |
| EvalPlus   | A rigorous evaluation framework for LLM4Code.                                                                    | [Link](https://github.com/evalplus/evalplus) |
| FastChat   | An open platform for training, serving, and evaluating large language model-based chatbots.                      | [Link](https://github.com/lm-sys/FastChat) |
| judges     | A small library of LLM judges.                                                                                   | [Link](https://github.com/quotient-ai/judges) |
| Evals      | Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks.            | [Link](https://github.com/openai/evals) |
| AgentEvals | Evaluators and utilities for evaluating the performance of your agents.                                         | [Link](https://github.com/langchain-ai/agentevals) |
| LLMBox     | A comprehensive library for implementing LLMs, including a unified training pipeline and comprehensive model evaluation. | [Link](https://github.com/RUCAIBox/LLMBox) |
| Opik       | An open-source end-to-end LLM Development Platform which also includes LLM evaluation.                           | [Link](https://github.com/comet-ml/opik) |
| pandas-ai   | Chat with your database (SQL, CSV, pandas, polars, MongoDB, NoSQL, etc.). | [Link](https://github.com/Sinaptik-AI/pandas-ai) |

### 2.10 LLM Monitoring

This section presents libraries and platforms for monitoring the performance, health, and usage of Large Language Models (LLMs) in production.

| Library              | Description                                                                                       | Link  |
|----------------------|-------------------------------------------------------------------------------------------------|-------|
| Opik                | An open-source end-to-end LLM Development Platform which also includes LLM monitoring.          | [Link](https://github.com/comet-ml/opik) |
| LangSmith           | Provides tools for logging, monitoring, and improving your LLM applications.                     | [Link](https://github.com/langchain-ai/langsmith-sdk) |
| Weights & Biases (W&B) | W&B provides features for tracking LLM performance.                                          | [Link](https://github.com/wandb) |
| Helicone            | Open source LLM-Observability Platform for Developers. One-line integration for monitoring, metrics, evals, agent tracing, prompt management, playground, etc. | [Link](https://github.com/Helicone/helicone) |
| Evidently          | An open-source ML and LLM observability framework.                                                | [Link](https://github.com/evidentlyai/evidently) |
| Phoenix            | An open-source AI observability platform designed for experimentation, evaluation, and troubleshooting. | [Link](https://github.com/Arize-ai/phoenix) |
| Observers          | A Lightweight Library for AI Observability.                                                       | [Link](https://github.com/cfahlgren1/observers) |

### 2.11 LLM Prompt Engineering

This section highlights libraries and tools that assist in crafting effective prompts for Large Language Models (LLMs), optimizing the LLM's output.

| Library             | Description                                                                                                      | Link  |
|---------------------|----------------------------------------------------------------------------------------------------------------|-------|
| PCToolkit          | A Unified Plug-and-Play Prompt Compression Toolkit of Large Language Models.                                   | [Link](https://github.com/3DAgentWorld/Toolkit-for-Prompt-Compression) |
| Selective Context  | Selective Context compresses your prompt and context to allow LLMs (such as ChatGPT) to process 2x more content. | [Link](https://pypi.org/project/selective-context/) |
| LLMLingua          | Library for compressing prompts to accelerate LLM inference.                                                  | [Link](https://github.com/microsoft/LLMLingua) |
| betterprompt       | Test suite for LLM prompts before pushing them to production.                                                 | [Link](https://github.com/stjordanis/betterprompt) |
| Promptify         | Solve NLP Problems with LLMs & easily generate different NLP Task prompts for popular generative models like GPT, PaLM, and more with Promptify. | [Link](https://github.com/promptslab/Promptify) |
| PromptSource      | PromptSource is a toolkit for creating, sharing, and using natural language prompts.                          | [Link](https://pypi.org/project/promptsource/) |
| DSPy              | DSPy is the open-source framework for programming—rather than prompting—language models.                      | [Link](https://github.com/stanfordnlp/dspy) |
| Py-priompt        | Prompt design library.                                                                                        | [Link](https://github.com/zenbase-ai/py-priompt) |
| Promptimizer      | Prompt optimization library.                                                                                  | [Link](https://github.com/hinthornw/promptimizer) |

### 2.12 LLM Structured Output Generation

This section features libraries for guiding Large Language Models (LLMs) to generate structured outputs, such as JSON or other specific formats.

| Library |	Description |	Link |
|------------|--------------------------------------------------------|------|
| Instructor |	Python library for working with structured outputs from large language models (LLMs). Built on top of Pydantic, it provides a simple, transparent, and user-friendly API. | [Link](https://github.com/instructor-ai/instructor) |
| XGrammar   | An open-source library for efficient, flexible, and portable structured generation. | [Link](https://github.com/mlc-ai/xgrammar) |
| Outlines   | Robust (structured) text generation | [Link](https://github.com/dottxt-ai/outlines) |
| Guidance   | Guidance is an efficient programming paradigm for steering language models. | [Link](https://github.com/guidance-ai/guidance) |
| LMQL      | A language for constraint-guided and efficient LLM programming. | [Link](https://github.com/eth-sri/lmql) |
| Jsonformer | A Bulletproof Way to Generate Structured JSON from Language Models. | [Link](https://github.com/1rgs/jsonformer) |

### 2.13 LLM Safety and Security

This section lists libraries for enhancing the safety and security of Large Language Models (LLMs), mitigating risks such as jailbreaking, prompt injection, and the generation of harmful content.

| Library         | Description  | Link |
|---------------|-----------------------------------------------------------|------|
| JailbreakEval | A collection of automated evaluators for assessing jailbreak attempts. | [Link](https://github.com/ThuCCSLab/JailbreakEval) |
| EasyJailbreak | An easy-to-use Python framework to generate adversarial jailbreak prompts. | [Link](https://github.com/EasyJailbreak/EasyJailbreak) |
| Guardrails    | Adding guardrails to large language models. | [Link](https://github.com/guardrails-ai/guardrails) |
| LLM Guard     | The Security Toolkit for LLM Interactions. | [Link](https://github.com/protectai/llm-guard) |
| AuditNLG      | AuditNLG is an open-source library that can help reduce the risks associated with using generative AI systems for language. | [Link](https://github.com/salesforce/AuditNLG) |
| NeMo Guardrails | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems. | [Link](https://github.com/NVIDIA/NeMo-Guardrails) |
| Garak        | LLM vulnerability scanner | [Link](https://github.com/NVIDIA/garak) |

### 2.14 LLM Embedding Models

This section presents libraries for generating text embeddings, which are vector representations of text used to capture semantic meaning and facilitate various NLP tasks.

| Library                   | Description                                         | Link |
|---------------------------|-----------------------------------------------------|------|
| Sentence-Transformers     | State-of-the-Art Text Embeddings                   | [Link](https://github.com/UKPLab/sentence-transformers) |
| Model2Vec                | Fast State-of-the-Art Static Embeddings             | [Link](https://github.com/MinishLab/model2vec) |
| Text Embedding Inference | A blazing fast inference solution for text embeddings models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. | [Link](https://github.com/huggingface/text-embeddings-inference) |

### 2.15 LLM Learning Resources and Tutorials

Title | Topic | Link |
| :---         |     :---:      |          ---: |
| GenAI HuggingFace   | Fine Tuning     | [Link](https://github.com/huggingface/smol-course)    |
| NLP + GENAI HuggingFace   | All topics     | [Link](https://huggingface.co/learn/nlp-course/en/chapter1/1?fw=pt)    |
| GenAI Groq |  AI Agents | [Link](https://github.com/neural-maze/agentic_patterns) |
| GenAI Parlance | RAG Evals Finetuning- Videos | [Link](https://parlance-labs.com/education/)  |
| Interview     | Data Science     | [Link](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers)      |
|| The Ultra-Scale Playbook:
| Training LLMs on GPU Clusters |  | [Link](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=high_level_overview) |
|| vLLM | | [Link](https://github.com/vllm-project/vllm) |
|| Unsloth.ai | | [Link](https://www.unsloth.ai/introducing) |

### 2.16  LLM-Specific Integrations

This section will list LLM related items that could not find a better location to fit into.

| Library       | Description                                                                                                                                   | Link                                            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| LLM Reasoners          | A library for advanced large language model reasoning. | [Link](https://github.com/maitrix-org/llm-reasoners) |

## 3. Data Management and Processing

This section provides a comprehensive collection of tools and libraries designed to streamline data management and processing workflows in AI projects. It encompasses data ingestion, cleaning, transformation, storage, versioning, and related tasks.

### 3.1 Data Ingestion

This section lists tools and libraries for ingesting data from various sources into your AI pipelines, enabling you to collect and consolidate data from diverse systems and formats.

| Library     | Description                                                                                                                                   | Link                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Airbyte       | An open-source data integration platform that helps you consolidate data from different sources into data warehouses, lakes, and databases.  | [Link](https://airbyte.com/)                  |
| Singer        | An open-source standard for writing scripts that extract data from any source and load it into any destination.                                 | [Link](https://www.singer.io/)               |
| Apache NiFi   | A dataflow system that automates the movement of data between disparate systems.                                                                | [Link](https://nifi.apache.org/)             |
| Logstash      | A data processing pipeline tool that ingests data from various sources, transforms it, and sends it to a stash like Elasticsearch.        | [Link](https://www.elastic.co/logstash)      |
| Apache Kafka  | A distributed streaming platform for building real-time data pipelines and streaming applications.                                                 | [Link](https://kafka.apache.org/)            |

### 3.2 Data Cleaning/Transformation

This section features libraries and tools for cleaning, transforming, and preparing data for machine learning and AI applications. It includes functionalities for data validation, standardization, and feature engineering.

| Library     | Description                                                                                                                                   | Link                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Great Expectations | A library for data validation, providing a standardized way to test and document your data pipelines.                                            | [Link](https://greatexpectations.io/)            |
| Dask          | A parallel computing library that extends the functionality of NumPy and Pandas to larger-than-memory datasets, enabling scalable data processing. | [Link](https://www.dask.org/)                     |
| Apache Beam   | A unified programming model for batch and stream data processing, allowing you to run data pipelines on various execution environments.                 | [Link](https://beam.apache.org/)                   |
| Pandas        | While also in the Data Science section, Pandas offers robust data manipulation capabilities, including cleaning, filtering, and transformation.         | [Link](https://pandas.pydata.org/)                |
| Pyjanitor     | A cleaning tool built on Pandas that provides a chainable API of convenient data cleaning functions. | [Link](https://pyjanitor-devs.github.io/pyjanitor/) |

### 3.3 Feature Stores

This section lists feature stores, which are centralized repositories for storing, managing, and serving machine learning features. They help ensure consistency, reusability, and discoverability of features across different AI projects.

| Library     | Description                                                                                                                                   | Link                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Feast         | An open-source feature store for managing and serving machine learning features in real-time.                                                    | [Link](https://feast.dev/)            |
| Tecton        | A commercial feature store platform that provides a centralized repository for storing and serving machine learning features.                        | [Link](https://www.tecton.ai/)        |
| Hopsworks    | A data-intensive platform for building and deploying machine learning models, including a feature store, data lake, and model serving capabilities. | [Link](https://www.hopsworks.ai/)     |
| Michelangelo  | Uber's internal machine learning platform, including a feature store, data lake, and model serving capabilities.                                  | (No Public Link - Uber Internal)       |

### 3.4 Data Versioning

This section features tools for versioning data, enabling you to track changes to your datasets over time and ensure reproducibility in your AI experiments.

| Library     | Description                                                                                                                                   | Link                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| DVC           | Data Version Control, a system for managing data and machine learning models, providing versioning, reproducibility, and collaboration features. | [Link](https://dvc.org/)                     |
| Pachyderm     | A data lineage and data versioning platform for building reproducible machine learning pipelines.                                               | [Link](https://www.pachyderm.com/)           |
| LakeFS        | An open-source data lake version control system that allows you to manage and version your data lake as if it were code.                       | [Link](https://lakefs.io/)                  |


### 3.5 Data Warehouses

This section features data warehouses, which are central repositories for storing and analyzing large volumes of structured and semi-structured data, enabling business intelligence and data-driven decision-making.

| Library     | Description                                                                                                                                   | Link                                     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| Snowflake     | A cloud-based data warehouse platform that provides scalable storage and compute resources for data analytics.                                    | [Link](https://www.snowflake.com/)      |
| Google BigQuery| A fully-managed, serverless data warehouse that enables scalable analysis over petabytes of data.                                                | [Link](https://cloud.google.com/bigquery) |
| Amazon Redshift| A fully managed, petabyte-scale data warehouse service in the cloud.                                                                              | [Link](https://aws.amazon.com/redshift/)  |

## 4. Deployment and Infrastructure

This section provides an overview of deployment and infrastructure resources for AI applications. It encompasses model serving frameworks, containerization technologies, cloud platforms, edge deployment tools, MLOps platforms, and serverless computing options.

### 4.1 Model Serving Frameworks

This section lists frameworks for deploying and serving machine learning models in a production environment, ensuring high performance, scalability, and reliability.

| Library               | Description                                                                                                                                   | Link                                                |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| TensorFlow Serving    | A flexible, high-performance serving system for machine learning models, designed for production environments.                              | [Link](https://www.tensorflow.org/tfx/serving)       |
| TorchServe            | A PyTorch-native model serving framework that makes it easy to deploy and serve PyTorch models at scale.                                      | [Link](https://pytorch.org/serve/)                  |
| ONNX Runtime          | A cross-platform inference and training accelerator for machine learning models, supporting a wide range of hardware and software platforms. | [Link](https://onnxruntime.ai/)                     |
| Clipper               | A prediction serving system that enables you to deploy and manage machine learning models from various frameworks.                             | [Link](https://www.cs.berkeley.edu/~matei/projects/clipper.html) |
| Seldon Core        | Kubernetes Model Serving. Open source framework for deploying machine learning models on Kubernetes. | [Link](https://www.seldon.io/) |

### 4.2 Containerization

This section features containerization technologies that package AI applications and their dependencies into isolated containers, ensuring consistency and portability across different environments.

| Library     | Description                                                                                                                                   | Link                                        |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| Docker        | A platform for building, shipping, and running applications in containers, providing isolation, portability, and reproducibility.                  | [Link](https://www.docker.com/)             |
| Kubernetes    | An open-source container orchestration system that automates the deployment, scaling, and management of containerized applications.           | [Link](https://kubernetes.io/)              |
| Podman        | A container engine that doesn't require a daemon to run containers, offering a lightweight and secure alternative to Docker.                    | [Link](https://podman.io/)                |

### 4.3 Cloud Platforms

This section lists cloud platforms that offer a comprehensive set of services and infrastructure for building, deploying, and managing AI applications at scale.

| Library               | Description                                                                                                                                   | Link                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| AWS SageMaker         | A fully managed machine learning service that enables data scientists and developers to quickly build, train, and deploy machine learning models. | [Link](https://aws.amazon.com/sagemaker/)   |
| Google AI Platform    | A suite of machine learning services on Google Cloud, providing tools for data preparation, model training, and model serving.                    | [Link](https://cloud.google.com/ai-platform) |
| Azure Machine Learning| A cloud-based machine learning service that enables you to build, train, and deploy machine learning models at scale.                               | [Link](https://azure.microsoft.com/en-us/services/machine-learning/) |
| IBM Watson Machine Learning| A platform to build, train, deploy, and manage machine learning models.                                | [Link](https://www.ibm.com/cloud/machine-learning) |

### 4.4 Edge Deployment

This section features tools and technologies for deploying AI models to edge devices, enabling real-time inference and processing closer to the data source.

| Library                 | Description                                                                                                                                   | Link                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| AWS IoT Greengrass      | A software that extends cloud capabilities to edge devices, enabling local compute, messaging, and data caching for IoT applications.         | [Link](https://aws.amazon.com/greengrass/)       |
| Azure IoT Edge          | A service that enables you to deploy cloud workloads (AI, analytics, custom business logic) to edge devices.                                  | [Link](https://azure.microsoft.com/en-us/services/iot-edge/) |
| TensorFlow Lite         | A lightweight version of TensorFlow designed for deploying machine learning models on mobile and embedded devices.                           | [Link](https://www.tensorflow.org/lite)          |
| Apache TVM              | An open-source deep learning compiler stack for CPUs, GPUs, and specialized accelerators.                                                     | [Link](https://tvm.apache.org/)                  |

### 4.5 MLOps Platforms

This section lists MLOps platforms that provide a unified set of tools and capabilities for managing the entire machine learning lifecycle, from data preparation to model deployment and monitoring.

| Library               | Description                                                                                                                                   | Link                                            |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| MLflow                | An open-source platform for managing the end-to-end machine learning lifecycle, including experiment tracking, model packaging, and deployment. | [Link](https://mlflow.org/)                    |
| Kubeflow              | A machine learning toolkit for Kubernetes, providing components for model training, deployment, and management.                                 | [Link](https://www.kubeflow.org/)               |
| CometML               | A platform for tracking, comparing, and optimizing machine learning experiments.                                                                 | [Link](https://www.comet.com/)                   |
| Weights & Biases (W&B)| A platform for tracking and visualizing machine learning experiments, providing tools for experiment tracking, hyperparameter optimization, and model management. | [Link](https://www.wandb.com/)                 |

### 4.6 Serverless Computing

This section features serverless computing platforms that allow you to run AI applications without managing the underlying infrastructure, providing automatic scaling, cost optimization, and event-driven execution.

| Library               | Description                                                                                                                                   | Link                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| AWS Lambda            | A serverless compute service that lets you run code without provisioning or managing servers.                                                | [Link](https://aws.amazon.com/lambda/)             |
| Google Cloud Functions| A serverless execution environment for building and connecting cloud services.                                                                  | [Link](https://cloud.google.com/functions)         |
| Azure Functions       | A serverless compute service that enables you to run code on-demand without provisioning or managing infrastructure.                            | [Link](https://azure.microsoft.com/en-us/services/functions/) |

## 5. Monitoring, Evaluation, and Observability

This section features tools and libraries for monitoring AI models, evaluating their performance, and ensuring data quality in production. It provides resources for observability, explainability, and continuous improvement.

### 5.1 Model Monitoring

This section lists platforms and libraries for monitoring the performance and behavior of AI models in production, enabling you to detect anomalies, identify degradation, and ensure model reliability.

| Library        | Description                                                                                              | Link                                             |
|----------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Evidently AI    | An open-source ML monitoring framework for analyzing model performance, data quality, and drift.         | [Link](https://www.evidentlyai.com/)             |
| Arize AI      | A platform for monitoring and analyzing machine learning models in production, providing insights into performance, data quality, and explainability. | [Link](https://www.arize.com/)                  |
| WhyLabs       | An AI observability platform for monitoring data and models in production, providing real-time alerts and insights.   | [Link](https://www.whylabs.ai/)               |
| Fiddler AI    | A platform for explaining and monitoring AI models, providing insights into model behavior, fairness, and bias.       | [Link](https://www.fiddler.ai/)               |
| Grafana       | Not specific to AI, but a useful tool for creating dashboards and alerting from time series data.       | [Link](https://grafana.com/)                     |

### 5.2 Data Quality Monitoring

This section highlights tools and libraries for monitoring the quality and integrity of data in AI pipelines, enabling you to detect data anomalies, ensure data consistency, and maintain data reliability.

| Library        | Description                                                                                              | Link                                          |
|----------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Great Expectations | (Also in Data Cleaning), a library for data validation, providing a standardized way to test and document your data pipelines.         | [Link](https://greatexpectations.io/)          |
| Deequ |  A library built on top of Apache Spark for defining and verifying data quality constraints.                   | [Link](https://github.com/awslabs/deequ)      |
| Soda SQL  | A data reliability tool to quickly find, analyze, and resolve data issues.                                 | [Link](https://www.soda.io/soda-sql)           |
| Dbt  | A transformation workflow that lets teams quickly and reliably deploy analytics code. | [Link](https://www.getdbt.com/)  |

### 5.3 Explainable AI (XAI)

This section features libraries and tools for explaining the decisions and behavior of AI models, enabling you to understand how models make predictions, identify biases, and build trust in AI systems.

| Library    | Description                                                                                                 | Link                                    |
|------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| SHAP       | A library for explaining the output of machine learning models using Shapley values, providing insights into feature importance and individual predictions. | [Link](https://shap.readthedocs.io/en/latest/) |
| LIME       | A library for explaining the predictions of machine learning models by approximating them locally with interpretable models.                       | [Link](https://github.com/marcotcr/lime)       |
| InterpretML| A toolkit that contains state-of-the-art machine learning interpretability techniques. | [Link](https://interpret.ml/)  |
| Alibi  | Explainable AI (XAI) for models with text, image and tabular data. | [Link](https://github.com/SeldonIO/alibi) |

### 5.4 A/B Testing

This section lists tools for A/B testing AI models, allowing you to compare the performance of different models and strategies in a production environment and make data-driven decisions.

| Library      | Description                                                                                                 | Link                                 |
|--------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------|
| GrowthBook   | An open-source feature flagging and A/B testing platform.                                                    | [Link](https://www.growthbook.io/)    |
| Statsig      | A feature management and experimentation platform that enables you to run A/B tests and control feature releases. | [Link](https://statsig.com/)         |
| Optimizely   | An experimentation platform for running A/B tests and personalizing experiences on websites and mobile apps.   | [Link](https://www.optimizely.com/)   |
| VWO          | A website optimization platform for running A/B tests, multivariate tests, and personalization campaigns.          | [Link](https://vwo.com/)             |

### 5.5 Logging and Tracing

This section features tools for logging and tracing events in AI applications, enabling you to monitor system behavior, debug issues, and gain insights into performance bottlenecks.

| Library   | Description                                                                                                     | Link                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Jaeger    | A distributed tracing system for monitoring and troubleshooting microservices-based applications.                 | [Link](https://www.jaegertracing.io/) |
| Prometheus| A systems monitoring and alerting toolkit. | [Link](https://prometheus.io/)  |
| Grafana   | (Also in Model Monitoring), a powerful data visualization tool often used for building dashboards with Prometheus data. | [Link](https://grafana.com/)         |
| Zipkin    | A distributed tracing system for gathering timing data needed to troubleshoot latency problems in microservice architectures.  | [Link](https://zipkin.io/)    |

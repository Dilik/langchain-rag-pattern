# Retrieval Augmented Generation with Langchain

## Overview

Retrieval augmented generation (RAG) is a powerfull approach which combines the capabilites of large language models (llms) with the ability to retrieve contextual information from external documents. RAG uses contextual documents to improve understanding and generate accurate responses. Retrieval based approach is very useful for asking questions or generate content from PDFs, videos, web pages, and external databases. By adding external documents, RAG enhances knowledge and provides richer output.

![RAG Pattern](/docs/images/RAG_Pattern.jpg "RAG Pattern")

## Langchain

Langchain is a rapidly growing open source project driven by the surge in interest in LLM's. It empowers developers by connecting your own/external data to language models, such as OpenAI's GPT. There are many large language models that trained offline and generate a text and main challenge for the developers is a tooling to work with these models. Entire ecosystem still developing and there is generally lack of sufficient tools to create complex applications and make production deployments.

Langchain addresses language model challenges, offering tools for tasks like prompt chaining, logging, callbacks, and efficient data connections. It's model-agnostic and supports exploration of various LLM offerings in a single interface. In this repo we will be exploring some of the basic tools to follow the RAG pattern using langchain

### Setup

Setup using devcontainer or venv

#### Devcontainer

- Docker Desktop
- VSCode Devcontainer Extension

#### venv

- python -m venv .venv
- source .venv/bin/activate `(Linux, MacOS)` or .venv/Scripts/activate `(Windows)`
- pip install -U pip wheel setuptools
- pip install -r requirements.txt

#### Azure Resources
- Deploy Azure OpenAI Service - [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)
- Deploy a Model in Azure OpenAI Studio
- More References - [Azure OpenAI Get Started](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line&pivots=programming-language-python)

### Samples

- Samples folder contains some of the basic examples to follow the RAG pattern using langchain using Jupyter notebook. [here](/samples/langchain-samples.ipynb)
  - Extract data from PDF
  - Split data using langchain tools
  - Embed data using using redis
  - Do a similarity search against the redis data
  - Generate text using GPT-3 and redis data as context

### Resources

- [Langchain](https://python.langchain.com/docs/get_started/introduction.html)
- [RAG Pattern](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-retrieval-augmented-generation?view=azureml-api-2)

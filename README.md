# GeoResearch Assistant 🌍

A small Python LLM-powered GeoResearch Assistant that answers questions about geography and climate using Retrieval-Augmented Generation (RAG).

## Features

- 🔍 **Semantic Search**: Uses sentence-transformers for intelligent document retrieval
- 🤖 **Text Generation**: Leverages Flan-T5-small for natural language answers
- 📚 **Knowledge Base**: Includes 35+ curated documents about geography and climate
- 🎯 **RAG Architecture**: Combines retrieval and generation for accurate, contextual answers

## Components

- **`embedder.py`**: Text embedding using sentence-transformers (all-MiniLM-L6-v2)
- **`retriever.py`**: Semantic similarity-based document retrieval
- **`llm_model.py`**: Text generation using Flan-T5-small
- **`geo_assistant.py`**: Main assistant combining retrieval and generation
- **`data.py`**: Sample geographic and climate knowledge base
- **`demo.ipynb`**: Interactive Jupyter notebook demonstration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Eliana-Di-Lodovico/geo-llm-assistant.git
cd geo-llm-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Jupyter Notebook

```bash
jupyter notebook demo.ipynb
```

## Example Questions

- "What is the highest mountain in the world?"
- "Which is the largest ocean on Earth?"
- "How much have global temperatures increased?"
- "What is the Amazon rainforest climate like?"
- "What causes monsoons?"

## How It Works

The assistant uses a RAG (Retrieval-Augmented Generation) approach:

1. **Embedding**: Questions are converted to vectors using sentence-transformers
2. **Retrieval**: Most relevant documents are found using cosine similarity
3. **Generation**: Retrieved context is used by Flan-T5 to generate answers

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- Sentence-Transformers
- NumPy
- Jupyter (for notebook demo)

## License

MIT License - See LICENSE file for details

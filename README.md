# Legal Document Question Answering with Bloom & FAISS

This project implements a question-answering system specialized in Spanish criminal law. It leverages the BigScience BLOOM-560m language model for text generation, multilingual sentence embeddings for document retrieval, and a FAISS vector store to efficiently retrieve relevant legal documents.

---

## Project Overview

The system answers legal questions by retrieving relevant court ruling summaries from a local document database and generating precise, context-aware responses based solely on the retrieved information.

Key features:

- **Model:** Uses the BLOOM-560m transformer model fine-tuned for text generation.
- **Embedding:** Uses a multilingual sentence transformer to embed legal summaries.
- **Retriever:** FAISS vector store to retrieve the top-k most relevant documents.
- **Custom Prompt:** Legal assistant prompt ensuring responses are precise and formal.
- **Documents:** Loads local `.txt` files from the `data/` folder, splits them for better retrieval.

---

## Repository Structure
```
RAG_ONGs
├── config.yml # Configuration file with model, embedding, retriever, and prompt settings
├── create_database.py # Script to load, split, embed, and index documents in FAISS
├── main.py # Main script to run question answering with retrieval
├── data/ # Folder containing legal summary .txt files to be indexed
├── faiss_index/ # Generated local FAISS index folder (created after running create_database.py)
├── requirements.txt # Python dependencies required for the project
└── README.md # This file
```

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/Lauragarcia07/RAG_ONGs.git
cd RAG_ONGs
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```


## Configuration
All model and system parameters are configured in config.yml


## Usage

1. **Create the FAISS vector database from your documents**
Place your legal summary .txt files inside the data/ folder, then run:

```bash
python create_database.py
```

This will:

- Load all .txt files from data/

- Split documents into chunks

- Embed the chunks with the multilingual embedding model

- Create and save a local FAISS index in faiss_index/

2. **Run the Question Answering system**
Run the main script to ask the configured question and get an answer with retrieved documents:

```bash
python main.py
```


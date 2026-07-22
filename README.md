# StudyMate AI

## Overview

StudyMate AI is an AI-powered learning assistant developed to improve the study experience of university students. The application allows users to upload lecture notes in PDF format and interact with the content using Artificial Intelligence. Instead of reading lengthy documents manually, students can generate summaries, ask questions, create quizzes, and reflect on their understanding through an interactive interface.

The project is built using Python and Streamlit with Retrieval-Augmented Generation (RAG) to provide context-aware responses based on uploaded documents.

---

## Objectives

The main objectives of this project are:

- Simplify learning from lecture notes
- Generate concise AI-powered summaries
- Answer questions using uploaded documents
- Create quizzes for self-assessment
- Encourage reflective learning
- Demonstrate the practical use of Large Language Models in education

---

## Features

- Upload lecture notes in PDF format
- Automatic text extraction and preprocessing
- Intelligent document chunking
- Vector database using ChromaDB
- AI-generated document summaries
- Context-aware question answering using RAG
- Automatic quiz generation
- Quiz scoring
- Learning reflection module
- Clean and user-friendly interface

---

## Technologies Used

### Programming Language

- Python 3.12

### Framework

- Streamlit

### AI & Machine Learning

- LangChain
- OpenRouter API
- Groq API
- Sentence Transformers

### Vector Database

- ChromaDB

### PDF Processing

- PyMuPDF
- PyPDF

### Other Libraries

- python-dotenv
- tiktoken

---

## Project Structure

```
StudyMate-AI/
│
├── agents/
├── components/
├── data/
├── pages/
├── prompts/
├── rag/
├── services/
├── tests/
├── utils/
│
├── Home.py
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/roshini-nawanjala/StudyMate-AI.git
```

Move into the project folder.

```bash
cd StudyMate-AI
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys.

Example:

```
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Run the application.

```bash
streamlit run Home.py
```

---

## How the System Works

1. Upload a lecture note in PDF format.
2. The document is processed and converted into text.
3. The text is divided into meaningful chunks.
4. Embeddings are generated and stored in ChromaDB.
5. Users can generate summaries.
6. Users can ask questions related to the uploaded document.
7. The system retrieves relevant content using RAG before generating responses.
8. Users can generate quizzes and receive scores.
9. The reflection module helps users evaluate their learning.

---

## Testing

The project includes unit tests for the core RAG components.

Test coverage includes:

- Chunking
- Embeddings
- Vector Store
- PDF Loader

---

## Future Improvements

Possible future enhancements include:

- Support for DOCX and PowerPoint files
- Voice-based interaction
- Multi-document knowledge base
- Personalized study recommendations
- User authentication
- Learning progress dashboard
- Cloud deployment

---

## Author

**Roshini Nawanjala**

Faculty of Information Technology

Horizon Campus

Sri Lanka
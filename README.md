# StudyMate AI

### An Agentic AI Learning Assistant using Retrieval-Augmented Generation (RAG) and Large Language Models

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.46-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Enabled-success?style=for-the-badge)

StudyMate AI is an AI-powered learning assistant developed using **Streamlit**, **LangChain**, **LangGraph**, and **Large Language Models (LLMs)**. The application leverages a **Retrieval-Augmented Generation (RAG)** architecture to help students interact with lecture materials more effectively.

Users can upload lecture notes in PDF format, generate concise AI-powered summaries, ask context-aware questions, create quizzes, receive automatic quiz reviews with performance feedback, and generate personalized learning reflections based on their quiz results.

The application combines semantic document retrieval using **ChromaDB** with modern language models to deliver accurate, context-aware, and interactive learning support through a clean and user-friendly interface.

---

# Live Demo

**StudyMate AI**

https://studymate-agent.streamlit.app/

---

# GitHub Repository

https://github.com/roshini-nawanjala/StudyMate-AI

# Features

- Upload lecture notes in PDF format
- Automatic PDF text extraction using PyMuPDF
- Intelligent document chunking for semantic retrieval
- Retrieval-Augmented Generation (RAG) for context-aware responses
- AI-powered document summarization
- Context-aware question answering based on uploaded documents
- AI-generated quizzes from lecture content
- Automatic quiz scoring and performance evaluation
- AI-generated quiz review with detailed explanations
- Personalized learning reflections based on quiz performance
- Semantic document retrieval using ChromaDB
- Sentence Transformer embeddings for similarity search
- Multi-agent workflow powered by LangGraph
- Automatic AI provider selection through internal routing
- Clean and user-friendly Streamlit interface

# Technology Stack

## Frontend

- Streamlit

## Backend

- Python 3.12

## AI Framework

- LangChain
- LangGraph

## Large Language Models (LLMs)

- Groq
- OpenRouter

## Retrieval System

- Retrieval-Augmented Generation (RAG)

## Vector Database

- ChromaDB

## Embedding Model

- Sentence Transformers (all-MiniLM-L6-v2)

## PDF Processing

- PyMuPDF
- PyPDF

## Supporting Libraries

- python-dotenv
- tiktoken

# System Architecture

StudyMate AI follows an Agentic Retrieval-Augmented Generation (RAG) architecture that combines document processing, semantic retrieval, vector storage, and Large Language Models to provide intelligent learning assistance.

The system consists of four main layers:

- **Presentation Layer** – Streamlit-based user interface for interacting with learning features.
- **Application Layer** – Coordinates document processing, retrieval, quiz generation, summaries, and reflections.
- **Retrieval Layer** – Performs semantic similarity search using ChromaDB and Sentence Transformer embeddings.
- **AI Layer** – Automatically routes requests to the configured Large Language Model for response generation.

The architecture below illustrates the overall workflow of the application.

![System Architecture](assets/screenshots/architecture.png)

---

# How StudyMate AI Works

The application follows a Retrieval-Augmented Generation (RAG) workflow to generate accurate, context-aware learning assistance.

1. The user uploads a lecture note in PDF format.
2. The PDF content is extracted using **PyMuPDF**.
3. The extracted text is divided into smaller semantic chunks.
4. Sentence Transformer generates vector embeddings for each chunk.
5. The embeddings are stored in **ChromaDB** for semantic retrieval.
6. The user selects one of the available learning tools:
   - Summary
   - Ask AI
   - Quiz
   - Reflection
7. The Retrieval Agent performs semantic similarity search to identify the most relevant document chunks.
8. The retrieved context is combined with the user's request.
9. The application automatically selects the configured AI provider through internal routing.
10. The selected Large Language Model generates a context-aware response.
11. The generated response is presented to the user through the Streamlit interface.

---

# Learning Workflow

The complete learning workflow is illustrated below.

```text
              Upload PDF
                   │
                   ▼
        Extract & Chunk Document
                   │
                   ▼
      Generate Vector Embeddings
                   │
                   ▼
      Store Embeddings in ChromaDB
                   │
                   ▼
      Choose Learning Feature
                   │
   ┌───────────┬───────────┬───────────┐
   ▼           ▼           ▼           ▼
Summary      Ask AI      Quiz     Reflection
                │
                ▼
        Retrieve Relevant Context
                │
                ▼
     Automatic AI Provider Routing
                │
                ▼
      Generate Context-Aware Response
```
# Project Structure

```text
StudyMate-AI/
│
├── agents/                 # Agent workflow components
├── assets/                 # Images and screenshots
│   └── screenshots/
├── components/             # Reusable UI components
├── data/                   # ChromaDB storage and uploaded data
├── models/                 # Embedding models and AI configuration
├── pages/                  # Streamlit application pages
├── prompts/                # Prompt templates
├── rag/                    # Retrieval-Augmented Generation pipeline
├── services/               # Business logic and AI services
├── tests/                  # Testing modules
├── utils/                  # Utility functions
│
├── app.py                  # Main application entry point
├── Home.py                 # Home page
├── config.py               # Configuration settings
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variable template
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/roshini-nawanjala/StudyMate-AI.git
```

## Navigate to the Project Directory

```bash
cd StudyMate-AI
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

## Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# Usage

1. Launch the StudyMate AI application.
2. Open the **Upload** page.
3. Upload a lecture note in PDF format.
4. Wait until the document is processed and indexed in ChromaDB.
5. Choose one of the available learning tools:
   - Summary
   - Ask AI
   - Quiz
   - Reflection
6. Generate AI-powered learning content based on the uploaded document.
7. Complete the quiz and submit your answers.
8. Review the AI-generated quiz evaluation and explanations.
9. Generate a personalized learning reflection based on your quiz performance.

> **Note:** AI provider selection is handled automatically by the application. Users do not need to configure or select an AI provider manually.

# Application Screenshots

The following screenshots demonstrate the key features and user interface of StudyMate AI.

---

## Home Page

The home page provides an overview of the application and quick access to all learning features.

![Home](assets/screenshots/home.png)

---

## Upload Page

Upload lecture notes in PDF format. The application extracts the document content, generates semantic chunks, and stores vector embeddings in ChromaDB for efficient retrieval.

![Upload](assets/screenshots/upload.png)

---

## Document Summary

Generate concise AI-powered summaries from uploaded lecture notes, helping students quickly understand the main concepts before studying in detail.

![Summary](assets/screenshots/summary.png)

---

## Ask AI

Interact with the uploaded document through context-aware question answering powered by Retrieval-Augmented Generation (RAG).

![Ask AI](assets/screenshots/ask-ai.png)

---

## AI Quiz

Generate multiple-choice quizzes directly from the uploaded lecture material. The application automatically evaluates answers and provides AI-generated explanations and performance feedback.

![Quiz](assets/screenshots/quiz.png)

---

## Learning Reflection

Generate a personalized learning reflection based on quiz performance, helping students identify strengths, weaknesses, and areas for further improvement.

![Reflection](assets/screenshots/reflection.png)

---

# Known Limitations

The current version of StudyMate AI has the following limitations:

- Supports PDF documents only
- Requires an active internet connection
- Requires valid API keys for AI services
- OCR is not supported for scanned PDF documents
- Large PDF files may require additional processing time
- Supports one uploaded document at a time

---

# Future Improvements

The following enhancements are planned for future versions of the project:

- Support for multiple document uploads
- OCR support for scanned documents
- User authentication and profile management
- Conversation history
- Cloud-based document storage
- Learning analytics dashboard
- Export summaries, quizzes, and reflections
- Mobile-responsive user interface
- Citation-aware AI responses
- Multi-language support

---

# Author

**Roshini Nawanjala**

Faculty of Information Technology  
Horizon Campus

GitHub Profile

https://github.com/roshini-nawanjala

---

# License

This project was developed for academic and educational purposes.

---

## Acknowledgements

This project was developed using the following open-source technologies:

- Streamlit
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers
- PyMuPDF
- Groq
- OpenRouter

Special thanks to the developers and maintainers of these projects for providing powerful open-source tools that made this project possible.
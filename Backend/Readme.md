# SHL Assessment Recommendation API

AI-powered SHL assessment recommendation system built using FastAPI, FAISS semantic search, Sentence Transformers, and Docker.

---

# Overview

This project is designed to recommend relevant SHL assessments based on hiring requirements provided by recruiters or hiring managers.

The system supports:

* Semantic search using FAISS
* Multi-turn conversation handling
* Grounded recommendations from SHL catalog data
* Comparison-style queries
* Off-topic query handling
* Dockerized deployment
* FastAPI REST API
* Swagger/OpenAPI documentation

The recommendations are generated only from the SHL assessment catalog to avoid hallucinated outputs.

---

# Features

## Semantic Retrieval

Uses Sentence Transformers (`all-MiniLM-L6-v2`) with FAISS vector search for semantic matching.

## Hybrid Ranking

Combines:

* Vector similarity
* Keyword boosts
* Technical skill matching
* Communication skill matching

for better recommendation quality.

## Stateless Multi-turn Conversations

Supports conversation history through the `messages` schema.

## Comparison Queries

Supports comparison-style prompts such as:

```text
What is the difference between OPQ and GSA?
```

## Off-topic Detection

Rejects unrelated queries outside SHL assessment recommendations.

## Docker Support

Fully containerized using Docker for reproducible deployment.

---

# Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Backend          | FastAPI               |
| Semantic Search  | FAISS                 |
| Embeddings       | Sentence Transformers |
| Model            | all-MiniLM-L6-v2      |
| Containerization | Docker                |
| API Docs         | Swagger/OpenAPI       |
| Language         | Python 3.12           |

---

# Project Structure

```text
shl-assessment-api/
│
├── main.py
├── retriever.py
├── build_index.py
├── prepare_catalog.py
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── clean_catalog.json
├── catalog_metadata.pkl
├── shl_index.faiss
└── README.md
```

## File Descriptions

| File                   | Purpose                              |
| ---------------------- | ------------------------------------ |
| `main.py`              | FastAPI backend and API endpoints    |
| `retriever.py`         | FAISS retrieval and ranking logic    |
| `build_index.py`       | Generates embeddings and FAISS index |
| `prepare_catalog.py`   | Cleans and preprocesses SHL catalog  |
| `app.py`               | SHL catalog data collection          |
| `catalog_metadata.pkl` | Processed metadata for retrieval     |
| `shl_index.faiss`      | FAISS vector index                   |

---

# API Endpoints

## Root Endpoint

```http
GET /
```

Returns API status message.

---

## Health Check

```http
GET /health
```

Returns:

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Main endpoint for assessment recommendations.

---

# Request Schema

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java developer with stakeholder communication skills"
    }
  ]
}
```

---

# Example Response

```json
{
  "reply": "Here are some recommended SHL assessments based on your hiring needs.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/products/product-catalog/view/java-8-new/",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": false
}
```

---

# Comparison Example

## Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is the difference between OPQ and GSA?"
    }
  ]
}
```

## Behavior

Returns grounded comparison information from the SHL catalog instead of hallucinated outputs.

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/your-username/shl-assessment-api.git
cd shl-assessment-api
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn main:app --reload
```

---

## Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t shl-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 shl-api
```

---

## Open API Docs

```text
http://127.0.0.1:8000/docs
```

---

# Retrieval Pipeline

The recommendation workflow:

```text
User Query
   ↓
FastAPI Backend
   ↓
Conversation Context Builder
   ↓
Sentence Transformer Embedding
   ↓
FAISS Semantic Search
   ↓
Hybrid Ranking
   ↓
Structured API Response
```

---

# Design Decisions

## Grounded Retrieval

Recommendations are generated only from SHL catalog data to reduce hallucinations.

## Hybrid Ranking

Semantic similarity alone was insufficient for technical role matching, so additional keyword boosting was introduced.

## Stateless Conversations

Conversation context is reconstructed from incoming message history instead of storing server-side state.

## Docker Deployment

Docker was used to ensure reproducible deployment and consistent runtime behavior.

---

# Future Improvements

Potential future enhancements:

* LLM-generated explanations
* Advanced reranking models
* Better comparison extraction
* Caching layer
* Evaluation metrics dashboard
* Cloud vector database integration

---

# Public Deployment

Example deployment:

```text
https://your-render-url.onrender.com/docs
```

---

# Author

Rushikesh Raghatate

---

# License

This project is intended for educational and assessment purposes.

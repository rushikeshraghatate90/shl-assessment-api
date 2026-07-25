# 🎯 SHL Assessment Recommendation System

<p align="center">
An AI-powered assessment recommendation platform that helps recruiters identify the most suitable <b>SHL assessments</b> using semantic search, hybrid ranking, and grounded AI recommendations.
</p>

<p align="center">

<a href="https://shl-assessment-api.streamlit.app">
<img src="https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

<a href="https://shl-assessment-api-ekjl.onrender.com/docs">
<img src="https://img.shields.io/badge/API-Swagger-009688?style=for-the-badge&logo=fastapi&logoColor=white">
</a>

<a href="https://shl-assessment-api-ekjl.onrender.com">
<img src="https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge">
</a>

<a href="https://github.com/rushikeshraghatate90/shl-assessment-api">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://github.com/rushikeshraghatate90/shl-assessment-api/blob/main/LICENSE">
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge">
</a>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/FAISS-Semantic_Search-7B61FF?style=flat-square">
<img src="https://img.shields.io/badge/Sentence_Transformers-all--MiniLM--L6--v2-orange?style=flat-square">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square">
<img src="https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=flat-square">

</p>

---

# 📖 About the Project

The **SHL Assessment Recommendation System** is an AI-powered recruitment assistant designed to help recruiters and hiring managers quickly identify the most relevant **SHL assessments** based on natural language hiring requirements.

Traditional keyword-based search often struggles to understand recruiter intent. This project addresses that limitation by combining **Sentence Transformer embeddings**, **FAISS semantic search**, and a **hybrid ranking algorithm** to retrieve accurate, grounded recommendations directly from the SHL assessment catalog.

The application supports conversational interactions, comparison queries, and role-specific recommendations while ensuring that all responses remain grounded in official SHL catalog data.

The system is deployed as a complete full-stack application with:

- 🚀 **Frontend:** Streamlit Cloud
- ⚡ **Backend:** FastAPI on Render
- 🧠 **Semantic Search:** FAISS
- 🤖 **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- 🐳 **Deployment:** Docker

---

# 🌐 Live Application

| Service | URL |
|----------|-----|
| 🚀 Live Demo | https://shl-assessment-api.streamlit.app |
| ⚡ Backend API | https://shl-assessment-api-ekjl.onrender.com |
| 📚 Swagger Documentation | https://shl-assessment-api-ekjl.onrender.com/docs |
| 💻 GitHub Repository | https://github.com/rushikeshraghatate90/shl-assessment-api |

---

# ✨ Features

- 🔍 Semantic search powered by FAISS
- 🤖 Sentence Transformer embeddings
- 💬 Multi-turn conversational recommendations
- 📊 Hybrid ranking combining semantic similarity and keyword matching
- 📈 Role-based SHL assessment recommendations
- ⚖️ Comparison queries (e.g., OPQ vs GSA)
- ✅ Grounded retrieval from SHL catalog data
- 🚫 Off-topic query detection
- ⚡ FastAPI REST API
- 🎨 Interactive Streamlit frontend
- 🐳 Dockerized backend deployment
- ☁️ Public deployment using Render and Streamlit Cloud

---

# 💡 Try These Queries

```
Hiring a Java Developer with stakeholder communication skills
```

```
Recommend assessments for a Data Scientist
```

```
Hiring a Customer Support Executive
```

```
Recommend assessments for a Python Developer
```

```
Looking for assessments for a Sales Manager
```

```
Difference between OPQ and GSA
```

---

# 🏗️ System Architecture

```
Recruiter
      │
      ▼
Streamlit Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Conversation Context Builder
      │
      ▼
Sentence Transformer
      │
      ▼
FAISS Semantic Search
      │
      ▼
Hybrid Ranking
      │
      ▼
Grounded SHL Recommendations
```

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Semantic Search | FAISS |
| Embedding Model | all-MiniLM-L6-v2 |
| NLP | Sentence Transformers |
| API Documentation | Swagger / OpenAPI |
| Containerization | Docker |
| Deployment | Render & Streamlit Cloud |
| Programming Language | Python 3.12 |

---

# 📂 Project Structure

```text
shl-assessment-api/

├── Backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── retriever.py
│   ├── build_index.py
│   ├── prepare_catalog.py
│   ├── catalog_metadata.pkl
│   ├── shl_index.faiss
│   └── README.md
│
├── Frontend/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── README.md
│
├── LICENSE
└── README.md
```

---

# 🔄 Recommendation Pipeline

```text
Recruiter Query
       │
       ▼
Conversation Context Builder
       │
       ▼
Sentence Transformer Embedding
       │
       ▼
FAISS Vector Search
       │
       ▼
Hybrid Ranking
       │
       ▼
Grounded SHL Recommendations
       │
       ▼
Interactive Streamlit Interface
```

---

# 📥 Clone Repository

Clone the repository:

```bash
git clone https://github.com/rushikeshraghatate90/shl-assessment-api.git
```

Navigate into the project directory:

```bash
cd shl-assessment-api
```

---

# ⚙️ Run Locally

## Backend

```bash
cd Backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd Frontend

pip install -r requirements.txt

streamlit run streamlit_app.py
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/chat` | Assessment Recommendation |

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java Developer with stakeholder communication skills"
    }
  ]
}
```

---

# 🚀 Deployment

### Frontend

Streamlit Cloud

https://shl-assessment-api.streamlit.app

### Backend

Render

https://shl-assessment-api-ekjl.onrender.com

### API Documentation

https://shl-assessment-api-ekjl.onrender.com/docs

---

# 🔮 Future Improvements

- Large Language Model generated explanations
- Advanced reranking models
- Streaming responses
- User authentication
- Analytics dashboard
- Conversation persistence
- Cloud vector database integration
- Performance benchmarking

---

# 👨‍💻 Author

**Rushikesh Raghatate**

B.Tech in Artificial Intelligence Engineering

GitHub: https://github.com/rushikeshraghatate90

LinkedIn: https://www.linkedin.com/in/rushikesh-raghatate/

---

# 📄 License

This project is licensed under the **MIT License**.

# ⚽ Streamlit AI Chatbot (Football) - RAG + Ollama

A powerful **AI Chatbot for Football Knowledge** built using:

- 🧠 **RAG (Retrieval-Augmented Generation)**
- 🤖 **Ollama (Local LLM)**
- ⚡ **Streamlit UI**
- 📄 **PDF / Knowledge Base Support**

This project allows users to **ask football-related questions** and get intelligent, context-aware answers from uploaded documents.

---

## 🚀 Features

- ⚽ Football-focused AI chatbot
- 🧠 RAG pipeline (context-aware responses)
- 📄 Upload PDFs (team stats, player data, match history)
- 🔍 Semantic search using embeddings
- 🤖 Local LLM via Ollama (no API cost)
- 💬 ChatGPT-like interface
- ⚡ Fast and lightweight

---

## 🧠 How It Works (RAG)

1. 📄 User uploads football-related documents
2. ✂️ Text is split into chunks
3. 🔢 Converted into embeddings
4. 💾 Stored in vector database (FAISS)
5. 🔍 Relevant context retrieved for query
6. 🤖 Ollama generates final answer using context

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **LLM:** Ollama (LLaMA / Mistral / etc.)  
- **Vector DB:** FAISS  
- **Embeddings:** Sentence Transformers  
- **Framework:** LangChain  

---

## 📁 Project Structure
streamlit-ai-chatbot-football/
│
├── .devcontainer/ # Dev container configuration
├── ingest/ # Data ingestion (PDF loading & chunking)
├── utils/ # Helper functions (prompts, formatting, etc.)
├── vectorstore/ # FAISS vector DB creation & retrieval
│
├── app.py # Main Streamlit application
├── requirements.txt # Dependencies
├── README.md # Project documentation

---

## 🧠 Architecture (RAG Pipeline)
User Query
↓
Retriever (FAISS)
↓
Relevant Context
↓
Ollama LLM
↓
Final Answer

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/streamlit-ai-chatbot-football.git
cd streamlit-ai-chatbot-football
---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/streamlit-ai-chatbot-football.git
cd streamlit-ai-chatbot-football

2. create environment
python -m venv myenv
myenv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

🤖 Setup Ollama
Install Ollama

👉 https://ollama.com

Pull Model
ollama pull mistra

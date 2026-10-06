# 🎓 UniSphere AI
## Your Intelligent University Information Assistant

AI-powered university information retrieval using RAG, ChromaDB, SentenceTransformers and Llama 3.2 via Ollama.

### Features
- Student/Admin login
- PDF upload and automatic indexing
- RAG question answering
- ChromaDB vector search
- Llama 3.2
- Source/page references
- Knowledge base search and category filter
- Voice input/output
- Chat history
- Admin document management
- Premium dark UI

### Run
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
ollama pull llama3.2
streamlit run app.py
```

### Demo credentials
Student: `student` / `student123`
Admin: `admin` / `admin123`

Replace the sample PDF with official university documents before final submission.

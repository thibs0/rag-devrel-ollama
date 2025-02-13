# Simple local devrel expert RAG AI chatbot (using ollama & mistral AI)
 
## Installation

- Install Ollama from [ollama.com](https://ollama.com)
- Download mistral AI & nomic text embedding for Ollama:
```bash
ollama pull nomic-embed-text
```
```bash
ollama pull mistral
```

- Install Python 3 (depends on your system)
- Install Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Launch Streamlit web interface

- Launch the Streamlit app:
```bash
streamlit run streamlit_app.py
```

Enjoy!

---

## Work with your own PDF files

- Reset the dadabase
```bash
python3 populate_database.py --reset
```

- Add PDF files into `/data` folder
- Run `populate_database.py` each time a new file is added or updated:
```bash
python3 populate_database.py
```


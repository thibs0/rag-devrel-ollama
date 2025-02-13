# rag-devrel-ollama
 
## Install

- Install Ollama from [ollama.com](https://ollama.com)
- Download mistral AI & nomic text embedding for Ollama:

```bash
ollama pull nomic-embed-text
```
```bash
ollama pull mistral
```

- Install Python 3
- Install Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Populate the database (embedding)

- Add PDF files into `/data` folder
- Run `populate_database.py` each time a new file is added or updated:

```bash
python3 populate_database.py
```

## Launch Streamlit web interface

- Launch Streamlit app:

```bash
streamlit run streamlit_app.py
```


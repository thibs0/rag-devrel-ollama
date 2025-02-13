# rag-devrel-ollama
 
## Requirements

- Install Python 3
- Install Ollama
- Install Python packages from _requirements.txt_:
`pip install -r requirements.txt`

## Populate the database (embedding)

- Add PDF files into _/data_ folder
- Run _populate_database.py_ each time a new file is added or updated:
`python3 populate_database.py`

## Launch Streamlit web interface

- Launch Streamlit app:
`streamlit run streamlit_app.py`

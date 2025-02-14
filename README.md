# Simple local RAG AI - Developer Relations - Talk to the Book

This Retrieval Augmented Generation (RAG) AI embeds the excellent book [Developer Relations](https://www.amazon.com/Developer-Relations-Build-Successful-Program/dp/1484271637/ref=sr_1_2) from my colleagues Caroline Lewko and James Parton at [DevRel.Agency](https://devrel.agency). It runs locally on your own computer.

This project is for you if:
* You want to talk to the book itself. It's fun, free, and fast to seek information from -- and a good complement to the paper version of the book too.
* You want to learn how to code a very simple local RAG AI project in python using ollama, based on PDF files. Instructions are given at the end to wipe out the database and embed your own PDF files instead.
* You'd like to contribute, for example with more DevRel content (PDF or other formats) for this DevRel RAG AI, or with other embeddings methods or other AIs, etc. (reach out to me!)

Dependencies: `ollama` `mistral` `langchain` `chromadb` `streamlit`

For any question, reach out to _thibs(at)devrel.agency_ or _thibault(at)cantegrel.com_

## Install

- Clone this repository -- from github interface or type in:
```bash
git clone https://github.com/thibs0/rag-devrel-ollama.git
cd rag-devrel-ollama
```

- Install Ollama from [ollama.com](https://ollama.com)
- Download mistral AI & nomic text embedding for Ollama:
```bash
ollama pull nomic-embed-text
ollama pull mistral
```

- Install Python 3 (depends on your system)
- Install Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Run

- Launch the Streamlit web app:
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

## Work with other types of content
Coming soon...

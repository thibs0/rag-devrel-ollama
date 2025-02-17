# Chat with the book "Developer Relations" `RAG` `ollama`

This Retrieval Augmented Generation (RAG) AI embeds the excellent book [Developer Relations](https://www.amazon.com/Developer-Relations-Build-Successful-Program/dp/1484271637/ref=sr_1_2) from my colleagues Caroline Lewko and James Parton at [DevRel.Agency](https://devrel.agency). It runs locally on your own computer.

This project is for you whether:
* you want to talk to the book itself. It's fun, free, and fast to seek information -- and a good complement to the paper version of the book too;
* you want to learn how to code a very simple local RAG AI project in python using ollama, based on PDF files. Instructions are given at the end to wipe out the database and embed your own PDF files instead;
* you'd like to contribute, for example with more DevRel content (PDF or other formats), or with other embeddings methods or other LLM, etc. (reach out to me!).

Dependencies: `ollama` `nomic-embed-text` `mistral` `langchain` `chromadb` `streamlit`

For any question, reach out to _thibs(at)devrel.agency_ or _thibault(at)cantegrel.com_

## Requirements

This project requires the following software to be installed on your machine first (Windows, Mac, Linux):

- [Ollama](https://ollama.com)
- [Python 3.12.9](https://www.python.org/downloads/release/python-3129/) (tested with former 3.x versions up to 3.12.9)
- C++ compilation toolchain:
  - on Windows, [install C++ build tools](https://github.com/bycloudai/InstallVSBuildToolsWindows)
  - on MacOS, execute in a terminal:
  ```bash
  xcode-select --install
  ```

- [Git](https://git-scm.com/) or [Github Desktop](https://desktop.github.com/download/) (optional although recommended)
 
# Install

- Download Mistral AI & Nomic Text Embedding for Ollama:
```bash
ollama pull mistral
ollama pull nomic-embed-text
```

- Clone this repository -- from GitHub interface or with Github desktop or with Git command line:
```bash
git clone https://github.com/thibs0/rag-devrel-ollama.git
cd rag-devrel-ollama
```

- Install Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Run

- Launch Ollama application or use the command:
```bash
ollama serve &
```

- Launch the Streamlit web app:
```bash
streamlit run streamlit_app.py
```
Enjoy!

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="/screenshot.png">
 <source media="(prefers-color-scheme: light)" srcset="/screenshot.png">
 <img alt="screenshot" src="/screenshot.png" width="800"/>
</picture>

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

## Dependencies

This project has been tested on MacOS (AppleSilicon, integrated GPUs) & Windows 11 (x64, RTX GPUs) with the following versions:

Python 3.12.9
- ollama-0.4.7
- langchain-0.3.18
- chromadb-0.6.3
- streamlit-1.42.0

## License
This is an open-source project provided under the [MIT License](LICENSE)

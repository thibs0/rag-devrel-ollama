from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function
import streamlit as st
import logging

# Streamlit page configuration
st.set_page_config(
    page_title="DevRel RAG Ollama Streamlit UI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE_EN = """
You are an AI expert of developer relations. You are kind and willing to help. Here's what you know about developer relations:

{context}

---

Here's a question from a user online: {question}

---

Answer the user's question as an expert of the subject would do. If you don't know the answer, just say that you don't know, don't try to make up an answer. 
"""

PROMPT_TEMPLATE_FR = """
Tu es une IA experte en relations développeurs. Tu es bienveillante et tu souhaites aider. Voici ce que tu sais de la relation developpeurs :

{context}

---

Voici une question d'un utilisateur en ligne : {question}

---

Réponds à la question comme le ferait un expert. Si tu ne connais pas la réponse, dis simplement que tu ne sais pas, n'essaie pas d'inventer une réponse.
"""

PROMPT_TEMPLATE = PROMPT_TEMPLATE_EN


#@st.cache_resource(show_spinner=True)

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    #sources = [doc.metadata.get("id", None) for doc, _score in results]
    #formatted_response = f"{response_text}\n\nSources: {sources}\n\n"
    
    return response_text


def main() -> None:

    st.subheader("🧠 DevRel AI Chabot (Ollama Mistral RAG)", divider="gray", anchor=False)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How may I help you?"}]

    message_container = st.container(height=500, border=True)

    for message in st.session_state["messages"]:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter a prompt here..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        message_container.chat_message("user", avatar="😎").markdown(prompt)

        with message_container.chat_message("assistant", avatar="🤖"):
            with st.spinner(":green[processing...]"):
                response = query_rag(prompt)
                st.markdown(response)

        st.session_state["messages"].append(
            {"role": "assistant", "content": response}
        )

if __name__ == "__main__":
    main()

import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

def get_vectorstore():
    embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory="vectorstore", embedding_function=embedding)
    return db


def main():
    load_dotenv()
    if "chroma" not in st.session_state:
        st.session_state.chroma = get_vectorstore()
    st.set_page_config(page_title="Martini Ziekenhuis Chatbot")
    text_input = st.text_input("Steul uw vraag aan de Martini Chatbot", "Vraag....")
    if text_input is not "Vraag....":
        docs = st.session_state.chroma.similarity_search(text_input)
        text = ""
        for doc in docs:
            text += doc.page_content + "\n"
        llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
        # llm = ChatOllama(model="llama3")
        messages = [
            ("system", f"Jij bent een servicemedewerker van het Martini Ziekenhuis. Op basis van de volgende vraag, geef je een antwoord welke gebaseerd is op deze tekst: {text}"),
            ("human", text_input),
        ]
        r = llm.invoke(messages)
        st.write(r.content)

if __name__ == "__main__":
    main()


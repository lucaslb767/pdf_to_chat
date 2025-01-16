from pathlib import Path
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from dotenv import load_dotenv, find_dotenv

import streamlit as st
_ = load_dotenv(find_dotenv())

FILE_DIRECTORY = Path(__file__).parent / 'files'
MODEL_NAME = 'gpt-4o-mini'

def document_loading():
    documents = []
    for arquivo in FILE_DIRECTORY.glob('*.pdf'):
        loader = PyPDFLoader(str(arquivo))
        docs_files = loader.load()
        documents.extend(docs_files)
    return documents

def split_docs(documents):
    recur_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2500,
        chunk_overlap = 250,
        separators=['\n\n','\n','.',' ','']
    )
    documents = recur_splitter.split_documents(documents)

    for i, doc in enumerate(documents):
        doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
        doc.metadata['doc_id'] = i
    
    return documents

def vectorStore(documents):
    embedding_model = OpenAIEmbeddings()
    vector_Store = FAISS.from_documents(
        documents= documents,
        embedding= embedding_model
    )
    return vector_Store

def create_conversation_chain():

    documents = document_loading()
    documents = split_docs(documents)
    vector_store = vectorStore(documents)


    chat = ChatOpenAI(model=MODEL_NAME)
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
        )
    retriever = vector_store.as_retriever()
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory = memory,
        retriever = retriever,
        return_source_documents = True,
        verbose=True
    )

    st.session_state['chain'] = chat_chain

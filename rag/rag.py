import os
import sqlite3
from decouple import config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
import shutil

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')
os.environ['HUGGINGFACE_API_KEY'] = config('HUGGINGFACE_API_KEY')

def rag_db():
    DB_PATH = 'db.sqlite3'
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, orbital_state, designation, orbit FROM chat_satellite")
    docs = cursor.fetchall()
    conn.close()

    documents = []
    for doc in docs:
        page_content = f"ID: {doc[0]}, Name: {doc[1]}, Orbital State: {doc[2]}, Designation: {doc[3]}, Orbit: {doc[4]}"
        documents.append(Document(page_content=page_content))

    persist_directory = 'chroma_data'

    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    os.makedirs(persist_directory)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(documents=documents)

    embedding = HuggingFaceEmbeddings()

    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )
    vector_store.add_documents(
        documents=chunks,
    )


from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from uuid import uuid4
import os
import streamlit as st  

CHUNK_SIZE = 1000
EMBEDDING_MODEL = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate"

vector_store = None
llm = None

if llm is None:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") 
    if not GROQ_API_KEY:
        raise RuntimeError("Groq API key not found in Streamlit secrets.")

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=600,
        api_key=GROQ_API_KEY
    )


def initialize_components():
    """Initialize LLM and Vector Store if not already initialized."""
    global llm, vector_store

    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=600)

    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )

def process_urls(urls, force_refresh=False):
    """
    Load URLs and embed them into Chroma vector DB.
    If data is already cached, skip re-embedding unless force_refresh=True.
    """
    yield("Initialize Components")
    initialize_components()

    if not VECTORSTORE_DIR.exists() or force_refresh:
        yield("Resetting collection and embedding new data...")
        vector_store.reset_collection()

        yield("Loading Data")
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()

        yield("Splitting Text")
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", " "],
            chunk_size=CHUNK_SIZE
        )
        docs = text_splitter.split_documents(data)

        yield("Add docs to vector DB")
        uuids = [str(uuid4()) for _ in range(len(docs))]
        vector_store.add_documents(docs, ids=uuids)
        yield("Data embedded and cached.")
    else:
        yield("Using cached vector DB.")


def generate_answer(query):
    global vector_store, llm
    if vector_store is None:
        raise RuntimeError("VectorDB not initialized. Run initialize_components().")

    retriever = vector_store.as_retriever()
    sources = retriever.invoke(query)

    context = "\n\n---\n\n".join(doc.page_content for doc in sources)

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful and precise AI assistant.
    Use only the provided context to answer the question.
    If the answer isn't found, say "I don't know."
    Write a short, factual paragraph.

    Context:
    {context}

    Question:
    {question}
    """)

    formatted_prompt = prompt.format(context=context, question=query)
    response = llm.invoke(formatted_prompt)
    answer_text = getattr(response, "content", str(response)).strip()

    source_urls = list({
        doc.metadata.get("source", "").strip().rstrip("/")
        for doc in sources if doc.metadata and doc.metadata.get("source")
    })

    clean_urls = [
        u for u in source_urls
        if len(u.replace("https://", "").replace("http://", "").split("/")) > 2
    ]

    formatted_output = (
        f"📘 **Answer:**\n{answer_text}\n\n"
        + (f"🔗 **Sources:**\n" + "\n".join(f"- {url}" for url in clean_urls)
           if clean_urls else "🔗 **Sources:** Not available")
    )

    return formatted_output, clean_urls

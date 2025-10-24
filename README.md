# QueryLink GroqQA

QueryLink GroqQA is a Streamlit web app that allows users to query multiple URLs using a Groq-powered AI assistant. It extracts, embeds, and searches documents from the web in real-time, providing concise, factual answers with sources.  
STREAMLIT URL : https://query-link-groq-by-saket.streamlit.app/

---

## 🌟 Features

- Query multiple URLs simultaneously (up to 3 at a time).  
- Uses **Groq LLM** for precise answers.  
- Embeds and indexes documents via **Chroma Vector DB**.  
- Automatic text splitting for better context handling.  
- Displays sources along with the AI-generated answer.  
- Easy-to-use Streamlit interface with live status updates.

---

## ⚙️ Code Overview

main.py – Streamlit interface
- Handles user input for URLs and questions.
- Displays progress and errors.
- Calls process_urls and generate_answer from groq_qa_querylink.py.

groq_qa_querylink.py – Backend logic
- Loads URLs and splits them into chunks.
- Embeds documents into a Chroma Vector Store.
- Queries the Groq LLM with context to generate answers.
- Returns answer along with source URLs.

---

## 📦 Dependencies
- streamlit==1.45.0
- langchain-core==1.0.0
- langchain-community==0.4
- langchain-groq==1.0.0
- langchain-chroma==1.0.0
- langchain-huggingface===1.0.0
- unstructured==0.18.15
- torch==2.7.1
- transformers==4.55.2
- sentence-transformers==5.1.1
- chromadb==1.2.0

import streamlit as st
from groq_qa_querylink import process_urls, generate_answer
import time

st.title("QueryLink GroqQA")

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

process_url_button = st.sidebar.button("Process URLs")

status_placeholder = st.empty()

if process_url_button:
    urls = [url for url in (url1, url2, url3) if url]
    if not urls:
        status_placeholder.error("At least 1 URL is needed")
    else:
        try:
            status_placeholder.info("Initializing embeddings.")
            time.sleep(0.5)

            status_placeholder.info("Processing URLs and embedding documents.")
            time.sleep(0.5)

            status_placeholder.success(message)
        except Exception as e:
            status_placeholder.error(f"Error processing URLs: {str(e)}")
query = st.text_input("Question")

if query:
    try:
        answer, sources = generate_answer(query)
        st.markdown(answer)
    except RuntimeError:
        st.error("You must process URLs first")
    except Exception as e:
        st.error(f"Error generating answer: {str(e)}")

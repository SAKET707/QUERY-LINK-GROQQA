import streamlit as st
from groq_qa_querylink import process_urls, generate_answer

st.title("QueryLink GroqQA")

# Sidebar for URL inputs
url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

# Button to process URLs
process_url_button = st.sidebar.button("Process URLs")

# Placeholder for status messages
status_placeholder = st.empty()

# Process URLs when button is clicked
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url]
    if not urls:
        status_placeholder.error("At least 1 URL is needed")
    else:
        status_placeholder.info("Processing URLs...")
        try:
            # Iterate over the generator to display status updates
            for status in process_urls(urls, force_refresh=True):
                status_placeholder.text(status)
            status_placeholder.success("URLs processed successfully!")
        except Exception as e:
            status_placeholder.error(f"Error processing URLs: {str(e)}")

# Input for the query
query = st.text_input("Question")

# Display answer and sources when a query is provided
if query:
    try:
        answer, sources = generate_answer(query)
        st.write(answer)
        
    except RuntimeError as e:
        st.error("You must process URLs first")
    except Exception as e:
        st.error(f"Error generating answer: {str(e)}")
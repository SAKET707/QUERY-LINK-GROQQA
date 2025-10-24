# QueryLink GroqQA

QueryLink GroqQA is a Streamlit web app that allows users to query multiple URLs using a Groq-powered AI assistant. It extracts, embeds, and searches documents from the web in real-time, providing concise, factual answers with sources.  

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

## 🚀 Demo

QueryLink GroqQA demonstrates its ability to extract and process information from multiple URLs, delivering accurate and contextually relevant answers. Below are two example screenshots showcasing the model's performance:

- **Image 1**: The model correctly answers a query using content from [Afghanistan to Restrict Water Flow, Build Dam on Kunar River](https://www.indiatoday.in/world/story/afghanistan-to-restrict-water-build-dam-on-kunar-chitral-hydro-pakistan-after-india-pause-indus-waters-treaty-2807572-2025-10-24).
- **Image 2**: The model accurately responds to a query based on [Piyush Goyal on Trade Talks with the US](https://www.indiatoday.in/business/story/do-not-do-deals-with-gun-to-our-head-piyush-goyal-on-trade-talks-with-us-2807857-2025-10-24).

<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://github.com/user-attachments/assets/2c3af4d5-d3a7-4c56-b788-02bdccebd03c" alt="QueryLink GroqQA Example 1: Water Restriction Query" width="400" height="400">
  <img src="https://github.com/user-attachments/assets/46dacff9-3e53-4cc3-ad28-8c0005be4284" alt="QueryLink GroqQA Example 2: Trade Talks Query" width="400" height="400">
</div>

### Reference URLs
The following URLs were used to test the model's query capabilities:
1. [Gold, Silver Prices Crash: Reasons Include Profit Booking, Easing Geopolitical Tensions](https://www.indiatoday.in/business/market/story/gold-silver-seeing-crash-why-reason-profit-booking-safe-haven-demand-easing-geopolitical-tensions-stronger-dollar-2807046-2025-10-23)
2. [Afghanistan to Restrict Water Flow, Build Dam on Kunar River](https://www.indiatoday.in/world/story/afghanistan-to-restrict-water-build-dam-on-kunar-chitral-hydro-pakistan-after-india-pause-indus-waters-treaty-2807572-2025-10-24)
3. [Piyush Goyal on Trade Talks with the US](https://www.indiatoday.in/business/story/do-not-do-deals-with-gun-to-our-head-piyush-goyal-on-trade-talks-with-us-2807857-2025-10-24)
  
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

---

---

## 📢 Get Started

Explore QueryLink GroqQA today by visiting the [live demo](https://query-link-groq-by-saket.streamlit.app/) and test its ability to query multiple URLs with accurate, source-backed answers. 

### Contributing
We welcome contributions to enhance QueryLink GroqQA! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

Please review the [Contributing Guidelines](CONTRIBUTING.md) for more details.

Thank you for checking out QueryLink GroqQA. Happy querying!

---

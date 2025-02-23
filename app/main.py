import streamlit as st
import requests
from typing import Optional

API_URL = "http://localhost:8000/summarize"

st.set_page_config(
    page_title="AI Text Summarizer",
    layout="wide"
)

def main():
    st.title("🤖 AI Text Summarizer")
    st.markdown("Transform long texts into concise summaries using NLP")
    
    with st.sidebar:
        st.header("Settings")
        algorithm = st.radio(
            "Summarization Method",
            ["abstractive", "extractive"],
            help="Abstractive generates new sentences, Extractive selects key sentences"
        )
        ratio = st.slider(
            "Summary Ratio", 
            min_value=0.1, 
            max_value=0.5, 
            value=0.2,
            help="Length of summary relative to original text"
        )
    
    text = st.text_area("Input Text", height=300, 
                       placeholder="Paste your text here...")
    
    if st.button("Generate Summary"):
        if len(text) < 100:
            st.error("Please enter at least 100 characters")
            return
            
        with st.spinner("Analyzing text..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "text": text,
                        "ratio": ratio,
                        "algorithm": algorithm
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.subheader("Summary")
                    st.write(result["summary"])
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Readability Score", f"{result['readability_score']:.1f}")
                    with col2:
                        st.metric("Processing Time", f"{result['processing_time']}s")
                else:
                    st.error(f"Error: {response.json()['detail']}")
            
            except Exception as e:
                st.error(f"API Error: {str(e)}")

if __name__ == "__main__":
    main()
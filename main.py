import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

st.title("Document Summarizer and Q&A")

uploaded_file = st.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:

    document = uploaded_file.read().decode("utf-8")
    
    st.subheader("Original Document")
    st.write(document)
    
    st.subheader("Summary")
    summary = summarizer(document, max_length=150, min_length=30, do_sample=False)
    st.write(summary[0]['summary_text'])
    
    st.subheader("Ask a question about the document")
    question = st.text_input("Enter your question:")
    if question:
        answer = qa_model(question=question, context=document)
        st.write("Answer:", answer['answer'])


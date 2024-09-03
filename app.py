import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DataFrameLoader
import time
import pandas as pd
from langchain_community.vectorstores import Milvus
import base64
from streamlit_modal import Modal
import streamlit.components.v1 as components
import os
import os
from langchain.embeddings.openai import OpenAIEmbeddings




st.subheader('We\'re here to help!', divider='rainbow')

st.sidebar.title("Understanding Your Benefits")
st.sidebar.caption('Simplifying Complex Documents with AI')

selectbox_insurance = st.sidebar.selectbox(
    "Select you insurance:",
    ("BCBS",)
)

st.sidebar.markdown('''
This app uses cutting-edge AI to understand your BCBS Athena or United Health EOBs, providing:

- Clear explanations for: Covered services & procedures, Costs & charges, Benefits summary.
- Simplified access: Select your EOB & get insights instantly.
- Peace of mind: Understand your health insurance & make informed decisions
Let AI handle the complexity, so you can focus on your health.

### How it works:

1. Select your EOB document (BCBS, Athena, or United Health).
2. AI analyzes the document and provides clear explanations.
''')

connection_args = None # Change this to your connection

embeddings = OpenAIEmbeddings()


def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message['role'] == 'assistant':
            st.image(message["image"], caption='Original Document')

if prompt := st.chat_input("Whats up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        vector_store = Milvus(
            embedding_function=embeddings,
            connection_args=connection_args,
            collection_name='bcbs_indexed_openai'
        )

        docs = vector_store.similarity_search(prompt)

        response = st.write_stream(response_generator(docs[0].page_content))
        page = int(docs[0].metadata['PAGE'])
        st.image(f'./bcbs_pages/page_{page}.png', caption='Original Document')
        col1, col2, col3 = st.columns([10, 1, 1])

        col2.button(":thumbsup:")
        col3.button(":thumbsdown:")
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image":f"./bcbs_pages/page_{page}.png"})
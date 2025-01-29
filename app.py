from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##promp template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title('Langchain Demo With Groq API')
input_text=st.text_input("Search the topic u want")

#Groq LLM
groq_model_id ="llama3-8b-8192"
llm = ChatGroq(model=groq_model_id)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
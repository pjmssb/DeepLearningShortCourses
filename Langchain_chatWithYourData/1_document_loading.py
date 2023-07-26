'''
In retrieval augmented generation (RAG), an LLM retrieves 
contextual documents from an external dataset as part of 
its execution.

This is useful if we want to ask question about specific 
documents (e.g., our PDFs, a set of videos, etc).
'''

import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("./Langchain_chatWithYourData/MachineLearning-Lecture01.pdf")
pages = loader.load()
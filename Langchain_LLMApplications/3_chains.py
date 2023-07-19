import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv 
_ = load_dotenv(find_dotenv()) #Lee el contenido de .env
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

df = pd.read_csv('./Langchain_LLMApplications/Data.csv')
print(df.head())

llm = ChatOpenAI(temperature=0.9)
import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv 
_ = load_dotenv(find_dotenv()) #Lee el contenido de .env
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

df = pd.read_csv('./Langchain_LLMApplications/Data.csv')
print(df.head())

llm = ChatOpenAI(temperature=0.9)

prompt = ChatPromptTemplate.from_template('What is the best name to describe a company that makes {product}?')

chain = LLMChain(llm=llm, prompt=prompt)

product = 'Queen size Sheet Set'
# print(chain.run(product))

#Cadena de Cadenas simple 

#Primera cadena
first_prompt = ChatPromptTemplate.from_template('What is the best name to describe a company that makes {product}?')
chain_one = LLMChain(llm=llm, prompt=first_prompt)

#Segunda cadena
second_prompt = ChatPromptTemplate.from_template('Write a 20 words description of the following company {company_name}')
chain_two = LLMChain(llm=llm, prompt=second_prompt)

overall_simple_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose = True)

#print(overall_simple_chain.run(product))
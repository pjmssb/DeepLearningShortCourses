import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import warnings
warnings.filterwarnings('ignore')

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=False
)

print(conversation.predict(input="Hi, my name is Andrew"))

print(conversation.predict(input="What is 1+1?"))

print(conversation.predict(input="What is my name?"))

print("Memory buffer >>>>>>>>>>>>>>>>>>>>>>>>>>")
print(memory.buffer)
print("Memory variables >>>>>>>>>>>>>>>>>>>>>>>")
print(memory.load_memory_variables({}))

memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, 
                    {"output": "What's up"})
print(memory.buffer)
print(memory.load_memory_variables({}))


memory = ConversationBufferWindowMemory(k=1)               
print(conversation.predict(input="Hi, my name is Andrew"))
print(conversation.predict(input="What is 1+1?"))
print(conversation.predict(input="What is my name?"))
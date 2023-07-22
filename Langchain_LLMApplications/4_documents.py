import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown

file = './Langchain_LLMApplications/OutdoorClothingCatalog_1000.csv'
loader = CSVLoader(file_path=file, encoding='utf-8')

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

query ="Please list all your shirts with sun protection \
in a table in markdown and summarize each one."

#response = index.query(query)

#print(response)

#Embeddings

loader = CSVLoader(file_path=file, encoding='utf-8')
docs = loader.load()
print(docs[0])

from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
embed = embeddings.embed_query("Hi my name is Harrison")
print(len(embed))
print(embed[:5])
db = DocArrayInMemorySearch.from_documents(
    docs, 
    embeddings
)
query = "Please suggest a shirt with sunblocking"
docs = db.similarity_search(query)
print(len(docs))
print(docs[0]) 
retriever = db.as_retriever()
llm = ChatOpenAI(temperature = 0.0)
qdocs = "".join([docs[i].page_content for i in range(len(docs))])
response = llm.call_as_llm(f"{qdocs} Question: Please list all your \
shirts with sun protection in a table in markdown and summarize each one.") 
print(response)

qa_stuff = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff",  #--> Hay varios métodos
    retriever=retriever, 
    verbose=True
)

query =  "Please list all your shirts with sun protection in a table \
in markdown and summarize each one."

response = qa_stuff.run(query)
print(response)

response = index.query(query, llm=llm)

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embeddings,
).from_loaders([loader])
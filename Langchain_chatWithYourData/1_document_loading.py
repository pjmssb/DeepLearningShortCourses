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



#PDF
'''
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("./Langchain_chatWithYourData/MachineLearning-Lecture01.pdf")
pages = loader.load()

print(len(pages))
page = pages[0]
print(page.page_content[0:500])
print(page.metadata)
'''


#Youtube
# ! pip install yt_dlp
# ! pip install pydub
# Windows Command  python .\Langchain_chatWithYourData\1_document_loading.py --ffmpeg-location .\Langchain_chatWithYourData\ff-essentials-6.0\bin\
# ffmpeg instalado especialmente, se ignora en github y NO LOGRÉ HACERLO FUNCIONAR EN WINDOWS
# Código del notebook del curso también falla
'''
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir="./Langchain_chatWithYourData"
loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()

docs[0].page_content[0:500]
'''


#URLs
'''
print(f"Este es el inicio de carga de URLs")
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")
#loader = WebBaseLoader("https://miasmoda.cl/") #--> Acceso no autorizado ????!!!!!!!!!
#loader = WebBaseLoader("https://miasmoda.cl/products/body-sabina") #--> Acceso no autorizado ????!!!!!!!!!
docs = loader.load()
print(docs[0].page_content[:500])
'''


#Notion
# Hay que construir un sitio así que se probó el código en el 
# notebook del curso
# Se deja aquí como referencia
'''
from langchain.document_loaders import NotionDirectoryLoader
loader = NotionDirectoryLoader("docs/Notion_DB")
docs = loader.load()
print(docs[0].page_content[0:200])
docs[0].metadata
'''


#URL with Beautiful Soup
# Check this: https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/data-structures/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
r = requests.get(url=URL, headers=headers)
print(r.content)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
'''
from langchain.document_loaders import BSHTMLLoader
loader = BSHTMLLoader("https://miasmoda.cl/products/body-sabina")
data = loader.load()
print(data)
'''
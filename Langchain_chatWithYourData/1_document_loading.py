'''
In retrieval augmented generation (RAG), an LLM retrieves 
contextual documents from an external dataset as part of 
its execution.

This is useful if we want to ask question about specific 
documents (e.g., our PDFs, a set of videos, etc).
'''


#PDF
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

print(len(pages))
page = pages[0]
print(page.page_content[0:500])
print(page.metadata)

#Youtube
# ! pip install yt_dlp
# ! pip install pydub
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir="./DeepLearningShortCourses/"
loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()
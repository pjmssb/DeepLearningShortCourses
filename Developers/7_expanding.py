#This includes the concept of temperature

import os
import openai
import tiktoken

from dotenv import load_dotenv, find_dotenv 
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    return response.choices[0].message["content"]

sentiment = "Positive"

review = f"""
Edward Burton
5,0 de 5 estrellas Fantastic!!!

Compra verificada

An exciting, well written journey through the world of Blockchain \
with an easy-to-read and fun style, not something you normally \
associate with the subject matter.

The author is obviously a true expert and the content is authoritative, \
informative and just plain interesting!

Highly recommended...
"""

prompt = f"""
You are a customer service AI assistant.
Your task is to create a chat response to a review from a valued customer.
Given the customer review delimited by ```, \
Generate a reply to thank the customer for her review.
If the review is Positive or Neutral , thank her for her review.
If the sentiment is negative, apologize and suggest they can reach out\
to customer service.
Make sure to use specific details from the review.
Write in a professional and concise tone.
Sign the chat as Mia Robbie.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""

response = get_completion(prompt, temperature=0.7)
print(response)
import os
import openai
import tiktoken

from dotenv import load_dotenv, find_dotenv 
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message["content"]


#Traducir un texto de una lengua a otra (o a varias)
#Decir en que idioma está escrito un texto
#Traducir a formas más formales o informales de una lengua
#Traducir muchos mensajes a un idioma   
#Tone transformation
#Transformación de formatos --> JSON 2 CSV 2 HTML
#Verificar la corrección gramática y estilo / Proofread & correct
#Follow APA rules or any other style

text = f"""
Texto muy largoo con alguna falltas y horrores de ortografia.
"""

prompt = f"Proofread and correct this review: ```{text}```"
response = "Texto muy largo con algunas faltas y errores de ortografía." #get_completion(prompt)
print(response)

from redlines import Redlines
diff = Redlines(text, response)
#print(Markdown(diff.output.Markdown))
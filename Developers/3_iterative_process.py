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

fact_sheet_bodie = f'''
PRODUCT NAME
Body Alejandra (BD1123)

PRODUCT TYPE
Body moldeador de figura, manga amplia.

OVERVIEW
Elaborado en el exterior con tela poli lycra colombiana y en el interior con malla powernet, el mismo material de las fajas postquirúrgicas, diseño y fabricación100% colombiano.
Reduce de 4 a 7 centímetros de cintura.
Comprime abdomen.
Mejora la postura.
Moldea la figura.
Forma arco para dar volumen al glúteo.
Únicos con sistema de control interno en malla powernet (compresión media) en abdomen, contorno y espalda baja.

PRECIO
25.990 CLP

COLORES
Blanco

TALLAS
M (36-38)Variante agotada o no disponible 
L (40) Disponible 
XL (42) Disponible
XXL (44)Variante agotada o no disponible
'''

prompt = f'''
Your task is to help a marketing team create a 
description a retail website of a product based 
on a technical fact sheet.

Write in Spanish a product description based on the information
provided in the technical specifications delimited by
triple backticks:

Use at most 280 characters.

At the end of the description include the 6 letters/digits 
product id code in the technical specification.

Technical specifications:```{fact_sheet_bodie}```   
'''

response = get_completion(prompt)
print(response)
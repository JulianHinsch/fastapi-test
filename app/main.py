from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv
import openai
import os

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai.api_key=OPENAI_API_KEY

app = FastAPI()

@app.get("/")
def root():
    return "Hello world"

@app.get("/completion/")
async def completion(question: Union[str, None] = None):
    if not OPENAI_API_KEY:
        return "Missing OPENAI_API_KEY environment variable"
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{ 'role': 'user', 'content': question }],
        temperature=0.6,
    )
    return response['choices'][0]['message']['content']

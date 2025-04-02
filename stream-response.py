import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

BASE_URL = os.getenv("OLLAMA_BASE_URL")
MODEL = os.getenv("MODEL")
API_KEY = os.getenv("OLLAMA_API_KEY")
openai = OpenAI(base_url=BASE_URL, api_key=API_KEY)

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "Can you describe about the Paris city?"}],
 temperature=0.7,
 stream=True
)

for chunk in response:
    message = chunk.choices[0].delta.content
    if message:
        print(message, end='', flush=True)    
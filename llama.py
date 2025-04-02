import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

BASE_URL = os.getenv("OLLAMA_BASE_URL")
MODEL = os.getenv("MODEL")
API_KEY = os.getenv("OLLAMA_API_KEY")
openai = OpenAI(base_url=BASE_URL, api_key=API_KEY)

system_message = "You are a helpful assistant"

def message_gpt(prompt):
    messages = [
        {"role" : "system", "content" : system_message},
        {"role" : "user", "content" : prompt}
    ]
    completion = openai.chat.completions.create(
        model = MODEL,
        messages = messages
    )
    return completion.choices[0].message.content

def stream_gpt(prompt):
    messages = [
        {"role" : "system", "content" : system_message},
        {"role" : "user", "content" : prompt}
    ]
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

forcing_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

gr.Interface(fn=stream_gpt, 
             inputs="textbox", 
             outputs="textbox", 
             flagging_mode="never", 
             js=forcing_dark_mode).launch(inbrowser = True)

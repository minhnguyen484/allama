import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

load_dotenv(override=True)

model = "gpt-4"
openai = OpenAI()


system_message = "You are a helpful assistant"

def message_gpt(prompt):
    messages = [
        {"role" : "system", "content" : system_message},
        {"role" : "user", "content" : prompt}
    ]
    completion = openai.chat.completions.create(
        model = model,
        messages = messages
    )
    return completion.choices[0].message.content

forcing_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

gr.Interface(fn=message_gpt, 
             inputs="textbox", 
             outputs="textbox", 
             flagging_mode="never", 
             js=forcing_dark_mode).launch(inbrowser = True)
import gradio as gr
from chatbot import Chatbot
from models.website import Website

system_message = "You are an assistant that analyzes the contents of a company \
    website landing page and creates a short brochure about the company for prospective\
    customers, investor and recruits. Response in markdown."

def stream_brochure(company_name, url):
    prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
    prompt += Website(url).get_contents()

    chatbot = Chatbot("ollama")
    stream = chatbot.chat(prompt)

    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

view = gr.Interface(
    fn = stream_brochure,
    inputs = [
        gr.Text(label="Company name:"),
        gr.Text(label="Landing page URL including http:// or https://")        
    ],
    outputs=[gr.Text(label="Brochure")],
    flagging_mode="never"
)

view.launch()
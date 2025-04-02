import gradio as gr
from chatbot import Chatbot

forcing_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

chatbot = Chatbot("ollama")

def chat(message, history):
    stream = chatbot.chat(message)
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

# gr.Interface(fn=get_response, 
#              inputs=[gr.Textbox(label="Prompt")], 
#              outputs=[gr.Textbox(label="Assistant")], 
#              flagging_mode="never", 
#              js=forcing_dark_mode).launch(inbrowser = True)

gr.ChatInterface(
    fn = chat,
    type = "messages"
).launch()
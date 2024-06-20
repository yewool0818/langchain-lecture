import random
import gradio as gr

def random_response(message, history):
    return random.choice(["YES", "NO"])

demo = gr.ChatInterface(random_response)

demo.launch()
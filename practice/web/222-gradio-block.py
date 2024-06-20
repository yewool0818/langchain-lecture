import gradio as gr

def greet(name):
    return "안녕하세요, {name}씨"


with gr.Blocks() as demo:
    name = gr.Textbox(label="NAME")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(
        fn=greet,
        inputs=name,
        outputs=output,
        api_name="greet"
    )

demo.launch()
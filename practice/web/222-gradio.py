import gradio as gr

def greet(name):
    return "안녕하세요 😊, " + name + "씨! 🎉"

iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(placeholder="이름을 입력하세요 👤"),
    outputs="text",
    title="인사하는 웹 어플리케이션",
    description="이름을 입력하면 인사말을 생성합니다. 😄"
)

if __name__ == "__main__":
    iface.launch()

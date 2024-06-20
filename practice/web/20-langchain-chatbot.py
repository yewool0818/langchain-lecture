import warnings
warnings.filterwarnings("ignore")

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr

# llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo-0613')
# 날짜정보 finetuning 모델
llm = ChatOpenAI(
    temperature=0,
    model='ft:gpt-3.5-turbo-0613:shinkisa::8VomhV43'
)

def predict(message, history):
    history_langchain_format = []

    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    
    history_langchain_format.append(HumanMessage(content=message))
    print("===================================")
    print("최종적인 prompt => ", history_langchain_format)
    gpt_response = llm(history_langchain_format)

    return gpt_response.content

gr.ChatInterface(predict).launch()

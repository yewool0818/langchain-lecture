import warnings
warnings.filterwarnings("ignore")

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr
import json

def save_history(history):
    with open('chat_history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo-0613')
# 날짜정보 finetuning 모델
llm = ChatOpenAI(
    temperature=0,
    model='gpt-3.5-turbo-0613'
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

    history.append((message, gpt_response.content))
    save_history(history)
    
    return gpt_response.content

gr.ChatInterface(predict).launch()

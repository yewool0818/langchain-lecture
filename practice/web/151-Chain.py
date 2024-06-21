
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("{topic}에 대한 아주 재밌는 짧은 이야기 3개 알려줘")

model = ChatOpenAI(temperature=0)
output_parser = StrOutputParser()

chain = prompt | model | output_parser

topic = "귀여운 강아지"

print(prompt)
print((prompt | model).invoke({"topic": topic}))


# print(chain.invoke({"topic": topic}))

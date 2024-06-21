
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

topic = "귀여운 강아지"
prompt = ChatPromptTemplate.from_template("{topic}에 대한 아주 재밌는 짧은 이야기 3개 알려줘")
prompt_value = prompt.invoke({"topic": topic})
# print(prompt_value.to_messages())
# print(prompt_value.to_string())

llm = OpenAI(model="gpt-3.5-turbo-instruct")
# message = llm.invoke(prompt_value)
# print(message)

input = {"topic": topic}
print(prompt.invoke(input))
print((prompt | llm).invoke(input))

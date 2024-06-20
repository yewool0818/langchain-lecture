import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Using LlamaIndex as a Callable Tool
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# 데이터 로딩
documents = SimpleDirectoryReader("./data").load_data()
# 벡터화
index = VectorStoreIndex.from_documents(documents=documents)

# Tool 생성
tools = [
    Tool(
        name="LlamaIndex",
        func=lambda q: str(index.as_query_engine().query(q)),
        description=u"seful for when you want to answer questions about the author. The input to this tool should be a complete english sentence.",
        return_direct=True,
    )
]

# 메모리 생성
memory = ConversationBufferMemory(memory_key="chat_history")

# llm 초기화
llm = ChatOpenAI(temperature=0, model="gpt-4o")

# agent 초기화
agent_executor = initialize_agent(
    tools,
    llm,
    agent="conversational-react-description",
    memory=memory
)

# # 첫 번째 질문 수행
# response1 = agent_executor.run(input="who is the author of this document?")
# print(f'#### 답변 => {response1}')

# # 두 번째 질문 수행
# response2 = agent_executor.run(input="please summarize the document")
# print(f'#### 답변 => {response2}')

# # 세 번째 질문 수행
# response3 = agent_executor.run(input="please answer in Korean")
# print(f'#### 답변 => {response3}')

# response4 = agent_executor.run(input="please summarize your answer to one sentence.")
# print(f'#### 답변 => {response4}')

response5 = agent_executor.run(input="Please tell me about cat.")
print(f'#### 답변 => {response5}')
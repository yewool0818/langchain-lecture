
from autogen.coding import LocalCommandLineCodeExecutor
from autogen import ConversableAgent, AssistantAgent
import datetime


llm_config = {"model": "gpt-4-turbo"}

# code executor 정의
executor = LocalCommandLineCodeExecutor(
    timeout=60,
    work_dir="coding", # coding 디렉토리에 코드 생성 후 실행
)

# agent 생성
# code executor config Agent 
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
    default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
)
# code wirter Agent
code_writer_agent = AssistantAgent(
    name="code_writer_agent",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)
# 코드 생성 프롬프트
code_writer_agent_system_message = code_writer_agent.system_message
# print(code_writer_agent_system_message)
# You are a helpful AI assistant.
# Solve tasks using your coding and language skills.
# In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
#     1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
#     2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
# ..(생략)..
# Reply "TERMINATE" in the end when everything is done.

# Task 정의
today = datetime.datetime.now().date()
message = f"Today is {today}. "\
"Create a plot showing stock gain YTD for NVDA and TLSA. "\
"Make sure the code is in markdown code block and save the figure"\
" to a file ytd_stock_gains.png."""

# 코드 실행 에이전트를 통해 실행
chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message=message
)
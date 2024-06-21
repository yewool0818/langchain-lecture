from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain_experimental.tools import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

# account for deprecation of LLM model
import datetime
# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-4o"
else:
    llm_model = "gpt-3.5-turbo-0301"

llm = ChatOpenAI(
    temperature = 0,
    model = llm_model
)
 
tools = load_tools(["llm-math", "wikipedia"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

# agent("What is the 25% of 300?")
agent("New Jeans 맴버들의 나이의 합은?")


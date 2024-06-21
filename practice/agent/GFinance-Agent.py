from langchain_community.tools.google_finance import GoogleFinanceQueryRun
from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain import OpenAI

tool = GoogleFinanceQueryRun(api_wrapper=GoogleFinanceAPIWrapper(serp_api_key="xoWfUXBMkk6sffM5jyso"))

llm = OpenAI()
tools = load_tools(["google-scholar", "google-finance"], llm=llm)
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

agent.run("Forcast Nvidia's stock in this week")

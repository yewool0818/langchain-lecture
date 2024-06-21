from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.chat_models import ChatOpenAI
import langchain

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
 
agent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)

# customer_list = [["Harrison", "Chase"],
#                  ["Lang", "Chain"],
#                  ["Dolly", "Too"],
#                  ["Elle", "Elem"],
#                  ["Geoff","Fusion"],
#                  ["Trance","Former"],
#                  ["Jen","Ayai"]
#                 ]

# agent.run(f"""Sort these customers by \
# last name and then first name \
# and print the output: {customer_list}""")

# langchain.debug = True
langchain.debug = False
code = "print(ads"
agent.run(f"""
Please Let me know what is the problem of origin code.
And write down new line : debug and create collect code with this code 
          
origin code:
```{code}```
 
""")
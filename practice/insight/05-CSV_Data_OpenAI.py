import pandas as pd
import os
import openai
import sys

from IPython.display import Markdown, HTML, display
from langchain.schema import HumanMessage
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent


llm = OpenAI(model="gpt-4o", temperature=0.0)

# Load the Excel file
file_path = 'wv-corelation.xlsx'

# Read the Excel file into a DataFrame
# df = pd.read_excel(file_path, engine='openpyxl')
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame to understand its structure
df.head()

# Convert the 'ds' column to datetime format
df['ds'] = pd.to_datetime(df['ds'])

# Set the 'ds' column as the index
df.set_index('ds', inplace=True)

# Resample the data to 1-hour intervals and calculate the mean for each interval
df_resampled = df.resample('1H').mean()

# Display the first few rows of the resampled DataFrame
# print(df_resampled.head())
df = df_resampled

## Prepare the Langchain dataframe agent

# Ensure you have your LLM instance created as `llm`

agent = create_pandas_dataframe_agent(llm=llm, df=df, verbose=True, allow_dangerous_code=True)

# Now you can invoke the agent with a query
response = agent.invoke("what are the names of the columns?")
# print(response)

## Design your prompt and ask your question
CSV_PROMPT_PREFIX = """
First set the pandas display options to show all the columns,
get the column names, then answer the question.
"""

CSV_PROMPT_SUFFIX = """
- **ALWAYS** before giving the Final Answer, try another method.
Then reflect on the answers of the two methods you did and ask yourself
if it answers correctly the original question.
If you are not sure, try another method.
- If the methods tried do not give the same result,reflect and
try again until you have two methods that have the same result.
- If you still cannot arrive to a consistent result, say that
you are not sure of the answer.
- If you are sure of the correct answer, create a beautiful
and thorough response using Markdown.
- **DO NOT MAKE UP AN ANSWER OR USE PRIOR KNOWLEDGE,
ONLY USE THE RESULTS OF THE CALCULATIONS YOU HAVE DONE**.
- **ALWAYS**, as part of your "Final Answer", explain how you got
to the answer on a section that starts with: "\n\nExplanation:\n".
In the explanation, mention the column names that you used to get
to the final answer.
"""

QUESTION = "Calculate and analyze the correlation of the 'wv' column with the remaining input columns of the 'target variable'."


print(agent.invoke(CSV_PROMPT_PREFIX + QUESTION + CSV_PROMPT_SUFFIX))
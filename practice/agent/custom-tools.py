from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

class WikiInputs(BaseModel):
    query: str = Field(
        description="query to look up in Wikipedia, should be 3 or less words"
    )
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1, 
    # doc_content_chars_max=300
)

tool = WikipediaQueryRun(
    name="wiki-tool",
    description="look up things in wikipedia",
    args_schema=WikiInputs,
    api_wrapper=api_wrapper,
    return_direct=True
)

print(tool.run("summer"))
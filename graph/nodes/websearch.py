

from typing import Any, Dict, List
from langchain_core.documents import Document
from langchain_tavily import TavilySearch

from graph.state import GraphState

web_search = TavilySearch(max_depth=3)

def websearch(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = state["documents"]

    tavily_search = web_search.invoke({"query":question})

    webresults = Document(page_content=tavily_search["query"])

    if documents is not None:
        documents.append(webresults)
    else:
        documents = [webresults]
    return {"documents":documents,"question":question}


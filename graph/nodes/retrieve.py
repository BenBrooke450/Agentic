

from typing import Any, Dict, List
from graph.state import GraphState
from ingestion import retriever


def retrieve(state: GraphState) -> Dict[str, Any]:

    print("---RETRIEVE STATE---")
    question  = state["question"]

    documents = retrieve.invoke(question)

    return {"documents": documents, "question": question}

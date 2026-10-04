


from typing import Any, Dict, List
from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:

    print("---check documents---")

    question = state["question"]

    documents = state["documents"]

    filter_docs = []

    for document in documents:
        score = retrieval_grader.invoke({"document":document.page_content,"question": question})
        grade = score.binary_score

        if grade.lower() == "yes":
            filter_docs.append(document)

        else:
            websearch = True
            continue

    return {"document":filter_docs,"question": question, "websearch": websearch}
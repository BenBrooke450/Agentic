

from dotenv import load_dotenv
from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from ingestion import retriever
load_dotenv()

def test_retrieval_grade_answer_yes():
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke({"document":doc_txt,"question": question})

    assert res.binary_score == "yes"


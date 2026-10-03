

from dotenv import load_dotenv
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import  UnstructuredLoader
from langchain_chroma import Chroma
from langchain.chat_models import init_chat_model
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import OllamaEmbeddings


load_dotenv()

embeddings = OllamaEmbeddings(model="embeddinggemma")

MODEL = "qwen3:1.7b"

llm = init_chat_model(f"ollama:{MODEL}")

URLs =["https://www.ibm.com/think/topics/ai-agents",
        "https://cloud.google.com/discover/what-is-prompt-engineering"]

docs = [doc for URL in URLs for doc in UnstructuredLoader(web_url=URL).load()]

splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

chunks_docs = splitter.split_documents(docs)

PineconeVectorStore.from_documents(chunks_docs,index_name="med-doc", embedding=embeddings,pinecone_api_key=os.getenv("PINECONE_API_KEY"))





vectorstore = PineconeVectorStore(index_name="med-doc",embedding=embeddings,pinecone_api_key=os.getenv("PINECONE_API_KEY"))


retriever = vectorstore.as_retriever()
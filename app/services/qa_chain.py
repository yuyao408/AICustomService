from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
from app.config import LLM_PROVIDER, OPENAI_API_KEY, OPENAI_MODEL, OLLAMA_MODEL, TOP_K
from app.services.vector_store import get_vector_store


def get_llm():
    if LLM_PROVIDER == "ollama":
        return ChatOllama(model=OLLAMA_MODEL)
    return ChatOpenAI(model=OPENAI_MODEL, openai_api_key=OPENAI_API_KEY, temperature=0)


def create_qa_chain():
    llm = get_llm()
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": TOP_K})
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )

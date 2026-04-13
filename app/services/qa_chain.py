from langchain_community.chat_models import ChatTongyi
from langchain.chains import RetrievalQA
from app.config import DASHSCOPE_API_KEY, DASHSCOPE_MODEL, TOP_K
from app.services.vector_store import get_vector_store


def get_llm():
    return ChatTongyi(
        model=DASHSCOPE_MODEL,
        dashscope_api_key=DASHSCOPE_API_KEY,
        temperature=0.1,
    )


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

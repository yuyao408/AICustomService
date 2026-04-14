from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.config import DASHSCOPE_API_KEY, DASHSCOPE_MODEL, TOP_K
from app.services.vector_store import get_vector_store


def get_llm():
    return ChatTongyi(
        model=DASHSCOPE_MODEL,
        dashscope_api_key=DASHSCOPE_API_KEY,
        temperature=0.1,
    )


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_qa_chain():
    llm = get_llm()
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": TOP_K})

    prompt = ChatPromptTemplate.from_messages([
        ("system", "请根据以下参考资料回答问题。如果资料信息不足，请说明。"),
        ("human", """参考资料：
{context}

问题：{question}

回答："""),
    ])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain, retriever

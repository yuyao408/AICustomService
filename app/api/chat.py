from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.qa_chain import create_qa_chain

router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    chain, retriever = create_qa_chain()
    answer = chain.invoke(request.question)
    source_docs = retriever.invoke(request.question)
    sources = [doc.page_content[:100] for doc in source_docs]
    return ChatResponse(answer=answer, sources=sources)

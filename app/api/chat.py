from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.qa_chain import create_qa_chain

router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    qa_chain = create_qa_chain()
    result = qa_chain({"query": request.question})
    sources = [doc.page_content[:100] for doc in result.get("source_documents", [])]
    return ChatResponse(answer=result["result"], sources=sources)

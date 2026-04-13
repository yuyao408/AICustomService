from pydantic import BaseModel
from typing import Optional, List


class UploadResponse(BaseModel):
    filename: str
    status: str
    chunks: int


class ChatRequest(BaseModel):
    question: str
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

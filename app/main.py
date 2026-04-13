from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload, chat

app = FastAPI(title="AI 知识库问答助手", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)


@app.get("/")
async def root():
    return {"message": "AI 知识库问答助手 API 已启动"}

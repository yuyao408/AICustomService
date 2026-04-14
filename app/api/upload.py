from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.schemas import UploadResponse
from app.services.document_loader import load_document, split_documents
from app.services.vector_store import get_vector_store, add_documents
from pathlib import Path
import shutil

router = APIRouter(prefix="/api", tags=["upload"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    file_path = str(UPLOAD_DIR / file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        documents = load_document(file_path)
        chunks = split_documents(documents)
        vector_store = get_vector_store()
        add_documents(vector_store, chunks)
        return UploadResponse(filename=file.filename, status="success", chunks=len(chunks))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import os
from app.config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    Docx2txtLoader,
)


def load_document(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()
    loaders = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".md": UnstructuredMarkdownLoader,
        ".docx": Docx2txtLoader,
    }
    loader_cls = loaders.get(ext)
    if not loader_cls:
        raise ValueError(f"不支持的文件格式: {ext}")
    return loader_cls(file_path).load()


def split_documents(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""],
    )
    return splitter.split_documents(documents)

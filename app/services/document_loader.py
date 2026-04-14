import os
from app.config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain_text_splitters import RecursiveCharacterTextSplitter
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
        ".md": UnstructuredMarkdownLoader,
        ".docx": Docx2txtLoader,
    }
    if ext == ".txt":
        return TextLoader(file_path, encoding="utf-8").load()
    loader_cls = loaders.get(ext)
    if not loader_cls:
        raise ValueError(f"不支持的文件格式: {ext}")
    return loader_cls(file_path).load()


def split_documents(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    if not documents:
        raise ValueError("文档加载后为空，无法分块")
    # 调试日志：检查加载的文档内容
    total_chars = sum(len(doc.page_content) for doc in documents)
    print(f"[DEBUG] 加载了 {len(documents)} 个文档页，总字符数: {total_chars}")
    if total_chars == 0:
        raise ValueError("文档内容为空，可能是不支持的文件类型或扫描件")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""],
    )
    return splitter.split_documents(documents)

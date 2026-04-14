from app.config import CHROMA_PERSIST_DIR, COLLECTION_NAME
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from app.config import DASHSCOPE_API_KEY, EMBEDDING_MODEL


def get_embeddings():
    return DashScopeEmbeddings(
        model=EMBEDDING_MODEL,
        dashscope_api_key=DASHSCOPE_API_KEY,
    )


def get_vector_store():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR,
    )   


def add_documents(vector_store, documents):
    vector_store.add_documents(documents)


def search_documents(vector_store, query, k=3):
    return vector_store.similarity_search(query, k=k)

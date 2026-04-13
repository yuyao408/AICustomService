from app.config import CHROMA_PERSIST_DIR, COLLECTION_NAME
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from app.config import LLM_PROVIDER, OPENAI_API_KEY


def get_embeddings():
    if LLM_PROVIDER == "ollama":
        return OllamaEmbeddings(model="nomic-embed-text")
    return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


def get_vector_store():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR,
    )


def add_documents(vector_store, documents):
    vector_store.add_documents(documents)
    vector_store.persist()


def search_documents(vector_store, query, k=3):
    return vector_store.similarity_search(query, k=k)

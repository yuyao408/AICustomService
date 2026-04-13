from dotenv import load_dotenv
import os

load_dotenv()

# LLM 配置
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "dashscope")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
DASHSCOPE_MODEL = os.getenv("DASHSCOPE_MODEL", "qwen-turbo")

# 嵌入模型配置
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-v4")

# 向量数据库配置
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma_db")
COLLECTION_NAME = "knowledge_base"

# 文本分块配置
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

# 检索配置
TOP_K = int(os.getenv("TOP_K", 3))

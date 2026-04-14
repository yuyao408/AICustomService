from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma

# 嵌入文本
text = """
Python 是一门面向对象的编程语言，由 Guido van Rossum 在 1991 年发布。
Python 广泛用于 Web 开发、数据分析、人工智能等领域。
FastAPI 是一个现代、快速的 Python Web 框架。
ChromaDB 是一个开源的向量数据库，适合本地使用。
LangChain 是一个用于构建 LLM 应用的框架。
"""

# 切块
splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap = 10)
chunks = splitter.create_documents([text])

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk.page_content}")    

# 向量化
embeddings = DashScopeEmbeddings(
    model= "text-embedding-v4",
    dashscope_api_key="sk-d5bcba5f8b724dbf879b7893862e04f1"
)

# 存入 ChromaDB（内存模式，关掉程序就没了，适合测试）
vectorstore  = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings,
)

# 查询
query = "Python 用来做什么？"
results = vectorstore.similarity_search(query, k=2)

print(f"\n问题: {query}")
print(f"检索到的相关片段:")
for i, doc in enumerate(results):
    print(f"  [{i}] {doc.page_content}")

# 接入大模型
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage

llm = ChatTongyi(
    model="qwen-turbo",
    dashscope_api_key="sk-d5bcba5f8b724dbf879b7893862e04f1",
    temperature=0.1,
)

# 构造提示词
context = "\n".join(doc.page_content for doc in results)
prompt = f"""请根据以下信息回答问题。如果信息不足，请说明。

参考资料：
{context}

问题：{query}

回答："""

message = [HumanMessage(content=prompt)]
answer = llm.invoke(message)  

print(f"\n模型回答: {answer.content}")

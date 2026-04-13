# AI 知识库问答助手

基于 LangChain + RAG 技术的知识库智能问答系统，支持文档上传、向量检索和自然语言问答。

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | FastAPI + LangChain |
| 向量数据库 | ChromaDB |
| 文档解析 | Unstructured / PyPDF2 |
| 前端 | Streamlit (轻量级 UI) |
| 语言模型 | OpenAI / Ollama 本地模型 |

## 项目结构

```
ai-knowledge-bot/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 入口
│   ├── config.py             # 配置管理
│   ├── models/               # 数据模型
│   │   └── schemas.py
│   ├── services/             # 业务逻辑
│   │   ├── document_loader.py  # 文档加载与解析
│   │   ├── text_splitter.py    # 文本分块
│   │   ├── vector_store.py     # 向量存储与检索
│   │   └── qa_chain.py         # RAG 问答链
│   └── api/                  # API 路由
│       ├── upload.py           # 文档上传接口
│       └── chat.py             # 问答接口
├── frontend/
│   └── app.py                # Streamlit 前端
├── data/                     # 文档存储目录
│   ├── uploads/              # 上传的原始文件
│   └── chroma_db/            # 向量数据库持久化
├── requirements.txt
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并填写 API Key：

```bash
cp .env.example .env
```

### 3. 启动后端

```bash
uvicorn app.main:app --reload
```

### 4. 启动前端

```bash
streamlit run frontend/app.py
```

## 功能

- [x] 多格式文档上传（PDF / TXT / Markdown / DOCX）
- [x] 自动分块与向量化
- [x] 语义检索 + LLM 问答
- [x] 简单 Web UI
- [ ] 多知识库隔离
- [ ] 对话历史管理
- [ ] 来源引用展示

## 许可证

MIT

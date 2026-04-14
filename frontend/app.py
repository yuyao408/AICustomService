import streamlit as st
import requests

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="AI 知识库问答", page_icon="📚")
st.title("📚 AI 知识库问答助手")

# 侧边栏：文档上传
with st.sidebar:
    st.header("上传知识库文档")
    uploaded_file = st.file_uploader("选择文件", type=["pdf", "txt", "md", "docx"])
    if uploaded_file and st.button("上传"):
        with st.spinner("正在处理文档..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            resp = requests.post(f"{API_BASE}/api/upload", files=files)
            if resp.status_code == 200:
                data = resp.json()
                st.success(f"上传成功! 分为 {data['chunks']} 个文本块")
            else:
                st.error(f"上传失败: {resp.text}")
    
# 主区域：问答
st.header("开始提问")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if question := st.chat_input("请输入你的问题..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            resp = requests.post(f"{API_BASE}/api/chat", json={"question": question})
            if resp.status_code == 200:
                answer = resp.json()["answer"]
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("请求失败")

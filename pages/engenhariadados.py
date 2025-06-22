import streamlit as st

st.title("📦 Engenharia de Dados")

subcategoria = st.selectbox(
    "Selecione uma subcategoria:",
    ["Microsoft Fabric", "Databricks", "Python"]
)

if subcategoria == "Microsoft Fabric":
    st.subheader("🚀 Microsoft Fabric")
    st.info("Trabalhando com parametros no Notebook do Microsoft Fabric.")
    
    st.video("videos/fabric_notebook.mp4") 
    st.info("Trabalhando com testess no Notebook do Microsoft Fabric.")
    st.video("videos/fabric_notebook.mp4") 
    
elif subcategoria == "Databricks":
    st.subheader("🔥 Databricks")
    st.info("Conteúdos, vídeos e materiais sobre Databricks.")
elif subcategoria == "Python":
    st.subheader("🐍 Python para Engenharia de Dados")
    st.info("Conteúdos e boas práticas de Python aplicadas à engenharia de dados.")
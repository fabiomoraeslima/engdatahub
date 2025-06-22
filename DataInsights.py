import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="EngData Hub | Cacau Show",
    page_icon="🍫",
    layout="wide"
)

# Título e cabeçalho
st.title("🍫 EngData Hub")
st.markdown("---")

st.subheader("👋 Bem-vindo ao **EngData Hub Cacau Show!**")

st.markdown("""
🚀 **Aqui você encontra:**
- 📚 Pílulas de conhecimento sobre Engenharia de Dados
- 🏗️ Melhores práticas e processos
- 🔍 Insights sobre ferramentas como Microsoft Fabric, Databricks, Python e muito mais

---

### 🎯 **Use o menu lateral** para escolher um tema e começar sua jornada.
""")

# Caixa de destaques
with st.container():
    st.markdown("""
    ### 🍬 **Destaques da semana**
    - 🎥 Novo vídeo sobre Microsoft Fabric disponível!
    - 📊 Tutorial prático de Databricks chegando em breve.
    - 🛠️ Melhores práticas para pipelines de dados no ar!

    ---
    """)
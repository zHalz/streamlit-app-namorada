import streamlit as st
from components.header import render_header

st.set_page_config(layout="wide")

# CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# HEADER + MENU
selected = render_header()

# =========================
# HOME (PAINEL)
# =========================
if selected == "Home":
    st.markdown("## 📊 Painel de Automação")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📂 Processamentos</h3>
            <p>Arquivos tratados</p>
            <h2>12</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>⚙️ Automações</h3>
            <p>Ferramentas disponíveis</p>
            <h2>3</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>⏱️ Tempo ganho</h3>
            <p>Horas economizadas</p>
            <h2>+5h</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🚀 Acesso rápido")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ir para Automações"):
            st.session_state["pagina"] = "Automações"

    with col2:
        if st.button("Área Especial ❤️"):
            st.session_state["pagina"] = "Especial"


# =========================
# AUTOMAÇÕES
# =========================
elif selected == "Automações":
    st.title("⚙️ Processador de PDF")

    uploaded_file = st.file_uploader("Envie seu PDF", type=["pdf"])

    if uploaded_file:
        st.success("Arquivo carregado com sucesso!")

        if st.button("Processar"):
            st.info("Processando...")
            st.success("Arquivo processado!")

            st.download_button(
                label="📥 Baixar Excel",
                data="conteudo_fake",
                file_name="resultado.xlsx"
            )


# =========================
# ESPECIAL
# =========================
elif selected == "Especial":
    st.title("❤️ Um espaço leve no meio da correria")

    st.markdown("""
    <div class="card">
        <h3>Mensagem do dia 💌</h3>
        <p>Você está indo muito bem. Continua assim 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Surpresa 😊"):
        st.balloons()
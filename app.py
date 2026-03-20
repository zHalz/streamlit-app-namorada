import streamlit as st
from streamlit_option_menu import option_menu
from components.header import render_header

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Nosso App ❤️",
    layout="wide"
)

# =========================
# CSS
# =========================
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# =========================
# HEADER
# =========================
render_header()

# =========================
# MENU
# =========================
selected = option_menu(
    menu_title=None,
    options=["Home", "Automações", "Especial"],
    icons=["house", "gear", "heart"],
    orientation="horizontal"
)

# =========================
# HOME
# =========================
if selected == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Nosso Espaço ❤️</h1>
        <p>Um lugar com tecnologia, carinho e surpresas</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">⚙️ Automações inteligentes</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📂 Processamento de arquivos</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">❤️ Espaço especial</div>', unsafe_allow_html=True)


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

            # 🔥 AQUI você vai plugar seu código real depois

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
    st.title("❤️ Um espaço só nosso")

    st.markdown("""
    <div class="card">
        <h3>Uma mensagem pra você 💌</h3>
        <p>Obrigado por estar comigo em todos os momentos</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Clique aqui 😊"):
        st.balloons()
        st.success("Você é incrível ❤️")
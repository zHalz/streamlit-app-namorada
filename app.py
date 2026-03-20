import streamlit as st

st.set_page_config(
    page_title="Nosso App ❤️",
    layout="wide"
)

# carregar css
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<div class="hero">
    <h1>Bem-vinda ❤️</h1>
    <p>Esse espaço foi feito com carinho pra você</p>
</div>
""", unsafe_allow_html=True)
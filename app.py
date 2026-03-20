import streamlit as st
from components.header import render_header
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# carregar css
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

render_header()

st.markdown("""
<div class="hero">
    <h1>Bem-vinda ❤️</h1>
    <p>Esse espaço foi feito com carinho pra você</p>
</div>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "Automações", "Especial"],
    icons=["house", "gear", "heart"],
    orientation="horizontal"
)

if selected == "Home":
    st.write("Home")

elif selected == "Automações":
    st.write("Automações")

elif selected == "Especial":
    st.write("❤️")
import streamlit as st
from streamlit_option_menu import option_menu

def render_header():
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.markdown('<div class="logo">Nosso App ❤️</div>', unsafe_allow_html=True)

    with col2:
        selected = option_menu(
            menu_title=None,
            options=["Home", "Automações", "Especial"],
            icons=["house", "gear", "heart"],
            orientation="horizontal"
        )

    return selected
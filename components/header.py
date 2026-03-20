import streamlit as st

def render_header():
    st.markdown("""
    <div class="header">
        <h2>Nosso App ❤️</h2>
    </div>
    """, unsafe_allow_html=True)
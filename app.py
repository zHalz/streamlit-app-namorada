from streamlit_option_menu import option_menu

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
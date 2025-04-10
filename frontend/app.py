import streamlit as st
from pages import logline, synopsis, scenes

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Logline Generator"

# Page registry
PAGES = {"Logline Generator": logline, "Synopsis Generator": synopsis, "Scenes Generator": scenes}


# Sidebar navigation
st.sidebar.title("Theatric.AI Navigation")
if st.sidebar.button("Go to Logline Generator"):
    st.session_state["current_page"] = "Logline Generator"
if st.sidebar.button("Go to Synopsis Generator"):
    st.session_state["current_page"] = "Synopsis Generator"

# Load the selected page
current_page = st.session_state["current_page"]
page = PAGES[current_page]
page.run()  # Each page module must define a `run()` function

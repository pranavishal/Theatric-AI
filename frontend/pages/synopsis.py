import streamlit as st
import requests

def run():
    API_BASE_URL = "http://127.0.0.1:8000"  # Backend URL

    # Title of the app
    st.title("Theatric.AI - Synopsis Generator")
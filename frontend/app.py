import streamlit as st
import requests
API_BASE_URL = "http://127.0.0.1:8000"
# Title of the app
st.title("Theatric.AI - Logline Generator")

# Input field for user prompt
prompt = st.text_area("Describe your story idea: (hint: If you can't think of anything, just tell me to come up with something on my own!)")

# Button to send the request
if st.button("Generate Logline"):
    if prompt:
        try:
            # Send a POST request to the backend
            response = requests.post(
                f"{API_BASE_URL}/generate-logline/",
                json={"prompt": prompt}
            )
            if response.status_code == 200:
                # Get the logline from the response
                logline = response.json().get("logline")
                st.success(f"Generated Logline: {logline}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a story idea to generate a logline.")

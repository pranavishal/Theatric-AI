import streamlit as st
import requests

def run():
    API_BASE_URL = "http://127.0.0.1:8000"  # Backend URL

     # Initialize session state to store logline
    if "synopsis" not in st.session_state:
        st.session_state["synopsis"] = None
    if "refinement_mode_synopsis" not in st.session_state:
        st.session_state["refinement_mode_synopsis"] = False
    if "complete_synopsis" not in st.session_state:
        st.session_state["complete_synopsis"] = False

    # Title of the app
    st.title("Theatric.AI - Synopsis Generator")

    st.text("Click below to generate your Synopsis from your logline")
    if st.button("Logline-Based Synopsis"):
        try:
            with open("../Outputs/logline.txt") as file:
                fileContents = file.read()
            response = requests.post(
                f"{API_BASE_URL}/generate-synopsis/",
                json={
                        "formerPrompt": fileContents
                }
            )
            if response.status_code == 200:
                st.session_state["synopsis"] = response.json().get("synopsis")
                st.session_state["refinement_mode"] = True
                st.success("Generated")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    

    
    # Display the logline at the bottom of the page in a read-only text box
    st.markdown("---")
    st.subheader("Current Synopsis:")
    st.text_area(
        "Generated Synopsis:",
        value=st.session_state["synopsis"] or "No synopsis generated yet.",
        height=150,
        # Make it read-only
        disabled=st.session_state["complete_synopsis"]
    )
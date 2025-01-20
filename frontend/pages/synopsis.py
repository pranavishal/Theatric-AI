import streamlit as st
import requests
import os

# Ensure the Outputs directory exists
OUTPUTS_DIR = "../Outputs"
if not os.path.exists(OUTPUTS_DIR):
    os.makedirs(OUTPUTS_DIR)

def run():
    API_BASE_URL = "http://theatratic-backend-container:8000"  # Backend URL

    # Initialize session state variables
    if "synopsis" not in st.session_state:
        st.session_state["synopsis"] = None
    if "refinement_mode_synopsis" not in st.session_state:
        st.session_state["refinement_mode_synopsis"] = False
    if "complete_synopsis" not in st.session_state:
        st.session_state["complete_synopsis"] = False

    # Title of the app
    st.title("Theatric.AI - Synopsis Generator")

    # Generate Synopsis from Logline
    st.text("Click below to generate your Synopsis from your logline")
    if st.button("Logline-Based Synopsis"):
        logline_file = os.path.join(OUTPUTS_DIR, "logline.txt")
        if os.path.exists(logline_file):
            try:
                with open(logline_file, "r") as file:
                    fileContents = file.read()
                response = requests.post(
                    f"{API_BASE_URL}/generate-synopsis/",
                    json={"formerPrompt": fileContents}
                )
                if response.status_code == 200:
                    st.session_state["synopsis"] = response.json().get("synopsis")
                    st.session_state["refinement_mode_synopsis"] = True
                    st.success("Synopsis generated successfully!")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error reading logline file: {e}")
        else:
            st.error("Logline file not found. Please generate a logline first.")

    # Display the current synopsis
    st.markdown("---")
    st.subheader("Current Synopsis:")
    st.text_area(
        "Generated Synopsis:",
        value=st.session_state["synopsis"] or "No synopsis generated yet.",
        height=150,
        disabled=st.session_state["complete_synopsis"]
    )

    # Mark as Complete (Optional future feature)
    if st.button("Mark as Complete"):
        if st.session_state["synopsis"]:
            st.session_state["complete_synopsis"] = True
            try:
                with open(os.path.join(OUTPUTS_DIR, "synopsis.txt"), "w") as file:
                    file.write(st.session_state["synopsis"])
                st.success("Synopsis saved successfully!")
            except Exception as e:
                st.error(f"Error saving synopsis: {e}")
        else:
            st.warning("Please generate a synopsis first.")


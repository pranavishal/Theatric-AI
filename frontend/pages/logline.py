import streamlit as st
import requests
import os

# Ensure the Outputs directory exists
OUTPUTS_DIR = "./Outputs"
if not os.path.exists(OUTPUTS_DIR):
    os.makedirs(OUTPUTS_DIR)


def run():
    API_BASE_URL = "http://127.0.0.1:8000"  # Backend URL

    # Title of the app
    st.title("Theatric.AI - Logline Generator")

    # Initialize session state variables
    if "logline" not in st.session_state:
        st.session_state["logline"] = None
    if "refinement_mode" not in st.session_state:
        st.session_state["refinement_mode"] = False
    if "complete" not in st.session_state:
        st.session_state["complete"] = False

    # Input field for user prompt
    prompt = st.text_area(
        "Describe your story idea: (hint: If you can't think of anything, just tell me to come up with something on my own!)"
    )

    # Button to generate logline
    if st.button("Generate Logline"):
        if prompt.strip():
            try:
                response = requests.post(
                    f"{API_BASE_URL}/generate_logline/", json={"prompt": prompt}
                )
                if response.status_code == 200:
                    st.session_state["logline"] = response.json().get("logline")
                    st.session_state["refinement_mode"] = True
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a story idea to generate a logline.")

    # Refinement functionality
    if st.session_state["refinement_mode"]:
        st.markdown("### Refinement Instructions")
        refinement = st.text_input("How would you want me to refine this logline?")
        if st.button("Refine!"):
            if refinement.strip():
                try:
                    with st.spinner("Refining logline... Please wait!"):
                        response = requests.post(
                            f"{API_BASE_URL}/generate_logline/",
                            json={
                                "prompt": st.session_state["logline"],
                                "refinement": refinement,
                            },
                        )
                        if response.status_code == 200:
                            st.session_state["logline"] = response.json().get("logline")
                        else:
                            st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter some refinement instructions")

    # Display the current logline
    st.markdown("---")
    st.subheader("Current Logline:")
    st.text_area(
        "Generated Logline:",
        value=st.session_state["logline"] or "No logline generated yet.",
        height=150,
        disabled=st.session_state["complete"],
    )

    # Mark as Complete and Save Logline
    if st.button("Mark as Complete"):
        if st.session_state["logline"]:
            st.session_state["complete"] = True
            try:
                with open(os.path.join(OUTPUTS_DIR, "logline.txt"), "w") as file:
                    file.write(st.session_state["logline"])
                st.success("Logline saved successfully!")
            except Exception as e:
                st.error(f"Error saving logline: {e}")
        else:
            st.warning("Please generate a logline first.")

    # Navigation to the next page
    if st.session_state["complete"] and st.button("Next ->"):
        st.session_state["current_page"] = "Synopsis Generator"

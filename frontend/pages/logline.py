import streamlit as st
import requests

def run():
    API_BASE_URL = "http://127.0.0.1:8000"  # Backend URL

    # Title of the app
    st.title("Theatric.AI - Logline Generator")

    # Initialize session state to store logline
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
        if prompt:
            try:
                response = requests.post(
                    f"{API_BASE_URL}/generate-logline/",
                    json={"prompt": prompt}
                )
                if response.status_code == 200:
                    st.session_state["logline"] = response.json().get("logline")
                    st.session_state["refinement_mode"] = True
                    #st.success("Logline Generated Successfully!")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a story idea to generate a logline.")

    if st.session_state["refinement_mode"]:
        st.markdown("### Refinement Instructions")
        refinement = st.text_input("How would you want me to refine this logline?")
        if st.button("Refine!"):
            if refinement.strip():
                try:
                    with st.spinner("Refining logline... Please wait!"):
                        response = requests.post(
                            f"{API_BASE_URL}/generate-logline/",
                            json={
                                    "prompt": st.session_state["logline"],
                                    "refinement": refinement
                                }
                        )
                        if response.status_code == 200:
                            st.session_state["logline"] = response.json().get("logline")
                            #st.success("Logline Refined Successfully!")
                        else:
                            st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter some refinement instructions")


    # Display the logline at the bottom of the page in a read-only text box
    st.markdown("---")
    st.subheader("Current Logline:")
    st.text_area(
        "Generated Logline:",
        value=st.session_state["logline"] or "No logline generated yet.",
        height=150,
        # Make it read-only
        disabled=st.session_state["complete"]
    )

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Mark as Complete"):
            if st.session_state["logline"]:
                st.session_state["complete"] = True
                with open("../Outputs/logline.txt", "w") as file:
                    file.write(st.session_state["logline"])
            else:
                st.warning("Please create a logline")

    if st.session_state["complete"]:
        col1.markdown("✔️", unsafe_allow_html=True)

    if st.session_state["complete"]:
        if st.button("Next ->"):
            st.session_state["current_page"] = "Synopsis Generator"
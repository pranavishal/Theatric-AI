import streamlit as st
import requests
import os
import time 

# Ensure the Outputs directory exists
OUTPUTS_DIR = "./Outputs"
if not os.path.exists(OUTPUTS_DIR):
    os.makedirs(OUTPUTS_DIR)

def run():
    API_BASE_URL = "http://127.0.0.1:8000"  # Backend URL

    # Initialize session state variables
    if "synopsis" not in st.session_state:
        st.session_state["synopsis"] = None
    
    # Initialize session state variables
    if "scenes" not in st.session_state:
        st.session_state["scenes"] = None
    
    if "complete" not in st.session_state:
         st.session_state["complete"] = False
    


    synopsis_file = os.path.join(OUTPUTS_DIR, "synopsis.txt")
    if os.path.exists(synopsis_file):
        try:
             with open(synopsis_file, "r") as file:
                fileContents = file.read()
             response = requests.post(
                    f"{API_BASE_URL}/split_synopsis_into_scenes/",
                    json={"synopsis": fileContents},
                )
             if response.status_code == 200:
                    st.session_state["scenes"] = response.json().get("scenes")
                    st.success("scenes generated successfully!")
                    try:
                        with open(os.path.join(OUTPUTS_DIR, "scenes.txt"), "w") as file:
                            file.write(st.session_state["scenes"])
                        st.success("Scenes saved successfully!")
                        st.session_state["complete"] = True
                    except Exception as e:
                        st.error(f"Error saving scenes: {e}")
             else:
                    st.error(f"Error: {response.status_code} - {response.text}")
                         
        except Exception as e:
                st.error(f"Error reading logline file: {e}")
    else:
        st.error("Synopsis file not found. Please generate a Synopsis first.")
    
    
    
    # Display the current synopsis
    st.markdown("---")
    st.subheader("Current Scenes:")
    st.text_area(
        "Generated Scenes:",
        value=st.session_state["scenes"] or "No synopsis generated yet.",
        height=150,
        disabled=True,
    )

    # Navigation to the next page
    if st.session_state["complete"] and st.button("Generate Trailer ->"):
        with st.spinner("Generating Trailer..."):
             time.sleep(10)


        
        
    




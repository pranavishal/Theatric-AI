# Theatric.AI - Logline Generator

Theatric.AI is a tool for filmmakers and writers that generates loglines, synopses, and treatments for their story ideas. Built using **FastAPI** for the backend and **Streamlit** for the frontend, it leverages OpenAI's GPT-4o model for text outputs so far.

# Installation

### Preqrequisites
- Python 3.9 or higher
- pip (Python package installer)
- Git

### Setup
1. Clone the repository
2. Install the requirements using the following command: pip install -r requirements.txt
3. Create a .env file in the backend folder and add your OpenAI API key: OPENAI_API_KEY=your-openai-key

### Running the Application
1. Running the backend:
Navigate to the backend folder
run the following command: uvicorn main:app --reload

2. Running the frontend:
Navigate to the frontend folder
run the following command **in a second terminal**: streamlit run app.py

Open http://localhost:8501 in your browser to access the app.

## Technologies Used

- **Backend**: FastAPI, OpenAI GPT-4o
- **Frontend**: Streamlit
- **Deployment**: Uvicorn
- **Dependencies**: python-dotenv, requests



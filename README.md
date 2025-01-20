# Theatric.AI - Logline Generator

Theatric.AI is a tool for filmmakers and writers that generates loglines, synopses, and treatments for their story ideas. Built using **FastAPI** for the backend and **Streamlit** for the frontend, it leverages OpenAI's GPT-4 model for text outputs.

## Installation

### Prerequisites
- Docker
- Docker Compose
- OpenAI API Key (required for backend functionality)

### Setup and Usage

#### 1. Clone the Repository
```bash
git clone https://github.com/your-repo-url.git
cd Theatric-AI
```

#### 2. Add Your OpenAI API Key
Update the `docker-compose.yml` file to include your OpenAI API key:
```yaml
environment:
  - OPENAI_API_KEY=your_openai_api_key
```

#### 3. Start the Application
Run the following command to start both the frontend and backend:
```bash
docker compose up -d
```

#### 4. Access the Application
- Frontend: [http://127.0.0.1:8501](http://127.0.0.1:8501)
- Backend API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### 5. Stop the Application
To stop the application, use:
```bash
docker compose down
```

---

## Technologies Used

- **Backend**: FastAPI, OpenAI GPT-4
- **Frontend**: Streamlit
- **Deployment**: Docker, Docker Compose
- **Dependencies**: Python, requests, python-dotenv

---

## API Endpoints
The backend exposes the following endpoints:

### `/generate-logline/`
**Method**: POST  
**Description**: Generates a logline based on a provided story idea.  
**Payload**:
```json
{
  "prompt": "A young chef discovers love in her kitchen."
}
```
**Response**:
```json
{
  "logline": "A young chef discovers love while exploring her culinary skills in Paris."
}
```

### `/generate-synopsis/`
**Method**: POST  
**Description**: Generates a synopsis based on a previously generated logline.  
**Payload**:
```json
{
  "formerPrompt": "A young chef discovers love while exploring her culinary skills in Paris."
}
```
**Response**:
```json
{
  "synopsis": "In a quaint Parisian cafe, a talented but shy chef discovers her passion for cooking while forming a heartfelt connection with a charming food critic."
}
```

---

## Project Structure
```plaintext
Theatric-AI/
├── frontend/             # Frontend code (Streamlit)
│   ├── Outputs/          # Generated outputs
│   ├── app.py            # Main Streamlit app
│   |── pages/            # Logline and Synopsis modules
|   |── requirements.txt  # Dependencies for the backend
├── backend/              # Backend code (FastAPI)
│   ├── main.py           # Main application file
│   └── requirements.txt  # Dependencies for the backend
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # Project documentation
```

---


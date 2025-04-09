from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.logline.models import LoglineRequest
from services.synopsis.models import SynopsisRequest
from services.logline.service import generate_logline
from services.synopsis.service import generate_synopsis


app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/generate_logline")
async def generate_logline_endpoint(request: LoglineRequest):
    try:
        logline = generate_logline(request)
        return {"logline": logline}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate_synopsis")
async def generate_synopsis_endpoint(request: SynopsisRequest):
    try:
        synopsis = generate_synopsis(request)
        return {"synopsis": synopsis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

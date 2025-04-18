from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.logline.models import LoglineRequest
from services.synopsis.models import SynopsisRequest
from services.scenes.models import SceneRequest
from services.narration.models import NarrationRequest
from services.prompts.models import PromptRequest
from services.logline.service import generate_logline
from services.synopsis.service import generate_synopsis
from services.scenes.service import generate_scenes
from services.narration.service import generate_narration
from services.prompts.service import generate_prompt



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

@app.post("/split_synopsis_into_scenes")
async def split_synopsis_into_scenes_endpoint(request: SceneRequest):
    try:
        scenes = generate_scenes(request)
        return {"scenes": scenes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_narration")
async def generate_narration_endpoint(request: NarrationRequest):
    try:
        narration = generate_narration(request)
        return {"narration": narration}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_trailer")
async def generate_trailer_endpoint(request: PromptRequest):
    try:
        theNarrationReq = NarrationRequest(
            scenes=request.promptBase,
        )
        narration = generate_narration(theNarrationReq)
        prompts = generate_prompt(request)
        print(prompts)
        return {"narration": narration}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


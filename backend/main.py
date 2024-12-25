from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Loading env variables (the openai gpt4 api key)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str = ""
    refinement: str = ""
    formerPrompt: str = ""

@app.post("/generate-logline/")
async def generate_logline(request: TextRequest):
    try:
        if not request.refinement:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a screenwriting assistant. You are to help generate a logline based on the information you recive in the prompt. If the prompt is empty, generate one completely by yourself."},
                    {"role": "user", "content": f"Create a logline: {request.prompt}"}
                ],
                temperature=0.5
            )
            return {"logline": response.choices[0].message.content}
        else:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a screenwriting assistant. You are to help generate a logline based on the information you recive in the prompt, or help refine an existing prompt based on refinement feedback."},
                    {"role": "user", "content": f"The current logline is {request.prompt}. Refine it with the following instructions: {request.refinement}"}
                ],
                temperature=0.5
            )
            return {"logline": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-synopsis/")
async def generate_logline(request: TextRequest):
    try:
        if not request.refinement:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": """You are a screenwriting assistant. 
                     You are to help generate a synopsis based on the logline you recieve in the prompt. 
                     It is to be a few paragraphs in length with the purpose of fleshing out the idea given in the logline. 
                     Be detailed, introduce characters, setting, and give the user a lot of clarity about the story from them reading your synopsis."""},
                    {"role": "user", "content": f"The logline is currently {request.formerPrompt}. Expand on this idea to make it a full synopsis."}
                ],
                temperature=0.5
            )
            return {"synopsis": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Loading env variables (the openai gpt4 api key)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class LoglineRequest(BaseModel):
    prompt: str
    refinement: str = ""

@app.post("/generate-logline/")
async def generate_logline(request: LoglineRequest):
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

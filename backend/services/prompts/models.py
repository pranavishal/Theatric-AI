from pydantic import BaseModel

class PromptRequest(BaseModel):
    promptBase: str
    promptType: str = ""
    promptContext: str
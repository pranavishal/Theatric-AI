from pydantic import BaseModel


class LoglineRequest(BaseModel):
    prompt: str
    refinement: str = ""

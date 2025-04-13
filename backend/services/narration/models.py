from pydantic import BaseModel


class NarrationRequest(BaseModel):
    scenes: str

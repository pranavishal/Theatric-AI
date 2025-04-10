from pydantic import BaseModel

class SceneRequest(BaseModel):
    synopsis: str


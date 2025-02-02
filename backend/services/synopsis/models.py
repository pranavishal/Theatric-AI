from pydantic import BaseModel


class SynopsisRequest(BaseModel):
    formerPrompt: str

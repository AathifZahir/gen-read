from pydantic import BaseModel

class RepoCloneRequest(BaseModel):
    url: str
from fastapi import FastAPI
from pydantic import BaseModel

# Types
class Request(BaseModel):
    content: str

class RedFlag:
    RedFlagId: int
    Phrase: str

# App
app = FastAPI()

@app.post("/check_tweet")
async def root(request: Request) -> list[RedFlag]:
    tweet: str = Request.content
    raise NotImplementedError()

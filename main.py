from fastapi import FastAPI
from service_runner import run_services
from type_annotations import RedFlag, Request

# App
app = FastAPI()

@app.post("/red_flags")
async def root(request: Request) -> list[RedFlag]:
    tweet: str = request.content

    return run_services(tweet)

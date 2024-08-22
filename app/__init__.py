from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ResistanceModel(BaseModel):
    shorthand: str


@app.get("/resistance")
def _() -> ResistanceModel:
    return ResistanceModel(shorthand="0R")

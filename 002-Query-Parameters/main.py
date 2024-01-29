from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class QueryModel(str, Enum):
    German = "GR"
    Chinese = "CZH"
    European = "EU"

@app.get('/items/')
async def read_item(made: QueryModel, skip: int = 0, limit: int = None):
    return {"made": made, "skip": skip, "limit": limit}


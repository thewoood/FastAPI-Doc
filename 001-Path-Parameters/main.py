import uvicorn
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    Razer = "Razer Co."
    Adobe = "Adobe Ent."
    Google = "Alphabet"

app = FastAPI()

@app.get("/items/{model_name}")
async def item(model_name: ModelName):
    if model_name.value == ModelName.Adobe.value:
        return {"Product": "PhotoShop"}
    elif model_name is ModelName.Google:
        return {"Product": "Pixel"}
    return {"Product": f"{ModelName.Razer.value} has no products!"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
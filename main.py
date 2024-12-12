from fastapi import FastAPI
from pydantic import BaseModel

from ml_models import AnimalClassificationModel

app = FastAPI()


class Features(BaseModel):
    paws_count: int
    has_fur: int
    mammal: int


@app.post("/make_inference")
def make_inference(features: Features):
    result = AnimalClassificationModel.make_inference(
        paws_count=features.paws_count, has_fur=features.has_fur, mammal=features.mammal
    )
    return {"result": result}

from fastapi import FastAPI
from DataModel import Model

app = FastAPI()


@app.get('/api')
async def hello():
    return {"Hello World"}


@app.post("/predict")
async def predict(data: Model):
    return data


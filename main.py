#Import FastAPI
from fastapi import FastAPI

app = FastAPI()

#V1 - API first route
@app.get("/")
def read_root():
    return {"Hello": "World"}
from typing import Union

from fastapi import FastAPI

from fastapi import FastAPI
from email_api import router as email_router 

app = FastAPI()

app.include_router(email_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
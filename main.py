from fastapi import FastAPI
from fastapilogger import FastAPILogger

app = FastAPI()

app.add_middleware(FastAPILogger)

@app.get("/")
def read_root():
    return {"Hello": "World"}

  
# from typing import Union

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
from typing import Union

from fastapi import FastAPI


from fastapilogger import FastAPILogger

app = FastAPI()

app.add_middleware(FastAPILogger)
# app.middleware("http")(FastAPILogger())

# Use FastAPILogger as middleware
# app.middleware("http")(FastAPILogger().log_middleware)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
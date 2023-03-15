from typing import Union
import uvicorn
from fastapi import FastAPI, Query,Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id:int=Path(title="The ID of the item to get"),
#     q:Union[str,None]=Query(default=None,alias="item-query"),
# ):
#     results =  {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results

if __name__=='__main__':
    uvicorn.run(app)
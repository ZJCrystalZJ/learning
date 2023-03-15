import uvicorn
from enum import  Enum
from fastapi import FastAPI,Query
from typing import Union
from pydantic import BaseModel
from pydantic import Required
from typing import List
##查询参数和字符串校验
app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# @a@app.get("/items/")
# async def read_items(
#     q: Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: list = Query(default=[])):
#     query_items = {"q": q}
#     return query_items




#查询参数列表多个值
# app = FastAPI()
#
# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default=None)):
#     query_items = {"q": q}
#     return query_items






# @app.get("/items/")
# async def read_items(q: str = Query(default=Required, min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results




#省略号声明必须参数


# app = FastAPI()
# @app.get("/items/")
# async def read_items(q: str = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#声明为必须参数
# app = FastAPI()
#
# @app.get("/items/")
# async def read_items(q: str = Query(min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#默认值
# app = FastAPI()
# @app.get("/items/")
# async def read_items(
#     q:str= Query(default="^fixedquery$",min_length=3)
# ):
#     results={"items":[{"item_id": "Foo"},{"item_id":"Bar"}]}
#     if q :
#         results.update({"q":q})
#     return results

# @app.get("/items/")
# async def read_items(
#     q:Union[str,None] = Query(
#         default=None,min_length=3,max_langth=50,regex="^fixedquery$")
# ):
#     results={"items":[{"item_id": "Foo"},{"item_id":"Bar"}]}
#     if q :
#         results.update({"q":q})
#     return results

# @app.get("/items")
# async def read_items(q:Union[str,None] = None):
#     results={"items":[{"item_id": "Foo"},{"item_id":"Bar"}]}
#     if q :
#         results.update({"q":q})
#     return results

if __name__=='__main__':
    uvicorn.run(app)
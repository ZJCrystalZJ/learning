import uvicorn
from enum import  Enum
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
##请求体
class Item(BaseModel):
    name:str
    description:Union[str,None]=None
    price:float
    tax: Union[float,None]=None

app = FastAPI()
##请求体+路径参数+查询参数
@app.put("/items/{item_id}")
async def create_item(item_id:int,item:Item,q:Union[str,None]=None):
    result = {"item_id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result



##请求体+路径参数
# @app.put("/items/{item_id}")
# async def create_item(item_id:int,item:Item):
#     return {"item_id": item_id,**item.dict()}
#
# @app.post("/items")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax= item.price+item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item
if __name__=='__main__':
    uvicorn.run(app)
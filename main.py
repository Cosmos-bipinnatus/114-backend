from typing import Annotated, List, Union
import os
import google_auth_oauthlib
from fastapi import Body, Cookie, FastAPI, Form, Path
from pydantic import BaseModel, Field

class TokenRequest(BaseModel):
    id_token:str

app = FastAPI()
"""
@app.post("/atuh/google")
async def google_auth(request:TokenRequest):

"""

@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"username": username}

@app.get("/'")
async def root():
    return  {"message": "Hello wowrld"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

"""

@app.get("/items/")
async def read_item(skip: int =0 , limit: int = 10):
    return fake_items_db[skip: skip + limit]

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}      
                  
]

"""

@app.get("/items")
async def read_items(ads_id: Annotated[str | None, Cookie()]):
    return {"ads_id": ads_id}

#async def read_items(ads_id: Annotated[str | None, Cookie()]) -> list[Item]:

"""

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump() #item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

    


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return Item



@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int , Path(title="The ID of the item to get",ge=0,le=1000)],
    q: str | None = None,
    item: Item | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results



@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
"""

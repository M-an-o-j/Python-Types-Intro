from fastapi import FastAPI, Form, File, UploadFile
from typing_extensions import Annotated
from pydantic import BaseModel
from datetime import datetime
from typing import Union
from fastapi.encoders import jsonable_encoder

app = FastAPI()

fake_db = {
    
}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


#Home Apis
@app.get("/", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def root():
    return {"message": "Hello World"}

@app.get("/head", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def head():
    return {"message": "Hello World"}

@app.post("/contact", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def contact(username: str, password: str):
    return {"message": "Hello World"}

@app.get("/tail", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}

#User Api
@app.get("/about", tags=["User"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}

@app.get("/users", tags=["User"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}

@app.post("/login/", tags=["User"])
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

#files
@app.post("/files/dd", tags=["Files"])
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/", tags=["Files"])
async def create_upload_file(file: UploadFile):
    return {
        "filename": file.filename,
        "filesize" : file.headers.values
        }

@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
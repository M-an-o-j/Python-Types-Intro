from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def root():
    return {"message": "Hello World"}
@app.get("/head", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def head():
    return {"message": "Hello World"}
@app.get("/tail", tags=["Home"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}

@app.get("/about", tags=["profile"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}
@app.get("/users", tags=["profile"], summary="For root page", description="This is the router for homepage it uses the root function")
async def tail():
    return {"message": "Hello World"}

from fastapi import FastAPI, File, UploadFile

app = FastAPI(
    title="Upload file",
    description="This is just simple code to upload files in fastapi server"
)

# MAX_FILE_SIZE = 1024 # 10 MB

@app.post("/upload")
async def upload_file(file: UploadFile = File()):
    # Save the uploaded file to the filesystem
    with open(f"uploads/{file.filename}", "wb") as f:
        content = await file.read()
        f.write(content)

    return {"filename": file.filename}

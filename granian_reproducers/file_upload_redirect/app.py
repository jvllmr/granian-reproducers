from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile, File, APIRouter

from typing import Annotated

FILESIZE = 250 * 1024  # 250 KiB
FILE = Path("granian_reproducers/infinite_upload/test.txt")


if not FILE.exists():
    FILE.write_bytes(b"\0" * FILESIZE)
    print(f"Created {FILE}: {FILESIZE} bytes")

app = FastAPI()


upload_router = APIRouter(prefix="/upload")


@app.get("/")
async def get_form():
    return FileResponse("granian_reproducers/infinite_upload/index.html")


@upload_router.post("/")
async def upload_file(file: Annotated[UploadFile, File()]):
    content = await file.read()
    return content


app.include_router(upload_router)

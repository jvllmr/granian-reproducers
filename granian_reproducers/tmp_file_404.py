"""
This is a case where granian cannot find the temporary file
probably because granian runs the background job before looking for the file to open it.

Pattern works with:
    - uvicorn
    - gunicorn (with uvicorn worker)
"""

from fastapi.responses import FileResponse
from fastapi import FastAPI
import tempfile
from starlette.background import BackgroundTask


class PlainTextResponse(FileResponse):
    media_type = "text/plain"


def create_plain_text_response(content: bytes, filename: str) -> PlainTextResponse:
    f = tempfile.NamedTemporaryFile()
    f.write(content)
    return PlainTextResponse(
        f.name,
        filename=f"{filename}.txt",
        background=BackgroundTask(lambda: f.close()),
    )


app = FastAPI()


@app.get("/")
async def fetch_text_file():
    return create_plain_text_response(b"Hello from test app!", "test")

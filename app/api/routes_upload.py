from fastapi import APIRouter, UploadFile, File
from app.services.parser import parse_file

router = APIRouter(prefix="/upload")

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    content = await parse_file(file)
    return {"content": content}

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import generate_questions_and_flashcards

router = APIRouter(prefix="/generate")

class MaterialInput(BaseModel):
    content: str

@router.post("/")
async def generate(input: MaterialInput):
    result = await generate_questions_and_flashcards(input.content)
    return result

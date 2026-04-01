from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import ask_question

router = APIRouter()


# Request model
class ChatRequest(BaseModel):
    question: str


# Response model
class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    answer = ask_question(request.question)

    return {"answer": answer}
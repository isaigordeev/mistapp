from mistralai import Mistral
from pydantic import BaseModel
from mistapp.config import api_key

from fastapi import APIRouter, Depends, HTTPException

match_generator_router = APIRouter()


def get_mistral_client():
    return Mistral(api_key=api_key)

class MatchRequest(BaseModel):
    model: str = "mistral-small-2501"
    content: str = "How are you doing?"


@match_generator_router.post("/match")
async def generate_role_match(
    request: MatchRequest,
    client: Mistral = Depends(get_mistral_client),
):
    chat_response = client.chat.complete(
        model=request.model,
        messages=[{"role": "user", "content": request.content}],
    )

    return {"response": chat_response.choices[0].message.content}
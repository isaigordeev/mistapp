from typing import Union

from mistralai import Mistral
from pydantic import BaseModel
from mistapp.config import api_key

from fastapi import APIRouter, Depends, HTTPException
from mistapp import generate_prompt, STANDART_PROMPT
import json

match_generator_router = APIRouter()

def get_mistral_client():
    return Mistral(api_key=api_key)

class MatchRequest(BaseModel):
    model: str = "mistral-small-2501"
    experience: str = "ML Engineer"
    role: str = "Physics teacher"
    prompt: str = STANDART_PROMPT
    postprompt: str = None,


@match_generator_router.post("/match")
async def generate_role_match(
    request: MatchRequest,
    client: Mistral = Depends(get_mistral_client),
):

    prompt = generate_prompt(request.experience, request.role)

    assert prompt is not None
    messages = [{"role": "user", "content": prompt}]

    if request.postprompt:
        messages.append({"role": "user", "content": request.postprompt})

    chat_response = client.chat.complete(
        model=request.model,
        messages=messages
    )

    if not request.postprompt:
        return bool(int(chat_response.choices[0].message.content))
    else:
        return (chat_response.choices[0].message.content)
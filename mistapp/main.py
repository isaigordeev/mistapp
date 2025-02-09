from fastapi import FastAPI, HTTPException, Depends
from mistapp.services.generate_match import match_generator_router

app = FastAPI()
@app.get("/")
async def root():
    return {"Hello": "World"}

app.include_router(match_generator_router, prefix="/services", tags=["match"])



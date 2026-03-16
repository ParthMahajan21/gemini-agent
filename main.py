import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

class Request(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Gemini AI Agent Running"}

@app.post("/agent")
def summarize(request: Request):
    prompt = f"Summarize this text: {request.text}"
    response = model.generate_content(prompt)

    return {"summary": response.text}

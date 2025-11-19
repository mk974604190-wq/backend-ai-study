from fastapi import FastAPI
from ai import ask_ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Study Backend Online!"}

@app.post("/ask")
def ask_question(question: str):
    answer = ask_ai(question)
    return {"answer": answer}

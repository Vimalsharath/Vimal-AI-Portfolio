from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rag.Chatbot import ask_ai


app = FastAPI()


# Allow React frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():

    return {
        "message": "Vimal AI Backend Running"
    }



@app.post("/chat")
def chat(question: dict):

    user_question = question["question"]

    answer = ask_ai(user_question)

    return {
        "answer": answer
    }
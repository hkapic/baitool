from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

ALLOWLIST_KEYWORDS = [
    "quran",
    "islam",
    "sunnah",
    "math",
    "geometry",
    "school",
    "education"
]

class Question(BaseModel):
    text: str

def is_allowed(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in ALLOWLIST_KEYWORDS)

@app.post("/ask")
def ask_question(q: Question):
    if not is_allowed(q.text):
        return {
            "status": "blocked",
            "response": "This question is not allowed. Please ask a school-appropriate question."
        }

    # Placeholder for real AI (safe response)
    return {
        "status": "ok",
        "response": "This is a safe AI-generated response based on approved content."
    }

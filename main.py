from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ServeX Review Categorizer")


class ReviewIn(BaseModel):
    text: str


CATEGORY_KEYWORDS = {
    "Good": ["good", "great", "love", "tasty", "amazing", "perfect", "delicious", "fresh"],
    "Bad": ["bad", "terrible", "awful", "cold", "stale", "worst", "burnt", "rude"],
    "Complain": ["complain", "complaint", "late", "refund", "manager", "dirty", "slow"],
    "Suggestions": ["suggest", "idea", "could", "should", "maybe", "wish", "recommend"]
}

PRIORITY_ORDER = ["Complain", "Bad", "Suggestions", "Good"]


def categorize(text: str) -> str:
    lowered = text.lower()
    scores = {category: 0 for category in CATEGORY_KEYWORDS}

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in lowered:
                scores[category] += 1

    best_score = max(scores.values())
    if best_score == 0:
        return "Suggestions"

    best_categories = [category for category, score in scores.items() if score == best_score]
    for category in PRIORITY_ORDER:
        if category in best_categories:
            return category

    return "Suggestions"


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/categorize")
def categorize_review(payload: ReviewIn) -> dict:
    category = categorize(payload.text)
    return {"category": category}

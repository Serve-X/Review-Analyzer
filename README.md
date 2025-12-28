# ServeX Review Categorizer

FastAPI service that categorizes review text into Good, Bad, Complain, or Suggestions using keyword rules.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

## Keyword rules

The service uses keyword matching to assign a category and defaults to `Suggestions` if no keywords match.

## API

- `POST /categorize` with `{ "text": "your review" }`
- `GET /health`

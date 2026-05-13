# ai-data-quality-explainer
AI data quality explainer

# AI Data Quality Incident Explainer

## Setup

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoint

POST /analyze-run

## Example

```
curl -X POST "http://127.0.0.1:8000/analyze-run" \
-H "Content-Type: application/json" \
-d @sample_request.json
```

## Output
Returns:
validation issues
structured KPI analysis
AI-generated incident summary (mocked)

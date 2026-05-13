from fastapi import FastAPI
from app.models import RunRequest
from app.validator import validate_rows
from app.analyzer import analyze
from app.llm import generate_incident_summary
from app.utils import generate_run_trace_id, get_timestamp

app = FastAPI()

@app.post("/analyze-run")
def analyze_run(payload: RunRequest):

    issues = validate_rows(payload.rows)
    analysis = analyze(payload.rows)

    summary = generate_incident_summary(
        analysis=analysis,
        issues=issues,
        run_id=payload.run_id
    )

    trace_id = generate_run_trace_id(payload.run_id)

    return {
        "run_id": payload.run_id,
        "trace_id": trace_id,
        "timestamp": get_timestamp(),
        "source_file": payload.source_file,
        "analysis": analysis,
        "issues": issues,
        "incident_summary": summary
    }

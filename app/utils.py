import uuid
import json
from datetime import datetime


def generate_run_trace_id(run_id: str) -> str:
    """
    Creates a trace-friendly ID combining run_id + unique suffix.
    Useful for logs and debugging distributed runs.
    """
    return f"{run_id}_{uuid.uuid4().hex[:8]}"


def safe_json_dumps(data):
    """
    Safely serialize data for logging or debugging.
    Avoids crashes when non-serializable types appear.
    """
    try:
        return json.dumps(data, default=str)
    except Exception:
        return str(data)


def get_timestamp():
    """
    Standard timestamp for incident reports/logging.
    """
    return datetime.utcnow().isoformat() + "Z"


def truncate_text(text: str, max_length: int = 300) -> str:
    """
    Prevents overly long LLM prompts or logs.
    """
    if not text:
        return ""
    return text[:max_length] + "..." if len(text) > max_length else text

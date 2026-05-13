from pydantic import BaseModel
from typing import List, Optional, Any, Dict

class RunRequest(BaseModel):
    run_id: str
    source_file: str
    rows: List[Dict[str, Any]]
    previous_day_summary: Optional[str] = None

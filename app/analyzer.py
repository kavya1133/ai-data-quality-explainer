from collections import Counter

def analyze(rows):
    summary = {}

    summary["total_rows"] = len(rows)
    summary["missing_kpi"] = sum(1 for r in rows if r.get("kpi_value") is None)
    summary["status_counts"] = dict(Counter(r.get("status") for r in rows))

    return summary

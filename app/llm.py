def generate_incident_summary(analysis, issues, run_id):
    return f"""
Run {run_id} Data Quality Incident:

- Total records: {analysis['total_rows']}
- Missing KPI values: {analysis['missing_kpi']}
- Status distribution: {analysis['status_counts']}

Detected Issues:
{chr(10).join("- " + i for i in issues[:4]) if issues else "- No major issues detected"}

Impact: Potential KPI under-reporting and region-level inconsistency.
Recommendation: Validate upstream ingestion and enforce schema checks.
"""

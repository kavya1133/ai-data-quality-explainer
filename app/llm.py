def generate_incident_summary(analysis, issues, run_id):

    return {
        "title": "Data Quality Incident Report",
        "run_id": run_id,
        "summary": {
            "total_records": analysis["total_rows"],
            "missing_kpi_values": analysis["missing_kpi"],
            "status_distribution": analysis["status_counts"]
        },
        "detected_issues": issues[:10],
        "impact": (
            "Potential KPI distortion due to invalid "
            "status and region inconsistencies."
        ),
        "recommendation": [
            "Enforce schema validation at ingestion layer",
            "Standardize allowed status values",
            "Add automated pipeline quality checks"
        ]
    }

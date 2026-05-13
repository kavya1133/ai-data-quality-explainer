def validate_rows(rows):
    issues = []

    for i, row in enumerate(rows):
        if not isinstance(row.get("kpi_value"), (int, float)):
            issues.append(f"Row {i}: Invalid KPI type")

        if row.get("kpi_value") is not None and row["kpi_value"] < 0:
            issues.append(f"Row {i}: Negative KPI value")

        if row.get("region") not in ["ME", "EU", "APAC", "US"]:
            issues.append(f"Row {i}: Unknown region")

        if row.get("status") not in ["delivered", "failed", "pending"]:
            issues.append(f"Row {i}: Invalid status")

    return issues

def evaluate_policy(
    risk_level: str,
    consent: str,
    permission: str
):
    if risk_level == "low" and permission == "allow":
        return "ALLOW", "low_risk_allowed"

    if risk_level == "high" and consent == "denied":
        return "DENY", "risk_high_consent_denied"

    if risk_level == "medium" and consent == "unknown":
        return "REVIEW", "risk_medium_consent_unknown"

    return "REVIEW", "manual_review_required"
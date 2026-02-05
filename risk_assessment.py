from data_handler import normalize_text

EMERGENCY_KEYWORDS = {
    "chest pain",
    "trouble breathing",
    "shortness of breath",
    "severe bleeding",
    "uncontrolled bleeding",
    "fainting",
    "loss of consciousness",
    "stroke",
    "slurred speech",
    "face droop",
    "seizure",
}

HIGH_SEVERITY_KEYWORDS = {
    "severe",
    "intense",
    "worst",
    "sudden",
    "unbearable",
    "high fever",
    "persistent",
}

MEDIUM_SEVERITY_KEYWORDS = {
    "moderate",
    "lasting",
    "pain",
    "nausea",
    "vomiting",
    "dizziness",
    "fatigue",
}


def assess_risk(symptoms: str) -> dict:
    normalized = normalize_text(symptoms)

    is_emergency = any(keyword in normalized for keyword in EMERGENCY_KEYWORDS)
    if is_emergency:
        return {
            "severity": "high",
            "is_emergency": True,
            "reason": "Possible emergency symptoms detected.",
        }

    if any(keyword in normalized for keyword in HIGH_SEVERITY_KEYWORDS):
        severity = "high"
    elif any(keyword in normalized for keyword in MEDIUM_SEVERITY_KEYWORDS):
        severity = "medium"
    else:
        severity = "low"

    return {
        "severity": severity,
        "is_emergency": False,
        "reason": "Severity estimated based on symptom keywords.",
    }

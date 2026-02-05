import csv
from datetime import datetime
from pathlib import Path
import re

DATA_PATH = Path("data/symptom_department.csv")
HISTORY_PATH = Path("data/interaction_history.csv")


def normalize_text(text: str) -> str:
    cleaned = text.lower().strip()
    cleaned = re.sub(r"[^a-z0-9\s]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def load_symptom_dataset():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    return DATA_PATH


def log_interaction(entry: dict) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = HISTORY_PATH.exists()

    with HISTORY_PATH.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "symptoms",
                "severity",
                "is_emergency",
                "self_care_advice",
                "doctor_visit_needed",
                "department",
                "recommended_doctor",
                "recommended_tests",
            ],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "timestamp": datetime.utcnow().isoformat(),
                **entry,
            }
        )

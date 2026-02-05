from data_handler import normalize_text

SELF_CARE_RULES = [
    {
        "keywords": ["fever", "cold", "flu", "cough", "sore throat"],
        "advice": "Rest, hydrate well, and consider warm fluids like soup or tea.",
        "doctor_visit": "See a doctor if fever is high, lasts more than 2-3 days, or symptoms worsen.",
    },
    {
        "keywords": ["headache", "migraine"],
        "advice": "Rest in a dark, quiet room and drink water.",
        "doctor_visit": "See a doctor if the headache is sudden, severe, or with vision changes.",
    },
    {
        "keywords": ["stomach pain", "abdominal pain", "nausea", "vomiting", "diarrhea"],
        "advice": "Try bland foods, small sips of water, and avoid heavy or spicy meals.",
        "doctor_visit": "See a doctor if pain is severe, persistent, or there is blood in stool/vomit.",
    },
    {
        "keywords": ["rash", "itching", "allergy", "skin irritation"],
        "advice": "Keep the area clean and dry; avoid scratching.",
        "doctor_visit": "See a doctor if the rash spreads quickly, blisters, or comes with fever.",
    },
    {
        "keywords": ["back pain", "joint pain", "muscle pain", "sprain"],
        "advice": "Rest, gentle stretching, and apply cold/heat packs.",
        "doctor_visit": "See a doctor if pain limits movement or follows an injury.",
    },
]

DEFAULT_SELF_CARE = "Rest, hydrate, and avoid strenuous activity."
DEFAULT_DOCTOR_VISIT = "If symptoms persist or worsen, consult a healthcare professional."

DEPARTMENT_RECOMMENDATIONS = {
    "Cardiology": {
        "doctor": "Cardiologist",
        "tests": "ECG, blood pressure check, cardiac enzymes",
    },
    "Neurology": {
        "doctor": "Neurologist",
        "tests": "Neurological exam, MRI/CT scan",
    },
    "Dermatology": {
        "doctor": "Dermatologist",
        "tests": "Skin exam, allergy testing",
    },
    "Gastroenterology": {
        "doctor": "Gastroenterologist",
        "tests": "Abdominal exam, stool test, ultrasound",
    },
    "Orthopedics": {
        "doctor": "Orthopedic specialist",
        "tests": "X-ray, physical exam",
    },
    "ENT": {
        "doctor": "ENT specialist",
        "tests": "Throat/nasal exam, hearing test",
    },
    "Pulmonology": {
        "doctor": "Pulmonologist",
        "tests": "Chest X-ray, spirometry",
    },
    "General Medicine": {
        "doctor": "Primary care physician",
        "tests": "General physical exam, basic labs",
    },
}


def get_self_care_advice(symptoms: str) -> dict:
    normalized = normalize_text(symptoms)
    for rule in SELF_CARE_RULES:
        if any(keyword in normalized for keyword in rule["keywords"]):
            return {
                "advice": rule["advice"],
                "doctor_visit": rule["doctor_visit"],
                "doctor_visit_needed": True,
            }

    return {
        "advice": DEFAULT_SELF_CARE,
        "doctor_visit": DEFAULT_DOCTOR_VISIT,
        "doctor_visit_needed": False,
    }


def get_department_recommendation(department: str) -> dict:
    recommendation = DEPARTMENT_RECOMMENDATIONS.get(department, {})
    return {
        "doctor": recommendation.get("doctor", "Primary care physician"),
        "tests": recommendation.get("tests", "Basic physical exam"),
    }

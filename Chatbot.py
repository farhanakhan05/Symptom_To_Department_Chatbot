from advice import get_department_recommendation, get_self_care_advice
from data_handler import log_interaction
from ml_model import predict_department
from risk_assessment import assess_risk

DISCLAIMER = (
    "This tool provides informational guidance only and is not a medical diagnosis. "
    "If you are in danger, seek emergency care immediately."
)

print("Symptom-to-Department Health Assistant")
print("Type 'exit' to quit")
print(f"Disclaimer: {DISCLAIMER}")

while True:
    symptoms = input("Tell me how you're feeling: ")

    if symptoms.lower() == "exit":
        print("Goodbye")
        break

    risk = assess_risk(symptoms)
    if risk["is_emergency"]:
        print("\n\u26a0\ufe0f Emergency warning: Possible emergency symptoms detected.")
        print("Please call local emergency services or go to the nearest emergency department.")

    advice = get_self_care_advice(symptoms)
    department = predict_department(symptoms)
    recommendation = get_department_recommendation(department)

    print(f"\nSeverity: {risk['severity'].title()}")
    print("Self-care advice:", advice["advice"])
    print("Doctor visit guidance:", advice["doctor_visit"])
    print("Recommended Department:", department)
    print("Recommended Doctor Type:", recommendation["doctor"])
    print("Suggested Common Tests:", recommendation["tests"])
    print("Next steps: Monitor symptoms and follow the guidance above.")
    print("-" * 40)

    log_interaction(
        {
            "symptoms": symptoms,
            "severity": risk["severity"],
            "is_emergency": risk["is_emergency"],
            "self_care_advice": advice["advice"],
            "doctor_visit_needed": advice["doctor_visit_needed"],
            "department": department,
            "recommended_doctor": recommendation["doctor"],
            "recommended_tests": recommendation["tests"],
        }
    )


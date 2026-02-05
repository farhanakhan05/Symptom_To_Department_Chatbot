# 🏥 Symptom-to-Department Health Assistant (Machine Learning)

## 📖 Project Overview
The **Symptom-to-Department Health Assistant** is a beginner-friendly **HealthTech Machine Learning project** that mimics the steps a person takes when they feel sick. It takes free-text symptoms, normalizes them, checks for emergency warnings, provides self-care guidance, and predicts the most relevant medical department using **NLP** and **Machine Learning classification**.

⚠️ *This project is for informational purposes only and does not provide medical diagnosis or treatment. If you believe you are experiencing an emergency, seek professional care immediately.*

---

## 🎯 Objectives
- Accept symptom descriptions as text input from users   
- Preprocess and normalize free-text symptoms  
- Assess severity (low, medium, high) and flag emergencies  
- Provide self-care guidance and doctor-visit recommendations  
- Predict the most suitable hospital department  
- Recommend doctor type and common diagnostic tests  
- Store each interaction in a CSV history file  
- Demonstrate an end-to-end ML workflow for beginners  

---

## 🧠 How It Works 
1. User enters symptom descriptions in free text.  
2. Text is normalized (lowercasing, punctuation cleanup).  
3. Rule-based checks assess severity and detect emergencies.  
4. Self-care advice and doctor-visit guidance are provided.  
5. The ML model (TF-IDF + Naive Bayes) predicts the best department.  
6. The assistant recommends doctor type and common tests.  
7. Interaction details are saved to a CSV history file.  

---

## 🗂️ Project Structure
- `Chatbot.py`: User interaction loop and orchestration  
- `data_handler.py`: Normalization and CSV history logging  
- `risk_assessment.py`: Severity scoring and emergency detection  
- `advice.py`: Self-care guidance and doctor/test recommendations  
- `ml_model.py`: TF-IDF + Naive Bayes model training and prediction  

---

## ✅ Features
- Free-text symptom input  
- Emergency keyword detection with immediate warnings  
- Severity assessment (low/medium/high)  
- Self-care and doctor-visit guidance  
- Department prediction with doctor/test suggestions  
- CSV logging for interaction history  

---

## 🚀 Getting Started
### 1) Install dependencies
```bash
pip install -r requirement.txt
```

### 2) Run the assistant
```bash
python Chatbot.py
```

### 3) Sample interaction
```
Tell me how you're feeling: chest tightness and shortness of breath

⚠️ Emergency warning: Possible emergency symptoms detected.
Please call local emergency services or go to the nearest emergency department.

Severity: High
Self-care advice: Rest, hydrate, and avoid strenuous activity.
Doctor visit guidance: If symptoms persist or worsen, consult a healthcare professional.
Recommended Department: Cardiology
Recommended Doctor Type: Cardiologist
Suggested Common Tests: ECG, blood pressure check, cardiac enzymes
```

---

## 🧾 Output & History
Each interaction is saved to `data/interaction_history.csv` with:
- timestamp  
- symptoms  
- severity  
- emergency flag  
- self-care advice  
- doctor-visit recommendation  
- predicted department  
- recommended doctor type  
- suggested common tests  

---

## ⚠️ Medical Disclaimer
This tool provides **informational guidance only** and is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

---


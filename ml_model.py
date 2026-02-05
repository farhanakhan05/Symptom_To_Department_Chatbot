import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from data_handler import load_symptom_dataset, normalize_text


def _train_model():
    dataset_path = load_symptom_dataset()
    data = pd.read_csv(dataset_path)
    data["Symptoms_text"] = data["Symptoms_text"].fillna("").map(normalize_text)

    X = data["Symptoms_text"]
    y = data["Department"]

    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vectorized, y)

    return vectorizer, model


_VECTORIZE, _MODEL = _train_model()


def predict_department(symptoms: str) -> str:
    normalized = normalize_text(symptoms)
    symptoms_tfidf = _VECTORIZE.transform([normalized])
    department = _MODEL.predict(symptoms_tfidf)
    return department[0]

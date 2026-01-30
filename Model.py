import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#load dataset
data = pd.read_csv("data/symptom_department.csv")

X = data['Symptoms_text']
y = data['Department']

#vectorize symptoms
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

#train model
model = MultinomialNB()
model.fit(X, y)

#predict department
def predict_department(Symptoms):
  Symptoms_tfidf = vectorizer.transform([Symptoms])
  department = model.predict(Symptoms_tfidf)
  return department[0]

print(predict_department("chest pain"))

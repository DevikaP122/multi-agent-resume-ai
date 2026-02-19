import pandas as pd
import joblib
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Resume.csv")

def clean_text(text):
    text = re.sub(r'\W', ' ', str(text))
    text = text.lower()
    return text

data['cleaned'] = data['Resume_str'].apply(clean_text)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('model', LogisticRegression(max_iter=1000))
])

pipeline.fit(data['cleaned'], data['Category'])

joblib.dump(pipeline, "model.pkl")

print("Model trained successfully")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example dataset
news_data = [
    ("The stock market saw a huge crash today", "Finance"),
    ("The football match between Brazil and Argentina ended in a draw", "Sports"),
    ("The president announced new policies for education", "Politics"),
]

texts, labels = zip(*news_data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def classify_news(news_text):
    X_input = vectorizer.transform([news_text])
    return model.predict(X_input)[0]

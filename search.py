import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Store news articles and their vectors
news_articles = []
vectorizer = TfidfVectorizer()
vectors = None  # Initialize empty vector storage

def add_news_to_index(article):
    """Adds a new article and updates the TF-IDF vectorizer."""
    global news_articles, vectors
    news_articles.append(article)
    vectors = vectorizer.fit_transform(news_articles)  # Fit only when a new article is added

def search_news(query):
    """Finds the most relevant articles using cosine similarity."""
    global vectors
    if vectors is None or len(news_articles) == 0:
     return []  # Return empty if no articles are stored
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(vectors, query_vector).flatten()   
    # Get top 5 highest similarity indices
    ranked_indices = np.argsort(similarities)[::-1][:5]   
    return [news_articles[i] for i in ranked_indices]

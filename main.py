from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from ner import extract_names
from scraper import scrape_news

from classifier import classify_news
from search import search_news, add_news_to_index
# Load SpaCy model
nlp = spacy.load("en_core_web_sm")
app = FastAPI()
class NewsRequest(BaseModel):
    article: str
@app.get("/")
def home():
    return {"message": "Welcome to the AI-powered News API!"}

@app.post("/extract")
def extract_news(request: NewsRequest):
    categorized_names = extract_names(request.article)
    return {"categorized_names": categorized_names}
@app.post("/scrape")
def scrape():
    articles = scrape_news()
    for article in articles:
        add_news_to_index(article)  # Index scraped articles in FAISS
    return {"articles": articles}

@app.post("/classify")
def classify(request: NewsRequest):
    category = classify_news(request.article)
    return {"category": category}

@app.post("/search")
def search(request: NewsRequest):
    results = search_news(request.article)
    return {"similar_news": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

📰 News Article Scraper & Named Entity Recognition (NER) Classification
Project Overview
This project aims to:

Scrape news articles from various online sources.

Extract named entities, focusing on person names, from the news content.

Classify articles into multiple categories such as Finance, Politics, Sports, etc.

(Future) Implement vector-based similarity search to find related news articles using FAISS.

🚀 Use Cases
News Aggregation: Automatically gather and classify news articles for media outlets.

Sentiment & Trend Analysis: Identify key persons and categorize trending topics in news.

Automated Reporting: Fetch, classify, and analyze news articles with entity extraction insights.

Search & Retrieval (Future): Quickly find similar news articles via FAISS vector search.

🛠 Step-by-Step Approach (Planned/Future Enhancements)
Step 1: Web Scraping for News Collection
Use requests and BeautifulSoup to scrape headlines/full articles from sites like BBC, CNN, Reuters.

Clean and preprocess text (remove HTML, stopwords, special characters).

Store scraped articles in a database or vector index for processing.

Step 2: Named Entity Recognition (NER)
Use SpaCy’s pre-trained model (en_core_web_sm) to extract PERSON entities.

Filter out irrelevant entities like locations, dates, or generic terms.

Associate extracted entities with their source articles.

Step 3: News Classification
Use rule-based or ML classifiers (e.g., Sentence Transformers) to categorize articles into topics like Finance, Politics, Sports, Technology, Entertainment.

Fine-tune models on labeled datasets such as AG News or Reuters for higher accuracy.

Step 4: FAISS-Based Similarity Search (Future)
Convert articles into vector embeddings using LangChain with OpenAI/BERT embeddings.

Store embeddings in FAISS for efficient nearest neighbor search.

Enable querying of similar news articles by vector similarity.

Step 5: Streamlit UI (Future)
Build an interactive dashboard to input news text and display:

Extracted person names

Classified categories

Similar news article recommendations

Step 6: Deployment & Scaling (Future)
Deploy backend API on AWS/GCP using FastAPI and Docker.

Automate news scraping with schedulers like Celery or Apache Airflow.

Use PostgreSQL or SQLite for persistent storage of news data and entities.

📩 Contact
For questions or collaboration, please reach out to:
contact.vipulbhatt@gmail.com

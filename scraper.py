import requests
from bs4 import BeautifulSoup
def scrape_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for item in soup.find_all("div", class_="gs-c-promo-body"):
        headline = item.find("h3")
        if headline:
            articles.append(headline.text.strip())
    return articles

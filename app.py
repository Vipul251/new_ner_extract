import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  

st.title("📢 AI-Powered News Extractor & Search")

# Scrape News
if st.button("Scrape Latest News 📰"):
    response = requests.post(f"{BASE_URL}/scrape")
    if response.status_code == 200:
        articles = response.json()["articles"]
        st.success(f"Scraped {len(articles)} news articles!")
        for article in articles:
            st.write(f"- {article}")
    else:
        st.error("Failed to scrape news!")

# Extract Names & Category
st.subheader("🔍 Extract Information from News")
news_text = st.text_area("Enter a news article:")
if st.button("Extract"):
    if news_text:
        response = requests.post(f"{BASE_URL}/extract", json={"article": news_text})
        if response.status_code == 200:
            data = response.json()
            st.success(f"News Category: {data['category']}")
            st.write("📝 **Names Extracted:**")
            st.write(", ".join(data['names']) if data['names'] else "No names found.")
        else:
            st.error("Failed to extract information.")
    else:
        st.warning("Please enter a news article.")

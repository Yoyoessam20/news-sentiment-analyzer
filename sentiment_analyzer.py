"""
News Sentiment Analyzer
Fetches the latest headlines from a live RSS feed (BBC News) and scores
each one's sentiment (Positive / Negative / Neutral) using VADER, a
lexicon-based NLP model that runs fully offline with no API required.
"""

import feedparser
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"
MAX_ARTICLES = 30

analyzer = SentimentIntensityAnalyzer()


def fetch_articles() -> list[dict]:
    """Fetch the latest headlines and links from the RSS feed."""
    feed = feedparser.parse(RSS_URL)
    return [
        {"title": entry.title, "link": entry.link}
        for entry in feed.entries[:MAX_ARTICLES]
    ]


def classify_sentiment(score: float) -> str:
    """Map VADER's compound score (-1 to 1) to a sentiment label."""
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"


def analyze_articles(articles: list[dict]) -> pd.DataFrame:
    results = []
    for article in articles:
        scores = analyzer.polarity_scores(article["title"])
        results.append({
            "title": article["title"],
            "link": article["link"],
            "sentiment_score": scores["compound"],
            "sentiment": classify_sentiment(scores["compound"]),
        })
    return pd.DataFrame(results)


if __name__ == "__main__":
    print("Fetching headlines from BBC News RSS ...")
    articles = fetch_articles()
    print(f"Fetched {len(articles)} articles. Analyzing sentiment ...\n")

    df = analyze_articles(articles)
    df.to_csv("data/news_sentiment.csv", index=False, encoding="utf-8-sig")

    print(f"Analyzed {len(df)} articles successfully.")
    print("Saved to data/news_sentiment.csv\n")
    print("Sentiment distribution:")
    print(df["sentiment"].value_counts().to_string())

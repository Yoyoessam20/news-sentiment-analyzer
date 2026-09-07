"""
Sentiment Analysis Report
Reads the output of sentiment_analyzer.py and reports summary statistics
plus a bar chart of the sentiment distribution.
"""

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = "data/news_sentiment.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILE)


def print_summary(df: pd.DataFrame) -> None:
    print("=" * 50)
    print(f"Total articles: {len(df)}")
    print(f"Average sentiment score: {df['sentiment_score'].mean():.3f}")
    print("(-1 = very negative, +1 = very positive)")
    print("=" * 50)

    print("\nTop 3 most positive headlines:")
    print(df.nlargest(3, "sentiment_score")[["title", "sentiment_score"]].to_string(index=False))

    print("\nTop 3 most negative headlines:")
    print(df.nsmallest(3, "sentiment_score")[["title", "sentiment_score"]].to_string(index=False))


def plot_sentiment_distribution(df: pd.DataFrame, output_path="data/sentiment_distribution.png") -> None:
    counts = df["sentiment"].value_counts()
    colors = {"Positive": "#4CAF50", "Negative": "#F44336", "Neutral": "#9E9E9E"}
    bar_colors = [colors.get(cat, "#999999") for cat in counts.index]

    plt.figure(figsize=(7, 5))
    plt.bar(counts.index, counts.values, color=bar_colors)
    plt.title("News Headline Sentiment Distribution")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nChart saved to {output_path}")


if __name__ == "__main__":
    df = load_data()
    print_summary(df)
    plot_sentiment_distribution(df)

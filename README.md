# News Sentiment Analyzer

A Python NLP tool that fetches live news headlines from a real RSS feed and scores their sentiment — no API key or paid service required.

## What it does

- Fetches the latest ~30 headlines from **BBC News's official RSS feed**
- Scores each headline's sentiment using **VADER**, a lexicon-based NLP model
- Classifies each into **Positive / Negative / Neutral**
- Reports summary statistics (most positive/negative headlines, average score)
- Generates a bar chart of the sentiment distribution

## Tech stack

`Python` · `feedparser` · `VADER Sentiment` · `Pandas` · `Matplotlib`

## Usage

```bash
pip install feedparser vaderSentiment pandas matplotlib
python sentiment_analyzer.py   # fetches headlines and scores sentiment
python sentiment_report.py     # generates the summary and chart
```

## How VADER works

VADER (Valence Aware Dictionary and sEntiment Reasoner) is a **lexicon-based** sentiment model: each word carries a pre-scored sentiment weight (derived from human ratings), and a sentence's overall score is computed from its words plus rules for negation, punctuation, and capitalization.

This makes it fast, free, and fully offline — but it has a known limitation: it can misjudge context. For example, a headline about a "cancer treatment breakthrough" can score negative because of the word "cancer" alone, even though the overall news is positive. This is a key difference from context-aware LLMs (like Claude), which read full sentence meaning rather than scoring individual words.

## Why RSS instead of HTML scraping

RSS feeds are published by the source specifically for third-party consumption — no scraping restrictions apply, unlike parsing a site's raw HTML.

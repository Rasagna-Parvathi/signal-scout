import feedparser
import pandas as pd
from datetime import datetime
import time

SOURCES = [
    {"name": "TechCrunch", "url": "https://techcrunch.com/feed/"},
    {"name": "TechCrunch Startups", "url": "https://techcrunch.com/category/startups/feed/"},
    {"name": "VentureBeat AI", "url": "https://venturebeat.com/category/ai/feed/"},
    {"name": "VentureBeat Business", "url": "https://venturebeat.com/category/business/feed/"},
    {"name": "Wired AI", "url": "https://www.wired.com/feed/category/ai/latest/rss"},
    {"name": "The Verge Tech", "url": "https://www.theverge.com/rss/index.xml"},
    {"name": "Crunchbase News", "url": "https://news.crunchbase.com/feed/"},
    {"name": "Reuters Technology", "url": "https://feeds.reuters.com/reuters/technologyNews"},
    {"name": "Yahoo Tech", "url": "https://news.yahoo.com/tech/rss"},
    {"name": "MIT Tech Review", "url": "https://www.technologyreview.com/feed/"},
    {"name": "ZDNet", "url": "https://www.zdnet.com/news/rss.xml"},
]

def classify_signal(title):
    title_lower = title.lower()

    if "raise" in title_lower:
        return "funding", 0.9
    elif "launch" in title_lower:
        return "product_update", 0.8
    elif "partner" in title_lower:
        return "partnership", 0.75
    elif "acquire" in title_lower:
        return "acquisition", 0.85
    elif "ai" in title_lower:
        return "ai_activity", 0.6
    else:
        return "general_tech", 0.5

def fetch_signals(source):
    feed = feedparser.parse(source["url"])
    signals = []
    for entry in feed.entries[:100]:
        category, confidence = classify_signal(entry.title)

        signals.append({
            "entity_name": entry.title,
            "entity_url": entry.link,
            "signal_type": "news_article",
            "signal_text": entry.title,
            "signal_date": entry.get("published", ""),
            "source_name": source["name"],
            "source_url": source["url"],
            "category_tag": category,
            "confidence": confidence,
            "scraped_at": datetime.now()
        })

    return signals

def main():
    all_signals = []
    seen_titles = set()

    for source in SOURCES:
        print(f"Fetching from {source['name']}...")
        signals = fetch_signals(source)

        for s in signals:
            if s["entity_name"] not in seen_titles:
                seen_titles.add(s["entity_name"])
                all_signals.append(s)

        time.sleep(1)

    print("\nTotal signals collected:", len(all_signals))

    df = pd.DataFrame(all_signals)
    df.to_csv("output.csv", index=False)
    print("Saved to output.csv")

if __name__ == "__main__":
    main()
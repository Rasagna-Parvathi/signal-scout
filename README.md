# Signal Scout – Track A Submission

## Track Chosen
Track A – Technical (Builder)

## Time Spent
Approximately 3 hours

## Overview
This project builds a lightweight "Signal Scout" that collects VC-relevant public web signals from multiple RSS sources and displays them in a clean interactive dashboard.

## Sources Used
- TechCrunch
- VentureBeat
- Wired AI
- The Verge
- Crunchbase News
- Reuters Technology
- Yahoo Tech
- MIT Technology Review
- ZDNet

## Data Collected
The system collects 100+ signals.

Each signal includes:
- entity_name
- entity_url
- signal_type
- signal_text
- signal_date
- source_name
- source_url
- category_tag
- confidence
- scraped_at

## How to Run

1. Activate virtual environment
2. Install dependencies:
   pip install -r requirements.txt

3. Run scraper:
   python scraper.py

4. Run dashboard:
   streamlit run viewer.py

## If I Had 1 More Day
- Add ranking score based on recency and confidence
- Store historical data in SQLite
- Improve entity extraction (separate company name from article title)
- Deploy the dashboard online
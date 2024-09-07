import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd 

ID: int = 3

# Define a list of clickbait words/phrases
CLICKBAIT_PHRASES: list[str] = pd.read_csv("../nice-words.csv")['2g1c'].tolist()

# Function to detect and flag clickbait words in a text
def detect_trolling(text: str) -> list[str]:
    flagged_info: list[str] = []

    for phrase in CLICKBAIT_PHRASES:
        if re.search(r'\b' + re.escape(phrase) + r'\b', text, re.IGNORECASE):
            # Append the flagged sentence and the triggering word/phrase
            flagged_info.append(phrase)

    return flagged_info

# Function to analyze sentiment using VADER
def trolling_service(text: str) -> list | None:
    flagged_info: list[str] = detect_trolling(text)

    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)

    if sentiment['neg'] > 0.5:
        return [(ID, word, None) for word in flagged_info]

    return None

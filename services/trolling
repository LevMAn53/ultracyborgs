import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd 

# Define a list of clickbait words/phrases
clickbait_phrases = pd.read_csv("/Users/levmanulak/Desktop/nice-words.csv")['2g1c'].tolist()

# Function to detect and flag clickbait words in a text
def detect_clickbait(text, clickbait_phrases):
    flagged_info = []
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    for sentence in sentences:
        # Check if any clickbait phrase is present in the sentence
        for phrase in clickbait_phrases:
            if re.search(r'\b' + re.escape(phrase) + r'\b', sentence, re.IGNORECASE):
                # Append the flagged sentence and the triggering word/phrase
                flagged_info.append((sentence, phrase))
                break  # Only append once per sentence
    
    return flagged_info

# Function to analyze sentiment using VADER
def analyze_sentiment(flagged_info):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_results = {}
    
    for sentence, phrase in flagged_info:
        sentiment = analyzer.polarity_scores(sentence)
        if sentiment['neg'] >0.4:
            # Flag sentences with negative sentiment > 0.5
            sentiment_results[sentence] = f"Flagged due to '{phrase}': trolling detected"
    
    return sentiment_results

# Example text (input a news article or any content)
news_article = input("Enter the news article: ")

# Detect and flag sentences containing clickbait words
flagged_info = detect_clickbait(news_article, clickbait_phrases)


if flagged_info:
    print("Flagged Sentences containing trolling:")
    sentiment_results = analyze_sentiment(flagged_info)
    
    for sentence, result in sentiment_results.items():
        print(f"\n- {sentence}")
        print(f"  {result}")
else:
    print("it's trolling-free!")

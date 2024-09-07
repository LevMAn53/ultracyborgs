import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Define a list of clickbait words/phrases
clickbait_phrases = ["Amazing", "Unbelievable", "Shocking", "Incredible", "Mind-blowing", "Jaw-dropping", 
    "Breathtaking", "Epic", "Insane", "Outrageous", "Unimaginable", "Miraculous", "Astonishing", 
    "Unstoppable", "Phenomenal", "Life-changing", "Spectacular", "Ultimate", "Revolutionary", 
    "Crazy", "Surprising", "Unthinkable", "Unprecedented", "Unreal", "Stunning", "Horrifying", 
    "Heartbreaking", "Heartwarming", "Tear-jerking", "Fascinating", "Unforgettable", "Inspiring", 
    "Heroic", "Unparalleled", "Groundbreaking", "Mind-boggling", "World-changing", "Exclusive", 
    "Extraordinary", "Unstoppable", "Explosive", "Sensational", "Greatest", "Unbeatable", 
    "Legendary", "Outrageous", "Must-see", "Unrivaled", "Furious", "Devastating", "Incomparable", 
    "Flawless", "Unstoppable", "Skyrocketing", "Devastating", "Scary", "Fearless", "Infallible", 
    "Game-changer", "Irresistible", "Life-saving", "Breakthrough", "Jaw-dropping", "Devastating", 
    "Shocking", "Frightening", "Mind-bending", "Explosive", "Unprecedented", "Top", "Best", 
    "Biggest", "Fastest", "Hottest", "Rarest", "Ultimate", "Secret", "Hidden", "Guaranteed", 
    "Proven", "Limited", "Fast", "Now", "Instantly", "Hurry", "New", "Crazy", "Wild", "Powerful", 
    "Urgent", "Free", "Exclusive", "Never", "Now", "Final", "Last", "Urgent", "Instant", "Bonus", 
    "Free", "Best-selling", "Record-breaking", "!!!"]

# Function to detect and flag clickbait words in a text
def detect_clickbait(text, clickbait_phrases):
    flagged_sentences = []
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    for sentence in sentences:
        # Check if any clickbait phrase is present in the sentence
        for phrase in clickbait_phrases:
            if re.search(r'\b' + re.escape(phrase) + r'\b', sentence, re.IGNORECASE):
                flagged_sentences.append(sentence)
                break
    
    return flagged_sentences

# Function to analyze sentiment using VADER
def analyze_sentiment(sentences):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_results = {}
    
    for sentence in sentences:
        sentiment = analyzer.polarity_scores(sentence)
        if sentiment['neg'] > 0.5:
            # Flag sentences with negative sentiment > 0.5
            sentiment_results[sentence] = "Flagged: Negative Sentiment"
        elif sentiment['pos'] > 0.5:
            # Ignore sentences with positive sentiment > 0.5
            sentiment_results[sentence] = "Positive Sentiment: Ignored"
        else:
            # Neutral sentiment, don't flag
            sentiment_results[sentence] = "Neutral Sentiment: No action"
    
    return sentiment_results

# Example text (input a news article or any content)
news_article = input("Enter the news article: ")

# Detect and flag sentences containing clickbait words
flagged_sentences = detect_clickbait(news_article, clickbait_phrases)

# If any clickbait sentences are flagged, analyze their sentiment
if flagged_sentences:
    print("Flagged Sentences with Clickbait Words and Sentiment Analysis:")
    sentiment_results = analyze_sentiment(flagged_sentences)
    
    for sentence, result in sentiment_results.items():
        print(f"\n- {sentence}")
        print(f"  {result}")
else:
    print("No clickbait detected.")

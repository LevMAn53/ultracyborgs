import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
import numpy as np

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to extract features from a headline
def extract_features(headline):
    # Tokenize the headline
    tokens = word_tokenize(headline)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    # Calculate sentiment score
    sentiment_score = sia.polarity_scores(headline)['compound']
    
    # Perform part-of-speech tagging
    pos_tags = pos_tag(lemmatized_tokens)
    
    # Perform named entity recognition
    named_entities = ne_chunk(pos_tags)
    
    # Extract features related to word choice, sentence structure, and use of adjectives/adverbs
    feature_set = {
        'word_count': len(tokens),
        'filtered_word_count': len(filtered_tokens),
        'lemmatized_word_count': len(lemmatized_tokens),
        'sentiment_score': sentiment_score,
        'pos_tags': pos_tags,
        'named_entities': named_entities
    }
    
    return feature_set

# Example usage
headline = "Breaking: New study reveals shocking truth about vaccines"
features = extract_features(headline)
print(features)
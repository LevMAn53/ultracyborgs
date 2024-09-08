import re
import pandas as pd 

ID: int = 3

# Define a list of clickbait words/phrases
CLICKBAIT_PHRASES: list[str] = pd.read_csv("./nice-words.csv")['2g1c'].tolist()

# Function to detect and flag clickbait words in a text
def trolling_service(text: str) -> list:
    flagged_info: list[str] = []

    for phrase in CLICKBAIT_PHRASES:
        if re.search(r'\b' + re.escape(phrase) + r'\b', text, re.IGNORECASE):
            # Append the flagged sentence and the triggering word/phrase
            flagged_info.append(phrase)

    return [(ID, word, None) for word in flagged_info]

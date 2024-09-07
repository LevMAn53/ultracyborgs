import re

ID: int = 1

# Function to detect the phrase "What about...?" and return a warning
def whataboutism_service(tweet: str) -> list | None:
    sentences = re.split(r'(?<=[.!?]) +', tweet)

    # Define the pattern for "What about...?"
    pattern1 = r'\bwhat about\b.*\?'
    pattern2 = r'\bas for\b.*\ '
    
    whataboutism_sentances = []

    for sentance in sentences:
        match1 = re.search(pattern1, sentance, re.IGNORECASE)
        match2 = re.search(pattern2, sentance, re.IGNORECASE)

        if match1 or match2:
            whataboutism_sentances.append((ID, sentance, None))

    return whataboutism_sentances if len(whataboutism_sentances) > 0 else None

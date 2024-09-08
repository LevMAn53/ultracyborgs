import re

ID: int = 1

WAT_PATTERNS: dict[str, str] = {
    "what about...?" : r'\bwhat about\b.*\?',
    "as for..." : r'\bas for\b.*\ ',
    "how about...?" : r'\bhow about\b.*\?',
    "why don’t (somebody) mention...?" : r'\bwhy (don’t|didn’t|won’t) ((\w+)|(\w+)\s(\w+)) mention\b.*\?',
    "but (somebody) never mention..." : r'\bbut ((\w+)|(\w+)\s(\w+)) never mention\b.* ',
    "what do (somebody) have to say about...?" : r'\bwhat (do|does) ((\w+)|(\w+)\s(\w+)) (have|has) to say about\b.*\?',
    "why are (somebody) not talking about...?" : r'\bwhy (are|is) ((\w+)|(\w+)\s(\w+)) not talking about\b.*\?',
    "how can (somebody) ignore...?" : r'\bhow can ((\w+)|(\w+)\s(\w+)) ignore\b.*\?',

}

# Function to detect the phrase "What about...?" and return a warning
def whataboutism_service(tweet: str) -> list | None:
    sentences = re.split(r'(?<=[.!?]) +', tweet)

    whataboutism_sentances = []


    for sentance in sentences:
        for name, pattern in WAT_PATTERNS.items():
            if re.search(pattern, sentance, re.IGNORECASE):
                whataboutism_sentances.append((ID, sentance, None))

    return whataboutism_sentances if len(whataboutism_sentances) > 0 else None
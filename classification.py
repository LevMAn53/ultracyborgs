def check_whataboutism(text):
    if "what about" in text.lower():
        print("AI: This content may contain whataboutism, which can divert attention from the original topic.")
    # else:
        # print("AI: No whataboutism detected.")

# Example usage
# text = "What about the economy?"
# check_whataboutism(text)

def analyze_emotional_language(text):
    emotional_to_neutral = {
        "horrific": "serious",
        "disgusting": "disagreable",
        "heartbreaking": "unfortunate coincidence",
        "disaster": "unfortunate event",
        "failure": "unsuccessful",
        "deceiving": "misleading",
    }

    # emotionally_charged_words = ["angry", "outraged", "horrified", "heartbreaking", "devastating"]
    bad = False
    for word in emotional_to_neutral:
        if word in text.lower():
            bad = True
            text.replace(word, emotional_to_neutral[word])
            # raise ValueError("Emotionally charged language detected.")
    if bad:
        print("AI: Reading original message could evoke strong emotions.")
    
    # print(f"AI: Here is a neutral version of the text: {text}")

    return text
    # else:
        # print("AI: No emotionally charged language detected.")

# Example usage
# text = "This is an outrage! How could they do this?"
# analyze_emotional_language(text)
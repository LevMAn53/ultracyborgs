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

    }

    emotionally_charged_words = ["angry", "outraged", "horrified", "heartbreaking", "devastating"]
    for word in emotionally_charged_words:
        if word in text.lower():
            print("AI: Reading this could evoke strong emotions.")
            for word in emotionally_charged_words:
                text.replace(word, emotional_to_neutral[word])
            print(f"AI: Here is a neutral version of the text: {text}")
            # raise ValueError("Emotionally charged language detected.")
            return text
    # else:
        # print("AI: No emotionally charged language detected.")

# Example usage
# text = "This is an outrage! How could they do this?"
# analyze_emotional_language(text)
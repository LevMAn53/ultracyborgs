import re


wat_patterns = {
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
def detect_manipulative_content(text):
    # Define the pattern for "What about...?"
    
    # pattern1 = r'\bwhat about\b.*\?'
    # pattern2 = r'\bas for\b.*\ '
    
    # Search for the pattern in the text
    # match1 = re.search(pattern1, text, re.IGNORECASE)
    # match2 = re.search(pattern2, text, re.IGNORECASE)

    # match = match1 or match2

    matches = []

    for name, pattern in wat_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            matches.append(name)
    
    if len(matches) > 0:
        for i in range(len(matches)):
            matches[i] = "'" + matches[i] + "'"

        print("Warning: This content may be manipulative! Detected phrases: " + ",".join(matches))
        return 1
    else:
        print("No manipulative content detected.")
        return 0 

# Example input text
content = input("Enter the content: ")


# >>> Example text to test few cases
# 
# content = """
# Why are we criticizing the government for its handling of the healthcare system?
# What about the issues with the education system? 
# Shouldn't we address those problems first before focusing on healthcare?
# What does Elon Mask have to say about global warming?
# How can he ignore pure childrens in Africa?
# """

# Detect manipulative phrase and return warning
detect_manipulative_content(content)

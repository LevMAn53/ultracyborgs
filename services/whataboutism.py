import re

# Function to detect the phrase "What about...?" and return a warning
def detect_manipulative_content(text):
    # Define the pattern for "What about...?"
    pattern1 = r'\bwhat about\b.*\?'
    pattern2 = r'\bas for\b.*\ '
    
    # Search for the pattern in the text
    match1 = re.search(pattern1, text, re.IGNORECASE)
    match2 = re.search(pattern2, text, re.IGNORECASE)

    match = match1 or match2
    
    if match:
        print("Warning: This content may be manipulative! Detected the phrase 'What about...?'")
        return 1
    else:
        print("No manipulative content detected.")
        return 0 

# Example input text
content = input("Enter the content: ")

# Detect manipulative phrase and return warning
detect_manipulative_content(content)

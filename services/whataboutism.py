import re

# Function to detect the phrase "What about...?" and return a warning
def detect_manipulative_content(text):
    # Define the pattern for "What about...?"
    pattern = r'\bwhat about\b.*\?'

    # Search for the pattern in the text
    match = re.search(pattern, text, re.IGNORECASE)
    
    if match:
        # Simulate a pop-up by printing a message to the console
        print("Warning: This content may be manipulative! Detected the phrase 'What about...?'")
    else:
        print("No manipulative content detected.")

# Example input text
content = input("Enter the content: ")

# Detect manipulative phrase and return warning
detect_manipulative_content(content)

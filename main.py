import classification
import data_ingestion
import nlp_analysis
from reporting_interface import present

print("="*100)
present("\nWelcome to the Information Neutralizer, a tool designed to help you discern fact from fiction in the information you encounter. Our software analyzes messages and rephrases them to present a more objective and balanced view, free from emotional bias and misleading claims. Whether you're navigating news articles, social media posts, or any other form of communication, the Information Neutralizer empowers you to make informed decisions based on clear, unbiased information.\n\n\n")


def run_protection_use_case(i, headline):
    size = len(headline)
    blured = "*" * size
    present(f'Incoming message: "{blured}"')
    classification.check_whataboutism(headline)
    headline = classification.analyze_emotional_language(headline)
    present("Neutralized message: ", nlp_analysis.neutralize_message(i, headline))
    response = input("Do you want to see the original? (yes/no): ")
    if response.lower() == "yes" or response.lower() == "y":
        print(f'Original message: "{headline}"')
    present("\n\n")



i = 0
for headline in data_ingestion.ingress:
    run_protection_use_case(i, headline)
    i += 1


def ingress_generator():
    run_protection_use_case(100, input("Provide message:")
)


"""
# enum: 

# emtional

"""

# Dozens of biases. Human have about 50 of them. Propagandist use those to play on the psychology. Consequently false emotional content is spreaded much quickly because humans are trapped.

# <celebrity name> ate my hamster




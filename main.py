import classification
import data_ingestion
import nlp_analysis

print("="*100)
print("Welcome to the Information Neutralizer, a tool designed to help you discern fact from fiction in the information you encounter. Our software analyzes messages and rephrases them to present a more objective and balanced view, free from emotional bias and misleading claims. Whether you're navigating news articles, social media posts, or any other form of communication, the Information Neutralizer empowers you to make informed decisions based on clear, unbiased information.")
i = 0
for headline in data_ingestion.ingress:
    size = len(headline)
    blured = "*" * size
    print(f'Incoming message: "{blured}"')

    
    classification.check_whataboutism(headline)
    headline = classification.analyze_emotional_language(headline)
    print("Neutralized message: ", nlp_analysis.neutralize_message(i, headline))
    response = input("Do you want to see the original? (yes/no): ")
    if response.lower() == "yes":
        print(f'Original message: "{headline}"')

    i += 1
    print("\n\n")

print("""
Provide message: The new policy is a disaster and will ruin the economy. 
Result: "The new policy has been met with concerns regarding its potential impact on the economy."


Provide message: The government's response to the crisis is a complete failure and shows their incompetence. 
Result: "The government's response to the crisis has been criticized by some for its effectiveness."


Provide message: This product is a scam and the company is deceiving its customers. 
Result: "Concerns have been raised about the product's promises and the company's transparency with its customers."


Provide message: The artist's new album is a masterpiece and the best work of the century. 
Result: "The artist's new album has been well-received by many and is considered a significant work by some critics."


Provide message: The new study claiming health benefits is bogus and just a marketing ploy. 
Result: "The new study's claims of health benefits are being scrutinized for their scientific validity and potential marketing motivations."


""")



"""
# enum: 

# emtional

"""
input("Provide message:")

# Dozens of biases. Human have about 50 of them. Propagandist use those to play on the psychology. Consequently false emotional content is spreaded much quickly because humans are trapped.

# <celebrity name> ate my hamster




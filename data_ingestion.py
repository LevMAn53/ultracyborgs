# Stream of messages to be used as input for the sentiment analysis model
messages = [
    "The new policy is a disaster and will ruin the economy. ",
    "The government's response to the crisis is a complete failure and shows their incompetence. ",
    "This product is a scam and the company is deceiving its customers. ",
    "The artist's new album is a masterpiece and the best work of the century. ",
    "The new study claiming health benefits is bogus and just a marketing ploy. ",
    "US, UK, Europe and Canada to block Swift access for some Russian banks",
    "- What is the salary of a Soviet engineer?\n- But what about US [the racist name for African Americans] get lynched!"
]

def ingress_generator():
    yield from messages

ingress = ingress_generator()


# todo Whataboutism
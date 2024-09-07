messages = ["The new policy is a disaster and will ruin the economy. ",
"The government's response to the crisis is a complete failure and shows their incompetence. ",
"This product is a scam and the company is deceiving its customers. ",
"The artist's new album is a masterpiece and the best work of the century. ",
"The new study claiming health benefits is bogus and just a marketing ploy. ",
]

def ingress_generator():
    yield from messages

ingress = ingress_generator()
next(ingress)
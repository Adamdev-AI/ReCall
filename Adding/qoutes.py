import random


def random_qoute():
    messages = [
        "Today: in the app. Tomorrow: in your head.",
        "Add it once. Remember it forever.",
        "What you save today, you recall tomorrow.",
        "Feed it in today. Pull it out tomorrow.",
        "Today it's data. Tomorrow it's memory.",
        "Give it to the app tonight — wake up knowing it.",
        "Input today. Retained tomorrow.",
        "You add the knowledge. We make it stick.",
        "Today it's in the app. Tomorrow it's in your mind."
    ]

    qoute = random.choice(messages)

    return qoute
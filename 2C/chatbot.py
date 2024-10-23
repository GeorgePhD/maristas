import random

api_key = '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'

user_hi = [
    "Hi",
    "Hello",
    "Hey",
    "Hi there",
    "Hi, how are you?",
    "What's up?",
    "How do you do?",
    "How are you?",
    "How are you doing?",
    "What's up?",
]

Chatbot_hi = [
    "Hi",
    "Hello",
    "Hey",
    "Hi there",
    "Hi, how are you?",
    "What's up?",
    "How do you do?",
    "How are you?",
    "How are you doing?",
    "What's up?",
    "Hey, how are you?",
    "Hey, what's up?",
    "What's up?",
    "I'm doing great!",
    "I'm well!",
    "I'm good!",
    "I'm well!",
    "I'm great!",
    "I'm doing okay!",
]

general_answers = [

    "I'm doing well!",
    "I'm well!",
    "I'm great!",
    "I'm good!",
    "I'm doing okay!",
    "I'm okay!",
    "I'm doing well!",
]

def start_chatbot_response(user_input):
    if user_input in user_hi:
        return random.choice(Chatbot_hi)
    else:
        return random.choice(general_answers)
    
print(start_chatbot_response("what's up?"))
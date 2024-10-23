import random

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
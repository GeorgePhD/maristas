import openai

# Set up your API key
openai.api_key = "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"  
# Replace with your actual API key

def chatbot_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the newer model for chat completion
        messages=messages,
        max_tokens=150,  # Limit of tokens in the response
        temperature=0.7  # Adjust creativity
    )
    return response.choices[0].message['content'].strip()

# Initialize conversation
messages = [{"role": "system", "content": "You are a helpful assistant."}]  # System message for context

print("Chatbot is ready! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    # Add user input to messages
    messages.append({"role": "user", "content": user_input})
    
    # Get the chatbot response
    bot_response = chatbot_response(messages)
    
    # Add the bot's response to messages
    messages.append({"role": "assistant", "content": bot_response})
    
    print(f"Chatbot: {bot_response}")

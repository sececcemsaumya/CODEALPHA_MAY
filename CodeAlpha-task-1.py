import random

# Define more responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?", "All good, how about you?", "I'm fantastic, thank you!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["I'm just a humble chatbot!", "I don't have a name, but you can call me Chatbot!", "Names aren't really my thing, but you can call me Chatbot!"],
    "age": ["I'm timeless!", "Age is just a number for me!", "I don't have an age, but I'm here to assist you!"],
    "weather": ["It's sunny today!", "Looks like rain is on the way.", "The weather forecast says it'll be cloudy.", "It's a beautiful day outside!"],
    "default": ["I'm not sure what you mean...", "Can you please rephrase that?", "Sorry, I didn't understand."]
}

# Function to respond to user input
def respond(message):
    # Check if the message matches any predefined responses
    for key in responses:
        if message.lower() == key:
            return random.choice(responses[key])
    # If no match found, return a default response
    return random.choice(responses["default"])

# Main function to run the chatbot
def main():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()

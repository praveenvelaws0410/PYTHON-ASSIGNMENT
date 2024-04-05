import random
import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a chatbot, but I'm doing fine!", "I don't have feelings, but thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I didn't understand. Can you please rephrase?", "I'm not sure what you mean."],
}

# Create a chatbot using the responses
chatbot = Chat(responses, reflections)

# Start the conversation
print("Chatbot: Hi! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot.respond(user_input))

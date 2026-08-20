def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "My name is SimpleBot."

    elif message == "help":
        return "You can say hello, ask how I am, or say bye."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I do not understand that."


print("SimpleBot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)

    print("SimpleBot:", response)

    if user_message.lower().strip() == "bye":
        break

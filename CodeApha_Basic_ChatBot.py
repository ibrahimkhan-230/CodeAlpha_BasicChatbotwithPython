def chatbot():
    print(" Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == 'hello':
            print(" Chatbot: Hi!")
        elif user_input == 'how are you':
            print(" Chatbot: I'm fine, thanks!")
        elif user_input == 'what is your name':
            print(" Chatbot: I'm Chatbot 101.")
        elif user_input == 'bye':
            print(" Chatbot: Goodbye! Have a great day.")
            break
        else:
            print(" Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
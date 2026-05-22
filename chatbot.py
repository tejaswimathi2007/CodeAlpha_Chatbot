# Simple Rule-Based Chatbot

def chatbot():

    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello":
            print(" Chatbot: Hi!")

        elif user_input == "how are you":
            print(" Chatbot: I am fine, thanks!")

        elif user_input == "what is your name":
            print(" Chatbot: I am a simple Python chatbot.")

        elif user_input == "bye":
            print(" Chatbot: Goodbye!")
            break

        else:
            print(" Chahtbot: Sorry, I don't understand.")

# function call
chatbot()
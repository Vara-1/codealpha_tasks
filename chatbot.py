def chatbot():
    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "hi":
            print("Bot: Hello!")
        elif user == "hii":
            print("Bot: Hello!")
        elif user == "how are you":
            print("Bot: I'm fine! how can i help you?")
        elif user == "bye":
            print("Bot: Goodbye!")
        elif user == "goodbye":
            print("Bot: Goodbye!")
        elif user == "good morning":
            print("Bot: Good morning!")
        elif user == "good night":
            print("Bot: Good night!")
        elif user == "good evening":
            print("Bot: Good evening!")
        elif user == "good afternoon":
            print("Bot: Good afternoon!")
        elif user == "what is your name":
            print("Bot: My name is Chatbot.")
        elif user == "what can you do":
            print("Bot: I can chat with you and answer your questions.")
        elif user == "i need help":
            print("Bot: Sure! What do you need help with?")
        elif user == "ok":
            print("Bot: Anything else?")
        elif user == "no":
            print("Bot: Alright! Have a great day!")
            break
        elif user == "thank you":
            print("Bot: You're welcome!")
            break
        else:
            print("Bot: I don't understand")

chatbot()
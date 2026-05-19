#Display Chatbot title 
print("🤖 Welcome to My Chatbot")

#Instruction for the user to exit the chatbot 
print("Type 'bye' to end the chat")

#Infinite loop to keep chatbot running
while True:

    #Take User input and convert it to lowercase
    user = input("You: ").lower()

    #Check if user says hello
    if "hello" in user:
        print("Bot: Hello! How can I help you?")

    #Check if user asks about chatbot's condition
    elif "how are you" in user:
        print("Bot: I am doing great!")

    #Check if user asks Chatbot's name
    elif "your name" in user:
        print("Bot: I am a simple Python chatbot.")

    #Check if user asks Chatbot's course
    elif "course" in user:
        print("Bot: I can help with basic  conversation.")

    #Exit condition 
    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    #Default response for unknown inputs
    else:
        print("Bot: Sorry, I don't understand.")
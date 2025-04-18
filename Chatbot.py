def chatbot():
    while True:
        var1=input("Type: ")

        if "what is your name" in var1:
            print("My name is Deepseek")
        elif "are you human" in var1:
            print("No, I am not a human")
        elif "can you help me in math" in var1:
            print("Yes, I can help you what's your question")
        elif "who are you" in var1:
            print("I am a  Ai Chatbot")
        else:
            print("Question Again")

chatbot()
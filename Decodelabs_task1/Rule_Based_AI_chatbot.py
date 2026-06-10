import time
exit_commands=("quit", "exit", "bye", "goodbye","okay thank you" , "ok bye")
data = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey! How can I help you?",
    "good morning": "Good morning! Hope you have a great day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",

    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "who created you": "I was created using Python and simple rules.",
    "what can you do": "I can answer predefined questions and have simple conversations.",
    "are you human": "No, I am a chatbot.",
    "how old are you": "I do not have an age like humans.",

    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that enables systems to learn from data.",
    "what is python": "Python is a popular programming language.",
    "what is java": "Java is an object-oriented programming language.",
    "what is programming": "Programming is the process of writing instructions for computers.",
    "what is a chatbot": "A chatbot is a software program that simulates conversation with users.",

    "what is the capital of france": "The capital of France is Paris.",
    "who is the father of computer": "Charles Babbage is known as the Father of the Computer.",

    "what day is today": "I cannot check the current day, but your system can.",
    "what time is it": "I cannot check the current time.",

    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "do you like coding": "Of course! Coding is what makes chatbots possible.",
    "what is your favorite language": "Python is one of my favorite languages.",
    "can you sing": "Sorry, I cannot sing, but I can chat with you.",
    "can you dance": "I can only dance in code!",

    "where do you live": "I live inside a computer program.",
    "are you smart": "I am smart within the limits of my programmed rules.",
    "do you have friends": "Other programs are my friends.",

    "thank you": "You're welcome!",
    "thanks": "Glad I could help!",
    "nice": "Thank you!",

    "bye": "Bye and take care!",
    "goodbye": "Goodbye! Have a wonderful day."
}

print("=== Rule-Based AI Chatbot ===")
print("Type 'quit', 'exit', 'bye', 'goodbye' , 'ok bye' or 'okay thank you' to end the chat.\n")
while True:
    user_input = input("You: ").lower().strip()

    print("Bot: Thinking...")
    time.sleep(1)
    if user_input in exit_commands:
        if user_input in data:
            print("Bot:", data[user_input])
        else:
            print("Bot: Goodbye! Have a great day.")
        break
    elif user_input in data:
        print("Bot:", data[user_input])
    else:
        print("Bot: Sorry, I didn't understand that.")
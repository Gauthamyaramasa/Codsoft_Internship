
### CODSOFT TASK-1 [Chatbot With Rule-Based Responses Using if-else statements] ###
def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm fine. How about you?!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "am fine" in user_input:
        return "Great to hear!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot."
    elif "what is the weather" in user_input:
        return "I'm sorry, I can't provide real-time weather information."
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "who is your creator" in user_input or "who made you" in user_input:
        return "I was created by Codsoft."
    elif "how old are you" in user_input:
        return "I don't have an age. I'm just a program."
    elif "what can you do" in user_input:
        return "I can provide information, answer questions, tell jokes, give recommendations, and more!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    elif "how does a computer work" in user_input:
        return "A computer processes data using electronic components like transistors and circuits."
    elif "can you help me learn programming" in user_input:
        return "Of course! I can provide programming resources and answer your coding questions."
    elif "recommend a book" in user_input:
        return "Sure! How about 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams?"
    elif "what's the meaning of life" in user_input:
        return "The answer to the ultimate question of life, the universe, and everything is 42."
    else:
        return "I'm sorry, I don't understand that."

# Main loop for the chatbot
print("Simple Chatbot: Hi there! How can I assist you today?")
while True:
    user_input = input("You: ").lower()
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

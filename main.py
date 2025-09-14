import random
responses = {
    "hello": ["Hello there!", "Hi! Nice to meet you", "Hey! How's it going?"],
    "how are you": ["I'm doing great, thanks! what about you?", "All good here 😊 You?"],
    "name": ["I,m Pybot, your Python chatbot 🤖", "You can call me Pybot!"],
    "help": ["Sure! Tell me what you need help with.", "I,m here to assist, go ahead!"],
    "bye": ["Goodbye! Take care 😄", "See you soon 👋", "Bye! Have a nice day!"]
}
unknown_responses = [
    "hmm...I didn,t quite get that 🤔", "can you say that differently?", "I,m learning! 🧠", "Interesting...tell me more!"
]
def advanced_chatbot():
    print("Pybot 🤖: Hi! I,m Pybot. Type 'bye' to exit.")
    while True:
        user_input = input("You:",).lower()
        matched = False
        for key in responses:
            if key in user_input:
                print("Pybot 🤖:", random.choice(responses[key]))
                matched = True
                if key == "bye":
                    return
                break
        if not matched:
            print("Pybot 🤖:", random.choice(unknown_responses))  
advanced_chatbot()
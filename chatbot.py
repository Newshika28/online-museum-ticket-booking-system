import random

# Define intents and associated keywords
intents = {
    "greet": [
        "hello", "hi", "hey", "good morning", "good evening", "hi there",
        "hello there", "hey bot", "greetings", "what's up", "yo", "hi assistant"
    ],
    "goodbye": [
        "bye", "goodbye", "see you later", "talk to you later", "see ya", "take care",
        "farewell", "I have to go", "catch you later", "thanks, bye"
    ],
    "book_tickets": [
        "book tickets", "reserve tickets", "buy tickets", "i want to book",
        "can you book my tickets", "help me reserve seats", "i need tickets",
        "get me two tickets", "how to book", "ticket booking", "book for me",
        "want to attend a show", "need museum tickets"
    ],
    "ask_schedule": [
        "what shows are available", "today's schedule", "any shows today",
        "what events are happening", "show timings please", "list today's shows",
        "what can I see today", "show list", "what's on", "any exhibitions today",
        "what's running in the museum", "give me the schedule"
    ],
    "thanks": [
        "thanks", "thank you", "thx", "appreciate it", "thanks a lot", "much appreciated",
        "thank you so much", "cheers", "cool thanks", "great help", "grateful"
    ]
}

# Define responses for each intent
responses = {
    "greet": ["Hello! 👋 Welcome to the Museum Ticket Assistant. How can I help you today?"],
    "goodbye": ["Goodbye! Hope you enjoy your visit to the museum!"],
    "book_tickets": ["Sure! I can help with that.\nLet’s get started:"],
    "ask_schedule": [
        "Today's show time slots are:\n⏰ 10:00 AM – 11:00 AM\n⏰ 11:00 AM – 12:00 PM\n⏰ 12:00 PM – 1:00 PM\n⏰ 1:00 PM – 2:00 PM\n⏰ 2:00 PM – 3:00 PM"
    ],
    "thanks": ["You're welcome! 😊"],
    "unknown": ["Sorry, I didn't understand that. Could you rephrase?"]
}

# Classify the user's intent based on their input
def classify_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return "unknown"

# Get a response based on the classified intent
def get_response(intent):
    return random.choice(responses.get(intent, responses["unknown"]))

# Handle the ticket booking process
def book_tickets_flow():
    print("🤖 Okay, let's book your museum tickets.")

    # Number of tickets
    while True:
        tickets = input("🎫 How many tickets do you need? (Max 10): ")
        if tickets.isdigit() and 1 <= int(tickets) <= 10:
            tickets = int(tickets)
            break
        else:
            print("❗ Please enter a valid number between 1 and 10.")

    # Booking date
    date = input("📅 What date would you like to book for? (e.g., 2025-07-20): ")

    # Time slot selection
    print("\n⏰ Available Time Slots:")
    time_slots = [
        "10:00 AM – 11:00 AM",
        "11:00 AM – 12:00 PM",
        "12:00 PM – 1:00 PM",
        "1:00 PM – 2:00 PM",
        "2:00 PM – 3:00 PM"
    ]
    for i, slot in enumerate(time_slots, 1):
        print(f"{i}. {slot}")

    while True:
        time_choice = input("🔢 Please choose a time slot (e.g., 1 for 10:00 AM – 11:00 AM): ")
        if time_choice.isdigit() and 1 <= int(time_choice) <= len(time_slots):
            selected_slot = time_slots[int(time_choice) - 1]
            break
        else:
            print("❗ Invalid input. Please enter a number between 1 and 5.")

    # Confirmation
    print(f"\n✅ Booking Confirmed!")
    print(f"🎟️ {tickets} ticket(s) on {date} at {selected_slot}")
    print("🎉 Enjoy your visit to the museum!")

# Main chatbot loop
def chat():
    print("🤖 Museum Bot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 Museum Bot: Goodbye!")
            break
        intent = classify_intent(user_input)
        if intent == "book_tickets":
            book_tickets_flow()
        else:
            response = get_response(intent)
            print("🤖 Museum Bot:", response)

# Entry point of the script
if __name__ == "__main__":
    chat()



def get_bot_response(user_input: str) -> str:
    """Matches user input to predefined responses using exact and partial rules."""
    text = user_input.strip().lower()
    if text in ["hello", "hi", "hey", "greetings"]:
        return "Hi!"
    elif text in ["how are you", "how are you?", "how's it going", "how do you do"]:
        return "I'm fine, thanks!"
    elif text in ["bye", "goodbye", "see ya", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try asking 'hello', 'how are you', or type 'bye' to exit."
def run_chatbot():
    """Main loop to run the interactive chatbot."""
    print("=" * 45)
    print("         BASIC CHATBOT INITIALIZED           ")
    print(" Type 'hello', 'how are you', or 'bye' to exit.")
    print("=" * 45)
    while True:
        try:
            user_input = input("\nYou: ")
            
            # Skip empty inputs
            if not user_input.strip():
                continue

            response = get_bot_response(user_input)
            print(f"Bot: {response}")

            # Exit condition
            if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break
if __name__ == "__main__":
    run_chatbot()
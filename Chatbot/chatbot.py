import random
import logging
import json

# Set up logging configuration
logging.basicConfig(filename='chatbot_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Predefined agent names and exit keywords
agent_names = ["Alex", "Jamie", "Taylor", "Jordan", "John", "Jimmy", "Ryan", "Denis", "Roger"]
exit_keywords = ["quit", "exit", "bye"]

# Function to load keyword-response pairs from a JSON file
def load_responses():
    with open('keywords_responses.json', 'r') as file:
        return json.load(file)

# Function to log messages
def log_message(message):
    logging.info(message)

# Greeting and agent name setup
def get_agent_name():
    return random.choice(agent_names)

# Main chatbot function
def chatbot():
    user_name = input("Welcome! What's your name? ").strip()
    if not user_name:
        user_name = "Friend"  # Default name if user doesn't input one
    agent_name = get_agent_name()
    
    greeting_message = f"Hi {user_name}, I'm {agent_name}, your assistant!"
    print(greeting_message)
    log_message(greeting_message)
    
    print(f"Feel free to ask me anything about our college or type 'bye' to exit.")
    
    # Load keyword-response pairs from the JSON file
    keywords_responses = load_responses()

    while True:
        user_input = input(f"{user_name}: ").strip().lower()
        log_message(f"{user_name}: {user_input}")  # Log the user's input
        
        if user_input in exit_keywords:
            confirmation = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            log_message(f"{user_name} decided to exit.")  # Log the exit decision
            if confirmation in ["yes", "y"]:
                farewell_message = f"{agent_name}: Goodbye, {user_name}! Take care!"
                print(farewell_message)
                log_message(farewell_message)  # Log farewell message
                break
            else:
                continuation_message = f"{agent_name}: Okay, let's continue!"
                print(continuation_message)
                log_message(continuation_message)  # Log continuation message
                continue
        
        # Keyword matching
        found_response = False
        input_words = set(user_input.split())
        for keyword in keywords_responses.keys():
            if keyword in input_words:
                response = random.choice(keywords_responses[keyword])
                print(f"{agent_name}: {response}")
                log_message(f"{agent_name}: {response}")  # Log the chatbot's response
                found_response = True
                break
        
        # If no keyword matched, provide a random response from 'noreply'
        if not found_response:
            generic_response = random.choice(keywords_responses['noreply'])
            print(f"{agent_name}: {generic_response}")
            log_message(f"{agent_name}: {generic_response}")  # Log the chatbot's response
        
        # Random disconnection simulation
        if random.random() < 0.1:  # 10% chance of disconnection
            disconnection_message = f"{agent_name}: Oops, I seem to have disconnected. One moment..."
            print(disconnection_message)
            log_message(disconnection_message)  # Log disconnection
            reconnection_message = f"{agent_name}: I'm back, {user_name}! Let's continue."
            print(reconnection_message)
            log_message(reconnection_message)  # Log reconnection

# Run the chatbot
if __name__ == "__main__":
    chatbot()
import sqlite3

# Function to get the chatbot response from the database
def chatbot_response(user_input):
    # Connect to the SQLite database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # Clean and process user input (convert to lowercase for case-insensitive matching)
    user_input = user_input.lower()
    
    # Query the database to find a matching response
    cursor.execute('''
    SELECT response FROM chatbot_responses WHERE question = ?
    ''', (user_input,))
    
    result = cursor.fetchone()  # Fetch the first matching result
    
    # If a response is found, return it; oqtherwise, return a default message
    if result:
        return result[0]
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
    
    # Close the database connection
    conn.close()

# Main loop for the chatbot interaction
def main():
    print("ChatBot: Hello! I'm here to assist you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit the chatbot if the user types 'bye'
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Take care!")
            break
        
        # Get the response from the database based on user input
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()

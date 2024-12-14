import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Create a table to store predefined questions and responses
cursor.execute('''
CREATE TABLE IF NOT EXISTS chatbot_responses (
    question TEXT PRIMARY KEY,
    response TEXT
)
''')

# Insert some predefined question-response pairs into the database
responses = {
         "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I am friday, your virtual assistant.",
        "say my name": "karthi .",
        "bye": "Goodbye! Have a great day ahead!",
        "thank you": "You're welcome! I'm here to assist you.",
        "who are you": "I am a chatbot created to help you with anything you need.",
        "what can you do": "I can help you with general information, provide assistance, and much more!",
        "how old are you": "I don't have an age, but I am always learning!",
        "where do you live": "I live in the digital world, ready to assist you anytime.",
        "what time is it": "I cannot check the time, but you can see it on your device!",
        "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
        "help": "Sure! How can I assist you today? You can ask me anything.",
        "weather": "I don't have live weather data, but you can check your local weather app for updates.",
        "favorite color": "I don't have preferences, but I think blue is a nice color.",
        "can you play music": "I can't play music directly, but I can suggest some great playlists!",
        "good morning": "Good morning! I hope you have a wonderful day!",
        "good evening": "Good evening! How was your day?",
        "good night": "Good night! Sleep well!",
        "what is your purpose": "My purpose is to help answer your questions and assist you with tasks.",
        "thank you very much": "You're very welcome! I'm always here to help.",
        "you're welcome": "Thank you for your kindness! 😊",
        "who created you": "I was created by developers to assist you with information and tasks.",
        "can you learn": "I can be updated with new data, but I don't learn in real-time like humans.",
        "are you real": "I am real in the sense that I exist as a program, but I'm not a human.",
        "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
        "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!"
}

# Insert predefined responses into the database (use REPLACE to avoid duplicates)
cursor.executemany('''
INSERT OR REPLACE INTO chatbot_responses (question, response) VALUES (?, ?)
''',[(key,value)for key,value in responses.items()])


# Commit changes and close the database connection
conn.commit()
conn.close()

print("Database initialized with predefined responses.")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '').lower()
    # Simple responses
    if user_input == "hello":
        return jsonify({"response": "Hi there! How can I help you?"})
    elif user_input == "how are you?":
        return jsonify({"response": "I'm doing great, thank you!"})
    else:
        return jsonify({"response": "I didn't understand that. Could you please rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)    


    "https://replit.com/@skarthikeyan211/project-of-chatbot"

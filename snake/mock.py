from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for the chat API
mock_data = [
    {"id": "0"},
    {"id": "1"}
]

@app.route('/api/chat', methods=['GET'])
def get_chat():
    chatId = request.args.get("chatId")
    if (chatId == 0):
        return jsonify([{"role": "user", "content": "helo"}, {"role": "assistant", "content": "hi there!"}])
    else:
        return jsonify([{"role": "user", "content": "helo"}, {"role": "assistant", "content": "hi there!"}])

@app.route('/api/chats', methods=['GET'])
def get_chats():
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
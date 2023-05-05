import asyncio

from flask import Flask, jsonify, request

from bot import create_supergroup

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to my Flask app!'})

@app.route("/create_channel", methods=['POST'])
def create_channel():
    if request.method == "POST":
        data = request.get_json()
        asyncio.run(create_supergroup(data["channel_title"]))
        return jsonify({'message': 'Channel created successfully!'})

if __name__ == '__main__':
    app.run()

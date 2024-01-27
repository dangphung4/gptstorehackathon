from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
from flask_socketio import SocketIO
import re


app = Flask(__name__)
API_KEY = os.environ.get("OPEN_AI_KEY")
print(API_KEY)
client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY", "api key here"))
socketio = SocketIO(app)


# Assuming each user has a unique user_id
# You can use a more sophisticated method for session management
user_sessions = {}  # This will store the conversation history

# Load the environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv('OPEN_AI_KEY')
MODEL = "gpt-3.5-turbo"

@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.json['user_id']
    user_message = request.json['message']

    # Retrieve conversation history for the user
    conversation = user_sessions.get(user_id, [])

    # Append the new user message to the conversation
    conversation.append({"role": "user", "content": user_message})

    # Generate a response from ChatGPT
    response = client.chat.completions.create(
         model=MODEL,
        messages=conversation
    )

    # Extract the generated reply
    reply = response.choices[0].message.content

    # Append the reply to the conversation
    conversation.append({"role": "assistant", "content": reply})

    # Store the updated conversation history
    user_sessions[user_id] = conversation

    return jsonify({'reply': reply})


def song_recommendations():
    user_id = request.json['user_id']
    prompt = request.json['prompt']

    # TODO: Extract song/artist names from the prompt
    # This is a simplified example. You might need more complex parsing or NLP here.
    song_or_artist = extract_song_or_artist(prompt)  

    # Fetch recommendations from Spotify
    # Replace this URL with your actual Spotify API endpoint
    spotify_response = requests.post('http://localhost:5000/', json={'song_or_artist': song_or_artist})
    recommendations = spotify_response.json()['recommendations']

    # Generate a ChatGPT response describing these songs
    description_prompt = f"Describe these songs: {recommendations}"
    chat_response = client.chat.completions.create(
        model=MODEL,
        prompt=description_prompt,
        max_tokens=150
    )
    description = chat_response.choices[0].text.strip()

    return jsonify({'description': description})

def extract_song_or_artist(speech_text):
    # Regular expression patterns to match song names and artists
    song_pattern = r'(?i)(?:song|track):?\s*(\w+(?:\s+\w+)*)'
    artist_pattern = r'(?i)(?:artist|singer|band):?\s*(\w+(?:\s+\w+)*)'

    # Extract song names and artists using regular expressions
    song_matches = re.findall(song_pattern, speech_text)
    artist_matches = re.findall(artist_pattern, speech_text)

    # Return the extracted song names and artists as a dictionary
    return {'songs': song_matches, 'artists': artist_matches}

@app.route('/artistsrecommedations', methods=['POST'])

@app.route('/')
def home():
    return 'Welcome to the home page!'

@socketio.on('send_message')
def handle_message(data):
    user_id = data['user_id']
    user_message = data['message']
    # Existing logic to handle chat messages
    socketio.emit('receive_message', {'reply': reply})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    socketio.run(app)


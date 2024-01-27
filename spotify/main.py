from flask import Flask, request, redirect
import requests
import base64
import urllib

# Initialize Flask app
app = Flask(__name__)

# Spotify API Credentials
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'user-top-read'

# Function to generate Spotify authorization URL
def get_auth_url():
    auth_url = 'https://accounts.spotify.com/authorize?'
    auth_url += 'response_type=code'
    auth_url += '&client_id=' + CLIENT_ID
    auth_url += '&scope=' + urllib.parse.quote(SCOPE)
    auth_url += '&redirect_uri=' + urllib.parse.quote(REDIRECT_URI)
    return auth_url

# Function to get access token
def get_access_token(code):
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(token_url, data=token_data)
    return response.json()

# Flask route for homepage
@app.route('/')
def index():
    return '<a href="' + get_auth_url() + '">Login with Spotify</a>'

# Flask route for Spotify callback
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = get_access_token(code)
    access_token = token_info['access_token']

    # Get song recommendations (example using the 'seed_artists' parameter)
    rec_url = 'https://api.spotify.com/v1/recommendations?seed_artists=4NHQUGzhtTLFvgF5SZesLK'
    headers = {'Authorization': 'Bearer ' + access_token}
    rec_response = requests.get(rec_url, headers=headers)
    rec_data = rec_response.json()

    return str(rec_data)  # Displaying recommendations as a string for simplicity

if __name__ == '__main__':
    app.run(debug=True)

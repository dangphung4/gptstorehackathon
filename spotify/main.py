from flask import Flask, request, redirect
import requests
import base64
import urllib

# Initialize Flask app
app = Flask(__name__)

# Spotify API Credentials
CLIENT_ID = 'a84453c58306431f9b82fc2dde760e69'
CLIENT_SECRET = '4cf441b1c10e4d3f91598947268376a8'
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
    response_json = response.json()

    if 'access_token' in response_json:
        return response_json ['access_token']
    else:
        print("Erroe in Spotify API response:", response_json)
        return None
# Function to search for a track and get its ID
def get_track_id(access_token, track_name):
    search_url = f'https://api.spotify.com/v1/search?q={urllib.parse.quote(track_name.encode("utf-8"))}&type=track&limit=1'
    headers = {'Authorization': 'Bearer ' + access_token}
    search_response = requests.get(search_url, headers=headers)
    search_data = search_response.json()

    if 'tracks' in search_data and 'items' in search_data['tracks'] and search_data['tracks']['items']:
        return search_data['tracks']['items'][0]['id']
    else:
        print("Error in Spotify track search API response:", search_response.text)
        return None
    
# Flask route for homepage
@app.route('/')
def index():
    return '<a href="' + get_auth_url() + '">Login with Spotify</a>'

# Flask route for Spotify callback
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = get_access_token(code)

    if token_info is not None:
        access_token = token_info

        user_input = request.args.get('user_input')

        if user_input is not None:
            print("Access Token", access_token)

            # Get track recommendations
            search_url = f'https://api.spotify.com/v1/search?q={urllib.parse.quote(user_input.encode("utf-8"))}&type=track&limit=1'
            headers = {'Authorization': 'Bearer ' + access_token}
            search_response = requests.get(search_url, headers=headers)

            if search_response.status_code == 200:
                search_data = search_response.json()
                # Extract the track ID from the search results
                track_id = search_data.get('tracks', {}).get('items', [])[0].get('id')
                if track_id:
                    return f"Recommended track ID: {track_id}"
                else:
                    return "No track found in the search results."
            else:
                print("Error in Spotify search API response:", search_response.text)
                return "Failed to fetch recommendations"
        else:
            return "User input is missing in the request."
    else:
        return "Failed to get access token"

if __name__ == '__main__':
    app.run(debug=True)
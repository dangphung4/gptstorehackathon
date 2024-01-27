from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key
openai.api_key = 'your_openai_api_key'

# Flask route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    song_recommendations = data['songs']  # Assuming 'songs' contains the recommendations from Spotify

    # Prepare prompt for OpenAI
    prompt = f"I received the following song recommendations: {song_recommendations}. Let's have a chat about music."

    # Make a call to OpenAI's GPT model
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different model if you prefer
        prompt=prompt,
        max_tokens=150
    )

    # Return the response from OpenAI
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)

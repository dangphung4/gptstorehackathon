# GPTStoreHackathon

## Team Members
- Ale
- Dang
- Rusul
- Shams

Welcome to the GPTStoreHackathon project repository! Our team has developed an innovative song recommender system that leverages the power of ChatGPT integration alongside Spotify's rich music library. This project aims to provide users with personalized song recommendations based on their musical tastes and preferences.

## Project Overview

Our AI-powered music recommendation app combines the conversational capabilities of ChatGPT with Spotify's comprehensive music database to deliver a unique and tailored music discovery experience. Users can interact with the app through natural language to find new songs and artists based on their current favorites.

## Tech Stack
- **React Native**: Used for building a cross-platform mobile application that delivers a seamless user experience on both Android and iOS devices.
- **Flask**: Serves as the backend framework, managing requests between the frontend, OpenAI, and Spotify APIs.
- **OpenAI**: Powers the conversational AI, interpreting user inputs to generate meaningful song recommendations.
- **Spotify API**: Provides access to Spotify's vast music library, enabling our app to fetch song data and recommendations.

## Installation
Instructions on how to set up the project locally. This section will be updated with step-by-step commands to clone, install dependencies, and run the project on your machine.

```bash
# Clone the repository
git clone git@github.com:dangphung4/gptstorehackathon.git

# Navigate to the project directory
cd gptstorehackathon

# Install dependencies

# For Flask backend Spotify, open up a new terminal 
# Navigate to spotify directory
cd spotify 
pip install -r requirements.txt
# Run the application
python3 main.py

# For Flask backend openai, open up a new terminal
# Navigate to spotify directory
cd openai 
pip install -r requirements.txt
# Run the application
python3 main.py

# For React Native
cd gpthack
npm install
# Start the React Native Expo app with a third terminal 
npx expo start
# Or Start React Native Expo with tunnel
npx expo start --tunnel

```

## Usage
The goal of this app was to be designed like the chatpgpt app on mobile devices. It is intended to be used this way in addition to real time and updated music recommendations. 

## Contributing
We welcome contributions from the community! Whether you're interested in fixing bugs, adding new features, or improving documentation, please feel free to fork the repository and submit a pull request. See `CONTRIBUTING.md` for more details on how to contribute to our project.

## License
---

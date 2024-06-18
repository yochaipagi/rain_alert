Weather Notification System
This Python script fetches weather data from the OpenWeatherMap API and sends a WhatsApp message via Twilio if rain is forecasted. It uses environment variables to keep sensitive information secure.

Features
Fetches weather data for a specified location.
Checks for rain in the upcoming forecast.
Sends a WhatsApp message to notify you if it's going to rain.
Prerequisites
Python 3.x
Twilio account with WhatsApp enabled.
OpenWeatherMap API key.
Installation
Clone this repository or download the script.

Install the required Python packages:

bash
Copy code
pip install requests twilio
Set up your environment variables:

AUTH_TOKEN: Your Twilio Auth Token.
OWN_API_KEY: Your OpenWeatherMap API Key.
You can set these in your terminal:

bash
Copy code
export AUTH_TOKEN='your_twilio_auth_token'
export OWN_API_KEY='your_openweathermap_api_key'

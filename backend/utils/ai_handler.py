import requests
import json

# Gemini API URL and API key
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
API_KEY = "AIzaSyCFF3UdJo4ETZ2xyYftPDNyIel90pi_fXM"  # Replace this with your actual API key

# Function to generate README from code summary
def generate_readme(code_summary: str):
    # Define the request body
    request_body = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": code_summary
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topK": 64,
            "topP": 0.95,
            "maxOutputTokens": 65536,
            "responseMimeType": "text/plain"
        }
    }

    # Send POST request to Gemini API
    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={API_KEY}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(request_body)
        )
        
        # Check if the response was successful
        if response.status_code == 200:
            result = response.json()
            return result.get("content", "No content generated")
        else:
            return f"Error {response.status_code}: {response.text}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

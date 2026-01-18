import requests
import json

def get_cohere_response(user_input, chat_history=[]):
    url = "https://api.cohere.com/v2/chat"
    api_key = "YOUR_COHERE_API_KEY"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    # Structured System Message to force Content Creation mode
    system_message = {
        "role": "system",
        "content": "You are an expert AI Content Strategist. Your goal is to generate high-converting blog posts, social media captions, and scripts. Format all output in clean Markdown."
    }

    payload = {
        "model": "command-r-plus-08-2024", # Use the latest Command R+ model
        "messages": [system_message] + chat_history + [{"role": "user", "content": user_input}],
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()['message']['content'][0]['text']
    else:
        return f"Error: {response.status_code} - {response.text}"

import requests

def call_firework_api(chunk, question, api_key):
    url = "https://api.firework.com/generate"  # replace with actual API endpoint
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "chunk": chunk,
        "question": question
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

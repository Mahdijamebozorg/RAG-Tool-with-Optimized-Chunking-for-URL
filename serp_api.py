import requests

def get_url_content(url, api_key):
    serp_url = f"https://serpapi.com/search?url={url}&api_key={api_key}"
    response = requests.get(serp_url)
    return response.text
import requests

def get_url_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve content. Status code: {response.status_code}")
    return response.text
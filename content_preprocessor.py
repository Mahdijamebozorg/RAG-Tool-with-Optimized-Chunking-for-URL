from bs4 import BeautifulSoup

def clean_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    cleaned_text = ' '.join(text.split())
    return cleaned_text  
from bs4 import BeautifulSoup

def clean_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Remove unnecessary HTML tags, ads, etc.
    return soup.get_text()

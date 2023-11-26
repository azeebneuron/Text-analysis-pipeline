import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to extract text from a URL
def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 404:
        return "error 404"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the article content
    article_content_tag = soup.find('div', class_='td-post-content tagdiv-type')  # Replace with the appropriate class or ID for the article content
    if article_content_tag:
        article_text = article_content_tag.get_text()
    else:
        print(f"No article content found for URL: {url}")
        return None

    return article_text

# Read URLs from the Excel file
input_data = pd.read_excel('Input.xlsx')
urls = input_data['URL'].tolist()
url_ids = input_data['URL_ID'].tolist()

# Extract data for each URL and save it to text files
for url, url_id in zip(urls, url_ids):
    article_text = extract_text_from_url(url)
    if article_text:
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)
    else:
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write("error 404")
# 

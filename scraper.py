import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve
import sys

dest = sys.argv[2]
url = sys.argv[1]


def scrapeSeals(url, keyword, download_folder):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all image links with "seal" in their filename
        image_links = soup.find_all('a', href=lambda href: href and keyword in href)
        
        print(image_links)
        # Create the download folder if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)
        
        # Download high-resolution images
        for link in image_links:
            img_page_url = urljoin(url, link['href'])
            img_response = requests.get(img_page_url)
            if img_response.status_code == 200:
                img_soup = BeautifulSoup(img_response.content, 'html.parser')
                img_tag = img_soup.find('div', class_='fullImageLink').find('a')
                if img_tag:
                    img_url = urljoin(url, img_tag['href'])
                    img_filename = os.path.basename(img_url)
                    img_path = os.path.join(download_folder, img_filename)
                    urlretrieve(img_url, img_path)
                    print(f"Downloaded: {img_url}")
            else:
                print(f"Failed to fetch image page: {img_page_url}")
    else:
        print(f"Failed to fetch {url}")



scrapeSeals(url, "seal", dest)
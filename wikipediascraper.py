import os
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve
import sys

dest = sys.argv[2]
url = sys.argv[1]


def scrapeSeals(url, keyword, download_folder):
    # Send a GET request to the URL

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        
        file_descriptions = soup.find_all('a', class_='mw-file-description', href=lambda href: href and ('seal' in href or 'Seal' in href))


        print(len(file_descriptions))
        for link in file_descriptions:
            filepage = requests.get("https://en.wikipedia.org" + link.get("href"))
            if filepage.status_code == 200:
                filehtml = BeautifulSoup(filepage.content, 'html.parser')
                imagelink = filehtml.find('a', text="Original file")
                if (imagelink):
                    imageurl = imagelink.get("href")
                    imageurl = "https:" + imageurl
                    filename = imageurl.split("/")[-1]
                    if os.path.exists(download_folder + "/" + filename): 
                        print("file already downloaded")
                        continue
                    imgdownload = requests.get(imageurl, headers=headers)
                    if imgdownload.status_code == 200:
                        with open(download_folder + "/" + filename, "wb") as image_file:
                            image_file.write(imgdownload.content)
                    else:

                        print(f"error {imgdownload.status_code} downloading file {imgdownload.url}")
                  
                else:
                    print(f"error finding original file link for {link.get('href')}")

            else:
                print("failed")


scrapeSeals(url, "seal", dest)
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urls = ['https://publicdomainreview.org/collections/all/']
idx = 0
for page in range(2, 49):
    for url in urls:
        try:
            htmldata = requests.get(url + str(page)).text
            soup = BeautifulSoup(htmldata, 'html.parser')  
            image_urls = []
            for item in soup.find_all('img'): 
                image_urls.append(item['src'])

            save_dir = './images'
        except Exception as e:
            continue

        # Download and save each image
        for i, image_url in enumerate(image_urls):
            try:
                # Send a GET request to the image URL
                response = requests.get(image_url)
                
                # Get the content of the response (image bytes)
                image_content = response.content
                
                # Generate a filename for the image
                filename = os.path.join(save_dir, f"image_{idx}.jpg")
                idx = idx + 1
                
                # Save the image to the local filesystem
                with open(filename, 'wb') as f:
                    f.write(image_content)
                
                print(f"Image saved successfully.")
            except Exception as e:
                print(f"Error saving image {idx+1}: {e}")
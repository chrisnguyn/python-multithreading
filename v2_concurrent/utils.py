import json
import os
import requests
from urllib.request import urlopen


def clear_images(directory):
    for img in os.listdir(directory):
        if img == 'note.txt':
            continue

        os.remove(f'{directory}/{img}')


def get_image_links(client_id):
    image_links = []
    url = 'https://api.imgur.com/3/gallery/random/random/'
    auth = { 'Authorization' : f'Client-ID {client_id}' }
    response = requests.get(url, headers=auth)
    data = response.json()

    for item in data['data']:
        if 'type' in item and item['type'] in { 'image/jpg', 'image/jpeg', 'image/png' }:
            image_links.append(item['link'])
    
    return image_links


def dl_image_link(directory, link):
    file_path = directory / os.path.basename(link)
    new_file = file_path.open('wb')

    with urlopen(link) as image:
        new_file.write(image.read())

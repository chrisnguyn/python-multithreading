import os
from dotenv import load_dotenv
from pathlib import Path
from time import time
from utils import clear_images, get_image_links, dl_image_link

load_dotenv()


def main():
    key = os.getenv('CLIENT_ID')
    download_path = Path('/mnt/c/Users/Chris/Desktop/concurrency/images')
    image_links = get_image_links(key)
    clear_images(download_path)
    timestamp = time()

    for link in image_links:
        dl_image_link(download_path, link)
    
    print(f'Finished downloading {len(image_links)} image(s) in {time() - timestamp} seconds.')


if __name__ == '__main__':
    main()

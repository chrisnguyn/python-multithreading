import os
from dotenv import load_dotenv
from pathlib import Path
from time import time
from utils import clear_images, get_image_links, dl_image_link

load_dotenv()


def main():
    key = os.getenv('CLIENT_ID')
    # dl_path = Path('/mnt/c/Users/Chris/Desktop/python-multithreading/images')  # windows
    dl_path = Path('/Users/chris/Desktop/Stuff/GitHub/python-multithreading/images')  # mac
    image_links = get_image_links(key)
    clear_images(dl_path)
    timestamp = time()

    for link in image_links:
        dl_image_link(dl_path, link)
    
    print(f'Finished downloading {len(image_links)} image(s) in {time() - timestamp} seconds.')


if __name__ == '__main__':
    main()

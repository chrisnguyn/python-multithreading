"""
https://docs.python.org/3/library/multiprocessing.html
why starmap: https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
why get_content('spawn'): https://stackoverflow.com/questions/50168647/multiprocessing-causes-python-to-crash-and-gives-an-error-may-have-been-in-progr

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))  # call a function with a list of input
"""

import os
import multiprocessing
from dotenv import load_dotenv
from itertools import repeat
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

    with multiprocessing.get_context('spawn').Pool() as pool:  # with Pool() as pool crashed bc macOS security
        pool.starmap(dl_image_link, zip(repeat(dl_path), image_links))  # pool.starmap instead of .map because 'dl_image_link' takes multiple parameters
    
    print(f'Finished downloading {len(image_links)} image(s) in {time() - timestamp} seconds.')


if __name__ == '__main__':
    main()

"""
https://docs.python.org/3/library/queue.html

import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')
"""

import os
from dotenv import load_dotenv
from pathlib import Path
from queue import Queue
from threading import Thread
from time import time
from utils import clear_images, get_image_links, dl_image_link

load_dotenv()


class Worker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue


    def run(self):
        while True:
            directory, link = self.queue.get()  # get work from queue

            try:
                dl_image_link(directory, link)
            finally:
                self.queue.task_done()  # do the work, and when done, close the task


def main():
    key = os.getenv('CLIENT_ID')
    # dl_path = Path('/mnt/c/Users/Chris/Desktop/python-multithreading/images')  # windows
    dl_path = Path('/Users/chris/Desktop/Stuff/GitHub/python-multithreading/images')  # mac
    image_links = get_image_links(key)
    clear_images(dl_path)
    timestamp = time()
    queue = Queue()

    for i in range(8):
        worker = Worker(queue)  # put worker thread into the queue
        worker.daemon = True
        worker.start()

    for link in image_links:  # for all the links we got, put work into the queue to be done
        queue.put((dl_path, link))

    queue.join()  # blocked until all tasks finish / queue is empty (this is why we have daemon = True, main thread exits when no daemon threads left)
    print(f'Finished downloading {len(image_links)} image(s) in {time() - timestamp} seconds.')


if __name__ == '__main__':
    main()

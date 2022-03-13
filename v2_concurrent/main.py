import os
from queue import Queue
from threading import Thread
from time import time
from utils import clear_images, get_image_links, dl_image_link


class Worker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue


    def run(self):
        while True:
            directory, link = self.queue.get()

            try:
                dl_image_link(directory, link)
            finally:
                self.queue.task_done()


def main():
    timestamp = time()
    key = os.getenv('CLIENT_ID')

import os
from functools import partial


class Fragment:
    # DATA_DIR = '../data/'
    TEMP_FILE = '../data/TEMPORARY_FILE'

    def __init__(self):
        self.make_fragments()

    def make_fragments(self):

        counter = 0

        with open(self.TEMP_FILE, 'r') as temp:
            for chunk in temp.read(512):
                if chunk:
                    temp_name = '../data/send/fragment' + str(counter)
                    counter = counter + 1
                    with open(temp_name, 'w') as out_file:
                        out_file.write(chunk)
                if not chunk:
                    break


if __name__ == '__main__':
    ob = Fragment()

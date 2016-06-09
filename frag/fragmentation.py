import os
from functools import partial

class Fragment:

	# DATA_DIR = '../data/'
	TEMP_FILE = '../data/TEMPORARY_FILE'

	def __init__(self):
		self.make_fragments()

	def make_fragments(self):

		counter = 0

		with open(self.TEMP_FILE, 'rb+') as temp:
			temp_name = '../data/send/fragment'+str(counter)
			with open(temp_name, 'wb') as out_file:
				for chunk in iter(partial(temp.read, 512), ''):
					out_file.write(chunk)
		# return True

				
if __name__ == '__main__':
	ob = Fragment()
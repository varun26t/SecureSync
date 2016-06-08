import os
import sys
import numpy as np

BLOCK = 512
DATA = os.path.join(os.path.join('/data/send/'))

def make_fragments(data, number):

	if(number > 0 ):
		temp = number
		while temp > 0:
			temp = temp - 1
			file = open(data)


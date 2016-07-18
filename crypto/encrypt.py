from Crypto.PublicKey import ElGamal
from Crypto import Random
import os

KEY = ''
BLOCK = None
K = Random.new()

osRandomKey = os.urnadom(24)

class Encrypt:
	def __init__(self, key):
		self.KEY = key


	def encrypt(self, absPath):
		return False

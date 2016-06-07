from Crypto.PublicKey import ElGamal
from Crypto import Random

KEY = ''
BLOCK = None
K = Random.new()

class Encrypt:
	def __init__(self, key):
		self.KEY = key


	def encrypt(self, absPath):
		return False

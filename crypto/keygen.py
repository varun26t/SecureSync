#!/usr/bin/python3
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal

def get_key():
	key = ElGamal.generate(1024, Random.new().read)
	return key

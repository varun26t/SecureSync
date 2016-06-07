#!/usr/bin/python3
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import ElGamal
from base64 import b64encode
def get_key():
	key = ElGamal.generate(256, get_random_bytes)
	comps = ('p','g','y','x')
	out = '\n'.join(["{} = {}".format(comp,getattr(key, comp)) for comp in comps])
	with open('./key', 'w+') as k:
		k.write(out)
	return key

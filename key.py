
key_pair = {}

def set_key(user, pub_key, priv_key):
	key_pair.update({ user: [pub_key, priv_key], })
	return True

def rertive_key(user):
	key_array = key_pair.get(user)
	return key_array
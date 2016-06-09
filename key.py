import pymongo
from datetime import datetime

class databaseCon:

	user_data = {}
	__collections = ''

	def __init__():
		client = pymongo.MongoClient("localhost", 27017)
		db = client.sync
		collections = db.users

	def __init__(self, user, y, x):
		client = pymongo.MongoClient("localhost", 27017)
		db = client.sync
		collections = db.users
		self.user_data = {
			'user': {}
				'username': user
				'pub_key': y
				'priv_key': x
				'datetime': datetime.utcnow()
			},
		}

	def insertinto(self):
		self.collections.insert_one(self.user_data)

		
	def finduser(self, username):
		key_dict = self.collections.find_one({{'username':username}})
		return key_dict





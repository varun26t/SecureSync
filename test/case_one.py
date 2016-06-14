from base64 import b64encode, b64decode

FILE = '../requirements.txt'
TEMP_FILE = '../data/TEMPORARY_FILE'

with open(FILE, 'rb+') as file:
	with open(TEMP_FILE, 'wb+') as out_file:
		file_bytes = b64encode(file.read())
		# print(file_bytes)
		out_file.write(file_bytes)
		print("Success")


with open(TEMP_FILE, 'rb+') as damn:
	with open('../data/temp', 'wb+') as dam:
		bt = b64decode(damn.read())
		# print(bt)
		dam.write(bt)
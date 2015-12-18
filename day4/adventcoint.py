
from hashlib import md5

SECRET_KEY = "ckczppom"

def find_hash():

	num = 0
	secret_hash = md5()
	secret_hash.update(SECRET_KEY)
	while True:
		current_hash = secret_hash.copy()
		current_hash.update(str(num))
		if current_hash.hexdigest().startswith("000000") or :
			print num
		num += 1

if __name__ == '__main__':
	find_hash()
	

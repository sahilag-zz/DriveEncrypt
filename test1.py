import os,sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
import Crypto.Util.Counter

		
def encrypt(key, filename):
	
	mac = HMAC.new(key, digestmod = SHA256)
	mac.update('hellooo')
	
	tag = mac.digest()
	print tag

	
	mac = HMAC.new(key, digestmod = SHA256)
	mac.update('hello')
	
	tag = mac.digest()
	print tag
	mac.update('oo')
	tag = mac.digest()
	print tag

	

 
	
def main(filename):

	key = os.urandom(32) # random key
	
	encrypt(key, filename)

if  __name__ =='__main__':
	main(sys.argv[1])









import os,sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
import Crypto.Util.Counter

		
def encrypt(key, filename, chunksize = 1024):
	
	key1 = key[:16]; key2 = key[16:]
	encfilename = filename + '.enc'

	iv = os.urandom(16) # random IV
	
	# counter for symmetric encryption in CTR mode
	ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
	cipher = AES.new(key1, AES.MODE_CTR, counter = ctr)
	mac = HMAC.new(key2, digestmod = SHA256)
	mac.update(iv)
	with open(filename, 'rb') as infile:
		with open(encfilename, 'wb') as outfile:
			outfile.write(iv)

			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0: break
				enc_chunk = cipher.encrypt(chunk)
				mac.update(enc_chunk)
				outfile.write(enc_chunk)
			outfile.write(mac.digest())
	return encfilename

    
def decrypt(key, encfilename, chunksize = 1024):

	key1 = key[:16]; key2 = key[16:]	
	
	outfilename = encfilename[:len(encfilename)-4]
	
	# reading tag
	f = open(encfilename, 'rb+') 
	f.seek(-32, os.SEEK_END)
	tag = f.read()
	f.seek(-32, os.SEEK_END) 
	f.truncate() 
	f.close()
	
	with open(encfilename, 'rb') as infile:
		#first 16 bytes of encrypted text is IV
		iv = infile.read(16)
		ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
		obj = AES.new(key1, AES.MODE_CTR, counter = ctr)
		mac = HMAC.new(key2, digestmod = SHA256)
		mac.update(iv)
		with open(outfilename, 'wb') as outfile:
		
			while True:
			
				chunk = infile.read(chunksize)
				if len(chunk) == 0: break

				outfile.write(obj.decrypt(chunk))
				
				mac.update(chunk) 
		
		outfile.close()			
		if (tag != mac.digest()):	
			f.open(outfilename, 'wb')
			f.write("error")
			
	
def main(filename):

	key = os.urandom(32) # random key
	
	encfilename = encrypt(key, filename)
	decrypt(key, encfilename)

if  __name__ =='__main__':
	main(sys.argv[1])









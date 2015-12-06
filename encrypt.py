import os,sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
import Crypto.Util.Counter

def readfile(filename, option):

	fo = open(filename, option)
	inread = fo.read()
	fo.close()
	return inread

def writefile(filename, option, outwrite):

	fo = open(filename, option) 
	fo.write(outwrite)
	fo.close()
		
def encrypt(plaintext, filename):
	
	key = os.urandom(16) # random key
    
	iv = os.urandom(16) # random IV
	
	# counter for symmetric encryption in CTR mode
	ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
	
	cipher = AES.new(key, AES.MODE_CTR, counter = ctr)
	ciphertext = cipher.encrypt(plaintext)
	
	mac = HMAC.new(key, digestmod = SHA256)
	mac.update(ciphertext)
	tag = mac.digest()

	encfilename = filename + '.enc'
	writefile(encfilename, 'wb',iv + ciphertext + tag)

	return key, encfilename

    
def decrypt(key, encfilename):

	
	enctext = readfile(encfilename, 'rb')
	
	#first 16 bytes of encrypted text is IV
	iv = enctext[0:16]
	#last 32 bytes is tag
	tag = enctext[len(enctext)-32:]
	#rest is ciphertext
	ciphertext = enctext[16:len(enctext)-32]
	
	ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
	obj = AES.new(key, AES.MODE_CTR, counter = ctr)
	
	mac = HMAC.new(key, digestmod = SHA256)
	mac.update(ciphertext)
	
	if (tag == mac.digest()):	
	
		dectext = obj.decrypt(ciphertext)
		#print "decryptedtext = ", dectext, len(dectext)
	
		writefile(encfilename[:len(encfilename)-4], 'wb', dectext) # removing ".enc"

	else:
		print "error"
	
def main(filename):

	plaintext = readfile(filename, 'rb')
	
	key, encfilename = encrypt(plaintext, filename)
	decrypt(key, encfilename)

if  __name__ =='__main__':
	main(sys.argv[1])









import os,sys
from Crypto.Cipher import AES
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
		
def encrypt(plaintext, filename, key):
	
	#key = os.urandom(16) # random key
    
	iv = os.urandom(16) # random IV
	
	# counter for symmetric encryption in CTR mode
	ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
	
	obj = AES.new(key, AES.MODE_CTR, counter = ctr)
	ciphertext = obj.encrypt(plaintext)
	
	encfilename = filename + '.enc'

	writefile(encfilename, 'wb',iv + ciphertext) # pass IV with encrypted text
	#print "ciphertext = ", ciphertext, len(ciphertext)
	return encfilename

    
def decrypt(key, encfilename):

	
	enctext = readfile(encfilename, 'rb')
	
	#first byte of encrypted text is IV
	iv = enctext[0:16]
	#rest is ciphertext
	ciphertext = enctext[16:]
	
	ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))
	obj = AES.new(key, AES.MODE_CTR, counter = ctr)
	
	dectext = obj.decrypt(ciphertext)
	#print "decryptedtext = ", dectext, len(dectext)
	
	writefile(encfilename[:len(encfilename)-4], 'wb', dectext) # removing ".enc"

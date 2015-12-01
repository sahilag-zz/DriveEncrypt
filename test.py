fo = open('test.txt', 'rb')

print "Name of the file: ", fo.name


line = fo.read()
print "Read Line: %s" % (line), len(line)

fo.close()

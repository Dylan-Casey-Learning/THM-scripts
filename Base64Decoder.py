#!/usr/bin/python
# -*- coding: utf-8 -*-

# import base64 module
import base64

# for the THM room the text file was encoded 15 times 5 each for base64,32,16
# define three functions
def B64(encoded):
    decoded = base64.b64decode(encoded)
    return decoded


def B32(encoded):
    decoded = base64.b32decode(encoded)
    return decoded


def B16(encoded):
    decoded = base64.b16decode(encoded)
    return decoded

# read file containing base64 code
encodedfile= open('base64.txt', 'rb').read()

#for loops for each base65, base32, base16
for i in range(5):
    encodedflag = B64(encodedfile)

for i in range(5):
    encodedflag = B32(encodedfile)

for i in range(5):
    if i != 4:
        encodedflag = B16(encodedfile)
    else:
        encodedflag = B16(encodedfile)
        print ('The flag is:', encodedfile)
# close file
encodedfile.close()

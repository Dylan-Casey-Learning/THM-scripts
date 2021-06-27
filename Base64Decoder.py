#!/usr/bin/python
# -*- coding: utf-8 -*-

# import base64 module
import base64

# for the THM room the text file was encoded 15 times 5 each for base64,32,16
# define three functions
def b64d(encoded):
    decoded = base64.b64decode(encoded)
    return decoded


def b32d(encoded):
    decoded = base64.b32decode(encoded)
    return decoded


def b16d(encoded):
    decoded = base64.b16decode(encoded)
    return decoded

# read file containing base64 code
encodedfile= open('base64.txt', 'rb').read()

#for loops for each base65, base32, base16
for i in range(5):
    encodedflag = b64d(encodedfile)

for i in range(5):
    encodedflag = b32d(encodedfile)

for i in range(5):
    if i != 4:
        encodedflag = b16d(encodedfile)
    else:
        encodedflag = b16d(encodedfile)
        print ('The flag is:', encodedfile)
# close file
encodedfile.close()
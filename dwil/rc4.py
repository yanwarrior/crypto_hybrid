#-------------------------------------------------------------------------------
# Name:        rc4
# Purpose:      thanks to emoticodes, we are love python
#
# Author:      neng dwil
#
# Created:     11/11/2014
# Copyright:   -
# Licence:     Free Licence For develop and learning
#-------------------------------------------------------------------------------

def rc4_crypt( data , key ):
    S = range(256)
    j = 0
    out = []

    #KSA Phase
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]

    #PRGA Phase
    i = j = 0
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

'''
## uji
kunci = "yanwarsolahudin"
with open(r'D:\uji\enkripsi file\enkripsi-dok1.doc.doc', 'rb') as f:
    data = f.read()

enkrip = rc4_crypt(data,kunci)

with open("D:/test.doc","wb") as h:
    h.write(enkrip)
'''

#-------------------------------------------------------------------------------
# Name:        module RSA
# Purpose:
#
# Author:      neng dwil
#
# Created:     11/11/2014
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import gmpy
import random
import time


class RSA:
    def generate_kunci(self, int_length):
        ## set waktu mulai
        self.__waktu_mulai = time.time()

        ## set panjang kunci
        panjang_kunci = int_length

        ## set minimal dan maksimal untuk generate kunci
        minimal = int("1" + str("0" * (panjang_kunci -1 )))
        maksimal = int("9" * panjang_kunci)

        ## set bilangan prima P
        self.__p = gmpy.next_prime(random.randrange(minimal,maksimal))

        ## set bilangan prima Q
        self.__q = gmpy.next_prime(random.randrange(minimal,maksimal))

        ## set bilangan modulo N
        self.__n = gmpy.mul(self.__p, self.__q)

        ## set bilangan PHI
        tp = gmpy.sub(self.__p, gmpy.mpz(1))    # (p - 1)
        tq = gmpy.sub(self.__q, gmpy.mpz(1))    # (q - 1)
        self.__phi = gmpy.mul(tp,tq)

        ## set bilangan Eksponen E
        self.__e = 0
        limit = random.randrange(gmpy.mpz(self.__phi)/2)
        while True:
            limit = limit + 1
            self.__e = gmpy.gcd(limit,gmpy.mpz(self.__phi))
            if self.__e == 1:
                self.__e = limit
                break

        ## set bilangan Eksponen D
        self.__d = gmpy.invert(self.__e, self.__phi)

        ## set waktu akhir
        self.__waktu_selesai = time.time() - self.__waktu_mulai

        hasil_kunci = [self.__p, self.__q, self.__n, self.__phi, self.__e, self.__d]

        ## kembalikan nilai kedalam bentuk string
        ## di karenakan bilangan cukup besar
        ## dan harus di kalkulasi sebagai objek
        ## yang dimulai dari objek init string
        return [str(i) for i in hasil_kunci]


    def enkripsi(self, str_data, int_n, int_e):
        '''return list numerik chiper'''
        ## set waktu mulai
        self.__waktu_mulai = time.time()

        ## set bilangan n dan e
        self.__modulo_n = int_n
        self.__eksponen_e = int_e

        ## ubah blok str_data menjadi blok ascii
        blok_ascii = [ord(i) for i in str_data]

        ## enkripsi blok ascii menjadi chiper
        chiper = [(int(gmpy.digits(gmpy.powmod(gmpy.mpz(i),
        gmpy.mpz(self.__eksponen_e), gmpy.mpz(self.__modulo_n))))) \
        for i in blok_ascii]

        self.__waktu_selesai = time.time() - self.__waktu_mulai

        return chiper

    def dekripsi(self, list_chiper, int_n, int_d):
        '''return plaintext string'''
        ## set Modulo N dan Eksponen D
        self.__modulo_n = int_n
        self.__eksponen_d = int_d

        ## set waktu mulai
        self.__waktu_mulai = time.time()

        ## dekripsi blok chiper
        plain = [(int(gmpy.digits(gmpy.powmod(gmpy.mpz(i), \
        gmpy.mpz(self.__eksponen_d), gmpy.mpz(self.__modulo_n))))) \
        for i in list_chiper]

        self.__waktu_selesai = time.time() - self.__waktu_mulai

        ## set block dengan character
        plain = [chr(i) for i in plain]

        ## join plain ke text
        return "".join(plain)

    def get_waktu(self):
        '''return float waktu selesai'''
        return self.__waktu_selesai






## cara generate kunci
'''
rsa = RSA()
print rsa.generate_kunci(50)
'''

'''
## cara enkripsi
enkripsi = RSA()
enkripsi.enkripsi("Yanwar Solahudin", 3233, 17)
'''
'''
## cara dekripsi
chiper = [99, 1632, 2235, 1107, 1632, 2412, 1992, 2680, 2185, 745, 1632, 2170, 2160, 1773, 3179, 2235]
dekripsi = RSA()
print dekripsi.dekripsi(chiper,3233,2753)
print dekripsi.get_waktu()
'''

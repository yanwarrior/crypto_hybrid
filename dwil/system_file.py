#-------------------------------------------------------------------------------
# Name:        SystemFile
# Purpose:
#
# Author:      neng dwil
#
# Created:     11/11/2014
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class System_File:

    def buat_file_kunci_publik(self, string_id, string_n, string_e, \
    string_direktori):
        '''membuat kunci publik- return path file'''

        ## catatan
        ## kunci dimulai index ke 0
        ## dimana index 0 = id dari kunci
        ## index 1 = nilai modulo n
        ## index 2 = nilai eksponen e
        string_id = str(string_id)
        string_n = str(string_n)
        string_e = str(string_e)
        key_file = string_direktori + string_id + "_publik.key"
        with open(key_file, "wb") as f:
            f.write(string_id)
            f.write("\n")
            f.write(string_n)
            f.write("\n")
            f.write(string_e)

        return key_file

    def buat_file_kunci_private(self, string_id, string_n, string_d, \
    string_direktori):
        '''membuat kunci private- return path file'''

        ## catatan
        ## kunci dimulai index ke 0
        ## dimana index 0 = id dari kunci
        ## index 1 = nilai modulo n
        ## index 2 = nilai eksponen d
        string_id = str(string_id)
        string_n = str(string_n)
        string_d = str(string_d)
        key_file = string_direktori + string_id + "_private.key"
        with open(key_file,"wb") as f:
            f.write(string_id)
            f.write("\n")
            f.write(string_n)
            f.write("\n")
            f.write(string_d)
        return key_file

    def buat_report_kunci(self, string_id, list_kunci, string_direktori):
        '''digunakan untuk menyimpan semua nilai
        hasil generate kunci untuk melakukan uji coba
        apakah algoritma RSA generate kunci telah benar'''
        ## catatan
        ## index 0 merupakan id kunci
        ## index 1 nilai Prima P
        ## index 2 nilai Prima Q
        ## index 3 nilai Modulo N
        ## index 4 nilai PHI
        ## index 5 nilai Eksponen E
        ## index 6 nilai Eksponen D
        key_uji = string_direktori + string_id + ".txt"
        with open(key_uji, "wb") as f:
            f.write("ID Kunci \t: " + string_id)
            f.write("\n")
            f.write("Prima P \t: " + list_kunci[0])
            f.write("\n")
            f.write("Prima Q \t: " + list_kunci[1])
            f.write("\n")
            f.write("Modulo N \t: " + list_kunci[2])
            f.write("\n")
            f.write("PHI \t\t: " + list_kunci[3])
            f.write("\n")
            f.write("Eksponen E \t: " + list_kunci[4])
            f.write("\n")
            f.write("Eksponen D \t: " + list_kunci[5])
        return key_uji

    def buat_file_session_key(self,string_chiper_key, string_direktori):
        '''dengan syarat session key harus sudah di enkripsi
        dengan kunci publik RSA inilah hybrid method'''
        session_key_file = string_direktori + "session.key"
        with open(session_key_file, "wb") as f:
            f.write(string_chiper_key)
        return session_key_file

    def baca_kunci_rsa(self, filekunci):
        '''mengembalikan nilai list yang terdiri dari :
        >> id kunci
        >> modulo
        >> eksponen'''
        eksponen = ""
        modulo = ""
        id_kunci = ""
        kunci = ""
        with open(filekunci, "rb") as f:
            kunci = f.readlines()

        id_kunci = kunci[0]
        modulo = kunci[1]
        eksponen = kunci[2]
        return [id_kunci, modulo, eksponen]

    def get_binary_file(self, filename):
        '''untuk membaca dan mengambalikan binary file'''
        with open(filename, "rb") as f:
            data = f.read()
        return data

    def create_file_rc4(self, filename, data):
        with open(filename, "wb") as f:
            f.write(data)



'''
## cara membuat file kunci publik
sistem_file = SystemFile()
print sistem_file.buat_file_kunci_publik("zen","3233","17","D:/")
'''

'''
## cara membuat file kunci private
sistem_file = SystemFile()
print sistem_file.buat_file_kunci_private("zen","3233","2753","D:/")
'''
'''
## cara membuat file uji kunci
sistem_file = SystemFile()
list_kunci = [\
'80601818204110043010927307380968927102050659296261', \
'52884000971577806746253657277147459106031751575683', \
'4262546632217093265099377112662429213481431249644710677864582612730416101930586307575811278660421263', \
'4262546632217093265099377112662429213481431249644577192045406924880658920965928191189603196249549320', \
'29639761235456150453856125152504077661669288886028991083162913022859503162187119471702306781760421', \
'122838589374590635755178617919618206312626118756916609671904032989302802065341603980439021447656021'\
]
sistem_file.buat_report_kunci("zen",list_kunci,"D:/")
'''




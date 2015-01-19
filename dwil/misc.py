import EasyDialogs
import os
import random
import string
import wx
import os.path

def get_dir():
    filename = EasyDialogs.AskFolder(
    message='Name the destination',
    defaultLocation=os.getcwd(),
    wanted=unicode,
    )

    path = filename
    if len(path) == 3:
        return path.replace('\\','/')
    else:
        return path.replace('\\','/') + '/'

def get_file(list_allow_file):
    '''get file berdasarkan saringan tertentu,
    thanks to : http://www.java2s.com/Tutorial/Python/0380__wxPython/ChooseafilefromFileDialog.htm'''
    #app = wx.PySimpleApp()
    wildcard = ""
    limit_wildcard = len(list_allow_file)
    for index,i in enumerate(list_allow_file):
        if index < limit_wildcard:
            wildcard += i + " Source (*." + i + ")|*." + i + "|"
        else:
            break
    '''wildcard = "Python source (*.py)|*.py| Compiled Python (*.pyc)|*.pyc|" \
            "All files (*.*)|*.*"'''
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.GetPath().replace("\\","/")
    dialog.Destroy()

def prompt():
    response = EasyDialogs.AskString('Keti ID Kunci', default='myIdKey')
    return response

def random_key():
    '''Generating random text strings of a given pattern
    Thanks To : http://stackoverflow.com/questions/367586/generating-random-text-strings-of-a-given-pattern'''
    digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
    chars = "".join( [random.choice(string.letters) for i in xrange(8)] )
    return digits + chars

def baca_ukuran_file(filename):
    '''membaca ukuran file dengan mode megabyte,
    mengembalikan nilai integer berupa ukuran file
    dalam megabyte'''
    statinfo = os.stat(filename)
    return int(statinfo.st_size / 1024)

def ambil_ekstensi_file(filename):
    ''' mengambil ekstensi file'''
    return os.path.splitext(filename)[1]

def ambil_nama_file(filename):
    return os.path.basename(filename)



'''
# cara menggunakan get_file
allow_ext = ['doc','docx','xls','py','key']
print get_file(allow_ext)
'''



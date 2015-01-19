#-------------------------------------------------------------------------------
# Name:        connectivity
# Purpose:      thanks a lot by : http://stackoverflow.com/questions/20913411/
#               test-if-an-internet-connection-is-present-in-python
#
# Author:      neng dwil
#
# Created:     13/11/2014
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

def is_connected():
    '''untuk mengecek konektivitas internet,
    mengembalikan nilai true jika konek ke internet,
    begitupun sebaliknya.'''
    REMOTE_SERVER = "www.google.com"
    try:
        # mendapatkan nama host dari google
        host = socket.gethostbyname(REMOTE_SERVER)
        # membuat sambungan koneksi host dengan port 80
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

'''
print is_connected()
'''
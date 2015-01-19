#-------------------------------------------------------------------------------
# Name:        mail_sender
# Purpose:
#
# Author:      neng dwil
#
# Created:     12/11/2014
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import smtplib
import base64
import wx

def sendMail(filename,sender, reciever, username, password, subject, msg, smtp, port):
    # Read a file and encode it into base64 format
    try:
        fo = open(filename, "rb")
        filecontent = fo.read()
        encodedcontent = base64.b64encode(filecontent)  # base64

        smtp = smtp + ":" + str(port)
        marker = "AUNIQUEMARKER"

        body = subject + "\n\n" + msg

        # Define the main headers.
        part1 = "From: From Person <%s>\nTo: To Person <%s>\nSubject: Sending \
        Attachement\nMIME-Version: 1.0\nContent-Type: \
        multipart/mixed; boundary=%s\n--%s\n" % \
        (sender,sender,marker, marker)

        # Define the message action
        part2 = "Content-Type: text/plain\nContent-Transfer-Encoding:\
        8bit\n\n%s\n--%s\n" % (body,marker)

        # Define the attachment section
        part3 = "Content-Type: multipart/mixed; \
        name=\"%s\"\nContent-Transfer-Encoding:base64\n\
        Content-Disposition: attachment; filename=%s\n\n%s\n--%s--\n" %\
        (filename, filename, encodedcontent, marker)

        message = part1 + part2 + part3

        try:
           server = smtplib.SMTP(smtp)
           server.starttls()
           server.login(username,password)
           server.sendmail(sender, reciever, message)
           server.quit()
           pesan = "Email Berhasil di kirim ke " + reciever
           notif = wx.MessageDialog(None, pesan, "Berhasil", \
           wx.ICON_INFORMATION)
           notif.ShowModal()
           return True
        except Exception:
            pesan = "Email Gagal Dikirm"
            notif = wx.MessageDialog(None, pesan, "Warning", \
            wx.ICON_INFORMATION)
            notif.ShowModal()
            return False
    except:
        pesan = "Terjadi kesalahan saat mengirim email"
        notif = wx.MessageDialog(None, pesan, "Warning", \
        wx.ICON_INFORMATION)
        notif.ShowModal()

'''
## cara menggunakan
filename = "D:/page.png"
sender = "solahudinyanwar@gmail.com"
reciever = "solahudinyanwar@gmail.com"
username = "solahudinyanwar@gmail.com"
password = "GueAnakBetawiAsli786"
subject = "Only Example Subject"
msg = "Only Example Body Message"
smtp = "smtp.gmail.com"
port = 587
sendMail(filename,sender, reciever, username, password, subject, msg, smtp, port)
'''











#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameMain

modules ={u'FrameDekripsi': [0, '', u'FrameDekripsi.py'],
 u'FrameDekripsiDanKonversi': [0, '', u'FrameDekripsiDanKonversi.py'],
 u'FrameEmail': [0, '', u'FrameEmail.py'],
 u'FrameEnkripsi': [0, '', u'FrameEnkripsi.py'],
 u'FrameGenerateKunci': [0, '', u'FrameGenerateKunci.py'],
 u'FrameMain': [1, 'Main frame of Application', u'FrameMain.py'],
 u'FrameTentangAplikasi': [0, '', u'FrameTentangAplikasi.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameMain.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()

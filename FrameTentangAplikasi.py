#Boa:Frame:Frame1

import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPBUTTON1, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, 
] = [wx.NewId() for _init_ctrls in range(16)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(456, 191), size=wx.Size(543, 396),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Tentang Aplikasi')
        self.SetClientSize(wx.Size(527, 358))
        self.SetIcon(wx.Icon(u'images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(527, 358),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Aplikasi Keamanan Dokumen', name='staticText1',
              parent=self.panel1, pos=wx.Point(134, 24), size=wx.Size(306, 25),
              style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 128, 192))
        self.staticText1.Enable(True)

        self.genBitmapButton1 = wx.lib.buttons.GenBitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPBUTTON1, name='genBitmapButton1',
              parent=self.panel1, pos=wx.Point(40, 24), size=wx.Size(72, 72),
              style=wx.NO_BORDER)
        self.genBitmapButton1.SetBitmapDisabled(wx.Bitmap(u'images/Extras-Security-icon.png',
              wx.BITMAP_TYPE_PNG))
        self.genBitmapButton1.Enable(False)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(129, 56),
              size=wx.Size(319, 2), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Dwi Kurnianingsih - Tugas Akhir', name='staticText2',
              parent=self.panel1, pos=wx.Point(128, 64), size=wx.Size(150, 13),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Universitas Budiluhur', name='staticText3',
              parent=self.panel1, pos=wx.Point(128, 80), size=wx.Size(101, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'V. 1.0.0', name='staticText4', parent=self.panel1,
              pos=wx.Point(408, 64), size=wx.Size(40, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Tentang Aplikasi :', name='staticText5',
              parent=self.panel1, pos=wx.Point(40, 128), size=wx.Size(109, 14),
              style=0)
        self.staticText5.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'aplikasi kriptografi menggunakan metode hybrid \ndengan Algoritma Asimetrus RSA dan Simetris RC4.',
              name='staticText6', parent=self.panel1, pos=wx.Point(40, 152),
              size=wx.Size(246, 26), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Fitur Tambahan :', name='staticText7', parent=self.panel1,
              pos=wx.Point(40, 200), size=wx.Size(103, 14), style=0)
        self.staticText7.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'fitur tambahan pada aplikasi ini adalah\ndapat mengkonversi dari file enkripsi excel\nke database mysql.\n\npengiriman kunci publik atau \nfile yang telah di enkripsi beserta\nkunci sesinya melalui email.',
              name='staticText8', parent=self.panel1, pos=wx.Point(40, 224),
              size=wx.Size(203, 91), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Batasan Jenis File :', name='staticText9',
              parent=self.panel1, pos=wx.Point(312, 128), size=wx.Size(114, 14),
              style=0)
        self.staticText9.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'jenis file yang digunakan adalah\nfile berekstensi gambar dan dokumen\ndengan batasan ukuran file kurang\ndari 5 Mb.',
              name='staticText10', parent=self.panel1, pos=wx.Point(312, 152),
              size=wx.Size(178, 52), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Versi Aplikasi :', name='staticText11',
              parent=self.panel1, pos=wx.Point(312, 224), size=wx.Size(88, 14),
              style=0)
        self.staticText11.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Versi 1.0.0', name='staticText12', parent=self.panel1,
              pos=wx.Point(312, 248), size=wx.Size(53, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

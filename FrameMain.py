#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import FrameGenerateKunci
import FrameEnkripsi
import FrameDekripsi
import FrameEmail
import FrameDekripsiDanKonversi
import FrameTentangAplikasi

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPBUTTON1, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(6)]

[wxID_FRAME1MENUHYBRIDDEKRIPSI, wxID_FRAME1MENUHYBRIDENKRIPSI, 
] = [wx.NewId() for _init_coll_menuHybrid_Items in range(2)]

[wxID_FRAME1MENUBANTUANKELUAR, wxID_FRAME1MENUBANTUANTENTANGAPLIKASI, 
] = [wx.NewId() for _init_coll_menuBantuan_Items in range(2)]

[wxID_FRAME1MENUEMAILKIRIMEMAIL] = [wx.NewId() for _init_coll_menuEmail_Items in range(1)]

[wxID_FRAME1MENURSAGENERATEKUNCI] = [wx.NewId() for _init_coll_menuRSA_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBantuan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUBANTUANTENTANGAPLIKASI,
              kind=wx.ITEM_NORMAL, text=u'Tentang Aplikasi')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_FRAME1MENUBANTUANKELUAR,
              kind=wx.ITEM_NORMAL, text=u'Keluar')
        self.Bind(wx.EVT_MENU, self.OnMenuBantuanTentangaplikasiMenu,
              id=wxID_FRAME1MENUBANTUANTENTANGAPLIKASI)
        self.Bind(wx.EVT_MENU, self.OnMenuBantuanKeluarMenu,
              id=wxID_FRAME1MENUBANTUANKELUAR)

    def _init_coll_menuRSA_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENURSAGENERATEKUNCI,
              kind=wx.ITEM_NORMAL, text=u'Generate Kunci RSA')
        self.Bind(wx.EVT_MENU, self.OnMenuRSAGeneratekunciMenu,
              id=wxID_FRAME1MENURSAGENERATEKUNCI)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuRSA, title=u'RSA')
        parent.Append(menu=self.menuHybrid, title=u'Hybrid')
        parent.Append(menu=self.menuEmail, title=u'Email')
        parent.Append(menu=self.menuBantuan, title=u'Bantuan')

    def _init_coll_menuEmail_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUEMAILKIRIMEMAIL,
              kind=wx.ITEM_NORMAL, text=u'Kirim Email')
        self.Bind(wx.EVT_MENU, self.OnMenuEmailKirimemailMenu,
              id=wxID_FRAME1MENUEMAILKIRIMEMAIL)

    def _init_coll_menuHybrid_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUHYBRIDENKRIPSI,
              kind=wx.ITEM_NORMAL, text=u'Enkripsi Hybrid')
        parent.Append(help='', id=wxID_FRAME1MENUHYBRIDDEKRIPSI,
              kind=wx.ITEM_NORMAL, text=u'Dekripsi Hybrid')
        self.Bind(wx.EVT_MENU, self.OnMenuHybridEnkripsiMenu,
              id=wxID_FRAME1MENUHYBRIDENKRIPSI)
        self.Bind(wx.EVT_MENU, self.OnMenuHybridDekripsiMenu,
              id=wxID_FRAME1MENUHYBRIDDEKRIPSI)

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menuRSA = wx.Menu(title='')

        self.menuHybrid = wx.Menu(title='')

        self.menuEmail = wx.Menu(title='')

        self.menuBantuan = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menuRSA_Items(self.menuRSA)
        self._init_coll_menuHybrid_Items(self.menuHybrid)
        self._init_coll_menuEmail_Items(self.menuEmail)
        self._init_coll_menuBantuan_Items(self.menuBantuan)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(503, 215), size=wx.Size(663, 480),
              style=wx.TRANSPARENT_WINDOW | wx.SYSTEM_MENU | wx.DEFAULT_FRAME_STYLE | wx.MINIMIZE_BOX,
              title=u'Hybrid - Menu Utama')
        self._init_utils()
        self.SetClientSize(wx.Size(647, 442))
        self.SetAutoLayout(False)
        self.Center(wx.BOTH)
        self.SetWindowVariant(wx.WINDOW_VARIANT_SMALL)
        self.SetIcon(wx.Icon(u'D:/Pythonizam/Kuliah/Tugas Akhir/Tugas Akhir - Dwi Kurnianingsih/images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))
        self.SetMenuBar(self.menuBar1)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(647, 442),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetForegroundColour(wx.Colour(116, 116, 116))

        self.genBitmapButton1 = wx.lib.buttons.GenBitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPBUTTON1, name='genBitmapButton1',
              parent=self.panel1, pos=wx.Point(185, 52), size=wx.Size(277, 244),
              style=wx.TRANSPARENT_WINDOW | wx.NO_BORDER | wx.NO_3D)
        self.genBitmapButton1.SetBitmapFocus(wx.Bitmap(u'images/System-Security-Firewall-ON-icon.png',
              wx.BITMAP_TYPE_PNG))
        self.genBitmapButton1.SetBitmapDisabled(wx.Bitmap(u'images/secrecy-icon.png',
              wx.BITMAP_TYPE_PNG))
        self.genBitmapButton1.Enable(False)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Aplikasi Keamanan Dokumen', name='staticText1',
              parent=self.panel1, pos=wx.Point(150, 304), size=wx.Size(346, 29),
              style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(66, 114, 166))
        self.staticText1.Center(wx.HORIZONTAL)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'RSA - RC4 - Hybrid Methode   - Dwi Kurnianginsih - Tugas Akhir',
              name='staticText2', parent=self.panel1, pos=wx.Point(151, 336),
              size=wx.Size(344, 14), style=0)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText2.Center(wx.HORIZONTAL)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Universitas Budiluhur', name='staticText3',
              parent=self.panel1, pos=wx.Point(270, 360), size=wx.Size(106, 14),
              style=0)
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Arial'))
        self.staticText3.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        

    def OnMenuRSAGeneratekunciMenu(self, event):
        '''menu untuk memanggil FrameGenerateKunci'''
        frm = FrameGenerateKunci.create(None)
        frm.Show()

    def OnMenuHybridEnkripsiMenu(self, event):
        '''menu untuk memanggil FrameEnkripsi'''
        frm = FrameEnkripsi.create(None)
        frm.Show()

    def OnMenuHybridDekripsiMenu(self, event):
        '''menu untuk memanggil FrameDekripsi'''
        frm = FrameDekripsi.create(None)
        frm.Show()

    def OnMenuHybridDekripsikonversiMenu(self, event):
        '''menu untuk memanggil FrameDekripDanKonversi'''
        frm = FrameDekripsiDanKonversi.create(None)
        frm.Show()

    def OnMenuEmailKirimemailMenu(self, event):
        '''menu untuk memanggil FrameEmail'''
        frm = FrameEmail.create(None)
        frm.Show()

    def OnMenuBantuanTentangaplikasiMenu(self, event):
        '''menu untuk memanggil FrameTentangAplikasi'''
        frm = FrameTentangAplikasi.create(None)
        frm.Show()

    def OnMenuBantuanKeluarMenu(self, event):
        self.Close()

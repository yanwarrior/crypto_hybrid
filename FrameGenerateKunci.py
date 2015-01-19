#Boa:Frame:FrameGenerateKunci

import wx
import wx.richtext
import wx.lib.buttons
import wx.stc
import dwil
import time

def create(parent):
    return FrameGenerateKunci(parent)

[wxID_FRAMEGENERATEKUNCI, wxID_FRAMEGENERATEKUNCIBTN_BERSIH, 
 wxID_FRAMEGENERATEKUNCIBTN_BROWSE_DIR_SIMPAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCIBTN_GENERATE, wxID_FRAMEGENERATEKUNCIPANEL1, 
 wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL1, wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL2, 
 wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL3, 
 wxID_FRAMEGENERATEKUNCISLIDER_KEKUATAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCISTATICBOX2, wxID_FRAMEGENERATEKUNCISTATICBOX3, 
 wxID_FRAMEGENERATEKUNCISTATICBOX4, wxID_FRAMEGENERATEKUNCISTATICBOX5, 
 wxID_FRAMEGENERATEKUNCISTATICTEXT1, wxID_FRAMEGENERATEKUNCISTATICTEXT2, 
 wxID_FRAMEGENERATEKUNCISTATICTEXT3, wxID_FRAMEGENERATEKUNCISTATICTEXT4, 
 wxID_FRAMEGENERATEKUNCISTATICTEXT5, 
 wxID_FRAMEGENERATEKUNCITXT_DIR_SIMPAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCITXT_INFO_DIR_SIMPAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCITXT_INFO_KEKUATAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCITXT_INFO_WAKTU, 
 wxID_FRAMEGENERATEKUNCITXT_KEKUATAN_KUNCI, 
 wxID_FRAMEGENERATEKUNCITXT_KUNCI_PUBLIK, 
] = [wx.NewId() for _init_ctrls in range(24)]

class FrameGenerateKunci(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGENERATEKUNCI,
              name=u'FrameGenerateKunci', parent=prnt, pos=wx.Point(12, 4),
              size=wx.Size(552, 714), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Hybrid - Generate Kunci RSA')
        self.SetClientSize(wx.Size(536, 676))
        self.SetIcon(wx.Icon(u'images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAMEGENERATEKUNCIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(536, 676),
              style=wx.TAB_TRAVERSAL)

        self.txt_kunci_publik = wx.StaticBox(id=wxID_FRAMEGENERATEKUNCITXT_KUNCI_PUBLIK,
              label=u'Kunci Publik : ', name=u'txt_kunci_publik',
              parent=self.panel1, pos=wx.Point(16, 16), size=wx.Size(504, 104),
              style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAMEGENERATEKUNCISTATICBOX2,
              label=u'Kunci Rahasia : ', name='staticBox2', parent=self.panel1,
              pos=wx.Point(16, 136), size=wx.Size(504, 104), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAMEGENERATEKUNCISTATICBOX3,
              label=u'Modulo N : ', name='staticBox3', parent=self.panel1,
              pos=wx.Point(16, 256), size=wx.Size(504, 104), style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAMEGENERATEKUNCISTATICBOX4,
              label=u'Direktori Penyimpana Kunci : ', name='staticBox4',
              parent=self.panel1, pos=wx.Point(16, 376), size=wx.Size(504, 64),
              style=0)

        self.txt_dir_simpan_kunci = wx.TextCtrl(id=wxID_FRAMEGENERATEKUNCITXT_DIR_SIMPAN_KUNCI,
              name=u'txt_dir_simpan_kunci', parent=self.panel1, pos=wx.Point(32,
              400), size=wx.Size(384, 21), style=0, value=u'')
        self.txt_dir_simpan_kunci.SetEditable(False)

        self.btn_browse_dir_simpan_kunci = wx.lib.buttons.GenButton(id=wxID_FRAMEGENERATEKUNCIBTN_BROWSE_DIR_SIMPAN_KUNCI,
              label=u'Browse', name=u'btn_browse_dir_simpan_kunci',
              parent=self.panel1, pos=wx.Point(432, 400), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_dir_simpan_kunci.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_simpan_kunciButton,
              id=wxID_FRAMEGENERATEKUNCIBTN_BROWSE_DIR_SIMPAN_KUNCI)

        self.staticText1 = wx.StaticText(id=wxID_FRAMEGENERATEKUNCISTATICTEXT1,
              label=u'Kekuatan Kunci RSA : ', name='staticText1',
              parent=self.panel1, pos=wx.Point(16, 448), size=wx.Size(107, 13),
              style=0)

        self.slider_kekuatan_kunci = wx.Slider(id=wxID_FRAMEGENERATEKUNCISLIDER_KEKUATAN_KUNCI,
              maxValue=230, minValue=40, name=u'slider_kekuatan_kunci',
              parent=self.panel1, pos=wx.Point(16, 472), size=wx.Size(424, 24),
              style=wx.SL_HORIZONTAL, value=20)
        self.slider_kekuatan_kunci.SetLabel(u'')
        self.slider_kekuatan_kunci.Bind(wx.EVT_COMMAND_SCROLL,
              self.OnSlider_kekuatan_kunciCommandScroll,
              id=wxID_FRAMEGENERATEKUNCISLIDER_KEKUATAN_KUNCI)

        self.txt_kekuatan_kunci = wx.TextCtrl(id=wxID_FRAMEGENERATEKUNCITXT_KEKUATAN_KUNCI,
              name=u'txt_kekuatan_kunci', parent=self.panel1, pos=wx.Point(456,
              472), size=wx.Size(56, 21), style=0, value=u'')
        self.txt_kekuatan_kunci.SetEditable(False)

        self.staticBox5 = wx.StaticBox(id=wxID_FRAMEGENERATEKUNCISTATICBOX5,
              label=u'Informasi : ', name='staticBox5', parent=self.panel1,
              pos=wx.Point(16, 504), size=wx.Size(504, 120), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAMEGENERATEKUNCISTATICTEXT2,
              label=u'Kekuatan Kunci                   : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(24, 528), size=wx.Size(138, 13),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAMEGENERATEKUNCISTATICTEXT3,
              label=u'Direktori Simpan                  :', name='staticText3',
              parent=self.panel1, pos=wx.Point(24, 560), size=wx.Size(136, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAMEGENERATEKUNCISTATICTEXT4,
              label=u'Waktu Pembuatan Kunci     : ', name='staticText4',
              parent=self.panel1, pos=wx.Point(24, 592), size=wx.Size(139, 13),
              style=0)

        self.txt_info_kekuatan_kunci = wx.TextCtrl(id=wxID_FRAMEGENERATEKUNCITXT_INFO_KEKUATAN_KUNCI,
              name=u'txt_info_kekuatan_kunci', parent=self.panel1,
              pos=wx.Point(168, 528), size=wx.Size(136, 21), style=0,
              value=u'')
        self.txt_info_kekuatan_kunci.SetEditable(False)

        self.txt_info_dir_simpan_kunci = wx.TextCtrl(id=wxID_FRAMEGENERATEKUNCITXT_INFO_DIR_SIMPAN_KUNCI,
              name=u'txt_info_dir_simpan_kunci', parent=self.panel1,
              pos=wx.Point(168, 560), size=wx.Size(280, 21), style=0,
              value=u'')
        self.txt_info_dir_simpan_kunci.SetEditable(False)

        self.txt_info_waktu = wx.TextCtrl(id=wxID_FRAMEGENERATEKUNCITXT_INFO_WAKTU,
              name=u'txt_info_waktu', parent=self.panel1, pos=wx.Point(168,
              592), size=wx.Size(100, 21), style=0, value=u'')
        self.txt_info_waktu.SetEditable(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAMEGENERATEKUNCISTATICTEXT5,
              label=u'Detik ', name='staticText5', parent=self.panel1,
              pos=wx.Point(272, 592), size=wx.Size(28, 16), style=0)

        self.btn_generate = wx.Button(id=wxID_FRAMEGENERATEKUNCIBTN_GENERATE,
              label=u'Generate', name=u'btn_generate', parent=self.panel1,
              pos=wx.Point(432, 632), size=wx.Size(83, 32), style=0)
        self.btn_generate.Bind(wx.EVT_BUTTON, self.OnBtn_generateButton,
              id=wxID_FRAMEGENERATEKUNCIBTN_GENERATE)

        self.btn_bersih = wx.Button(id=wxID_FRAMEGENERATEKUNCIBTN_BERSIH,
              label=u'Bersih', name=u'btn_bersih', parent=self.panel1,
              pos=wx.Point(344, 632), size=wx.Size(75, 32), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAMEGENERATEKUNCIBTN_BERSIH)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(40, 40), size=wx.Size(456, 64),
              style=wx.TRANSPARENT_WINDOW | wx.richtext.RE_MULTILINE,
              value=u'')
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.richTextCtrl1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.richTextCtrl1.SetForegroundColour(wx.Colour(0, 128, 0))

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL2,
              parent=self.panel1, pos=wx.Point(40, 160), size=wx.Size(456, 64),
              style=wx.TRANSPARENT_WINDOW | wx.richtext.RE_MULTILINE,
              value=u'')
        self.richTextCtrl2.SetLabel(u'richText')
        self.richTextCtrl2.SetEditable(False)
        self.richTextCtrl2.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.richTextCtrl2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.richTextCtrl2.SetForegroundColour(wx.Colour(128, 0, 0))

        self.richTextCtrl3 = wx.richtext.RichTextCtrl(id=wxID_FRAMEGENERATEKUNCIRICHTEXTCTRL3,
              parent=self.panel1, pos=wx.Point(40, 280), size=wx.Size(456, 64),
              style=wx.TRANSPARENT_WINDOW | wx.richtext.RE_MULTILINE,
              value=u'')
        self.richTextCtrl3.SetLabel(u'richText')
        self.richTextCtrl3.SetEditable(False)
        self.richTextCtrl3.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.richTextCtrl3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.richTextCtrl3.SetForegroundColour(wx.Colour(0, 0, 160))

    def __init__(self, parent):
        self._init_ctrls(parent)
        kekuatan_kunci = self.slider_kekuatan_kunci.GetValue()
        self.txt_kekuatan_kunci.SetValue(str(kekuatan_kunci))
        
    
    def __bersih(self):
        self.txt_dir_simpan_kunci.SetValue("")
        self.txt_info_dir_simpan_kunci.SetValue("")
        self.richTextCtrl1.SetValue("")
        self.richTextCtrl2.SetValue("")
        self.richTextCtrl3.SetValue("")
        self.txt_info_dir_simpan_kunci.SetValue("")
        self.txt_info_kekuatan_kunci.SetValue("")
        self.txt_info_waktu.SetValue("")

    def OnBtn_browse_dir_simpan_kunciButton(self, event):
        '''mencari direktori simpan kunci'''
        path = dwil.get_dir()
        self.txt_dir_simpan_kunci.SetValue(path)

    def OnSlider_kekuatan_kunciCommandScroll(self, event):
        '''scroll kekuatan kunci'''
        kekuatan_kunci = self.slider_kekuatan_kunci.GetValue()
        self.txt_kekuatan_kunci.SetValue(str(kekuatan_kunci))

    def OnBtn_generateButton(self, event):
        ''' tombol generate '''
        if self.txt_dir_simpan_kunci.GetValue() == '':
            notif = wx.MessageDialog(self,"Set direktori yang kosong","Notifikasi",wx.CANCEL)
            notif.ShowModal()
            
        else:
            # menentukan ID KEY
            id_key = dwil.prompt()
            gk = dwil.RSA()
            kekuatan_kunci = self.slider_kekuatan_kunci.GetValue()
            kunci = gk.generate_kunci(int(kekuatan_kunci))
            waktu = gk.get_waktu()
            
            # set richText kunci publik (i=4)
            self.richTextCtrl1.SetValue(kunci[4])
            
            # set richText kunci private (i=5)
            self.richTextCtrl2.SetValue(kunci[5])
            
            # set richText kunci Modulo N (i=2)
            self.richTextCtrl3.SetValue(kunci[2])
            
            # objek simpan kunci
            key = dwil.System_File()
            string_n = self.richTextCtrl3.GetValue()
            string_e = self.richTextCtrl1.GetValue()
            string_d = self.richTextCtrl2.GetValue()
            string_direktori = self.txt_dir_simpan_kunci.GetValue()
            
            # menyimpan kunci publik
            key.buat_file_kunci_publik(id_key, string_n, string_e, string_direktori)
            
            # menyimpan kunci rahasia
            key.buat_file_kunci_private(id_key, string_n, string_d, string_direktori)
            
            # menyimpan kunci testing
            key.buat_report_kunci(id_key, kunci, string_direktori)
            
            # buat notifikasi kalau kunci berhasil di buat dan di simpan
            notifikasi = "Pembuatan Kunci Berhasil, silahkan cek di : " + \
            self.txt_dir_simpan_kunci.GetValue()
            notif = wx.MessageDialog(self,notifikasi,"Notifikasi",wx.CANCEL)
            notif.ShowModal()
            
            # set info kekuatan kunci
            self.txt_info_kekuatan_kunci.SetValue(self.txt_kekuatan_kunci.GetValue() + " Digit Prima")
            
            # set info direktori simpan
            self.txt_info_dir_simpan_kunci.SetValue(self.txt_dir_simpan_kunci.GetValue())
            
            # set info waktu yang dibutuhkan untuk membuat kunci
            self.txt_info_waktu.SetValue(str(gk.get_waktu()))
            

    def OnBtn_bersihButton(self, event):
        '''tombol bersih'''
        self.__bersih()

    
            

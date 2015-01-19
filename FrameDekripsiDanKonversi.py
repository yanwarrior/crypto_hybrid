#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.lib.buttons
import dwil
import MySQLdb
import thread
import time

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_BERSIH, 
 wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI, 
 wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI, 
 wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA, 
 wxID_FRAME1BTN_BROWSE_KUNCI_SESI, wxID_FRAME1BTN_DEKRIPSI_KONVERSI, 
 wxID_FRAME1BTN_KONVERSI, wxID_FRAME1BTN_TES_KONEKSI, 
 wxID_FRAME1CHKBOX_HEADER, wxID_FRAME1CMB_SHEETS, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1RICHTEXTCTRL2, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, wxID_FRAME1STATICBOX4, 
 wxID_FRAME1STATICBOX5, wxID_FRAME1STATICBOX6, wxID_FRAME1STATICBOX7, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, wxID_FRAME1STATICTEXT17, 
 wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL11, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TXT_COLS, wxID_FRAME1TXT_DATABASE, wxID_FRAME1TXT_DIR_DEKRIPSI, 
 wxID_FRAME1TXT_EXCEL_KONVERSI, wxID_FRAME1TXT_FIELDS, 
 wxID_FRAME1TXT_FILE_DEKRIPSI, wxID_FRAME1TXT_FILE_KUNCI_RAHASIA_RSA, 
 wxID_FRAME1TXT_FILE_KUNCI_SESI, wxID_FRAME1TXT_HOST, 
 wxID_FRAME1TXT_INFO_ID_KUNCI, wxID_FRAME1TXT_INFO_WAKTU, 
 wxID_FRAME1TXT_PASSWORD, wxID_FRAME1TXT_ROWS, wxID_FRAME1TXT_TABEL, 
 wxID_FRAME1TXT_USERNAME, 
] = [wx.NewId() for _init_ctrls in range(57)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(10, 6), size=wx.Size(1116, 484),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Hybrid - Dekripsi & Konversi')
        self.SetClientSize(wx.Size(1100, 446))
        self.SetIcon(wx.Icon(u'D:/tawi/images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1100, 446),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Kunci : ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(512, 128), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kunci Rahasia RSA : ', name='staticText1',
              parent=self.panel1, pos=wx.Point(32, 40), size=wx.Size(100, 13),
              style=0)

        self.txt_file_kunci_rahasia_rsa = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_KUNCI_RAHASIA_RSA,
              name=u'txt_file_kunci_rahasia_rsa', parent=self.panel1,
              pos=wx.Point(32, 56), size=wx.Size(400, 21), style=0, value=u'')
        self.txt_file_kunci_rahasia_rsa.SetEditable(False)

        self.btn_browse_file_kunci_rahasia_rsa = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA,
              label=u'Browse', name=u'btn_browse_file_kunci_rahasia_rsa',
              parent=self.panel1, pos=wx.Point(440, 56), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_kunci_rahasia_rsa.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_kunci_rahasia_rsaButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'File Kunci Sesi RC4 : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(32, 88), size=wx.Size(100, 13),
              style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(96, -56), size=wx.Size(100, 21),
              style=0, value='textCtrl2')

        self.txt_file_kunci_sesi = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_KUNCI_SESI,
              name=u'txt_file_kunci_sesi', parent=self.panel1, pos=wx.Point(32,
              104), size=wx.Size(400, 21), style=0, value=u'')
        self.txt_file_kunci_sesi.SetEditable(False)

        self.btn_browse_kunci_sesi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_KUNCI_SESI,
              label=u'Browse', name=u'btn_browse_kunci_sesi',
              parent=self.panel1, pos=wx.Point(440, 104), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_kunci_sesi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_kunci_sesiButton,
              id=wxID_FRAME1BTN_BROWSE_KUNCI_SESI)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Pengaturan MySQL : ', name='staticBox2',
              parent=self.panel1, pos=wx.Point(552, 16), size=wx.Size(200, 272),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Nama Host : ', name='staticText3', parent=self.panel1,
              pos=wx.Point(568, 40), size=wx.Size(63, 13), style=0)

        self.txt_host = wx.TextCtrl(id=wxID_FRAME1TXT_HOST, name=u'txt_host',
              parent=self.panel1, pos=wx.Point(568, 56), size=wx.Size(160, 21),
              style=0, value=u'localhost')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Nama Database : ', name='staticText4', parent=self.panel1,
              pos=wx.Point(568, 88), size=wx.Size(87, 13), style=0)

        self.txt_database = wx.TextCtrl(id=wxID_FRAME1TXT_DATABASE,
              name=u'txt_database', parent=self.panel1, pos=wx.Point(568, 104),
              size=wx.Size(160, 21), style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Username : ', name='staticText5', parent=self.panel1,
              pos=wx.Point(568, 136), size=wx.Size(59, 13), style=0)

        self.txt_username = wx.TextCtrl(id=wxID_FRAME1TXT_USERNAME,
              name=u'txt_username', parent=self.panel1, pos=wx.Point(568, 152),
              size=wx.Size(160, 21), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Kata Sandi MySQL : ', name='staticText6',
              parent=self.panel1, pos=wx.Point(568, 184), size=wx.Size(98, 13),
              style=0)

        self.txt_password = wx.TextCtrl(id=wxID_FRAME1TXT_PASSWORD,
              name=u'txt_password', parent=self.panel1, pos=wx.Point(568, 200),
              size=wx.Size(160, 21), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Nama Tabel : ', name='staticText7', parent=self.panel1,
              pos=wx.Point(568, 232), size=wx.Size(67, 13), style=0)

        self.txt_tabel = wx.TextCtrl(id=wxID_FRAME1TXT_TABEL, name=u'txt_tabel',
              parent=self.panel1, pos=wx.Point(568, 248), size=wx.Size(160, 21),
              style=0, value=u'')

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Informasi Kunci Rahasia : ', name='staticBox3',
              parent=self.panel1, pos=wx.Point(16, 160), size=wx.Size(512, 128),
              style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Modulo N : ', name='staticText8', parent=self.panel1,
              pos=wx.Point(32, 192), size=wx.Size(55, 13), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(32, 208), size=wx.Size(224, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Eksponen D : ', name='staticText9', parent=self.panel1,
              pos=wx.Point(288, 192), size=wx.Size(67, 13), style=0)

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self.panel1, pos=wx.Point(288, 208), size=wx.Size(224, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl2.SetLabel(u'richText')
        self.richTextCtrl2.SetEditable(False)
        self.richTextCtrl2.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'ID Kunci : ', name='staticText10', parent=self.panel1,
              pos=wx.Point(568, 376), size=wx.Size(50, 13), style=0)

        self.txt_info_id_kunci = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_ID_KUNCI,
              name=u'txt_info_id_kunci', parent=self.panel1, pos=wx.Point(568,
              392), size=wx.Size(128, 21), style=0, value=u'')
        self.txt_info_id_kunci.SetEditable(False)
        self.txt_info_id_kunci.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'File dan Direktori : ', name='staticBox4',
              parent=self.panel1, pos=wx.Point(16, 304), size=wx.Size(512, 128),
              style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'File yang akan di dekrip dan konversi : ',
              name='staticText11', parent=self.panel1, pos=wx.Point(32, 328),
              size=wx.Size(187, 13), style=0)

        self.txt_file_dekripsi = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_DEKRIPSI,
              name=u'txt_file_dekripsi', parent=self.panel1, pos=wx.Point(32,
              344), size=wx.Size(400, 21), style=0, value=u'')
        self.txt_file_dekripsi.SetEditable(False)

        self.btn_browse_file_dekripsi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI,
              label=u'Browse', name=u'btn_browse_file_dekripsi',
              parent=self.panel1, pos=wx.Point(440, 344), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_dekripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_dekripsiButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Direktori Penyimpanan Hasil Dekripsi : ',
              name='staticText12', parent=self.panel1, pos=wx.Point(32, 376),
              size=wx.Size(183, 13), style=0)

        self.textCtrl11 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL11,
              name='textCtrl11', parent=self.panel1, pos=wx.Point(-48, -64),
              size=wx.Size(100, 21), style=0, value='textCtrl11')

        self.txt_dir_dekripsi = wx.TextCtrl(id=wxID_FRAME1TXT_DIR_DEKRIPSI,
              name=u'txt_dir_dekripsi', parent=self.panel1, pos=wx.Point(32,
              392), size=wx.Size(400, 21), style=0, value=u'')
        self.txt_dir_dekripsi.SetEditable(False)

        self.btn_browse_dir_simpan_dekripsi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI,
              label=u'Browse', name=u'btn_browse_dir_simpan_dekripsi',
              parent=self.panel1, pos=wx.Point(440, 392), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_dir_simpan_dekripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_simpan_dekripsiButton,
              id=wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI)

        self.staticBox5 = wx.StaticBox(id=wxID_FRAME1STATICBOX5,
              label=u'Info :', name='staticBox5', parent=self.panel1,
              pos=wx.Point(552, 304), size=wx.Size(200, 128), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Nama Sheet : ', name='staticText13', parent=self.panel1,
              pos=wx.Point(808, 88), size=wx.Size(69, 13), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'field : ', name='staticText14', parent=self.panel1,
              pos=wx.Point(824, 168), size=wx.Size(30, 13), style=0)

        self.txt_fields = wx.TextCtrl(id=wxID_FRAME1TXT_FIELDS,
              name=u'txt_fields', parent=self.panel1, pos=wx.Point(824, 184),
              size=wx.Size(224, 21), style=0, value=u'')
        self.txt_fields.SetEditable(False)

        self.btn_dekripsi_konversi = wx.Button(id=wxID_FRAME1BTN_DEKRIPSI_KONVERSI,
              label=u'Dekripsi', name=u'btn_dekripsi_konversi',
              parent=self.panel1, pos=wx.Point(984, 384), size=wx.Size(83, 32),
              style=0)
        self.btn_dekripsi_konversi.Bind(wx.EVT_BUTTON,
              self.OnBtn_dekripsi_konversiButton,
              id=wxID_FRAME1BTN_DEKRIPSI_KONVERSI)

        self.btn_tes_koneksi = wx.Button(id=wxID_FRAME1BTN_TES_KONEKSI,
              label=u'Tes Koneksi', name=u'btn_tes_koneksi', parent=self.panel1,
              pos=wx.Point(888, 384), size=wx.Size(88, 32), style=0)
        self.btn_tes_koneksi.Bind(wx.EVT_BUTTON, self.OnBtn_tes_koneksiButton,
              id=wxID_FRAME1BTN_TES_KONEKSI)

        self.btn_bersih = wx.Button(id=wxID_FRAME1BTN_BERSIH, label=u'Bersih',
              name=u'btn_bersih', parent=self.panel1, pos=wx.Point(808, 384),
              size=wx.Size(72, 32), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAME1BTN_BERSIH)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'Waktu Yang dibutuhkan : ', name='staticText15',
              parent=self.panel1, pos=wx.Point(568, 336), size=wx.Size(125, 13),
              style=0)

        self.txt_info_waktu = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_WAKTU,
              name=u'txt_info_waktu', parent=self.panel1, pos=wx.Point(568,
              352), size=wx.Size(88, 21), style=0, value=u'')
        self.txt_info_waktu.SetEditable(False)
        self.txt_info_waktu.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label=u'Detik', name='staticText16', parent=self.panel1,
              pos=wx.Point(672, 360), size=wx.Size(25, 13), style=0)

        self.cmb_sheets = wx.ComboBox(choices=[], id=wxID_FRAME1CMB_SHEETS,
              name=u'cmb_sheets', parent=self.panel1, pos=wx.Point(808, 104),
              size=wx.Size(248, 21), style=0, value=u'')
        self.cmb_sheets.SetLabel(u'')
        self.cmb_sheets.Bind(wx.EVT_COMBOBOX, self.OnCmb_sheetsCombobox,
              id=wxID_FRAME1CMB_SHEETS)

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label=u'row :', name='staticText17', parent=self.panel1,
              pos=wx.Point(824, 216), size=wx.Size(26, 13), style=0)

        self.txt_rows = wx.TextCtrl(id=wxID_FRAME1TXT_ROWS, name=u'txt_rows',
              parent=self.panel1, pos=wx.Point(824, 232), size=wx.Size(224, 21),
              style=0, value=u'')
        self.txt_rows.SetEditable(False)

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label=u'cols :', name='staticText18', parent=self.panel1,
              pos=wx.Point(824, 272), size=wx.Size(26, 13), style=0)

        self.txt_cols = wx.TextCtrl(id=wxID_FRAME1TXT_COLS, name=u'txt_cols',
              parent=self.panel1, pos=wx.Point(824, 288), size=wx.Size(224, 21),
              style=0, value=u'')
        self.txt_cols.SetEditable(False)

        self.btn_konversi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_KONVERSI,
              label=u'Konversi', name=u'btn_konversi', parent=self.panel1,
              pos=wx.Point(992, 328), size=wx.Size(64, 24), style=0)
        self.btn_konversi.Enable(True)
        self.btn_konversi.Bind(wx.EVT_BUTTON, self.OnBtn_konversiButton,
              id=wxID_FRAME1BTN_KONVERSI)

        self.txt_excel_konversi = wx.TextCtrl(id=wxID_FRAME1TXT_EXCEL_KONVERSI,
              name=u'txt_excel_konversi', parent=self.panel1, pos=wx.Point(808,
              64), size=wx.Size(248, 21), style=0, value=u'')
        self.txt_excel_konversi.SetEditable(False)

        self.staticBox6 = wx.StaticBox(id=wxID_FRAME1STATICBOX6,
              label=u'Compare Data SQL dan Excel : ', name='staticBox6',
              parent=self.panel1, pos=wx.Point(784, 16), size=wx.Size(296, 416),
              style=0)

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label=u'File Excel Yang akan di Konversi : ', name='staticText19',
              parent=self.panel1, pos=wx.Point(808, 48), size=wx.Size(163, 13),
              style=0)

        self.staticBox7 = wx.StaticBox(id=wxID_FRAME1STATICBOX7,
              label=u'Data Excel : ', name='staticBox7', parent=self.panel1,
              pos=wx.Point(808, 144), size=wx.Size(256, 224), style=0)

        self.chkbox_header = wx.CheckBox(id=wxID_FRAME1CHKBOX_HEADER,
              label=u'Field Header Excel', name=u'chkbox_header',
              parent=self.panel1, pos=wx.Point(824, 328), size=wx.Size(112, 24),
              style=0)
        self.chkbox_header.SetValue(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.btn_konversi.Disable()

    def OnBtn_browse_file_kunci_rahasia_rsaButton(self, event):
        '''method ini digunakan untuk mencari file kunci rahasia RSA'''
        
        # menggunakan fungsi get_file() pada package dwil 
        # dengan batasan file berformat ekstensi .key
        allow_key = ['key']
        kunci_rahasia = dwil.get_file(allow_key)
        
        # nilai url kunci rahasia akan ditampilkan
        # di self.txt_file_kunci_rahasia_rsa
        self.txt_file_kunci_rahasia_rsa.SetValue(kunci_rahasia)
        
        # setelah nilai url tampil, maka selanjutnya
        # menampilkan nilai isi kunci rahasia tersebut
        # ke richtext1, richtext2 dan self.txt_info_id_kunci
        # dimana 
        # richtext1 = modulo N
        # richtext2 = eksponen D
        # self.txt_info_id_kunci = id kuncinya
        # dengan index file >>>
        # 0 : id kunci
        # 1 : modulo N
        # 2 : eksonen D
        # untuk membaca kunci tersebut, kita memerlukan sebuah method
        # dari package dwil di kelas System_File
        # untuk melakukan pembacaan kunci
        # dan mengambil nilainya.  
        # method tersebut bernama baca_kunci_rsa(filename)
        # parameter isikan sebagai url dimana file kunci rahasia tersebut
        # berada. bisa di ambil dari self.txt_file_kunci_rahasia_rsa
        # yang sudah di set dengan url link kunci tersebut.
        
        ## membuat objek
        fs = dwil.System_File()
        filename = self.txt_file_kunci_rahasia_rsa.GetValue()
        
        try:
            
            ## tampung ke nilai_kunci (list)
            ## menggunakan try jika kunci tidak valid
            nilai_kunci = fs.baca_kunci_rsa(filename)
            
            ## tampilkan id ke self.txt_info_id_kunci
            self.txt_info_id_kunci.SetValue(nilai_kunci[0].replace("\n",""))
            
            ## tampilkan modulo N ke richtext1
            self.richTextCtrl1.SetValue(nilai_kunci[1])
            
            ## tampilkan eksponen D ke richtext2
            self.richTextCtrl2.SetValue(nilai_kunci[2])
            
        except:
            
            notifikasi = "Kunci Tidak Valid"
            notif = wx.MessageDialog(self, notifikasi,"Error", wx.ICON_ERROR)
            notif.ShowModal()
            self.richTextCtrl1.SetValue("")
            self.richTextCtrl2.SetValue("")
            self.txt_info_id_kunci.SetValue("")
            self.txt_file_kunci_rahasia_rsa.SetValue("")
        
        
        
        # selanjutnya check ke absahan kunci
        # melalui tes numerikal pada nilai
        # yang ada di richtext1 dan richtext2.
        # jika ia bukan numerik, maka
        # berikan notifikasi ke user kalau
        # kunci ini tidak valid.
        notifikasi = ""
        valid_n = self.richTextCtrl1.GetValue().replace("\n","")
        valid_d = self.richTextCtrl2.GetValue().replace("\n","")
        if not valid_n.isdigit():
            notifikasi += "Kunci Tidak Valid, N bukan sebuah bilangan\n"
        if not valid_d.isdigit():
            notifikasi += "Kunci Tidak Valid, D bukan sebuah bilangan\n"
        if notifikasi != "":
            notif = wx.MessageDialog(self, notifikasi,"Error", wx.ICON_ERROR)
            notif.ShowModal()
            self.richTextCtrl1.SetValue("")
            self.richTextCtrl2.SetValue("")
            self.txt_info_id_kunci.SetValue("")
            self.txt_file_kunci_rahasia_rsa.SetValue("")

    def OnBtn_browse_kunci_sesiButton(self, event):
        '''mencari kunci sesi rc4'''
        
        # mendapatkan url kunci sesi dari path
        # tempat kunci tersebut disimpan.
        # menggunakan fungsi get_file(list_allow_file)
        # di peckage file misc package dwil
        # dimana file dibatasi hanya .key nya saja
        
        ## mengisi variabel kunci_sesi
        kunci_sesi = dwil.get_file(['key'])
        
        # setelah cek apakan kunci ini valid.
        # dengam method isnumeric() bisa mengecek
        # apakah nilainya numerik atau karakter.
        
        ## baca kunci sesi, untuk mengambil nilainya.
        ## nilai kunci sesi di tampung di chiper_kunci_sesi
        with open(kunci_sesi, "rb") as f:
            data = f.read()
        chiper_kunci_sesi = data
        notifikasi = ""
        checking_chiper_sesi = True
        list_data = data.split(" ")
        
        for i in data.replace(" ",""):
            if i.isdigit():
                checking_chiper_sesi = True
            else:
                checking_chiper_sesi = False
        
                
        if checking_chiper_sesi == False:
            notifikasi += "Maaf kunci sesi tidak valid\n"
            notif = wx.MessageDialog(self,notifikasi, "Error", wx.ICON_ERROR)
            notif.ShowModal()
            
        # jika valid, maka proses selanjutnya 
        # adalah proses dekrip
        # nilai kunci sesi tersebut.
        # tampung dulu nilai kunci N dan D nya,
        # tapi sebelumnya harus mengecek apakah nilai D dan N
        # sudah di sertakan di richtext1 dan 2.
        # jika kedua nilai tersebut kosong, maka 
        # tampilkan notifkasi terlebih dahulu.
        else:
            
            nilai_n = self.richTextCtrl1.GetValue()
            nilai_d = self.richTextCtrl2.GetValue()
            notifikasi = ""
            if nilai_n == "":
                notifikasi += "Nilai N kosong, silahkan menyertakan file kunci "
                notifikasi += "Rahasia terlebih dahulu untuk melakukan proses ini\n"
            if nilai_d == "":
                notifikasi += "Nilai D kosong, silahkan menyertakan file kunci "
                notifikasi += "Rahasia terlebih dahulu untuk melakukan proses ini\n"
            if notifikasi != "":
                notif = wx.MessageDialog(self, notifikasi, "Error", wx.ICON_ERROR)
                notif.ShowModal()
            else:
                
                # jika tidak ada kesalahan, maka proses
                # dekripsi kunci segera dilaksanakan.
                # proses ini memerlukan method dekripsi
                # dari class RSA yang ada di package dwil.
                # method ini mengembalikan plaintext semula
                enk = dwil.RSA()
                
                try:
                    
                    plaintext_sesi = enk.dekripsi(chiper_kunci_sesi.split(" "), int(nilai_n), int(nilai_d))
                    
                    ## tampilkan plaintext asli kunci sesi
                    ## ke self.txt_file_kunci_sesi
                    self.txt_file_kunci_sesi.SetValue(plaintext_sesi)
                    
                except:
                    
                    notifikasi += "Maaf kunci sesi tidak valid\n"
                    notif = wx.MessageDialog(self,notifikasi, "Error", wx.ICON_ERROR)
                    notif.ShowModal()

    def OnBtn_browse_file_dekripsiButton(self, event):
        '''digunakan untuk mengambil file yang akan di dekripsi'''
        
        # gunakan fungsi get_file(allow_ext)
        # di dalam package dwil
        # untuk mengambil file yang akan di dekripsi
        allow_file = ['xls']
        file_yg_didekrip = dwil.get_file(allow_file)
        
        # tampilkan nilai nya di self.txt_file_dekripsi
        self.txt_file_dekripsi.SetValue(file_yg_didekrip)

    def OnBtn_browse_dir_simpan_dekripsiButton(self, event):
        '''digunakan untuk menyeleksi direktori
        tempat penyimpanan file yang telah di dekripsi'''
        
        # menggunakan fungsi get_dir()
        # yang ada di dalam package dwil
        # untuk mendapatkan path dirnya
        dir_simpan = dwil.get_dir()
        
        # menampilkan nilainya di self.txt_dir_dekripsi
        self.txt_dir_dekripsi.SetValue(dir_simpan)

    def OnBtn_dekripsi_konversiButton(self, event):
        '''method event klik ini 
        digunakan untuk mendekripsi dokumen'''
    
        # menggunakan thread sistem untuk
        # memastikan kelancaran sebuah program
        # saat mendekripsi file yang cukup besar.
        # memastikan program agar tidak not responding
        thread.start_new_thread(self.__dekrip, ("",))
        
        
    def __dekrip(self,x):
        '''method ini digunakan untuk mendekripsi
        dimana akan di panggil oleh event klik dari
        tombol dekripsi dengan sistem threading. sifatnya private
        dengan inisial tanda __ di methodnya. 
        parameter x hanya sebuah tampungan untuk penyangga parameter
        saat sistem threading di mulai.'''
        
        # set start time
        start_time = time.time()
        
        # sebelum proses dekripsi dokumen, adakalanya
        # mengecek elemen yang dibutuhkan.
        # elemen 1 : self.txt_file_kunci_sesi
        # *untuk mengambil kunci sesi buat ngedekripsi dokumen
        # elemen 2 : self.txt_file_dekripsi
        # *untuk mengambil file yang akan di dekripsi
        # elemen 3 : self.txt_dir_dekripsi
        # *untuk menyimpan hasil file yang telah di dekripsi
        # jika masih terdapat elemen yang kosong, maka
        # program akan menampilkan notifikasi kesalahan yang
        # terjadi. sesuai kriteria kesalahan yang dilakukan.
        kunci_sesi = self.txt_file_kunci_sesi.GetValue()
        file_dekrip = self.txt_file_dekripsi.GetValue()
        dir_simpan = self.txt_dir_dekripsi.GetValue()
        
        ## pengecekan dimulai
        notifikasi = ""
        
        ## pengecekan kunci sesi
        if kunci_sesi == "":
            notifikasi += \
            "Kunci Sesi Kosong, Sertakan File kunci sesi terlebih dahulu\n"
        
        ## pengecekan file yang akan di dekrip
        if file_dekrip == "":
            notifikasi += \
            "Anda belum menyertakan file yang akan di dekripsi\n"
        
        ## pengecekan direktori penyimpanan file
        ## hasil dekripsi
        if dir_simpan == "":
            notifikasi += \
            "Anda belum menyertakan direktori tempat menyimpan hasil dekripsi\n"
        
        ## cek notifikasi, jika notifikasi ada notif
        ## kesalahan yang masuk, maka secara default program
        ## akan menampilkan error sesuai errornya.
        if notifikasi != "":
            
            ## tampilkan notifikasi
            notif = wx.MessageDialog(self,notifikasi,"Error", wx.ICON_ERROR)
            notif.ShowModal()
            
        else:
            
            try:
                
                ## jika tidak ada kesalahan, maka 
                ## proses dekripsi akan berlangsung.
                ## ambil nama file dengan fungsi
                ## ambil_nama_file(filename)
                nama_file = dwil.ambil_nama_file(file_dekrip)
                
                ## set identitas penamaan file
                ## hasil dekripsi
                nama_file_dekrip = "dekripsi-"
                
                ## membaca biner file
                with open(file_dekrip, "rb") as f:
                    data = f.read()
                
                ## melakukan proses dekripsi
                data = dwil.rc4_crypt(data, kunci_sesi)
                
                ## hasilnya akan di simpan kembali dalam bentuk file
                with open(dir_simpan+nama_file_dekrip+nama_file,"wb") as d:
                    d.write(data)
                
                ## menampilkan notifikasi berhasil
                notifikasi  = "Dekripsi Berhasil, silahkan cek : " + \
                dir_simpan+nama_file_dekrip+nama_file
                notifikasi += "Untuk melakukan proses konversi ke database, " 
                notifikasi += "silahkan pilih opsi lanjut"
                notifikasi += " Dibagian opsi mysql dan informasi file excel"
                notif = wx.MessageDialog(self, notifikasi, "Error", wx.OK)
                notif.ShowModal()
                
                # setelah proses dekripsi selesai,
                # maka aktifkan tombol konversi
                self.btn_konversi.Enable()
                
                # selanjutnya baca data excel
                # yang telah di dekripsi
                # untuk melakukan proses 
                # pembacaan cols, rows dan fieldnya
                file_konversi = dir_simpan+nama_file_dekrip+nama_file
                self.txt_excel_konversi.SetValue(file_konversi)
                
                # setting sheets
                excel_file = self.txt_excel_konversi.GetValue()
                excel = dwil.ExcelUtil(excel_file)
                list_excel = excel.getAllSheets()
                for sheet in list_excel:
                    self.cmb_sheets.Append(sheet)
                
                # set end time
                end_time = time.time() - start_time
                self.txt_info_waktu.SetValue(str(end_time))
                
            except:
                
                notifikasi = "Terjadi kesalahan saat proses dekripsi"
                notif = wx.MessageDialog(self, notifikasi, "Error", wx.ICON_ERROR)
                notif.ShowModal()

    def OnCmb_sheetsCombobox(self, event):
        '''digunakan untuk memilih sheets secara interaktif'''
        
        # menggunakan sistem threading, untuk memastikan
        # sebuah program mendapatkan dan menampilkan
        # informasi data excel tidak terjadi lambat.
        # di karenakan jika data file excel tersebut cukup
        # besar akan memakan resource memori komputer
        # cukup besar pula, maka dari itu penggunaan sistem
        # thread wajib di gunakan dalam program ini.
        thread.start_new_thread( self.__cmb_pilih_sheets, ("",) )
        
    def __cmb_pilih_sheets(self, x):
        '''method ini digunakan untuk terusan dari (potongan)
        method event seleksi combobox untuk memilih sheet.
        digunakan sebagai pendukung threading di saat
        user memilih sheet dengan event combobox'''
        
        sheet       = self.cmb_sheets.GetStringSelection()
        excel_file  = self.txt_excel_konversi.GetValue()
        excel       = dwil.ExcelUtil(excel_file)
        
        # mendapatkan jumlah kolom
        jumlah_kolom    = excel.getColsInExcel(sheet)
        
        # mendapatkan jumalh row
        jumlah_row      = excel.getRowsInExcel(sheet)
        
        # mendapatkan tipedata
        list_tipe_data  = excel.getDataTypeExcel(sheet, \
        jumlah_kolom, startRows=1)
        
        # mendapatkan jumlah field name excel
        jumlah_field    = len(excel.getHeaderFieldNameExcel(sheet, \
        jumlah_kolom, startRows=0))
        
        # memasukan jumlah kolom
        self.txt_cols.SetValue(str(jumlah_kolom))
        
        # memasukan jumlah row
        self.txt_rows.SetValue(str(jumlah_row))
        
        # memasukan jumlah field
        self.txt_fields.SetValue(str(jumlah_field))

    def OnBtn_tes_koneksiButton(self, event):
        '''tombol untuk tes koneksi'''
        
        # sebelum tes koneksi, periksa
        # terlebih dahulu beberapa elemen
        # seperti host, nama database,
        # password, username dan nama table.
        # berikan notifikasi jika terdapat
        # data atau elemen yang masih kosong.
        host = self.txt_host.GetValue()
        dbnm = self.txt_database.GetValue()
        user = self.txt_username.GetValue()
        pswd = self.txt_password.GetValue()
        tabel= self.txt_tabel.GetValue()
        
        notifikasi =""
        
        ## cek host
        if host == "":
            notifikasi += "Anda belum memasukan host mysql\n"
        
        ## cek database
        if dbnm == "":
            notifikasi += "Anda belum memasukan nama database\n"
        
        ## cek username
        if user == "":
            notifikasi += "Anda belum memasukan username\n"
        
        ## cek nama tabel
        if tabel == "":
            notifikasi += "Anda belum memasukan nama tabel\n"
        
        ## cek notifikasi
        if notifikasi == "":
            
            # untuk mengecek koneksi mysql
            # anda perlu menggunakan class MySqlUtil
            # pada package dwil dengan method testConnection(self)
            try:
                
                # start koneksi ke mysql
                mysql = dwil.MySqlUtil(host, user, pswd, dbnm)
                koneksi = mysql.testConnection()
                
                if koneksi:
                    
                    # jika hasilnya True, maka tampilkan notif
                    # kalau mysql terhubung.
                    pesan = "MySql terkoneksi"
                    notif = wx.MessageDialog(self,pesan,"Info",wx.ICON_INFORMATION)
                    notif.ShowModal()
                    
                    # jika koneksi sukses, maka selanjutnya adalah
                    # mendapatkan jumlah field dalam suatu table
                    dataType = mysql.getDataTypeInField(tabel)
                    
                    
                else:
                    
                    # jika hasilnya False, maka tampilkan notif
                    # error koneksi
                    pesan = "Anda tidak terhubung ke MySql"
                    notif = wx.MessageDialog(self,pesan,"Info",wx.ICON_WARNING)
                    notif.ShowModal()
                    
            except MySQLdb.Error, e:
                
                    pesan = "Koneksi Error %d : %s" % (e.args[0], e.args[1])
                    notif = wx.MessageDialog(self,pesan,"Info",wx.ICON_WARNING)
                    notif.ShowModal()
                    
        # jika notifikasi error ada.
        # tampilkan notifikasi error tersebut
        else:
            notif = wx.MessageDialog(self,notifikasi,"Info",wx.ICON_STOP)
            notif.ShowModal()

    def OnBtn_konversiButton(self, event):
        '''untuk melakukan konversi'''
        
        # menggunakan sistem threading untuk memastikan
        # saat program melakukan konversi dengan data yang cukup besar
        # tidak terjadi not responding.
        thread.start_new_thread(self.__konversi,("", ))
        
    def __konversi(self,x):
        '''method ini digunakan untuk meneruskan method event klik
        dari event tombol konversi dengan sistem threading'''
        
        # mengambil penggunaan header
        header = self.chkbox_header.GetValue()
        
        # mengambil nama host
        host = self.txt_host.GetValue()
        
        # mengambil nama user
        user = self.txt_username.GetValue()
        
        # mengambil password
        pswd = self.txt_password.GetValue()
        
        # mengambil nama database
        dbnm = self.txt_database.GetValue()
        
        # mengambil nama tabel
        tbl  = self.txt_tabel.GetValue()
        
        # menyeleksi sheet yang dibutuhkan
        sheet = self.cmb_sheets.GetStringSelection()
        
        # init notifikasi
        notifikasi = ""
        
        # cek txt host
        if host == "":
            notifikasi += "Anda belum mengisi nama host\n"
        
        # cek txt user
        if user == "":
            notifikasi += "Anda belum mengisi username\n"
        
        # cek txt database
        if dbnm == "":
            notifikasi += "Anda belum mengisi nama database\n"
        
        # cek isi tabel
        if tbl == "":
            notifikasi += "Anda belum mengisi nama tabel\n"
        
        # cek isi sheet yang di seleksi
        if sheet == "":
            notifikasi += "Anda belum memilih sheet\n"
        
        # cek apakah ada notifikasi eror
        if notifikasi != "":
            
            # tampilkan pesan eror
            notif = wx.MessageDialog(self, notifikasi, "Error", wx.ICON_ERROR)
            notif.ShowModal()
            
        # jika notifikasi kosong, maka lakukan :
        else:
            
            try:
                
                # file excel yang akan di konversi
                file_excel = self.txt_excel_konversi.GetValue()
                
                # mengambil data excel 
                excel = dwil.ExcelUtil(file_excel)
                data_excel = excel.excelConvert(sheet, header)
                
                # export data excel ke database
                mysql = dwil.MySqlUtil(host, user, pswd, dbnm)
                export_data = mysql.exportExcelMySQL(data_excel,tbl)
                
                # cek hasil export data
                if export_data:
                    # tampilkan pesan berhasil
                    pesan = "Berhasil Melakukan Konversi"
                    notif = wx.MessageDialog(self,pesan,"Notif",wx.OK)
                    notif.ShowModal()
                else:
                    
                    # gagal export, tampilkan pesan eror
                    pesan = "Gagal Melakukan Konversi"
                    notif = wx.MessageDialog(self,pesan,"Notif",wx.ICON_ERROR)
                    notif.ShowModal()
            except:
                
                # kejadian seperti gagalnya koneksi
                # tampilkan notif gagal 
                # koneksi dan eror saat export
                pesan   = "Gagal Melakukan Konversi, ini bisa "
                pesan  += "terjadi karena sebuah rows file "
                pesan  += "excel melebihi index pada field "
                pesan  += "tabel di database, "
                pesan  += "atau bisa juga terjadi karena "
                pesan  += "Anda belum terkoneksi dengan server mysql"
                notif = wx.MessageDialog(self,pesan,"Notif",wx.ICON_ERROR)
                notif.ShowModal()
        
            
    def __bersih(self):
        self.txt_cols.SetValue("")
        self.txt_database.SetValue("")
        self.txt_dir_dekripsi.SetValue("")
        self.txt_excel_konversi.SetValue("")
        self.txt_fields.SetValue("")
        self.txt_file_dekripsi.SetValue("")
        self.txt_file_kunci_rahasia_rsa.SetValue("")
        self.txt_file_kunci_sesi.SetValue("")
        self.txt_host.SetValue("")
        self.txt_info_id_kunci.SetValue("")
        self.txt_info_waktu.SetValue("")
        self.txt_password.SetValue("")
        self.txt_rows.SetValue("")
        self.txt_tabel.SetValue("")
        self.txt_username.SetValue("")
        self.richTextCtrl1.SetValue("")
        self.richTextCtrl2.SetValue("")
        
        self.btn_konversi.Disable()

    def OnBtn_bersihButton(self, event):
        self.__bersih()
        
        
                
        
        
                
            
            
        
        

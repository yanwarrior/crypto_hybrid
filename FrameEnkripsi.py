#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.lib.buttons
import dwil
import time
import thread

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_BERSIH, wxID_FRAME1BTN_BROWSE_DIR_ENKRIP, 
 wxID_FRAME1BTN_BROWSE_FILE_ENKRIP, 
 wxID_FRAME1BTN_BROWSE_FILE_KUNCI_PUBLIK_RSA, wxID_FRAME1BTN_ENKRIPSI, 
 wxID_FRAME1BTN_RANDOM_KUNCI_SESI, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1RICHTEXTCTRL2, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1STSBAR, wxID_FRAME1TXT_DIR_SIMPAN_ENKRIPSI, 
 wxID_FRAME1TXT_FILE_ENKRIPSI, wxID_FRAME1TXT_FILE_KUNCI_PUBLIK_RSA, 
 wxID_FRAME1TXT_INFO_ID_KUNCI, wxID_FRAME1TXT_INFO_WAKTU, 
 wxID_FRAME1TXT_KUNCI_SESI, 
] = [wx.NewId() for _init_ctrls in range(30)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(10, 37), size=wx.Size(504, 542),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hybrid - Enkripsi')
        self.SetClientSize(wx.Size(488, 504))
        self.SetIcon(wx.Icon(u'images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(488, 504),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Kunci : ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 48), size=wx.Size(456, 128), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kunci Publik RSA : ', name='staticText1',
              parent=self.panel1, pos=wx.Point(32, 72), size=wx.Size(89, 13),
              style=0)

        self.txt_file_kunci_publik_rsa = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_KUNCI_PUBLIK_RSA,
              name=u'txt_file_kunci_publik_rsa', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(344, 21), style=0, value=u'')
        self.txt_file_kunci_publik_rsa.SetEditable(False)
        self.txt_file_kunci_publik_rsa.SetBackgroundColour(wx.Colour(255, 255,
              255))

        self.btn_browse_file_kunci_publik_rsa = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_PUBLIK_RSA,
              label=u'Browse', name=u'btn_browse_file_kunci_publik_rsa',
              parent=self.panel1, pos=wx.Point(384, 88), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_kunci_publik_rsa.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_kunci_publik_rsaButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_PUBLIK_RSA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Kunci Sesi RC4 (128 Bit) : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(32, 120), size=wx.Size(125, 13),
              style=0)

        self.txt_kunci_sesi = wx.TextCtrl(id=wxID_FRAME1TXT_KUNCI_SESI,
              name=u'txt_kunci_sesi', parent=self.panel1, pos=wx.Point(32, 136),
              size=wx.Size(344, 21), style=0, value=u'')
        self.txt_kunci_sesi.SetEditable(True)
        self.txt_kunci_sesi.SetForegroundColour(wx.Colour(0, 0, 0))
        self.txt_kunci_sesi.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.btn_random_kunci_sesi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_RANDOM_KUNCI_SESI,
              label=u'Random', name=u'btn_random_kunci_sesi',
              parent=self.panel1, pos=wx.Point(384, 136), size=wx.Size(76, 25),
              style=0)
        self.btn_random_kunci_sesi.Bind(wx.EVT_BUTTON,
              self.OnBtn_random_kunci_sesiButton,
              id=wxID_FRAME1BTN_RANDOM_KUNCI_SESI)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Informasi Kunci Publik : ', name='staticBox2',
              parent=self.panel1, pos=wx.Point(16, 184), size=wx.Size(456, 128),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Moduo N :', name='staticText3', parent=self.panel1,
              pos=wx.Point(32, 208), size=wx.Size(50, 13), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(32, 224), size=wx.Size(136, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self.panel1, pos=wx.Point(192, 224), size=wx.Size(136, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl2.SetLabel(u'richText')
        self.richTextCtrl2.SetEditable(False)
        self.richTextCtrl2.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Eksponen E : ', name='staticText4', parent=self.panel1,
              pos=wx.Point(192, 208), size=wx.Size(66, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='staticText5', name='staticText5', parent=self.panel1,
              pos=wx.Point(48, -168), size=wx.Size(55, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'ID Kunci : ', name='staticText6', parent=self.panel1,
              pos=wx.Point(352, 208), size=wx.Size(50, 13), style=0)

        self.txt_info_id_kunci = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_ID_KUNCI,
              name=u'txt_info_id_kunci', parent=self.panel1, pos=wx.Point(352,
              224), size=wx.Size(100, 21), style=0, value=u'')
        self.txt_info_id_kunci.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.txt_info_id_kunci.SetEditable(False)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'File dan Direktori : ', name='staticBox3',
              parent=self.panel1, pos=wx.Point(16, 320), size=wx.Size(456, 128),
              style=0)

        self.txt_file_enkripsi = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_ENKRIPSI,
              name=u'txt_file_enkripsi', parent=self.panel1, pos=wx.Point(32,
              360), size=wx.Size(344, 21), style=0, value=u'')
        self.txt_file_enkripsi.SetEditable(False)
        self.txt_file_enkripsi.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'File yang akan di Enkripsi : ', name='staticText7',
              parent=self.panel1, pos=wx.Point(32, 344), size=wx.Size(130, 13),
              style=0)

        self.btn_browse_file_enkrip = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_ENKRIP,
              label=u'Browse', name=u'btn_browse_file_enkrip',
              parent=self.panel1, pos=wx.Point(384, 360), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_enkrip.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_enkripButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_ENKRIP)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Direktori Penyimpanan File Enkripsi : ',
              name='staticText8', parent=self.panel1, pos=wx.Point(32, 392),
              size=wx.Size(176, 13), style=0)

        self.txt_dir_simpan_enkripsi = wx.TextCtrl(id=wxID_FRAME1TXT_DIR_SIMPAN_ENKRIPSI,
              name=u'txt_dir_simpan_enkripsi', parent=self.panel1,
              pos=wx.Point(32, 408), size=wx.Size(344, 21), style=0, value=u'')
        self.txt_dir_simpan_enkripsi.SetEditable(False)
        self.txt_dir_simpan_enkripsi.SetBackgroundColour(wx.Colour(255, 255,
              255))

        self.btn_browse_dir_enkrip = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_DIR_ENKRIP,
              label=u'Browse', name=u'btn_browse_dir_enkrip',
              parent=self.panel1, pos=wx.Point(384, 408), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_dir_enkrip.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_enkripButton,
              id=wxID_FRAME1BTN_BROWSE_DIR_ENKRIP)

        self.btn_enkripsi = wx.Button(id=wxID_FRAME1BTN_ENKRIPSI,
              label=u'Enkripsi', name=u'btn_enkripsi', parent=self.panel1,
              pos=wx.Point(392, 456), size=wx.Size(83, 32), style=0)
        self.btn_enkripsi.Bind(wx.EVT_BUTTON, self.OnBtn_enkripsiButton,
              id=wxID_FRAME1BTN_ENKRIPSI)

        self.btn_bersih = wx.Button(id=wxID_FRAME1BTN_BERSIH, label=u'Bersih',
              name=u'btn_bersih', parent=self.panel1, pos=wx.Point(296, 456),
              size=wx.Size(83, 32), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAME1BTN_BERSIH)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Waktu Yang Dibutuhkan : ', name='staticText9',
              parent=self.panel1, pos=wx.Point(16, 464), size=wx.Size(126, 13),
              style=0)

        self.txt_info_waktu = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_WAKTU,
              name=u'txt_info_waktu', parent=self.panel1, pos=wx.Point(168,
              464), size=wx.Size(48, 21), style=0, value=u'')
        self.txt_info_waktu.SetEditable(False)
        self.txt_info_waktu.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Detik', name='staticText10', parent=self.panel1,
              pos=wx.Point(232, 464), size=wx.Size(25, 13), style=0)

        self.stsbar = wx.StatusBar(id=wxID_FRAME1STSBAR, name=u'stsbar',
              parent=self.panel1, style=0)
        self.stsbar.SetStatusText(u'Status : none')
        self.stsbar.SetBackgroundColour(wx.Colour(229, 229, 229))

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def __bersih(self):
        '''membersihkan form enkripsi'''
        self.txt_dir_simpan_enkripsi.SetValue("")
        self.txt_file_enkripsi.SetValue("")
        self.txt_file_kunci_publik_rsa.SetValue("")
        self.txt_info_id_kunci.SetValue("")
        self.txt_info_waktu.SetValue("")
        self.richTextCtrl1.SetValue("")
        self.richTextCtrl2.SetValue("")
        self.txt_info_id_kunci.SetValue("")
        self.txt_kunci_sesi.SetValue("")
        

    def OnBtn_browse_file_kunci_publik_rsaButton(self, event):
        '''untuk mengambil kunci publik'''
        # allow file key
        allow_key = ['key']
        
        # get file
        file_kunci_publik = dwil.get_file(allow_key)
        
        # masukan path dan file key ke self.txt_file_kunci_publik_rsa
        self.txt_file_kunci_publik_rsa.SetValue(file_kunci_publik)
        
        ## setelah direktori kunci telah di isi dengan
        ## file kunci beserta pathnya, maka
        ## saatnya melakukan pengisian self.richTextCtrl1 (modulo N)
        ## self.richTextCtrl2 (eksponen E) dan self.txt_info_id_kunci
        kunci = dwil.System_File()
        kunci_publik = kunci.baca_kunci_rsa(self.txt_file_kunci_publik_rsa.GetValue())
        
        # set nilai Modulo N
        self.richTextCtrl1.SetValue(kunci_publik[1])
        
        # set nilai Eksponen E
        self.richTextCtrl2.SetValue(kunci_publik[2])
        
        # set nilai Kunci ID
        self.txt_info_id_kunci.SetValue(kunci_publik[0])

    def OnBtn_random_kunci_sesiButton(self, event):
        '''untuk random kunci RC4 sebesar 16 Character (128 Bit)'''
        # panggil fungsi random_key() untuk mendapatkan 
        # karakter random dan masukan nilainya ke variabel kunci_rc4
        kunci_rc4 = dwil.random_key()
        
        # set nilai self.txt_kunci_sesi
        self.txt_kunci_sesi.SetValue(kunci_rc4)

    def OnBtn_browse_file_enkripButton(self, event):
        '''mengambil file yang akan di enkripsi, 
        dalam hal ini masih bebas file apapun'''
        
        # set file yang di izinkan untuk di enkripsi
        allow_file = ['doc','docx','xls','xlsx','jpeg',\
        'JPEG','jpg','JPG','png','PNG','gif','GIF','ppt','pptx','mp3']
        
        # mengeset batasan ukuran file yang diperbolehkan
        allow_size = 5000 ## satuan kb / 5 mb
        
        # mengambil file dengan open dialog windows dg nama file_enkrip
        file_enkrip = dwil.get_file(allow_file)
        
        # memasukan nama file beserta path nya ke self.txt_file_enkripsi
        self.txt_file_enkripsi.SetValue(file_enkrip)
        
        # mengecek ukuran file, jika lebih dari ukuran yang di batasi
        # maka program memberikan notifikasi kesalahan
        # dan mengeset self.txt_file_enkripsi menjadi kosong kembali
        ukuran_file = dwil.baca_ukuran_file(self.txt_file_enkripsi.GetValue())
        print ukuran_file
        if ukuran_file > allow_size:
            notifikasi = "Ukuran file di batasi sebesar " + str(allow_size/1000) + " mb"
            notifikasi += " Ukuran file yang anda input lebih besar"
            notifikasi += " pilih ukuran di bawah " + str(allow_size/1000)  + " mb"
            notif = wx.MessageDialog(self,notifikasi,"Ukuran File",wx.CANCEL)
            notif.ShowModal()   
            self.txt_file_enkripsi.SetValue("")     

    def OnBtn_browse_dir_enkripButton(self, event):
        '''untuk mengambil direktori tempat menyimpan
        file hasil enkripsi'''
        # set path direktori
        path = dwil.get_dir()
        
        # set nilai path ke self.txt_dir_simpan_enkripsi
        self.txt_dir_simpan_enkripsi.SetValue(path)

    def OnBtn_enkripsiButton(self, event):
        '''untuk melakukan enkripsi file'''
        ## catatan :
        ## dalam melakukan enkripsi, sebelumnya kita harus memeriksa 
        ## 1. file kunci
        ## 2. nilai kunci RC4 random
        ## 3. nilai modulo N
        ## 4. nilai eksponen E
        ## 5. nilai file yang akan di enkripsi
        ## 6. nilai direktori tempat yang akan di enkripsi
        ## dengan membuat variabel notifikasi
        ## dimana untuk menampung kesalahan yang terjadi
        ## sebelum proses enkripsi dimulai.
        notifikasi = ""
        
        # cek file kunci
        if self.txt_file_kunci_publik_rsa.GetValue() == "":
            notifikasi += "Anda harus memilih kunci untuk melakukan proses enkripsi\n"
        
        # cek kunci RC4
        if self.txt_kunci_sesi.GetValue() == "":
            notifikasi += "Anda harus mengisi kunci sesi untuk melakukan proses enkripsi\n"
            
        # cek panjang kunci RC4
        if len(self.txt_kunci_sesi.GetValue()) < 8:
            notifikasi += "Kunci sesi di bawah 8 karakter tidak di izinkan, minimal 9 karakter\n"
        
        # cek batas kunci RC4
        if len(self.txt_kunci_sesi.GetValue()) > 16:
            notifikasi += "Batas panjang kunci sesi harus lebih dari 8 karakter dan kurang dari sama dengan 16 karakter\n"
        
        # cek nilai modulo N
        if self.richTextCtrl1.GetValue() == "":
            notifikasi += "Pilih kunci publik yang sesuai untuk mendapatkan nilai Modulo N\n"
            
        # cek nilai eksponen E
        if self.richTextCtrl2.GetValue() == "":
            notifikasi += "Pilih kunci publik yang sesuai untuk mendapatkan nilai Eksponen E\n"
        
        # cek file yang akan dienkripsi
        if self.txt_file_enkripsi.GetValue() == "":
            notifikasi += "Pilih file yang akan di enkripsi\n"
        
        # cek direktori tempat penyimpanan file yang akan dienkripsi
        if self.txt_dir_simpan_enkripsi.GetValue() == "":
            notifikasi += "Pilih direktori tempat penyimpanan enkripsi\n"
            
        # cek notifikasi, jika terdapat kesalahan
        # maka lakukan :
        if notifikasi != "":
            notif = wx.MessageDialog(self, notifikasi, "Peringatan", wx.ICON_WARNING)
            notif.ShowModal()
        else:
            thread.start_new_thread(self.enkrips,("",))

    def OnBtn_bersihButton(self, event):
        '''tombol bersih'''
        self.__bersih()
        
    def enkrips(self,y):
        try:
            
            # set time
            start_time = time.time()
            
            
            # matikan tombol enkripsi
            self.btn_enkripsi.Disable()
            # matikan layar form
            self.Disable()
            # status bar
            self.stsbar.SetStatusText("Status : Dimulai")
            # membaca binary file
            self.stsbar.SetStatusText("Status : Membaca Binary File")
            binary_file = dwil.System_File()
            data = binary_file.get_binary_file(self.txt_file_enkripsi.GetValue())
            data = str(data)
            
            # proses enkripsi dimulai dengan RC4 dengan kunci sesi RC4
            enkrip = dwil.rc4_crypt(data, self.txt_kunci_sesi.GetValue())
             
            # ambil ekstensi file yang di enkripsi
            eks = dwil.ambil_ekstensi_file(self.txt_file_enkripsi.GetValue())
            
            # ambil nama file yang di enkripsi
            namafile = dwil.ambil_nama_file(self.txt_file_enkripsi.GetValue())
            
            # buat filename baru hasil enkripsi
            filename_enkrip = self.txt_dir_simpan_enkripsi.GetValue()
            filename_enkrip += "enkripsi-"+namafile+eks
            buat_file = dwil.System_File()
            buat_file.create_file_rc4(filename_enkrip,enkrip)
                
            # simpan kunci simetris RC4 (kunci sesi)
            # yang sebelumnya akan di enkripsi dengan
            # kunci publik RSA
            self.stsbar.SetStatusText("Status : Penyimpanan Kunci Sesi")
            kunci_sesi = self.txt_kunci_sesi.GetValue()
            enkrip_kunci_sesi = dwil.RSA()
            enkrip_rsa = enkrip_kunci_sesi.enkripsi(kunci_sesi, int(self.richTextCtrl1.GetValue()),\
            int(self.richTextCtrl2.GetValue()))
            id_sesi = self.txt_info_id_kunci.GetValue()
            id_sesi = id_sesi.replace('\n','')
            rc4_file_key = self.txt_dir_simpan_enkripsi.GetValue() + id_sesi + "-kunci sesi.key"
            enkrip_rsa = [str(i) for i in enkrip_rsa]
            enkrip_rsa = " ".join(enkrip_rsa)
            with open(rc4_file_key,"wb") as f:
                f.write(enkrip_rsa)
            
            self.stsbar.SetStatusText("Status : Selesai Melakukan Enkripsi")
            # notif berhasil mengenkripsi hybrid
            notifikasi = "Enkripsi Berhasil, file yang di enkripsi dengan "
            notifikasi += "File kunci sesi berada di dalam folder " + self.txt_dir_simpan_enkripsi.GetValue()
                
            notif = wx.MessageDialog(self,notifikasi,"Berhasil", wx.OK)
            notif.ShowModal()
            
            self.stsbar.SetStatusText("Status : None")
            # hidupkan tombol enkripsi
            self.btn_enkripsi.Enable()
            # hidupkan layar form
            self.Enable()
            
            # set end time
            end_time = time.time() - start_time
            self.txt_info_waktu.SetValue(str(end_time))
        except:
            # notif gagal mengenkripsi hybrid
            notifikasi = "Terjadi kesalahan saat melakukan enkripsi"
            notif = wx.MessageDialog(self,notifikasi,"Error", wx.ICON_ERROR)
            notif.ShowModal()
            self.__bersih()
        
            
    
            
        
        
        
        

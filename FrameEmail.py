#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.lib.buttons
import wx.stc
import dwil
import thread

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_BERSIH, wxID_FRAME1BTN_BROWSE_FILE_ATTACHMENT, 
 wxID_FRAME1BTN_KIRIM, wxID_FRAME1BTN_KONEKSI, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STS, wxID_FRAME1TXT_ATTACHMENT, wxID_FRAME1TXT_PASSWORD, 
 wxID_FRAME1TXT_PENERIMA_EMAIL, wxID_FRAME1TXT_PORT, wxID_FRAME1TXT_SMTP, 
 wxID_FRAME1TXT_SUBJEK, wxID_FRAME1TXT_USERNAME, 
] = [wx.NewId() for _init_ctrls in range(26)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(8, 55), size=wx.Size(596, 536),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Hybrid - Send Attachment via Email')
        self.SetClientSize(wx.Size(580, 498))
        self.SetIcon(wx.Icon(u'images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(580, 498),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Sending Email', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(544, 264), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Subjek :', name='staticText1', parent=self.panel1,
              pos=wx.Point(288, 40), size=wx.Size(40, 13), style=0)

        self.txt_subjek = wx.TextCtrl(id=wxID_FRAME1TXT_SUBJEK,
              name=u'txt_subjek', parent=self.panel1, pos=wx.Point(288, 56),
              size=wx.Size(248, 21), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Penerima Email : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(32, 40), size=wx.Size(82, 13),
              style=0)

        self.txt_penerima_email = wx.TextCtrl(id=wxID_FRAME1TXT_PENERIMA_EMAIL,
              name=u'txt_penerima_email', parent=self.panel1, pos=wx.Point(32,
              56), size=wx.Size(240, 21), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Pesan : ', name='staticText3', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(40, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'File Attachment : ', name='staticText4',
              parent=self.panel1, pos=wx.Point(32, 224), size=wx.Size(86, 13),
              style=0)

        self.txt_attachment = wx.TextCtrl(id=wxID_FRAME1TXT_ATTACHMENT,
              name=u'txt_attachment', parent=self.panel1, pos=wx.Point(32, 240),
              size=wx.Size(424, 21), style=0, value=u'')

        self.btn_browse_file_attachment = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_ATTACHMENT,
              label=u'Browse', name=u'btn_browse_file_attachment',
              parent=self.panel1, pos=wx.Point(464, 240), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_attachment.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_attachmentButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_ATTACHMENT)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Akun : ', name='staticBox2', parent=self.panel1,
              pos=wx.Point(16, 296), size=wx.Size(272, 136), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Username : ', name='staticText5', parent=self.panel1,
              pos=wx.Point(32, 320), size=wx.Size(59, 13), style=0)

        self.txt_username = wx.TextCtrl(id=wxID_FRAME1TXT_USERNAME,
              name=u'txt_username', parent=self.panel1, pos=wx.Point(32, 336),
              size=wx.Size(216, 21), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Password : ', name='staticText6', parent=self.panel1,
              pos=wx.Point(32, 368), size=wx.Size(57, 13), style=0)

        self.txt_password = wx.TextCtrl(id=wxID_FRAME1TXT_PASSWORD,
              name=u'txt_password', parent=self.panel1, pos=wx.Point(32, 384),
              size=wx.Size(216, 21), style=0, value=u'')

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label='staticBox3', name='staticBox3', parent=self.panel1,
              pos=wx.Point(312, 296), size=wx.Size(248, 136), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'SMTP : ', name='staticText7', parent=self.panel1,
              pos=wx.Point(328, 320), size=wx.Size(37, 13), style=0)

        self.txt_smtp = wx.TextCtrl(id=wxID_FRAME1TXT_SMTP, name=u'txt_smtp',
              parent=self.panel1, pos=wx.Point(328, 336), size=wx.Size(208, 21),
              style=0, value=u'')

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Port (587 gmail port) :', name='staticText8',
              parent=self.panel1, pos=wx.Point(328, 368), size=wx.Size(107, 13),
              style=0)

        self.txt_port = wx.TextCtrl(id=wxID_FRAME1TXT_PORT, name=u'txt_port',
              parent=self.panel1, pos=wx.Point(328, 384), size=wx.Size(56, 21),
              style=0, value=u'')

        self.btn_kirim = wx.Button(id=wxID_FRAME1BTN_KIRIM, label=u'Kirim',
              name=u'btn_kirim', parent=self.panel1, pos=wx.Point(472, 448),
              size=wx.Size(91, 32), style=0)
        self.btn_kirim.Bind(wx.EVT_BUTTON, self.OnBtn_kirimButton,
              id=wxID_FRAME1BTN_KIRIM)

        self.btn_bersih = wx.Button(id=wxID_FRAME1BTN_BERSIH, label=u'Bersih',
              name=u'btn_bersih', parent=self.panel1, pos=wx.Point(368, 448),
              size=wx.Size(83, 32), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAME1BTN_BERSIH)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(32, 112), size=wx.Size(504, 100),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')

        self.sts = wx.StaticText(id=wxID_FRAME1STS,
              label=u'Check Status Koneksi : ', name=u'sts', parent=self.panel1,
              pos=wx.Point(24, 456), size=wx.Size(113, 13), style=0)

        self.btn_koneksi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_KONEKSI,
              label=u'Tes Koneksi', name=u'btn_koneksi', parent=self.panel1,
              pos=wx.Point(208, 448), size=wx.Size(80, 32), style=0)
        self.btn_koneksi.SetBackgroundColour(wx.Colour(64, 128, 128))
        self.btn_koneksi.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_koneksi.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btn_koneksi.SetThemeEnabled(False)
        self.btn_koneksi.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.btn_koneksi.Bind(wx.EVT_BUTTON, self.OnBtn_koneksiButton,
              id=wxID_FRAME1BTN_KONEKSI)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def __bersih(self):
        self.txt_subjek.SetValue("")
        self.txt_attachment.SetValue("")
        self.txt_username.SetValue("")
        self.txt_password.SetValue("")
        self.richTextCtrl1.SetValue("")
        self.txt_smtp.SetValue("")
        self.txt_port.SetValue("")
        self.txt_penerima_email.SetValue("")
        

    def OnBtn_browse_file_attachmentButton(self, event):
        '''tombol untuk mencari file yang akan di kirim 
        lewat email'''
        # ambil file yang akan di kirim dengan fungsi 
        # get_file(list_allow_file) dari package dwil
        # masukan nilai url filenya di dalam variabel 
        # file_attachment lalu tampilkan ke self.txt_attachment
        ## set allow file
        list_allow_file =  ['key','7z','tar.gz','gz','zip','rar',\
        'doc','docx','xls','xlsx','jpeg',\
        'JPEG','jpg','JPG','png','PNG','gif',\
        'GIF','ppt','pptx','mp3']
        ## set file_attachment
        file_attachment = dwil.get_file(list_allow_file)
        ## set self.txt_attachment
        self.txt_attachment.SetValue(file_attachment)

    def OnBtn_koneksiButton(self, event):
        '''untuk mendapatkan status koneksi'''
        # untuk melakukan pengiriman data
        # via email, dibutuhkan koneksi ke internet,
        # fungsi sub event klik ini digunakan
        # untuk mengecek apakah user terhubung atau tidak ke internet
        # dengan menggunakan fungsi is_connected()
        # di dalam package dwil
        koneksi = dwil.is_connected()
        
        # jika hasilnya True, maka
        # status user saat ini memang
        # tersambung ke jaringan internet
        if koneksi:
            # menampilkan notifikasi 
            # bahwa user terhubung ke internet
            # dan bisa melakukan proses
            # pengiriman data dengan email 
            # dengan program ini
            notifikasi = "Anda terhubung ke jaringan internet, Anda "
            notifikasi += "bisa melakukan pengiriman data via email"
            notif = wx.MessageDialog(self,notifikasi,"Konktivitas",wx.ICON_INFORMATION)
            notif.ShowModal()
        else:
            # menampilkan notifikasi
            # bahwa user tidak terhubung ke internet
            # dan memberitahu kepada user
            # bahwa ia tidak bisa melakukan proses
            # pengiriman data melalui email pada program ini
            notifikasi = "Untuk melakukan pengiriman email dengan program ini"
            notifikasi += " Anda perlu terhubung ke jaringan internet"
            notif = wx.MessageDialog(self,notifikasi,"Konktivitas",wx.ICON_EXCLAMATION)
            notif.ShowModal()

    def OnBtn_kirimButton(self, event):
        '''tombol ini digunakan untuk melakukan
        pengiriman email'''
        # catatan penting (bingiiits) :
        # ***************************************************************
        # untuk mengirim email beserta filenya
        # maka kita menggunakan fungsi mailSender()
        # yang udah dibuat di dalam package dwil
        # dimana memiliki param sebagai berikut :
        # ---------------------------------------------------------------
        # param 1 : filename    -> isi file
        # param 2 : sender      -> isi email anda
        # param 3 : reciever    -> isi email penerima 
        # param 4 : username    -> isi username anda
        # param 5 : password    -> isi password anda
        # param 6 : subject     -> seperti judul
        # param 7 : msg         -> isi pesan yang anda ingin kirim
        # param 8 : smtp        -> isi smtp (gmail : smtp.gmail.com)
        # param 9 : port        -> isi port (gmail : 587) 
        # *****************************************************************
        
        # dari parameter di atas maka kita akan 
        # mengeset ke dalam 9 variabel yang masing2
        # isinye berupa nilai yang dibutuhkan untuk
        # menggunakan fungsi sendMail()
        # dalam proses pengiriman email beserta jeroannya (file yang di sertakan)
        ## 1. set variabel filename (isi path file)
        filename = self.txt_attachment.GetValue()
        ## 2. set variabel sender - asumsikan username juga 
        ## menggunakan nama yang sama dengan nama email kite
        sender = self.txt_username.GetValue()
        ## 3. set variabel reciever
        reciever = self.txt_penerima_email.GetValue()
        ## 4. set variabel username
        username = self.txt_username.GetValue()
        ## 5. set variabel password
        password = self.txt_password.GetValue()
        ## 6. set variabel subject
        subject = self.txt_subjek.GetValue()
        ## 7. set variabel msg
        msg = self.richTextCtrl1.GetValue()
        ## 8. set variabel smtp
        smtp = self.txt_smtp.GetValue()
        ## 9. set variabel port
        port = self.txt_port.GetValue()
        
        # setelah melakukan pengesetan variabel
        # dengan beberapa nilai, maka selanjutnya
        # adalah menyaring kesalahan yang terjadi
        # oleh user saat tombol pengiriman email
        # di tekan.
        # penyaringan kesalahan dilakukan 
        # untuk memberikan notifikasi kesalahan
        # yang dilakukan oleh user.
        notifikasi = ""
        ## kesalahan saat file belum di sertakan
        if filename == "":
            notifikasi += "Anda belum menyertakan sebuah file yang akan dikirim\n"
        ## kesalahan saat username belum di sertakan
        if username == "":
            notifikasi += "Masukan Username !\n"
        ## kesalahan saat password lupa di input
        if password == "":
            notifikasi += "Masukan Password !\n"
        ## kesalahan saat smtp belum di input
        if smtp == "":
            notifikasi += "Masukan SMTP !\n"
        ## kesalahan saat port belum di masukan
        if port == "":
            notifikasi += "Masukan PORT !\n"
            
        if filename != "":
            # dan yang terpenting adalah
            # mengecek apakah file tersebut 
            # kapasitas size nya di izinkan.
            # dalam hal ini kita bisa menggunakan fungsi baca_ukuran_file()
            # dengan parameter file yang dikirim
            # yang ada di package dwil
            ukuran_file = dwil.baca_ukuran_file(filename)
            ukuran_standar = 5000 ## 5 megabyte (5000 kilobyte)
            if ukuran_file > ukuran_standar:
                notifikasi += "Ukuran file terlalu besar"
        
        # jika noifikasi kosong ini berarti
        # tidak terjadi kesalahan, maka proses
        # pengiriman email akan berlangsung
        if notifikasi == "":
            
            # menggunakan Threading Pool
            # untuk menjaga agar program tidak
            # terlalu berat dalam melakukan proses
            # pengiriman dan menghindari terjadinya
            # not responding program.
            thread.start_new_thread(dwil.sendMail, (filename,sender, reciever, \
            username, password, subject, msg, smtp, port,) )
            
            '''
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(dwil.sendMail,\
            (filename,sender, reciever, \
            username, password, subject, msg, smtp, port))
            
            
            # kita dapat mengecek apakah pengiriman email
            # berhasil. fungsi sendMail() mengembalikan nilai
            # boolean True jika pengiriman berhasil, dan
            # mengembalikan nilai Boolean False jika pengiriman gagal
            mail = async_result.get()
            if mail:
                
                # jika email berhasil di kirim maka
                # tampilkan notifikasi kalau email
                # telah berhasil di kirim
                pesan = "Email Berhasil di kirim ke " + reciever
                notif = wx.MessageDialog(self, pesan, "Berhasil", \
                wx.ICON_INFORMATION)
                notif.ShowModal()
            
            # jika email gagal di kirim maka
            # program akan menampilkan notifikasi kalau
            # email tidak berhasil dikirim
            else:
                pesan = "Terjadi kesalahan pada pengiriman email, silahkan cek kembali"
                pesan += "Password, username beserta port dan SMTP nya"
                notif = wx.MessageDialog(self, pesan, "Berhasil", \
                wx.ICON_ERROR)
                notif.ShowModal()
            '''
        
        # jika notifikasi tidak kosong
        # ini berarti terjadi kesalahan,
        # proses pengiriman tidak akan dilakukan.
        # tampilkan notifikasi ke user
        # agar user tau dimana letak kesalahannya
        else:    
            notif = wx.MessageDialog(self, notifikasi, "Kesalahan Terjadi", \
            wx.ICON_ERROR)
            notif.ShowModal()

    def OnBtn_bersihButton(self, event):
        self.__bersih()
        
        

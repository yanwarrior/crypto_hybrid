#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.lib.buttons
import dwil
import thread
import time

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_BERSIH, 
 wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI, 
 wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI, 
 wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA, 
 wxID_FRAME1BTN_BROWSE_KUNCI_SESI, wxID_FRAME1BTN_DEKRIPSI, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1RICHTEXTCTRL2, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1STSBAR, wxID_FRAME1TXT_DIR_DEKRIPSI, wxID_FRAME1TXT_FILE_DEKRIPSI, 
 wxID_FRAME1TXT_FILE_KUNCI_RAHASIA_RSA, wxID_FRAME1TXT_FILE_KUNCI_SESI, 
 wxID_FRAME1TXT_INFO_ID_KUNCI, wxID_FRAME1TXT_INFO_WAKTU, 
] = [wx.NewId() for _init_ctrls in range(30)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(17, 64), size=wx.Size(499, 534),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hybrid - Dekripsi')
        self.SetClientSize(wx.Size(483, 496))
        self.SetIcon(wx.Icon(u'images/Dakirby309-Windows-8-Metro-Folders-OS-Security-Approved-Metro.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(483, 496),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Kunci : ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 56), size=wx.Size(448, 120), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Kunci Rahasia RSA : ', name='staticText1',
              parent=self.panel1, pos=wx.Point(32, 80), size=wx.Size(100, 13),
              style=0)

        self.txt_file_kunci_rahasia_rsa = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_KUNCI_RAHASIA_RSA,
              name=u'txt_file_kunci_rahasia_rsa', parent=self.panel1,
              pos=wx.Point(32, 96), size=wx.Size(336, 21), style=0, value=u'')
        self.txt_file_kunci_rahasia_rsa.SetEditable(False)

        self.btn_browse_file_kunci_rahasia_rsa = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA,
              label=u'Browse', name=u'btn_browse_file_kunci_rahasia_rsa',
              parent=self.panel1, pos=wx.Point(376, 96), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_kunci_rahasia_rsa.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_kunci_rahasia_rsaButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_KUNCI_RAHASIA_RSA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'File Kunci Sesi RC4 : ', name='staticText2',
              parent=self.panel1, pos=wx.Point(32, 120), size=wx.Size(100, 13),
              style=0)

        self.txt_file_kunci_sesi = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_KUNCI_SESI,
              name=u'txt_file_kunci_sesi', parent=self.panel1, pos=wx.Point(32,
              136), size=wx.Size(336, 21), style=0, value=u'')
        self.txt_file_kunci_sesi.SetEditable(False)

        self.btn_browse_kunci_sesi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_KUNCI_SESI,
              label=u'Browse', name=u'btn_browse_kunci_sesi',
              parent=self.panel1, pos=wx.Point(376, 136), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_kunci_sesi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_kunci_sesiButton,
              id=wxID_FRAME1BTN_BROWSE_KUNCI_SESI)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Informasi Kunci Rahasia : ', name='staticBox2',
              parent=self.panel1, pos=wx.Point(16, 184), size=wx.Size(448, 120),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Modulo N : ', name='staticText3', parent=self.panel1,
              pos=wx.Point(32, 208), size=wx.Size(55, 13), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(32, 224), size=wx.Size(136, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.richTextCtrl1.SetEditable(False)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Eksponen D : ', name='staticText4', parent=self.panel1,
              pos=wx.Point(184, 208), size=wx.Size(67, 13), style=0)

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self.panel1, pos=wx.Point(184, 224), size=wx.Size(136, 64),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl2.SetLabel(u'richText')
        self.richTextCtrl2.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.richTextCtrl2.SetEditable(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='staticText5', name='staticText5', parent=self.panel1,
              pos=wx.Point(48, -160), size=wx.Size(55, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'ID Kunci : ', name='staticText6', parent=self.panel1,
              pos=wx.Point(336, 208), size=wx.Size(50, 13), style=0)

        self.txt_info_id_kunci = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_ID_KUNCI,
              name=u'txt_info_id_kunci', parent=self.panel1, pos=wx.Point(336,
              224), size=wx.Size(88, 21), style=0, value=u'')
        self.txt_info_id_kunci.SetBackgroundColour(wx.Colour(242, 242, 242))
        self.txt_info_id_kunci.SetEditable(False)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'File dan Direktori : ', name='staticBox3',
              parent=self.panel1, pos=wx.Point(16, 312), size=wx.Size(448, 128),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'File yang akan di Dekripsi :', name='staticText7',
              parent=self.panel1, pos=wx.Point(32, 336), size=wx.Size(128, 13),
              style=0)

        self.txt_file_dekripsi = wx.TextCtrl(id=wxID_FRAME1TXT_FILE_DEKRIPSI,
              name=u'txt_file_dekripsi', parent=self.panel1, pos=wx.Point(32,
              352), size=wx.Size(336, 21), style=0, value=u'')
        self.txt_file_dekripsi.SetEditable(False)

        self.btn_browse_file_dekripsi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI,
              label=u'Browse', name=u'btn_browse_file_dekripsi',
              parent=self.panel1, pos=wx.Point(376, 352), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_file_dekripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_file_dekripsiButton,
              id=wxID_FRAME1BTN_BROWSE_FILE_DEKRIPSI)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Direktori Penyimpan File Dekripsi : ', name='staticText8',
              parent=self.panel1, pos=wx.Point(32, 384), size=wx.Size(165, 13),
              style=0)

        self.txt_dir_dekripsi = wx.TextCtrl(id=wxID_FRAME1TXT_DIR_DEKRIPSI,
              name=u'txt_dir_dekripsi', parent=self.panel1, pos=wx.Point(32,
              400), size=wx.Size(336, 21), style=0, value=u'')
        self.txt_dir_dekripsi.SetEditable(False)

        self.btn_browse_dir_simpan_dekripsi = wx.lib.buttons.GenButton(id=wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI,
              label=u'Browse', name=u'btn_browse_dir_simpan_dekripsi',
              parent=self.panel1, pos=wx.Point(376, 400), size=wx.Size(76, 25),
              style=0)
        self.btn_browse_dir_simpan_dekripsi.Bind(wx.EVT_BUTTON,
              self.OnBtn_browse_dir_simpan_dekripsiButton,
              id=wxID_FRAME1BTN_BROWSE_DIR_SIMPAN_DEKRIPSI)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Waktu Yang Dibutuhkan : ', name='staticText9',
              parent=self.panel1, pos=wx.Point(24, 456), size=wx.Size(126, 13),
              style=0)

        self.txt_info_waktu = wx.TextCtrl(id=wxID_FRAME1TXT_INFO_WAKTU,
              name=u'txt_info_waktu', parent=self.panel1, pos=wx.Point(160,
              456), size=wx.Size(48, 21), style=0, value=u'')
        self.txt_info_waktu.SetEditable(False)
        self.txt_info_waktu.SetBackgroundColour(wx.Colour(242, 242, 242))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Detik', name='staticText10', parent=self.panel1,
              pos=wx.Point(224, 456), size=wx.Size(25, 13), style=0)

        self.btn_dekripsi = wx.Button(id=wxID_FRAME1BTN_DEKRIPSI,
              label=u'Dekripsi', name=u'btn_dekripsi', parent=self.panel1,
              pos=wx.Point(376, 448), size=wx.Size(83, 32), style=0)
        self.btn_dekripsi.Bind(wx.EVT_BUTTON, self.OnBtn_dekripsiButton,
              id=wxID_FRAME1BTN_DEKRIPSI)

        self.btn_bersih = wx.Button(id=wxID_FRAME1BTN_BERSIH, label=u'Bersih',
              name=u'btn_bersih', parent=self.panel1, pos=wx.Point(296, 448),
              size=wx.Size(75, 32), style=0)
        self.btn_bersih.Bind(wx.EVT_BUTTON, self.OnBtn_bersihButton,
              id=wxID_FRAME1BTN_BERSIH)

        self.stsbar = wx.StatusBar(id=wxID_FRAME1STSBAR, name=u'stsbar',
              parent=self.panel1, style=0)
        self.stsbar.SetStatusText(u'Status : None')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtn_browse_file_kunci_rahasia_rsaButton(self, event):
        '''tombol mencari file kunci rahasia'''
        # set filename kunci rahasia di file_kunci_rahasia
        # dimana nilai ini merupakan nilai yang diambil
        # dari dwil.get_file(['key']), hanya di izinkan
        # file berekstensi .key nya saja yang bisa di ambil
        # ini berarti penyaringan file.
        file_kunci_rahasia = dwil.get_file(['key'])
        
        # setelah file_kunci_rahasia kita dapatkan
        # masukan nilainya ke self.txt_file_kunci_rahasia_rsa
        self.txt_file_kunci_rahasia_rsa.SetValue(file_kunci_rahasia)
        
        # proses pembacaan file kunci rahasia 
        # akan dilakukan oleh method baca_kunci_rsa(self, filekunci)
        # dari kelas System_File yang ada di paket dwil.
        # nilai kuncinya akan kita tampung ke dalam
        # variabel list (karena return daru method tersebut berupa list)
        # dengan index 0 adalah id kunci nya
        # dengan index 1 adalah nilai modulo N nya
        # dengan index 2 adalah nilai eksponen D nya
        data_kunci_rahasia = dwil.System_File()
        list_data_kunci_rahasia = data_kunci_rahasia.baca_kunci_rsa(file_kunci_rahasia)
        
        # kita set masing-masing nilai
        # berdasarkan index list_data_kunci_rahasia
        nilai_d = list_data_kunci_rahasia[2]
        nilai_n = list_data_kunci_rahasia[1]
        nilai_id = list_data_kunci_rahasia[0]
        
        # setelah itu kita akan menampilkan isi dari
        # file kunci rahasia rsa ke self.richTextCtrl1 (modulo n)
        # self.richTextCtrl2 (eksponen d) dan ke
        # self.txt_info_id_kunci (id kuncinya)
        ## tampilkan modulo N
        self.richTextCtrl1.SetValue(nilai_n)
        ## tampilkan eksponen D
        self.richTextCtrl2.SetValue(nilai_d)
        ## tampilkan id kunci rahasia 
        ## namun sebelumnya harus di hilangkan terlebih dahulu
        ## karakter '\n' nya
        nilai_id = nilai_id.replace("\n","")
        self.txt_info_id_kunci.SetValue(nilai_id)

    def OnBtn_browse_kunci_sesiButton(self, event):
        '''tombol ini kalo di teken bakal 
        ngejalanin perinteh buat nyari file session
        dengan penyaringan file hanya file berekstensi .key ajah'''

        # setelah nilai tersebut kita dapatkan dan 
        # kita tampung ke dalam file_kunci_sesi
        # maka nilai kunci sesi masih dalam ke adaan ter-enkripsi.
        # proses selanjutnya adalah mendekripsi file kunci sesi tersebut
        # dengan kunci rahasia rsa yang sudah dibuat sebelumnya.
        # dengan syarat kunci tersebut harus tersedia dengan
        # mengambil nilai url kunci rahasia rsa tersebut dari
        # self.txt_file_kunci_rahasia_rsa. kalau txt tersebut
        # masih kosong, maka program akan mengeluarkan notifikasinya
        # kalau anda harus mengisi kunci rahasia terlebih dahulu
        ## cek kunci rahasia
        if self.txt_file_kunci_rahasia_rsa.GetValue() == "":
            
            ## memberikan notifikasi
            notifikasi = "maaf, anda perlu menyertakan kunci rahasia RSA"
            notif = wx.MessageDialog(self,notifikasi, "Notifikasi", wx.OK)
            notif.ShowModal()
            
        ## jika kunci rahasia sudah di sertakan maka lakukan
        ## proses berikut untuk mendekripsi kunci sesi RC4-nya
        else:
            # memakai fungsi get_file() yang ade
            # di dalem file misc dimana ntu udeh di
            # daftarin ke package dwil.
            # fungsi ini mengembalikan nilai tempat dimana 
            # file kunci session berada yang kita pilih
            # misalnya D:/kunci/kunci_session.key
            # nilainya akan di tampung di variabel
            # file_kunci_sesi dalam bentuk string
            file_kunci_sesi = dwil.get_file(['key'])
            
            # mengambil nilai modulo N dan eksponen D
            # dari self.richTextCtrl1 dan self.richTextCtrl2
            # dan mengesetnya di dalam variabel n dan d
            # dengan memformatnya ke bentuk integer
            n = int(self.richTextCtrl1.GetValue())
            d = int(self.richTextCtrl2.GetValue())
            
            # mengambil nilai-nilai kunci sesi rc4
            # untuk di dekripsi dengan method dekripsi
            # dari sebuah class RSA() pada paket dwil
            with open(file_kunci_sesi,"rb") as f:
                ## masukan ke dalam variabel block_chiper 
                block_chiper = f.read()
            ## split dari spasi dan block_chiper menjadi list
            block_chiper = block_chiper.split(" ")
            ## waktunya dekripsi
            dek = dwil.RSA()
            dekrip = dek.dekripsi(block_chiper, n, d)
            ## hasilnya di tampilkan di self.txt_file_kunci_sesi
            self.txt_file_kunci_sesi.SetValue(dekrip)

    def OnBtn_browse_file_dekripsiButton(self, event):
        '''tombol ini digunakan untuk mencari dokumen yang
        akan di dekripsi oleh kunci sesi yang telah di dekripsi
        oleh RSA Kunci Publik'''
        # mencari file yang akan di enkripsi
        # dengan menggunakan fungsi get_file(list_allow_file)
        # yang nantinya url dari file tersebut akan di simpan
        # kedalam variabel file_dek
        list_allow_file =  ['doc','docx','xls','xlsx','jpeg',\
        'JPEG','jpg','JPG','png','PNG','gif','GIF','ppt','pptx','mp3']
        file_dek = dwil.get_file(list_allow_file)
        
        # cek apakah file lebih dari 5 mb ?
        # dengan menggunakan baca_ukuran_file(filename)
        # pada package dwil. jika file lebih besar
        # dari allow_size yang ditentukan
        # maka program akan menampilkan notifikasi
        # bahwa file dengan size tersebut tidak di izinkan
        allow_size = 5000 ## 5000 kilobyte
        if dwil.baca_ukuran_file(file_dek) > allow_size:
            ## tampilkan notifikasi
            notifikasi = "Maaf ukuran file terlalu besar. "
            notifikasi += "program ini hanya di rekomendasikan untuk kapasitas"
            notifikasi += " size file di bawah 5 Mb"
            notif = wx.MessageDialog(self, notifikasi, "Perhatian !",wx.CANCEL)
            notif.ShowModal()
        else:
            # jika file memenuhi syarat dalam ukuran
            # yang sesuai dengan ukuran yang di izinkan
            # maka :
            # tampilkan url file_dek ke dalam
            # self.txt_file_dekripsi
            self.txt_file_dekripsi.SetValue(file_dek)

    def OnBtn_browse_dir_simpan_dekripsiButton(self, event):
        '''tombol ini digunakan untuk melakukan proses
        untuk mencari direktori tempat penyimpanan file hasil
        dekripsi'''
        # mencari direktori dengan fungsi get_dir
        # pada package dwil. string direktori tersebut
        # akan ditampung ke dalam variabel dir_simpan
        dir_simpan = dwil.get_dir()
        
        # selanjutnya dir_simpan akan di tampilkan
        # ke self.txt_dir_dekripsi
        self.txt_dir_dekripsi.SetValue(dir_simpan)

    def OnBtn_dekripsiButton(self, event):
        '''tombol ini digunakan untuk mendekrip file'''
        # gunakan threading
        thread.start_new_thread(self.__dekrip, ("",))
            
    def __freeze(self):
        self.Disable()
    
    def __not_freeze(self):
        self.Enable()
    
    def __dekrip(self,x):
        
        # set time
        start_time = time.time()
        
        # pertama yang harus dilakukan adalah
        # mengecek beberapa elemen dari nilai yang kosong
        # ini digunakan karena proses ini 
        # membutuhkan nilai dari elemen2 tersebut
        # pengecekan pertama adalah pengecekan 
        # 1. cek isi rc4 kunci sesi
        # 2. cek isi file yang akan di dekrip
        # 3. cek isi direktori yang akan dijadikan tempat penyimpanan
        #    file hasil dekripsi
        # dari pengecekan tersebut, jika terdapat
        # data yang kosong, maka program akan
        # menampilkan notifikasi sesuai kesalahahnya
        # agar user bisa tau dimana terjadi kesalahan.
        ## kunci sesi
        kunci_sesi = self.txt_file_kunci_sesi.GetValue()
        ## file yang akan di enkripsi
        file_dekrip = self.txt_file_dekripsi.GetValue()
        ## direktori penyimpanan hasil dekripsi file
        dir_simpan = self.txt_dir_dekripsi.GetValue()
        ## variabel notifikasi
        notifikasi = ""
        ## pengecekan berlangsung
        if kunci_sesi == "":
            notifikasi += "File Kunci sesi belum di set\n"
        if file_dekrip == "":
            notifikasi += "Sertakan File yang akan di dekripsi\n"
        if dir_simpan == "":
            notifikasi += "Sertakan direktori tempat penyimpanan file hasil dekripsi\n"
        ## cek apakah ada notifikasi kesalahan
        if notifikasi != "":
            ## berarti terdapat kesalahan, kita tampilkan
            ## dalam bentuk modal dialog
            ## agar user tau kesalahannya dimana
            notif = wx.MessageDialog(self,notifikasi, "Kesalahan Terjadi", wx.CANCEL)
            notif.ShowModal()
        ## jika notifikasi tidak ada, maka proses dekripsi 
        ## akan berlangsung
        else:
            self.stsbar.SetStatusText("Status : Proses Dekripsi Dimulai")
            self.__freeze()
            # proses pertama, mengambil data 
            # dari file yang di duga telah di enkripsi
            # atau file yang mau di dekripsi.
            file_dekrip = self.txt_file_dekripsi.GetValue()
            
            # selanjutnya, mengambil nama filenya
            # lalu mengambil nama ekstensi file tersebut
            # dan dimasukan ke dalam dua variabel 
            # yakni variable ext dan nama_file.
            # kita menggunakan dua fungsi, 
            # fungsi untuk mengambil ekstensi file 
            # yaitu ambil_ekstensi_file(filename)
            # dan fungsi untuk mengambil nama file
            # yaitu ambil_nama_file(filename)
            # yang dua fungsi itu berada pada satu package
            # yaitu package dwil.
            file_asli = self.txt_file_dekripsi.GetValue()
            ## ambil ekstensi file
            ext = dwil.ambil_ekstensi_file(file_asli)
            ## ambil nama file 
            nama_file = dwil.ambil_nama_file(file_asli)
            
            # proses berikutnya adalah mengambil semua 
            # data-data biner dalam file tersebut
            # yang datanya akan dimasukan kedalam
            # variabel data_dekrip (string)
            
            with open(file_asli, "rb") as f:
                data_dekrip = f.read()
                
            # menyiapkan password simetris dari
            # kunci sesi yang akan di masukan 
            # kedalam variabel kunci_sesi
            kunci_sesi = self.txt_file_kunci_sesi.GetValue()
            
            # menyiapkan nama file yang akan
            # digunakan untuk menyimpan kembali
            # file hasil dekripsi
            nama_file_dekrip = self.txt_dir_dekripsi.GetValue() + "dekripsi-" + \
            nama_file
            
            # proses enkripsi dimulai
            # dengan fungsi rc4_crypt
            # yang ada di package dwil
            datapulih = dwil.rc4_crypt(data_dekrip ,kunci_sesi)
            
            # hasilnya akan di simpan kembali
            # sesuai format filenya
            # dari data yang telah di dekripsi (dipulihkan)
            # dengan rc4
            with open(nama_file_dekrip, "wb") as fd:
                fd.write(datapulih)
            self.stsbar.SetStatusText("Status : Proses Dekripsi Selesai")
            # setelah selesai tampilkan notifikasi
            # bahwa file berhasil di dekripi
            # dan berikan juga tempat penyimpanan file dekripsi tersebut
            notifikasi = "File berhasil di dekripsi dengan kunci " + kunci_sesi
            notifikasi += " ,silahkan cek di " + nama_file_dekrip
            notif = wx.MessageDialog(self,notifikasi,"Sukses Dekripsi", wx.OK)
            notif.ShowModal()
            self.stsbar.SetStatusText("Status : None")
            self.__not_freeze()
            # set end time
            end_time = time.time() - start_time
            self.txt_info_waktu.SetValue(str(end_time))
            
    def __bersih(self):
        self.txt_dir_dekripsi.SetValue("")
        self.txt_file_dekripsi.SetValue("")
        self.txt_file_kunci_rahasia_rsa.SetValue("")
        self.txt_file_kunci_sesi.SetValue("")
        self.txt_info_id_kunci.SetValue("")
        self.txt_info_waktu.SetValue("")
        self.richTextCtrl1.SetValue("")
        self.richTextCtrl2.SetValue("")

    def OnBtn_bersihButton(self, event):
        self.__bersih()            
        
            
        
        
        
        
        
        
            
            
        
        
        

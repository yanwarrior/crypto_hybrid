#-------------------------------------------------------------------------------
# Name:        excel_util
# Purpose:
#
# Author:      neng dwil
#
# Copyright:   (c) neng dwil 2014
# Licence:     Free Licence
#-------------------------------------------------------------------------------
import xlrd, datetime
'''
################################################################################
@ LANGKAH KONVERSI EXCEL TO MYSQL  - jurnal python 2014 - new implem
    - by yanzen
################################################################################

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
STEP 1      |   *stepworkinexcel                                               |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1.  mengambil jumlah row pada excel
    ===============================
    simpan datanya di sebuah variabel bernama row_excel dimana
    datanya berupa banyaknya row pada excel.
    row_excel = row - 1

2.  mengambil jumlah col pada excel
    ===============================
    simpan datanya di sebuah variabel bernama col_excel dimana
    datanya berupa banyaknya kolom pada file excel.
    col_excel = col - 1

3.  mengambil nilai (nama) header field
    ===================================
    dalam format yang ditentukan (secara umum), nama header field
    dari excel ada pada rentang row[0] dan col[col_excel].
    simpan datanya dalam bentuk array atau list di variabel list_field_excel.
    list_field_excel = cell_value(row[0],col[col_excel])

4.  mengambil tipe data pada isi di index 1 (not zero)
    ==================================================
    di python pada module xlrd telah ditentukan format data
    berdasarkan nilai dari suatu cell tertentu.
    0 : Empty
    1 : Text
    2 : Number
    3 : Date
    4 : Boolean
    5 : Error
    6 : Blank
    langkahnya adalah menyaring isi data pada index pertama (setelah field).
    simpan ke dalam sebuah variabel data_type_excel. dalam hal ini row berada
    pada index ke 1 atau di singkat row[1], ambil sebanyak col_excel.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
STEP 2      |   *stepworkinmysql                                               |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1.  mengambil jumlah field pada sebuah tabel
    ========================================
    simpan datanya ke dalam variabel tbl_field. misalnya
    tbl_field = 4

2.  mengambil nilai (nama) field pada suatu tabel
    =============================================
    simpan nilainya ke dalam variabel tbl_name_field dalam bentuk list array.
    misalnya tbl_name_field = ['ID','NAME','EMAIL','AGE']

3.  mengambil tipe data pada tiap-tiap field
    ========================================
    simpan nilainya ke dalam variabel tbl_type_field dalam bentuk list array.
    kita bulatkan saja untuk tipe data yang mengandung bilangan yakni ke Number
    misalnya tbl_type_field =['Number','Text','Date']

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
STEP 3      |   *stepcomparedata                                               |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1.  membandingkan col_excel dengan tbl_field
2.  membandingkan list_field_excel dengan tbl_name_field    --> extreme method
3.  membandingkan data_type_excel dengan tbl_type_field

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
STEP 4      |   *stepinsertidata                                               |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1.  masukan semua data dari excel ke mysql tabel jika step ketiga
    memenuhi syarat.

'''

class ExcelUtil:

    def __init__(self, excelFile):
        self.__excelFile = excelFile
        self.__book = xlrd.open_workbook(excelFile)
        self.__allSheets = self.__book.sheet_names()
        self.__dataType = [0, 1, 2, 3, 4, 5, 6]


    def getAllSheets(self):
        '''return list all sheets in excel'''
        self.__allSheets = [str(i) for i in self.__allSheets]
        return self.__allSheets

    def getColsInExcel(self,sheetName):
        '''return Cols In Excel'''
        worksheet = self.__book.sheet_by_name(sheetName)
        numCols = worksheet.ncols
        return numCols

    def getRowsInExcel(self,sheetName):
        '''return int Rows in excel'''
        worksheet = self.__book.sheet_by_name(sheetName)
        numRows = worksheet.nrows - 1
        return numRows

    def getHeaderFieldNameExcel(self, sheetName, endCols, startRows=0):
        '''return string list field excel name'''
        worksheet = self.__book.sheet_by_name(sheetName)
        headerField = []
        for i in range(endCols):
            headerField.append(str(worksheet.cell_value(rowx=startRows, colx=i)).upper())
        return headerField

    def getDataTypeExcel(self, sheetName, endCols, startRows=1):
        '''return string data Type excel value
            0 : Empty
            1 : Text
            2 : Number
            3 : Date
            4 : Boolean
            5 : Error
            6 : Blank
        '''
        worksheet = self.__book.sheet_by_name(sheetName)
        dataType = []
        for i in range(endCols):
            typeData = int(worksheet.cell_type(rowx=startRows, colx=i))
            dataType.append(typeData)

        for i,d in enumerate(dataType):
            if      d == 0:    dataType[i] = 'Empty'.upper()
            elif    d == 1:    dataType[i] = 'Text'.upper()
            elif    d == 2:    dataType[i] = 'Number'.upper()
            elif    d == 3:    dataType[i] = 'Date'.upper()
            elif    d == 4:    dataType[i] = 'Boolean'.upper()
            elif    d == 5:    dataType[i] = 'Error'.upper()
            elif    d == 6:    dataType[i] = 'Blank'.upper()
        return dataType

    def excelConvert(self, sheet, header):
        workbook = self.__book
        worksheet = workbook.sheet_by_name(sheet)
        num_rows = worksheet.nrows - 1


        num_cells = worksheet.ncols - 1
        if header:
            curr_row = 0
        else:
            curr_row = -1
        data_front = []
        data_in = []
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            print 'Row:', curr_row
            curr_cell = -1
            while curr_cell < num_cells:
                curr_cell += 1
                '''
                0 : Empty
                1 : Text
                2 : Number
                3 : Date
                4 : Boolean
                5 : Error
                6 : Blank
                '''
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = worksheet.cell_type(curr_row, curr_cell)
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                if cell_type == 0:
                    data_in.append('Empty')
                if cell_type == 1:
                    data_in.append(str(cell_value))
                if cell_type == 2:
                    data_in.append(str(int(cell_value)))
                if cell_type == 3:
                    a1_as_datetime = \
                    datetime.datetime(*xlrd.xldate_as_tuple(cell_value, workbook.datemode))
                    data_in.append(str(a1_as_datetime).split(" ")[0])
                if cell_type == 4:
                    data_in.append(str(cell_value))
                if cell_type == 5:
                    data_in.append('Null')
                if cell_type == 6:
                    data_in.append('')

            data_front.append(data_in)
            data_in = []

        return data_front






'''

## contoh penggunaan
excel = ExcelUtil("D:/book.xls")
sheets = excel.getAllSheets()

# mengambil jumlah col pada excel
cols = excel.getColsInExcel(sheets[0])
# mengambil jumlah row pada excel
rows = excel.getRowsInExcel(sheets[0])
# mengambil nilai (nama) header field
print excel.getHeaderFieldNameExcel(sheets[0],cols)
# mengambil tipe data pada isi di index 1 (not zero)
print excel.getDataTypeExcel(sheets[0],cols,startRows=1)
'''


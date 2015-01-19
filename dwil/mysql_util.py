#-------------------------------------------------------------------------------
# Name:        mysql_util
# Purpose:
#
# Author:      neng dwil
#
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
'''
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
'''
try:
    import MySQLdb
except ImportError:
    print "Anda Belum Menginstall Module MySQLdb"


class MySqlUtil:

    def __init__(self, host, user, password, dbnm):
        self.__objSql = MySQLdb.connect(host, user, password, dbnm)
        self.__cursor = self.__objSql.cursor()

        self.__numericType = [\
                                'int',\
                                'tinyint',\
                                'smallint',\
                                'mediumint',\
                                'biginteger',\
                                'float',\
                                'double',\
                                'decimal'\
                            ]

        self.__dateType = [\
                                'date',\
                                'datetime',\
                                'timestamp',\
                                'time','year'\
                            ]
        self.__textType = [\
                                'char',\
                                'varchar',\
                                'blob','text',\
                                'tinyblob',\
                                'mediumblob',\
                                'longblob','enum'\
                            ]


    def getNumFieldInTable(self, tableName):
        '''get Num Field in Table'''
        sql = """ SHOW COLUMNS FROM %s """ % tableName
        self.__cursor.execute(sql)
        data = []
        num = self.__cursor.fetchall()
        return len(num)


    def getFieldValueInTable(self,tableName):
        '''get Field Value in Table'''
        sql = """ SHOW COLUMNS FROM %s """ % tableName
        self.__cursor.execute(sql)
        data = []
        fields = self.__cursor.fetchall()
        for i in fields:
            for j in i:
                par = j
                break
            data.append(par.upper())
        return data

    def getDataTypeInField(self, tableName):
        '''get data type field value in table'''
        sql = """ SHOW COLUMNS FROM %s """ % tableName
        self.__cursor.execute(sql)
        data = ''
        fields = self.__cursor.fetchall()
        dataType = []

        for i,d in enumerate(fields):
            for j in d:
                data = d[1]
                break
            dataType.append(data)

        cari = '('
        for i,d in enumerate(dataType):
            index = d.find(cari)
            dataType[i] = d[:index]

        for i,d in enumerate(dataType):
            if d in self.__numericType:
                dataType[i] = 'NUMBER'
            elif d in self.__dateType:
                dataType[i] = 'DATE'
            elif d in self.__textType:
                dataType[i] = 'TEXT'

        return dataType

    def testConnection(self):
        try:
            self.__cursor.execute("SELECT VERSION()")
            results = self.__cursor.fetchone()
            # Check if anything at all is returned
            if results:
                return True
            else:
                return False
        except MySQLdb.Error:
            print "ERROR IN CONNECTION"
        return False

    def exportExcelMySQL(self, excelDataList, tableName):
        # Prepare SQL query to INSERT a record into the database.
        try:
            for index,i in enumerate(excelDataList):
                r = "%s," * len(excelDataList[index])
                var_string = r[:-1]
                sql = "INSERT INTO %s VALUES (%s);" % (tableName,var_string)
                self.__cursor.execute(sql,excelDataList[index])
                self.__objSql.commit()
            self.__objSql.close()
            return True
        except:
            return False



'''

data = [['12345', 'Yanwar', '22'], ['234543', 'zensu', '34']]
db = MySqlUtil('localhost', 'root', '', 'dblatihan')
db.exportExcelMySQL(data, 'mahasiswa')
'''
'''
## cara menggunakan MySqlUtil
# buat objek
obj = MySqlUtil('localhost','root','','kantor')
# mengambil jumlah field pada sebuah tabel
obj.getNumFieldInTable('pegawai')
# mengambil nilai (nama) field pada suatu tabel
print obj.getFieldValueInTable('pegawai')
# mengambil tipe data pada tiap-tiap field
obj.getDataTypeInField('pegawai')
'''















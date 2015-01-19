#-------------------------------------------------------------------------------
# Name:        compare_excsql
# Purpose:
#
# Author:      neng dwil
#
# Copyright:   (c) neng dwil 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
STEP 3      |   *stepcomparedata                                               |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1.  membandingkan col_excel dengan tbl_field
2.  membandingkan data_type_excel dengan tbl_type_field
'''

class CompareExcel2Mysql:

    def compareCols(self, numColsExcel, numColsSql):
        '''return boolean if both values not the same'''
        if numColsExcel == numColsSql:
            return True
        else:
            return False

    def compareDataType(self, dataTypeExcel, dataTypeSQL):
        result = True
        if len(dataTypeExcel) != len(dataTypeSQL):
            result = False
        else:
            for i in range(len(dataTypeExcel)):
                if dataTypeExcel[i] == dataTypeSQL[i]:
                    result = True
                else:
                    result = False
                    break

        return result



'''
['ID', 'HARI', 'JUMLAH', 'GODAR', 'UMUR', 'TANGGAL']
['KODEPEGAWAI', 'NAMAPEGAWAI', 'JENISKELAMIN']
'''
'''

dataTypeExcel = ['TEXT', 'NUMBER', 'NUMBER', 'TEXT', 'NUMBER', 'DATE']
dataTypeSQL = ['TEXT', 'NUMBER', 'NUMBER', 'TEXT', 'NUMBER', 'DATE']

check = CompareExcel2Mysql()
hasil = check.compareDataType(dataTypeExcel,dataTypeSQL)
print hasil
'''
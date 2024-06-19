import openpyxl
wb = openpyxl.Workbook() #capital W Creates new workbook wb
#print(wb.sheetnames())
print(type(wb))

sheet = wb['Sheet']

sheet ['A1'].value  
print(sheet ['A1'].value == None) 

sheet['A1'] = 42
sheet['A2'] = 'Hello'

import os
os.chdir('D:\\Python Projects\\Automate Boring Stuff With Python')
wb.save('example editted.xlsx')
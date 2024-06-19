import PyPDF2
import os
os.chdir('D:\Python Projects\Automate Boring Stuff With Python')

pdfFile = open('Massage For Dummies - for dummies.pdf', 'rb')
#pdfs are binary files there read-binary

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getNumPages
print(reader.numPages)
print(page)


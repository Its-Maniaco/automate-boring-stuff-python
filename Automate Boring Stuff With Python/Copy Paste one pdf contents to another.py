#Copy Paste one pdf contents to another

import PyPDF2, os

os.chdir("D:\Python Projects\Automate Boring Stuff With Python")
pdf1File = open ("Massage For Dummies - for dummies.pdf", 'rb')
pdf2File = open ("Google Privacy post.pdf", 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter(  )   
for pageNum in range (reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range (reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combined2PDF.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close( )
pdf2File.close()
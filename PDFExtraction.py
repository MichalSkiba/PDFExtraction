import PyPDF2

pdfFileObj = open('C:\\Users\\Developer\\Downloads\\t450 schemat.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


def podziel(poczatek, koniec):
    writer = PyPDF2.PdfFileWriter()
    if koniec > pdfReader.numPages-1 or poczatek < 0:
        print('PDF Nie posiada tylu stron')
    else:
        for x in range(poczatek, koniec):
            writer.addPage(pdfReader.getPage(x))
            pdfOutputFile = open('MergedFiles.pdf', 'wb')
        writer.write(pdfOutputFile)
        pdfOutputFile.close()
        pdfFileObj.close()


podziel(5, 10)
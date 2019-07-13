/*Function Name - data_splitter
This python function will returns data as list, this is exract data from pdf page by page and appending it in a list*/

import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

def data_splitter(path):
    data = [] 
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(fname, page+1) 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))
        pdfFileObj = open(output_filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        data.append(pageObj.extractText())
    return data

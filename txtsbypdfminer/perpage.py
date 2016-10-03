from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
import sys
from pdfminer.layout import LAParams

print "load"
# Open a PDF file.
fp = open('D:\\xionpdf\\xion.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Process each page contained in the document.
print "write"
i = 0
for page in PDFPage.create_pages(document):
    i += 1
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    outfp = file("D:\\xionpdf\\xionpdf_pdfminer_outputs\\txt_pages\\p"+str(i)+".txt", "w")
    device = TextConverter(rsrcmgr, outfp, codec="utf-8", laparams = LAParams())
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    interpreter.process_page(page)
    
    device.close()
    outfp.close()

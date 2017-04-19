import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from gtts import gTTS
import os

def pdfparser(data):
    xyz=data
    fp = file(data, 'rb')
    # Process each page contained in the document.
    i=0

    for page in PDFPage.get_pages(fp):
        i=i+1 
        print("page No."+str(i) )
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        
        interpreter.process_page(page)
        pt = retstr.getvalue()
        print(pt)
        tts = gTTS(text=pt, lang='en')
        fn = xyz+"_page_"+str(i)+".mp3";
        tts.save(fn)
        #retstr= StringIO()
        #data =  retstr.getvalue()
        
    #tts = gTTS(text=data, lang='en')
    #fn = xyz+".mp3"
    #tts.save(fn)
    #print (data)

if __name__ == '__main__':
    pdfparser(sys.argv[1])
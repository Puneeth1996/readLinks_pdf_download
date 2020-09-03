from glob import glob
import os, shutil
import pikepdf

PATH = r'C:\Users\punee\Desktop\readLinks_pdf_download\test'
EXT = "*.pdf"
temp_cfn = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
urls = []
for file in temp_cfn:
    pdf_file = pikepdf.Pdf.open(file)
    for page  in pdf_file.pages:
        for annots in page.get('/Annots'):
            uri = annots.get('/A').get('/URI')
            if(uri is not None):
                print( "\n\n", '[FILE] '+ str(file) +'\n [+] URL FOUND ' , uri, "\n\n" )
                urls.append(urls)

print("[*] Total URLs extracted:", len(urls))

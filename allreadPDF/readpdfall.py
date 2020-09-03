from glob import glob
import os, shutil
import csv
import sys, re
import time
import collections
import dateutil.parser
from datetime import datetime
import dateparser
import pandas as pd
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
                print(' [+] URL FOUND ', uri)
                urls.append(urls)

print("[*] Total URLs extracted:", len(urls))

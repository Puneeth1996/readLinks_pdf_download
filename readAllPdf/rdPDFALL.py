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


PATH = r'C:\Users\punee\Desktop\readLinks_pdf_download\test'
EXT = "*.pdf"
temp_cfn = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

for fle in temp_cfn:
    print(fle)


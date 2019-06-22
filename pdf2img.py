from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string
import re
import datetime
from xlwt import Workbook

pages = convert_from_path('/home/ujjwal/Downloads/Invoice.pdf', 500)

for page in pages:
    newimg=page.resize((2000,2000))
    newimg.save('taegu.png', 'PNG')

image = Image.open('taegu.png', mode='r')

res=image_to_string(image)
#print(res)
f=open("/home/ujjwal/taegu","a")
f.write(res)
with open("/home/ujjwal/taegu",'r+') as myfile:
    i=0
    for line in myfile:
        GSTIN_Bill_to_Party_s=GSTIN_Ship_to_Party_s=gst_s=re.search(r'GSTIN No. (\S+)',line)
        state_code_s=re.search(r'State Cod (\S+)',line)
        invoice_no_s=re.search(r'tak (\S+)',line)
        invoice_date_s=re.search(r'ENS',line)
        Place_of_Supply_s=Place_of_Supply_s=Ship_to_party_s=re.search(r'(Shipped To)',line)
        tml_po_s=re.search(r'PO',line)
        hsn_s=re.search(r'HSN',line)
        Description_goods=re.search(r'(1)',line)







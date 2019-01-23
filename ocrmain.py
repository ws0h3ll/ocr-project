from pytesseract import image_to_string
from PIL import Image
from simpleocrscan import simplescanmulti, simplescansing
from google import gsrch, gsrchocr
print("########MENU########")
print("Simple scan (ss)")
print("Find a webpage (gs)")
print("########MENU########")
wttd = raw_input("What would you like to do ? ")
if str(wttd) == "ss":
    wttds = raw_input("Single (s) or multiple images (ms) : ")
    if wttds == "s":
        simplescansing()
    if wttds == "ms":
        simplescanmulti()
elif str(wttd) == "gs":
    gsrchocr()

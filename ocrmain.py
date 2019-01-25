#modules
from pytesseract import image_to_string 
from PIL import Image
from simpleocrscan import simplescanmulti, simplescansing
from google import gsrch, gsrchocr
# start of code
print("########MENU########")
print("Simple scan (ss)")
print("Find a webpage (gs)")
print("########MENU########")
wttd = raw_input("What would you like to do ? ") # add input sanitisation here !!!!
if str(wttd) == "ss":
    wttds = raw_input("Single (s) or multiple images (ms) : ") # two diff functions to either recurse through files or just do one file on its own
    if wttds == "s": # single image
        simplescansing()
    if wttds == "ms": # multiple images
        simplescanmulti()
elif str(wttd) == "gs":
    gsrchocr() # google search module (imported from local file)

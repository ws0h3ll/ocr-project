def simplescanmulti():
    doimg = True
    cnt = 1
    while doimg == True:
        pathtoimg = raw_input("Path to image to OCR : ")
        read = image_to_string(Image.open(pathtoimg), lang='eng')
        print("Text for image number " + str(cnt) + " is : " + read)
        print("--------------------------------------------- \n")
        cnt += 1
        cont = raw_input("Would you like to exit ? (y/n) ")
        if str(cont).lower == "y":
            doimg = False
            print("Goodbye")
        elif str(cont).lower == "n":
            doimg = True
            print("--------------------------------------------- \n")
            next
def simplescansing():
    pathtoimg = raw_input('Path to image to OCR : ')
    read = image_to_string(Image.open(pathtoimg), lang='eng')
    print(read)

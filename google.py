def gsrch(q):
    selected = False
    import webbrowser
    try:
        from googlesearch import search
    except ImportError:
        print("Google isnt install properly")
    num = 1
    b = ""
    c= ""
    d = ""
    e = ""
    f = ""
    for a in search(query=q, tld="co.in", num=5, stop=1, pause=2):
        if num == 1:
            b = a
        if num == 2:
            c = a
        if num == 3:
            d = a
        if num == 4:
            e = a
        if num == 5:
            f = a
            break
        num += 1
    print("------------------------------------")
    print("The first result was : " + b)
    print("------------------------------------")
    print ("The second result was : " + c)
    print("------------------------------------")
    print("The third result was : " + d)
    print("------------------------------------")
    print("The fourth result was : " + e)
    print("------------------------------------")
    print("The fith result was : " + f)
    print("------------------------------------")
    choice = raw_input("Which would you like to open ? (1,2,3,4,5)")
    print("------------------------------------")
    if choice == "1":
        webbrowser.open(b)
        selected = True
    if choice == "2":
        webbrowser.open(c)
        selected = True
    if choice == "3":
        webbrowser.open(d)
        selected = True
    if choice == "4":
        webbrowser.open(e)
        selected = True
    if choice == "5":
        webbrowser.open(f)
        selected = True
    if selected == False:
        print("Incorrect input")

def gsrchocr():
        from pytesseract import image_to_string
        from PIL import Image
        pathtoimg = raw_input("Path to image to OCR : ")
        read = image_to_string(Image.open(pathtoimg), lang='eng')
        selected = False
        import webbrowser
        try:
            from googlesearch import search
        except ImportError:
            print("Google isnt install properly")
        num = 1
        b = ""
        c= ""
        d = ""
        e = ""
        f = ""
        for a in search(query=read, tld="co.in", num=5, stop=1, pause=2):
            if num == 1:
                b = a
            if num == 2:
                c = a
            if num == 3:
                d = a
            if num == 4:
                e = a
            if num == 5:
                f = a
                break
            num += 1
        print("------------------------------------")
        print("The first result was : " + b)
        print("------------------------------------")
        print ("The second result was : " + c)
        print("------------------------------------")
        print("The third result was : " + d)
        print("------------------------------------")
        print("The fourth result was : " + e)
        print("------------------------------------")
        print("The fith result was : " + f)
        print("------------------------------------")
        choice = raw_input("Which would you like to open ? (1,2,3,4,5)")
        print("------------------------------------")
        if choice == "1":
            webbrowser.open(b)
            selected = True
        if choice == "2":
            webbrowser.open(c)
            selected = True
        if choice == "3":
            webbrowser.open(d)
            selected = True
        if choice == "4":
            webbrowser.open(e)
            selected = True
        if choice == "5":
            webbrowser.open(f)
            selected = True
        if selected == False:
            print("Incorrect input")

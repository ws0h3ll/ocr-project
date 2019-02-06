import urllib
opener = urllib.FancyURLopener({})
url = raw_input('Which url would you like to open? ')
f = opener.open(url)
a = f.read()
print(a)

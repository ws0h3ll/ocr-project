from ftplib import FTP
session = FTP('')
file = open('file','rb')
session.storbinary('STOR file', file)
while 1:
    filename = raw_input('Which file would you like to download ? ')
    if filename == 'n':
        break
    session.retrbinary("RETR " + filename, open(filename, 'wb').write)

session.retrlines('LIST')
file.close()
session.close()

import pyqrcode
import png
from pystyle import Colors, Colorate
# Url var
url = input("Enter You're URl:")
filename = input("FileName (put a .png at the end.):")
print("Created File...")
# Make QR code
uurl_QR = pyqrcode.create(url)

# Download
uurl_QR.png(filename, scale = 10)

# Made by xiv

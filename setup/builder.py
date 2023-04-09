import os
from time import sleep

print("""
__________                                             
\______   \_______ ___.__. ______ _____ _____  ___  ___
 |     ___/\_  __ <   |  |/  ___//     \\__  \ \  \/  /
 |    |     |  | \/\___  |\___ \|  Y Y  \/ __ \_>    < 
 |____|     |__|   / ____/____  >__|_|  (____  /__/\_ \
                   \/         \/      \/     \/      \/
""")
print("\n[- Builder version 2.1 -]\n")
print("BTW. Do you need install ALL requeriments, include pyarmor + pyinstaller. PYTHON 3.8.9 or don't work !!!!")
sleep(2)
os.system('pyarmor pack -e"--onefile --noconsole --icon NONE" setup.py')

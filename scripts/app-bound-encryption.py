import winreg
import os
import subprocess

def manage_chrome():
    try:
        reg_path = r"Software\Policies\Google\Chrome"
        reg_key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, reg_path)
        reg.SetValueEx(reg_key, "ApplicationBoundEncryptionEnabled", 0, reg.REG_DWORD, 0)
        reg.CloseKey(reg_key)
        print("Registry modification completed. 'App Bound Encryption' disabled.")
        
        cookies_path = os.path.join(os.getenv("LOCALAPPDATA"), r"Google\Chrome\User Data\Default\Network\Cookies")
        local_state_path = os.path.join(os.getenv("LOCALAPPDATA"), r"Google\Chrome\User Data\Local State")
        
        if os.path.exists(cookies_path):
            os.remove(cookies_path)
            print(f"Deleted cookies file: {cookies_path}")
        else:
            print("v20 cookies file not found.")
        
        if os.path.exists(local_state_path):
            os.remove(local_state_path)
            print(f"Deleted 'Local State' file: {local_state_path}")
        else:
            print("'Local State' file not found.")
        
        subprocess.run("taskkill /F /IM chrome.exe /T", shell=True, check=True)
        print("All Chrome processes terminated.")
        
    except Exception as e:
        print(f"Error: {e}")

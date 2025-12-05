# ⚡ PowerShell Security Research Scripts

Windows-focused security research scripts using PowerShell for deep system integration.

## Categories

### 🍪 Cookies
Browser cookie extraction using Windows APIs.

### 💰 Wallets
Cryptocurrency wallet detection and analysis on Windows.

### 💬 Discord
Discord security testing with PowerShell remoting.

### 📱 Telegram
Telegram session extraction for Windows systems.

### 📡 Exfiltration
Windows-native exfiltration techniques.

### 🛡️ Evasion
PowerShell-based evasion and obfuscation methods.

## Why PowerShell?
- Native Windows integration
- Deep system access
- WMI and .NET framework access
- Scripting flexibility
- Remote execution capabilities
- Built into Windows

## Requirements
- PowerShell 5.1+ or PowerShell Core 7+
- Windows 10/11 or Windows Server
- Execution policy set appropriately

## Execution Policy
```powershell
# For testing (run as Administrator)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

## Running Scripts
```powershell
.\script-name.ps1
```

## ⚠️ Disclaimer
All code is for educational and authorized security testing only. Follow all applicable laws and regulations.

## Security Notes
- PowerShell scripts are often flagged by AV
- Use only in controlled environments
- Understand script execution policies
- Be aware of logging and monitoring

## Contributing
PowerShell contributions welcome! Please ensure:
- Comment-based help documentation
- Error handling with Try/Catch
- Support for common parameters
- Compatible with PowerShell 5.1+
- Follow PowerShell best practices

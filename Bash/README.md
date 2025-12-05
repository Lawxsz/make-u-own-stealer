# 🐚 Bash Security Research Scripts

Unix/Linux security research scripts using Bash for system-level operations.

## Categories

### 🍪 Cookies
Browser cookie extraction on Linux/macOS systems.

### 💰 Wallets
Cryptocurrency wallet detection and analysis for Unix systems.

### 💬 Discord
Discord security testing on Linux platforms.

### 📱 Telegram
Telegram session extraction for Unix-based systems.

### 📡 Exfiltration
Unix-native exfiltration techniques.

### 🛡️ Evasion
Shell-based evasion and obfuscation methods.

## Why Bash?
- Universal on Unix/Linux systems
- No compilation required
- Direct system command access
- Pipe and redirection power
- Lightweight and fast
- Available on most servers

## Requirements
- Bash 4.0+
- Common Unix utilities (find, grep, awk, sed)
- OpenSSL (for encryption operations)
- curl or wget (for network operations)

## Making Scripts Executable
```bash
chmod +x script-name.sh
```

## Running Scripts
```bash
./script-name.sh
```

## ⚠️ Disclaimer
All code is for educational and authorized security testing only. Follow all applicable laws and regulations.

## Best Practices
- Always validate user input
- Use `set -euo pipefail` for safer scripts
- Quote variables properly
- Check command availability before use
- Handle errors gracefully

## Contributing
Bash contributions welcome! Please ensure:
- POSIX compliance where possible
- Clear comments and documentation
- Error handling
- ShellCheck validation
- Support for common Linux distributions

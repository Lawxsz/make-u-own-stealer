# 🐍 Python Security Research Tools

Complete Python implementations of security research tools for educational purposes.

## 📦 Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## 📂 Categories

### 🍪 [Cookies](cookies/)
Browser cookie extraction with support for all major browsers.

**Features:**
- Chrome, Firefox, Edge, Opera, Brave support
- Password extraction
- Credit card data analysis
- Bookmark extraction
- App-Bound Encryption bypass

**Files:**
- `cookie_retriever.py` - Advanced cookie extraction
- `passwords_cards_cookies.py` - Comprehensive data extraction
- `passwords_cookies_bookmarks.py` - Browser data harvesting

### 💰 [Wallets](wallets/)
Cryptocurrency wallet security analysis.

**Features:**
- MetaMask wallet analysis
- Exodus wallet extraction
- Browser extension analysis
- Seed phrase detection

**Files:**
- `metamask.py` - MetaMask security testing
- `exodus.py` - Exodus wallet analysis
- `js/` - Browser extension injection scripts

### 💬 [Discord](discord/)
Discord security testing and token analysis.

**Features:**
- Token extraction
- Account information gathering
- Multi-account support
- RAT (Remote Administration Tool) research

**Files:**
- `discord.py` - Discord token extractor
- `discord_rat.py` - Advanced Discord security testing

### 📱 [Telegram](telegram/)
Telegram session security research.

**Features:**
- Session file location
- Session data extraction
- Multi-account support

**Files:**
- `telegram.py` - Telegram session extractor

### 🛡️ [Evasion](evasion/)
Antivirus evasion and obfuscation techniques.

**Features:**
- AV detection
- Chrome App-Bound Encryption bypass
- Security tool detection

**Files:**
- `search_antivirus.py` - Antivirus detection
- `app-bound-encryption.py` - Encryption bypass techniques

### 🖥️ [System Info](system_info/)
System information gathering tools.

**Features:**
- Hardware information
- System specifications
- Screenshot capture
- Webcam access

**Files:**
- `machine.py` - System information collector
- `screenshot.py` - Screen capture
- `campic.py` - Webcam capture

### 🎮 [Gaming](gaming/)
Gaming platform security research.

**Features:**
- Steam account analysis
- Roblox security testing

**Files:**
- `steam.py` - Steam account extractor
- `roblox.py` - Roblox security testing

### 📡 [Exfiltration](exfiltration/)
Data exfiltration technique demonstrations.

**Planned Features:**
- DNS exfiltration
- HTTP/HTTPS exfiltration
- Custom protocol exfiltration

## 🚀 Quick Start

### Basic Cookie Extraction

```python
cd cookies
python cookie_retriever.py
```

### Wallet Analysis

```python
cd wallets
python metamask.py
```

### Discord Token Extraction

```python
cd discord
python discord.py
```

## 📋 Requirements

See `requirements.txt` for all dependencies. Common requirements include:

- `pycryptodome` - Cryptography operations
- `requests` - HTTP requests
- `pywin32` - Windows API access (Windows only)
- `psutil` - System information
- `pillow` - Image processing

## ⚠️ Important Notes

### Legal Disclaimer

All tools are for **EDUCATIONAL and AUTHORIZED TESTING ONLY**. Unauthorized use is illegal.

### Usage Guidelines

- ✅ Use only on your own systems
- ✅ Obtain explicit permission for testing
- ✅ Use in controlled lab environments
- ✅ Report vulnerabilities responsibly
- ❌ Never use without authorization
- ❌ Don't violate Terms of Service
- ❌ Don't access others' data without permission

### Security Considerations

- These scripts may be flagged by antivirus software
- Only run in isolated testing environments
- Never store or transmit real user credentials
- Understand the code before executing

## 🔧 Configuration

Some scripts use `config.py` for configuration. Review and modify settings before use:

```python
# config.py example
WEBHOOK_URL = "your_webhook_here"  # For testing exfiltration
DEBUG_MODE = True  # Enable verbose logging
```

## 🧪 Testing

Run tests to ensure everything works:

```bash
cd ../tests
pytest test_python/
```

## 📖 Examples

Check the `/examples` directory for comprehensive usage examples:

- Basic single-tool usage
- Multi-tool integration
- Error handling patterns
- Safe testing practices

## 🤝 Contributing

Contributions to Python implementations are welcome! Please:

- Follow PEP 8 style guide
- Add type hints
- Include docstrings
- Write unit tests
- Update documentation

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

## 📊 Module Status

| Module | Status | Notes |
|--------|--------|-------|
| Cookies | ✅ Complete | All major browsers supported |
| Wallets | ✅ Complete | MetaMask, Exodus implemented |
| Discord | ✅ Complete | Token extraction working |
| Telegram | ✅ Complete | Session extraction working |
| Evasion | ✅ Complete | AV detection, encryption bypass |
| System Info | ✅ Complete | Full system profiling |
| Gaming | ✅ Complete | Steam, Roblox supported |
| Exfiltration | 🟡 In Progress | DNS, HTTP planned |

## 🔍 Code Quality

All Python code follows:
- PEP 8 style guidelines
- Type hints for function signatures
- Comprehensive error handling
- Security best practices
- Clean code principles

## 📚 Learning Resources

To better understand these implementations:

1. Study browser security models
2. Learn about encryption methods
3. Understand platform APIs
4. Review security best practices
5. Explore defensive techniques

## 🛠️ Troubleshooting

### Common Issues

**Import Errors:**
```bash
pip install -r requirements.txt --upgrade
```

**Permission Errors:**
- Run as administrator (Windows) or with sudo (Linux)
- Check file permissions

**Browser Not Supported:**
- Check browser installation paths
- Update browser-specific code
- Consult documentation

## 📞 Support

- **Issues:** Report bugs via GitHub Issues
- **Questions:** Join Telegram community
- **Ideas:** Start a GitHub Discussion

---

**Remember:** These tools are for learning and authorized testing only. Always act ethically and legally.

# 🔐 InfoSec Research Toolkit - Community Edition

A comprehensive, community-driven repository of security research tools and techniques across multiple programming languages. This project serves as an educational resource for security professionals, researchers, and students.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/purpose-educational-green.svg)]()
[![Community](https://img.shields.io/badge/community-driven-orange.svg)]()

## 📋 Overview

This repository contains security research implementations across multiple categories and programming languages. Each implementation demonstrates specific techniques for authorized security testing, defensive research, and educational purposes.

### 🌟 Star this repository for updates!

**Community Links:**
- 📱 Telegram: [@lawxszdev](https://t.me/lawxszdev)
- 💬 Community Channel: [Prysmax C2](https://t.me/prysmaxc2)
- 🌐 Website: [prysmax.site](https://prysmax.site)
- 🛠️ Contact: [@Lawxsz](https://t.me/Lawxsz)

## 🗂️ Repository Structure

```
├── 📁 Python/          # Python implementations (most complete)
│   ├── cookies/        # Browser cookie extraction
│   ├── wallets/        # Cryptocurrency wallet analysis
│   ├── discord/        # Discord security research
│   ├── telegram/       # Telegram session analysis
│   ├── exfiltration/   # Data exfiltration techniques
│   ├── evasion/        # AV evasion and obfuscation
│   ├── system_info/    # System information gathering
│   └── gaming/         # Gaming platform security (Steam, Roblox)
│
├── 📁 C-CPP/           # C/C++ implementations
├── 📁 Rust/            # Rust implementations
├── 📁 Golang/          # Go implementations
├── 📁 PowerShell/      # PowerShell scripts
├── 📁 Bash/            # Bash scripts
│
├── 📁 utils/           # Cross-language utilities
│   ├── encryption/     # Encryption tools
│   ├── compression/    # Compression utilities
│   └── obfuscation/    # Code obfuscation tools
│
├── 📁 tests/           # Testing environments and scripts
├── 📁 examples/        # Usage examples and integration guides
└── 📁 docs/            # Additional documentation
```

## 🎯 Features by Category

### 🍪 Browser Data Extraction
- **Cookies:** Chrome, Firefox, Edge, Opera, Brave
- **Passwords:** Browser saved passwords
- **Bookmarks:** Browser bookmarks and history
- **Credit Cards:** Saved payment methods
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

### 💰 Cryptocurrency Wallets
- **MetaMask:** Browser extension data extraction
- **Exodus:** Desktop wallet analysis
- **Multi-wallet:** Support for various wallet types
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

### 💬 Communication Platforms
- **Discord:** Token extraction and security analysis
- **Telegram:** Session file analysis
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

### 📡 Data Exfiltration
- **DNS Exfiltration:** DNS-based data transfer
- **HTTP/HTTPS:** Web-based exfiltration
- **Custom Protocols:** Advanced exfiltration methods
- **Status:** 🟡 Python (In Progress) | 🔴 Other languages (Contributions welcome)

### 🛡️ Evasion Techniques
- **AV Detection:** Antivirus detection methods
- **Encryption Bypass:** App-bound encryption bypass
- **Obfuscation:** Code obfuscation techniques
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

### 🖥️ System Information
- **Hardware Info:** System specifications
- **Screenshots:** Screen capture functionality
- **Webcam:** Camera access for security testing
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

### 🎮 Gaming Platforms
- **Steam:** Steam account security analysis
- **Roblox:** Roblox security testing
- **Status:** ✅ Python (Complete) | 🔴 Other languages (Contributions welcome)

## 🚀 Quick Start

### Python
```bash
cd Python
pip install -r requirements.txt

# Example: Extract cookies
cd cookies
python cookie_retriever.py
```

### Rust
```bash
cd Rust/[category]
cargo build --release
cargo run --release
```

### Go
```bash
cd Golang/[category]
go build
./[binary_name]
```

### C/C++
```bash
cd C-CPP/[category]
mkdir build && cd build
cmake ..
make
```

### PowerShell
```powershell
cd PowerShell\[category]
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\script.ps1
```

### Bash
```bash
cd Bash/[category]
chmod +x script.sh
./script.sh
```

## 🤝 Contributing

We welcome contributions in any programming language! This is a community-driven project.

### How to Contribute

1. **Fork** the repository
2. **Choose** a language and category
3. **Implement** your security research tool
4. **Document** your code thoroughly
5. **Test** in safe, isolated environments
6. **Submit** a pull request

### Contribution Guidelines

- ✅ Educational and research-focused
- ✅ Well-documented with examples
- ✅ Follows ethical guidelines
- ✅ Includes proper disclaimers
- ✅ Clean, readable code
- ✅ Error handling and safety checks
- ❌ No malicious intent or capability
- ❌ No hardcoded credentials or personal data

### Priority Areas for Contribution

1. **C/C++ implementations** - High performance, low-level access
2. **Rust implementations** - Memory safety and modern approach
3. **Go implementations** - Cross-platform simplicity
4. **PowerShell scripts** - Windows-native capabilities
5. **Bash scripts** - Unix/Linux system integration

## 📚 Educational Purpose

This repository is designed for:

- 🎓 **Students** learning about cybersecurity
- 🔬 **Researchers** studying security techniques
- 🛡️ **Security Professionals** testing defensive measures
- 👨‍💻 **Developers** understanding security vulnerabilities
- 🏫 **Educators** teaching security concepts

## ⚠️ Legal Disclaimer

**IMPORTANT:** This repository is for **EDUCATIONAL and AUTHORIZED SECURITY TESTING ONLY**.

- ✅ Use only on systems you own or have explicit permission to test
- ✅ Authorized penetration testing engagements
- ✅ Security research in controlled environments
- ✅ CTF competitions and security challenges
- ✅ Learning and defensive security improvement

- ❌ Unauthorized access to computer systems is ILLEGAL
- ❌ Using these tools without permission may violate laws
- ❌ Violating Terms of Service of platforms is prohibited
- ❌ The authors are NOT responsible for misuse

**By using this code, you agree to use it responsibly and legally.**

## 🔒 Ethical Guidelines

1. **Authorization:** Always obtain explicit permission
2. **Responsible Disclosure:** Report vulnerabilities properly
3. **Privacy:** Respect user privacy and data protection
4. **Transparency:** Be clear about your testing activities
5. **Compliance:** Follow all applicable laws and regulations
6. **No Harm:** Never cause damage or disruption

## 📖 Documentation

Each category includes detailed documentation:
- Individual README files per category
- Code comments and inline documentation
- Usage examples in `/examples`
- Testing guides in `/tests`

## 🛠️ Tools and Utilities

The `/utils` directory contains:
- **Encryption:** AES, RSA, ChaCha20 implementations
- **Compression:** Data compression for efficiency
- **Obfuscation:** Code and string obfuscation techniques

## 🧪 Testing

The `/tests` directory provides:
- Unit tests for individual modules
- Integration tests for complete workflows
- Mock environments for safe testing
- Test fixtures and sample data

## 📊 Project Status

| Language | Status | Completion |
|----------|--------|------------|
| Python | ✅ Active | ~80% |
| C/C++ | 🔴 Seeking Contributors | ~0% |
| Rust | 🔴 Seeking Contributors | ~0% |
| Go | 🔴 Seeking Contributors | ~0% |
| PowerShell | 🔴 Seeking Contributors | ~0% |
| Bash | 🔴 Seeking Contributors | ~0% |

## 🎯 Roadmap

- [x] Restructure repository for multi-language support
- [x] Complete Python implementations
- [x] Documentation for all categories
- [ ] C/C++ implementations
- [ ] Rust implementations
- [ ] Go implementations
- [ ] PowerShell scripts
- [ ] Bash scripts
- [ ] Cross-language integration examples
- [ ] Automated testing suite
- [ ] CI/CD pipeline
- [ ] Community contribution guidelines
- [ ] Video tutorials and guides

## 🌐 Related Projects

- [Prysmax Compiler](https://github.com/Lawxsz/prysmax) - Compile your Python files easily and for free!
- Prysmax.store - FUD Stealer with advanced features

## 📞 Contact & Support

- **Telegram:** [@Lawxsz](https://t.me/Lawxsz)
- **Discord:** lawxszoficialx12
- **Channel:** [@prysmaxc2](https://t.me/prysmaxc2)
- **Issues:** Use GitHub Issues for bug reports and feature requests

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who help build this educational resource
- The security research community for sharing knowledge
- All maintainers of the libraries and tools we depend on

## ⭐ Support the Project

If you find this project useful:
- ⭐ Star this repository
- 🔄 Share with others interested in security
- 🤝 Contribute code or documentation
- 💬 Join our community discussions
- 📢 Provide feedback and suggestions

---

**Remember:** With great power comes great responsibility. Use these tools ethically and legally.

**Last Updated:** December 2025

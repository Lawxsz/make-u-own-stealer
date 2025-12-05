# 🛠️ Utility Tools

Cross-language utility functions and helpers for security research operations.

## Categories

### 🔐 Encryption (`encryption/`)
Tools and libraries for encrypting exfiltrated data before transmission.

**Features:**
- AES encryption implementations
- RSA key generation and usage
- ChaCha20 encryption
- Encryption key management
- Secure random generation

**Languages:** Python, C/C++, Rust, Go

### 📦 Compression (`compression/`)
Data compression utilities to reduce exfiltration footprint.

**Features:**
- GZIP compression
- ZLIB compression
- Custom compression algorithms
- Archive creation (ZIP, TAR)
- Stream compression

**Languages:** Python, C/C++, Rust, Go

### 🎭 Obfuscation (`obfuscation/`)
Code and data obfuscation techniques for evasion research.

**Features:**
- String obfuscation
- Code obfuscation
- Control flow flattening
- Variable name mangling
- Dead code insertion
- Binary packing

**Languages:** Python, PowerShell, JavaScript, Bash

## Usage Examples

### Encryption
```python
# Python example
from encryption import encrypt_data, decrypt_data

encrypted = encrypt_data(sensitive_data, key)
decrypted = decrypt_data(encrypted, key)
```

### Compression
```python
# Python example
from compression import compress_data, decompress_data

compressed = compress_data(large_data)
original = decompress_data(compressed)
```

### Obfuscation
```python
# Python example
from obfuscation import obfuscate_string, deobfuscate_string

obfuscated = obfuscate_string("sensitive_string")
original = deobfuscate_string(obfuscated)
```

## ⚠️ Disclaimer
These utilities are for educational and authorized security testing only. Encryption and obfuscation should not be used to hide malicious activity.

## Contributing
Contributions welcome for all languages! Please ensure:
- Clean, documented code
- Example usage
- Unit tests
- Cross-platform compatibility where possible

# 💰 Cryptocurrency Wallet Extraction - Technical Documentation

## Overview
Browser extension wallets store encrypted seed phrases and private keys in local storage. This document explains the technical details of how these wallets work and how they can be compromised for educational and defensive purposes.

---

## Table of Contents
1. [Browser Extension Architecture](#browser-extension-architecture)
2. [MetaMask Technical Details](#metamask-technical-details)
3. [Exodus Wallet Details](#exodus-wallet-details)
4. [Storage Locations](#storage-locations)
5. [Execution Flow](#execution-flow)
6. [Defense Mechanisms](#defense-mechanisms)

---

## Browser Extension Architecture

### How Browser Extensions Store Data

Browser extensions use **Local Extension Settings** to persist data:

```
Storage Type: LevelDB (Key-Value Database)
Location: Browser Profile\Local Extension Settings\<extension_id>\
Encryption: Varies by extension
```

### Extension ID Structure

Each extension has a unique 32-character ID:

**MetaMask:** `nkbihfbeogaeaoehlefnkodbefgpgknn`
**Binance Wallet:** `fhbohimaelbohpjbbldcngcnapndodjp`
**Phantom:** `bfnaelmomeimhlpmgjnjophhpkkoljpa`

---

## MetaMask Technical Details

### Storage Location

```
Chrome:
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn\

Edge:
%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn\

Brave:
%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn\
```

### LevelDB Structure

**Files:**
- `CURRENT` - Points to current MANIFEST file
- `MANIFEST-*` - Database metadata
- `*.ldb` - Sorted table files (actual data)
- `*.log` - Write-ahead log files
- `LOCK` - Database lock file

### Data Storage Format

```json
{
  "data": {
    "KeyringController": {
      "vault": "<encrypted_vault_data>"
    }
  }
}
```

### Vault Encryption

**MetaMask Encryption Process:**

1. **User Password → Encryption Key**
   ```
   Password → PBKDF2-SHA256 (iterations: 600,000) → Encryption Key
   ```

2. **Vault Structure**
   ```json
   {
     "data": "<encrypted_seed_phrase_and_keys>",
     "iv": "<initialization_vector>",
     "salt": "<pbkdf2_salt>"
   }
   ```

3. **Encryption Algorithm**
   - Algorithm: AES-128-CTR or AES-256-GCM
   - Mode: Counter (CTR) or Galois/Counter (GCM)
   - Key derivation: PBKDF2

### What Can Be Extracted

**Without Password:**
- ❌ Seed phrase (encrypted)
- ❌ Private keys (encrypted)
- ✅ Wallet addresses (public data)
- ✅ Transaction history (public on blockchain)
- ✅ Vault structure (encrypted blob)

**With Password Cracking:**
- ✅ Complete seed phrase (12/24 words)
- ✅ All private keys
- ✅ Full wallet recovery

---

## Exodus Wallet Details

### Desktop Application

**Installation Path:**
```
Windows:
%APPDATA%\Exodus\

macOS:
~/Library/Application Support/Exodus/

Linux:
~/.config/Exodus/
```

### Data Structure

```
Exodus/
├── exodus.wallet/          # Main wallet data
│   ├── seed.seco          # Encrypted seed phrase
│   ├── info.seco          # Wallet metadata
│   └── passphrase.json    # Password verification
├── exodus.conf            # Configuration
└── logs/                  # Application logs
```

### Encryption Scheme

**Exodus uses:**
- Algorithm: AES-256-GCM
- Key derivation: PBKDF2-SHA256
- Iterations: 100,000+
- Additional obfuscation layers

### File Format: `.seco`

```
SECO File Structure:
┌─────────────────────────────┐
│ Header (Magic bytes)         │
├─────────────────────────────┤
│ Version info                 │
├─────────────────────────────┤
│ Salt (for key derivation)    │
├─────────────────────────────┤
│ IV (Initialization Vector)   │
├─────────────────────────────┤
│ Encrypted data               │
├─────────────────────────────┤
│ Auth tag (GCM)              │
└─────────────────────────────┘
```

---

## Storage Locations

### Complete Path List

```python
WALLET_PATHS = {
    # Browser Extensions
    "MetaMask_Chrome": "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",
    "MetaMask_Edge": "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",
    "MetaMask_Brave": "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",
    "MetaMask_Opera": "%APPDATA%\\Opera Software\\Opera GX Stable\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",

    # Desktop Wallets
    "Exodus": "%APPDATA%\\Exodus\\exodus.wallet",
    "Atomic": "%APPDATA%\\atomic\\Local Storage\\leveldb",
    "Electrum": "%APPDATA%\\Electrum\\wallets",
    "Bitcoin_Core": "%APPDATA%\\Bitcoin\\wallets",
}
```

---

## Execution Flow

### Script: `metamask.py`

```
┌─────────────────────────────────────────────────────────┐
│ 1. BROWSER PROCESS TERMINATION                          │
│    - Kills all browser processes                         │
│    - Ensures file access isn't locked                    │
│    - Uses: os.system("taskkill /F /IM chrome.exe /T")   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 2. DIRECTORY ENUMERATION                                 │
│    - Checks multiple browser profile paths               │
│    - Looks for extension ID directories                  │
│    - Validates directory existence                       │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 3. RECURSIVE DIRECTORY COPY                              │
│    - Copies entire LevelDB directory                     │
│    - Destination: %TEMP%\Metamask_<browser>             │
│    - Preserves all database files                        │
│    - Uses custom copy_directory() function               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 4. COMPRESSION                                           │
│    - Creates ZIP archive                                 │
│    - Includes all .ldb, .log files                       │
│    - Preserves directory structure                       │
│    - Uses: zipfile.ZipFile()                            │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 5. FILE HOSTING (EXFILTRATION)                           │
│    - Gets Gofile.io server via API                       │
│    - Uploads ZIP to file host                            │
│    - Receives download link                              │
│    - Uses: requests.post()                               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 6. NOTIFICATION (C2 COMMUNICATION)                       │
│    - Sends Discord webhook                               │
│    - Includes download link                              │
│    - Uses: DiscordWebhook API                           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 7. CLEANUP                                               │
│    - Deletes temporary ZIP file                          │
│    - Removes copied directory                            │
│    - Erases traces                                       │
└─────────────────────────────────────────────────────────┘
```

---

## Attack Vectors

### 1. Extension Data Theft

**Method:**
- Copy Local Extension Settings directory
- Data includes encrypted vault
- Can be cracked offline with password bruteforce

**Requirements:**
- User-level file access
- Browser not running (or forced termination)

### 2. Clipboard Monitoring

**Method:**
- Monitor clipboard for seed phrases
- Users often copy/paste during setup
- Can capture plaintext seed phrases

**Not implemented in these scripts but common technique**

### 3. Browser Extension Injection

**Method:**
- Inject malicious extension
- Hook into MetaMask API
- Capture transactions and passwords

### 4. Memory Dumping

**Method:**
- Dump browser process memory
- Search for decrypted vault data
- Requires elevated privileges

---

## Defense Mechanisms

### Extension-Side Protections

1. **Password Protection**
   - Vault encrypted with user password
   - Strong PBKDF2 key derivation
   - **Weakness:** Users often use weak passwords

2. **Auto-Lock**
   - Extension locks after inactivity
   - Requires password re-entry
   - **Weakness:** Can be disabled by user

3. **Phishing Detection**
   - Warns on suspicious sites
   - Checks transaction recipients
   - **Weakness:** Can be bypassed with lookalike domains

### System-Side Protections

1. **Antivirus/EDR**
   - Detects known wallet stealers
   - Monitors extension directory access
   - Behavioral analysis

2. **File System Monitoring**
   - Alert on extension data access
   - Monitor for mass file copying
   - Track process genealogy

### User-Side Best Practices

1. **Hardware Wallets**
   - Use Ledger, Trezor for storage
   - Extension becomes "watch-only"
   - Private keys never on computer

2. **Strong Passwords**
   - 20+ character passwords
   - Use password manager
   - Never reuse passwords

3. **Multiple Wallets**
   - Hot wallet for small amounts
   - Cold wallet for long-term storage
   - Hardware wallet for large amounts

4. **Regular Security Audits**
   - Check authorized apps
   - Review transaction history
   - Monitor for unauthorized access

---

## Detection Indicators

### File System Indicators
```
- Access to Local Extension Settings while browser closed
- Copying of LevelDB directories
- ZIP creation in temp directories
- Mass file upload to cloud services
```

### Process Indicators
```
- Taskkill commands targeting browsers
- Python/script execution with file I/O to extension dirs
- Suspicious network connections (Discord webhooks, file hosts)
```

### Network Indicators
```
- Large uploads to Gofile.io, Anonfiles, etc.
- Discord webhook traffic with embedded links
- Connections to known C2 infrastructure
```

---

## Wallet-Specific Security

### MetaMask Security Features

1. **Secret Recovery Phrase**
   - 12-word BIP39 mnemonic
   - Generates all keys deterministically
   - **If compromised:** Complete wallet loss

2. **Password vs Recovery Phrase**
   - Password: Encrypts local vault
   - Recovery Phrase: Master key to all accounts
   - **Both required for complete security**

3. **Permissions System**
   - Dapps require explicit approval
   - Per-site permissions
   - **Can be bypassed if vault is stolen**

### Exodus Security Features

1. **Built-in Password Manager**
   - Stores password in encrypted form
   - Auto-fill on application start
   - **Weakness:** Password in memory while app running

2. **Backup Encryption**
   - Email backups are encrypted
   - Requires password to restore
   - **Weakness:** Email account compromise

3. **Asset Passwords**
   - Additional password per asset
   - Extra layer of protection
   - **Rarely used by average users**

---

## Cryptocurrency Attack Statistics

### Common Attack Vectors (2024 Data)

| Attack Vector | Percentage | Average Loss |
|--------------|------------|--------------|
| Phishing | 45% | $7,500 |
| Malware/Stealers | 30% | $12,000 |
| Exchange Hacks | 15% | $50,000+ |
| Social Engineering | 10% | $15,000 |

### Most Targeted Wallets

1. MetaMask (60% of attacks)
2. Trust Wallet (15%)
3. Exodus (10%)
4. Atomic Wallet (8%)
5. Others (7%)

---

## Mitigation Recommendations

### For Users:

1. **Use Hardware Wallets**
   - Ledger Nano S/X
   - Trezor Model T
   - SafePal

2. **Enable All Security Features**
   - Auto-lock after 5 minutes
   - Require password for transactions
   - Enable phishing detection

3. **Separate Wallets**
   - Trading wallet (small amounts)
   - Savings wallet (cold storage)
   - Never mix use cases

4. **Regular Backups**
   - Store seed phrase physically
   - Never digital seed phrase storage
   - Multiple secure locations

5. **Security Software**
   - Updated antivirus
   - EDR if available
   - Regular system scans

### For Developers:

1. **Implement Warning Systems**
   - Alert on unusual transactions
   - Whitelist known addresses
   - Multi-signature requirements

2. **User Education**
   - In-app security tips
   - Phishing awareness
   - Transaction verification

3. **Advanced Protection**
   - Biometric authentication
   - Time-locked transactions
   - Social recovery mechanisms

### For Enterprise:

1. **Multi-Signature Wallets**
   - Require 2-of-3 or 3-of-5 signatures
   - Gnosis Safe or similar
   - Distributed key custody

2. **Monitoring & Alerts**
   - Real-time transaction monitoring
   - Anomaly detection
   - Immediate incident response

3. **Employee Training**
   - Security awareness programs
   - Phishing simulations
   - Incident reporting procedures

---

## Educational Value

This information helps:

- **Security Researchers:** Understand wallet security models
- **Wallet Developers:** Build better protection mechanisms
- **Users:** Understand risks and protection methods
- **Incident Responders:** Investigate crypto theft
- **Forensic Analysts:** Recover and analyze wallet data

---

## References

- [MetaMask Security Documentation](https://docs.metamask.io/guide/common-terms.html#security)
- [BIP39 Mnemonic Specification](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [LevelDB Documentation](https://github.com/google/leveldb/blob/main/doc/index.md)
- [PBKDF2 Specification](https://tools.ietf.org/html/rfc2898)
- [Cryptocurrency Security Best Practices](https://www.cisa.gov/cryptocurrency)

---

**Last Updated:** December 2025
**Purpose:** Educational and defensive security research only
**Warning:** Unauthorized access to cryptocurrency wallets is illegal and unethical

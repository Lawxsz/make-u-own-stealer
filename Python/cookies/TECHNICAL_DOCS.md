# 🍪 Browser Cookie Extraction - Technical Documentation

## Overview
Browser cookie extraction involves accessing encrypted browser databases and decrypting cookie data using the browser's encryption keys. This document explains the technical details for educational and defensive purposes.

---

## Table of Contents
1. [Chrome/Chromium-based Browsers](#chromechromium-based-browsers)
2. [Encryption Mechanisms](#encryption-mechanisms)
3. [App-Bound Encryption (Chrome 127+)](#app-bound-encryption)
4. [Execution Flow](#execution-flow)
5. [Defense Mechanisms](#defense-mechanisms)

---

## Chrome/Chromium-based Browsers

### File Locations

**Cookie Database:**
```
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies
```

**Encryption Key Storage:**
```
%LOCALAPPDATA%\Google\Chrome\User Data\Local State
```

### Database Structure

The `Cookies` file is a SQLite database with the following schema:

```sql
CREATE TABLE cookies(
    creation_utc INTEGER NOT NULL,
    host_key TEXT NOT NULL,
    top_frame_site_key TEXT NOT NULL,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    encrypted_value BLOB NOT NULL,
    path TEXT NOT NULL,
    expires_utc INTEGER NOT NULL,
    is_secure INTEGER NOT NULL,
    is_httponly INTEGER NOT NULL,
    last_access_utc INTEGER NOT NULL,
    has_expires INTEGER NOT NULL,
    persistent INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    samesite INTEGER NOT NULL,
    source_scheme INTEGER NOT NULL,
    source_port INTEGER NOT NULL,
    is_same_party INTEGER NOT NULL
);
```

**Key Fields:**
- `encrypted_value`: BLOB containing AES-GCM encrypted cookie value
- `host_key`: Domain the cookie belongs to
- `name`: Cookie name
- `expires_utc`: Expiration timestamp (Chrome epoch format)

---

## Encryption Mechanisms

### Version History

| Version Prefix | Encryption Method | Chrome Version |
|---------------|-------------------|----------------|
| `v10` | AES-256-GCM | Chrome 80+ |
| `v11` | AES-256-GCM | Chrome 80+ |
| `v20` | App-Bound Encryption | Chrome 127+ |

### V10/V11 Encryption (Pre-App-Bound)

#### Encryption Process:

1. **Master Key Retrieval**
   - Located in `Local State` JSON file
   - Path: `os_crypt.encrypted_key`
   - Format: Base64-encoded, DPAPI-encrypted key

2. **Master Key Decryption**
   ```
   Encrypted Key Format: "DPAPI" + <DPAPI encrypted data>

   Steps:
   1. Base64 decode the encrypted_key value
   2. Remove first 5 bytes ("DPAPI" prefix)
   3. Call CryptUnprotectData (Windows DPAPI)
   4. Result: 256-bit AES key
   ```

3. **Cookie Value Decryption**
   ```
   Encrypted Value Format: "v10/v11" (3 bytes) + IV (12 bytes) + Ciphertext + Auth Tag (16 bytes)

   Steps:
   1. Remove version prefix (first 3 bytes)
   2. Extract IV (next 12 bytes)
   3. Extract ciphertext (remaining bytes - 16)
   4. Extract auth tag (last 16 bytes)
   5. Decrypt using AES-256-GCM with master key
   ```

#### APIs Used:

**Windows (via pywin32):**
```python
from win32crypt import CryptUnprotectData

# Decrypt DPAPI-protected data
decrypted_data = CryptUnprotectData(encrypted_data, None, None, None, 0)[1]
```

**Cryptography (via PyCryptodome):**
```python
from Crypto.Cipher import AES

# AES-GCM decryption
cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
plaintext = cipher.decrypt_and_verify(ciphertext, auth_tag)
```

---

## App-Bound Encryption

### Introduction (Chrome 127+)

Google introduced **App-Bound Encryption** to prevent cookie theft even if malware gains system access.

### How It Works

1. **Elevation Service**
   - Chrome installs a Windows service: `elevation_service.exe`
   - Runs with SYSTEM privileges
   - Only Chrome.exe can communicate with it
   - Service performs encryption/decryption operations

2. **IPC Communication**
   - Chrome process requests decryption via named pipes
   - Service validates caller identity (process signature verification)
   - Service performs operation and returns result

3. **Key Storage**
   - Encryption keys stored in SYSTEM-protected location
   - Not accessible even to admin-level processes
   - Bound to Chrome's digital signature

### Technical Details

**Registry Policy:**
```
HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome
Value: ApplicationBoundEncryptionEnabled
Type: DWORD
0 = Disabled (requires enterprise policy)
1 = Enabled (default)
```

**Encrypted Data Format:**
```
"v20" (3 bytes) + <Service-encrypted data>
```

### Defense Improvements

App-Bound Encryption protects against:
- ✅ Malware running as regular user
- ✅ Malware running as administrator
- ✅ Memory dumping attacks
- ✅ DLL injection into browser process

Does NOT protect against:
- ❌ Kernel-level malware
- ❌ Malware that hooks the elevation service
- ❌ Browser process memory scraping (before encryption)
- ❌ Network interception (cookies in transit)

---

## Execution Flow

### Script: `cookie_retriever.py`

```
┌─────────────────────────────────────────────────────────┐
│ 1. BROWSER TERMINATION                                  │
│    - Calls taskkill on all browser processes            │
│    - Ensures database isn't locked                      │
│    - Uses: os.system("taskkill /F /IM chrome.exe")     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 2. MASTER KEY EXTRACTION                                │
│    - Reads Local State JSON file                        │
│    - Extracts os_crypt.encrypted_key                    │
│    - Base64 decodes the key                             │
│    - Removes "DPAPI" prefix (5 bytes)                   │
│    - Calls CryptUnprotectData (DPAPI)                   │
│    - Result: 256-bit AES master key                     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 3. DATABASE COPY                                        │
│    - Locates Cookies SQLite database                    │
│    - Creates temporary copy to avoid locks              │
│    - Uses: shutil.copy2()                               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 4. COOKIE EXTRACTION                                    │
│    - Connects to SQLite database                        │
│    - Queries: SELECT host_key, name, encrypted_value... │
│    - Iterates through all cookie records                │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 5. DECRYPTION PROCESS                                   │
│    For each encrypted_value:                            │
│    - Check version prefix (v10/v11)                     │
│    - Extract IV (12 bytes)                              │
│    - Extract ciphertext                                 │
│    - Extract auth tag (16 bytes)                        │
│    - Decrypt with AES-256-GCM                           │
│    - Decode UTF-8                                       │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 6. FORMAT CONVERSION                                    │
│    - Converts Chrome epoch to Unix timestamp            │
│    - Formula: (chrome_time / 1000000) - 11644473600     │
│    - Formats in Netscape cookie format                  │
│    - Format: domain\tFALSE\tpath\tSECURE\texpiry\tname\tvalue │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 7. OUTPUT                                               │
│    - Saves to text file                                 │
│    - One cookie per line                                │
│    - Compatible with browser import tools               │
│    - Location: SavedCookies/<browser>_cookies.txt       │
└─────────────────────────────────────────────────────────┘
```

---

## Windows APIs Used

### 1. DPAPI (Data Protection API)

**Function:** `CryptUnprotectData`

```c
BOOL CryptUnprotectData(
  DATA_BLOB            *pDataIn,      // Encrypted data
  LPWSTR               *ppszDataDescr, // Description
  DATA_BLOB            *pOptionalEntropy, // Extra entropy
  PVOID                pvReserved,     // Reserved
  CRYPTPROTECT_PROMPTSTRUCT *pPromptStruct, // Prompt info
  DWORD                dwFlags,        // Flags
  DATA_BLOB            *pDataOut       // Decrypted output
);
```

**Purpose:** Decrypt data encrypted with DPAPI (user-specific encryption)

**Python Wrapper:**
```python
from win32crypt import CryptUnprotectData
decrypted = CryptUnprotectData(encrypted, None, None, None, 0)[1]
```

### 2. Process Termination

**Function:** `taskkill` command

```batch
taskkill /F /IM <process_name> /T
```

**Flags:**
- `/F` - Force termination
- `/IM` - Image name (process name)
- `/T` - Terminate child processes

---

## Defense Mechanisms

### Browser-Side Protections

1. **File Locking**
   - Database locked while browser running
   - Prevents direct file access
   - **Bypass:** Terminate browser or copy file

2. **DPAPI Encryption**
   - Master key encrypted with user credentials
   - Only current user can decrypt
   - **Bypass:** Malware runs in user context

3. **App-Bound Encryption (Chrome 127+)**
   - Service-level encryption
   - Process identity verification
   - **Bypass:** Requires kernel-level access or service compromise

### System-Side Protections

1. **Antivirus Detection**
   - Signature-based detection of known stealers
   - Behavioral analysis of cookie access
   - Monitoring of DPAPI calls

2. **File System Monitoring**
   - EDR tools monitor sensitive file access
   - Alerts on cookie database access

3. **Process Monitoring**
   - Detect suspicious process termination
   - Monitor for mass file copying

### User-Side Protections

1. **Browser Extensions**
   - Cookie autodelete extensions
   - Session management tools

2. **Security Practices**
   - Regular cookie clearing
   - Use of container tabs
   - Avoiding "Remember Me" on sensitive sites

---

## Detection Indicators

### File Access Patterns
```
- Access to Local State without Chrome running
- Copying of Cookies database
- Temporary SQLite files in unusual locations
- Mass reading of cookie databases
```

### Process Indicators
```
- Taskkill commands targeting browsers
- Python/script execution with DPAPI calls
- Access to multiple browser profile directories
```

### Network Indicators
```
- Large data uploads to file-sharing services
- Webhook/Discord API calls with cookie data
- Connections to known C2 servers
```

---

## Mitigation Recommendations

### For Users:
1. Keep Chrome updated (use App-Bound Encryption)
2. Use hardware security keys (WebAuthn)
3. Enable 2FA on all accounts
4. Regularly clear cookies
5. Use antivirus with behavioral detection

### For Developers:
1. Implement proper session management
2. Use short-lived session tokens
3. Monitor for suspicious logins (new location, device)
4. Implement IP whitelisting where appropriate
5. Use secure, httpOnly, sameSite cookies

### For Administrators:
1. Deploy EDR solutions
2. Monitor for unusual DPAPI activity
3. Restrict user permissions
4. Network segmentation
5. Regular security audits

---

## Educational Use Cases

This information is valuable for:
- **Security Researchers:** Understanding attack vectors
- **Defenders:** Building detection rules
- **Developers:** Implementing secure session management
- **Forensic Analysts:** Understanding data recovery
- **Students:** Learning about encryption and security

---

## References

- [Chromium Security: Cookie Encryption](https://www.chromium.org/developers/design-documents/secure-cookie-storage/)
- [Microsoft DPAPI Documentation](https://docs.microsoft.com/en-us/windows/win32/api/dpapi/)
- [Google: App-Bound Encryption Whitepaper](https://security.googleblog.com/)
- [SQLite Database Format](https://www.sqlite.org/fileformat.html)

---

**Last Updated:** December 2025
**Purpose:** Educational and defensive security research only

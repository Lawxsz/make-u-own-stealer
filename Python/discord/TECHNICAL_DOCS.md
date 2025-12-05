# 💬 Discord Token Extraction - Technical Documentation

## Overview
Discord stores authentication tokens in local storage files. These tokens provide complete account access without requiring passwords. This document explains the technical implementation for educational and defensive purposes.

---

## Table of Contents
1. [Discord Token Structure](#discord-token-structure)
2. [Storage Locations](#storage-locations)
3. [Token Types](#token-types)
4. [Extraction Methodology](#extraction-methodology)
5. [Execution Flow](#execution-flow)
6. [Defense Mechanisms](#defense-mechanisms)

---

## Discord Token Structure

### Token Format

Discord uses three token formats:

```
1. Standard Token (Bot/User):
   Format: [A-Za-z0-9_-]{24}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27}
   Example: XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX

2. MFA Token (Multi-Factor Authentication):
   Format: mfa\.[A-Za-z0-9_-]{84}
   Example: mfa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

3. Legacy Token:
   Format: [A-Za-z0-9_-]{59}
   (Mostly deprecated - example not shown for security)
```

### Token Components

**Standard Token Breakdown:**
```
[USER_ID_BASE64_24_CHARS].[TIMESTAMP_6_CHARS].[HMAC_SIGNATURE_27_CHARS]
│                         │                    │
│                         │                    └─ HMAC signature
│                         └────────────────────── Timestamp
└──────────────────────────────────────────────── User ID (Base64)
```

**Part 1: User ID**
- Base64 encoded Discord user ID
- Example: `[BASE64_ENCODED_USER_ID]` → `[NUMERIC_USER_ID]`

**Part 2: Timestamp**
- Creation timestamp (Base64)
- Used for token rotation

**Part 3: HMAC**
- Cryptographic signature
- Validates token integrity
- Generated with secret key

---

## Storage Locations

### Desktop Application

```
Windows:
%APPDATA%\discord\Local Storage\leveldb\

%APPDATA%\discordcanary\Local Storage\leveldb\

%APPDATA%\discordptb\Local Storage\leveldb\
```

```
macOS:
~/Library/Application Support/discord/Local Storage/leveldb/

~/Library/Application Support/discordcanary/Local Storage/leveldb/

~/Library/Application Support/discordptb/Local Storage/leveldb/
```

```
Linux:
~/.config/discord/Local Storage/leveldb/

~/.config/discordcanary/Local Storage/leveldb/

~/.config/discordptb/Local Storage/leveldb/
```

### Browser-Based Discord

```
Chrome:
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\leveldb\

Edge:
%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Local Storage\leveldb\

Firefox:
%APPDATA%\Mozilla\Firefox\Profiles\<profile>\storage\default\https+++discord.com\

Opera:
%APPDATA%\Opera Software\Opera Stable\Local Storage\leveldb\

Brave:
%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Local Storage\leveldb\
```

---

## Token Types

### 1. User Tokens

**Purpose:** Authenticate regular Discord users

**Capabilities:**
- Send/receive messages
- Join servers
- Access DMs
- Modify account settings
- Complete account control

**Risks if Compromised:**
- Account takeover
- Message history access
- Impersonation
- Spam/phishing from account
- Access to all servers

### 2. Bot Tokens

**Purpose:** Authenticate Discord bots

**Format:** Starts with `Bot ` prefix

**Capabilities:**
- Limited by bot permissions
- Cannot access DMs
- Server-specific actions
- API rate limits

### 3. MFA Tokens

**Purpose:** Tokens with 2FA enabled accounts

**Special Characteristics:**
- Longer format (84 characters)
- Prefixed with `mfa.`
- Additional security checks
- Shorter expiration time

---

## Extraction Methodology

### LevelDB File Structure

Discord uses LevelDB for local storage:

```
leveldb/
├── CURRENT          # Points to active MANIFEST
├── LOCK            # Database lock
├── LOG             # Operation log
├── MANIFEST-000001 # Database metadata
├── 000003.log      # Write-ahead log (contains recent data)
├── 000005.ldb      # Sorted string table (persistent data)
└── 000007.ldb      # Sorted string table
```

### Token Storage Format

Tokens stored in key-value pairs:

```
Key: _https://discord.com<random>token
Value: "TOKEN_HERE"
```

Example from `.log` or `.ldb` file:
```
...random_data...
_https://discord.com‎localStorage:token"[EXAMPLE_TOKEN_REDACTED_FOR_SECURITY]"...more_data...
```

### Extraction Process

1. **File Reading**
   - Read `.log` files (most recent data)
   - Read `.ldb` files (persistent data)
   - Read `.sqlite` files (Firefox)

2. **Pattern Matching**
   - Use regex to find token patterns
   - Match standard token format
   - Match MFA token format

3. **Deduplication**
   - Remove duplicate tokens
   - Keep only valid formats

4. **Validation** (optional)
   - Test token with Discord API
   - Retrieve account information

---

## Execution Flow

### Script: `discord.py`

```
┌─────────────────────────────────────────────────────────┐
│ 1. ENVIRONMENT VARIABLE READING                          │
│    - os.getenv("localAPPDATA") → Local AppData          │
│    - os.getenv("APPDATA") → Roaming AppData             │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 2. PATH ENUMERATION                                      │
│    - Iterates through predefined path dictionary         │
│    - Checks: Discord app, browsers, mods (Lightcord)    │
│    - Appends "local Storage\leveldb" to each            │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 3. DIRECTORY EXISTENCE CHECK                             │
│    - os.path.exists(path)                                │
│    - Validates each storage location                     │
│    - Skips non-existent paths                           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 4. FILE ITERATION                                        │
│    - os.listdir(leveldb_path)                           │
│    - Filters: .log, .ldb, .sqlite files                 │
│    - Opens each file with error handling                 │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 5. LINE-BY-LINE PROCESSING                              │
│    - file.readlines() with errors="ignore"               │
│    - Ignores binary data read errors                     │
│    - Processes each line for tokens                      │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 6. REGEX MATCHING                                        │
│    - Pattern 1: r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"       │
│    - Pattern 2: r"mfa\.[\w-]{84}"                       │
│    - re.findall() extracts all matches                   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 7. DEDUPLICATION                                         │
│    - Checks if "token | platform" exists in list         │
│    - Prevents duplicate entries                          │
│    - Associates token with source platform               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ 8. WEBHOOK EXFILTRATION                                  │
│    - Creates Discord embed                               │
│    - Sends via webhook POST request                      │
│    - Includes: tokens, platform, custom branding         │
└─────────────────────────────────────────────────────────┘
```

---

## Discord API Endpoints

### Token Validation

```http
GET https://discord.com/api/v9/users/@me
Authorization: TOKEN_HERE
```

**Response if valid:**
```json
{
  "id": "1057389568636774410",
  "username": "ExampleUser",
  "discriminator": "1234",
  "email": "user@example.com",
  "verified": true,
  "phone": "+1234567890",
  "mfa_enabled": true,
  "locale": "en-US",
  "premium_type": 2
}
```

### Account Information

```http
GET https://discord.com/api/v9/users/@me/billing/payment-sources
Authorization: TOKEN_HERE
```

Returns: Credit card information, PayPal, etc.

### Guild (Server) Information

```http
GET https://discord.com/api/v9/users/@me/guilds
Authorization: TOKEN_HERE
```

Returns: All servers the user is in

---

## Attack Scenarios

### 1. Token Theft → Account Takeover

**Attack Chain:**
```
1. Extract token from local storage
2. Validate token via API
3. Change email/password
4. Enable 2FA with attacker's device
5. Lock out legitimate user
```

### 2. Token Theft → Spam/Phishing

**Attack Chain:**
```
1. Extract token
2. Access all servers
3. Send mass DMs with malicious links
4. Spread malware to contacts
```

### 3. Token Theft → Information Gathering

**Attack Chain:**
```
1. Extract token
2. Access private DMs
3. Exfiltrate message history
4. Extract personal information
5. Blackmail/doxing
```

---

## Defense Mechanisms

### Discord-Side Protections

1. **Token Rotation**
   - Tokens expire periodically
   - Password change invalidates tokens
   - Logout invalidates current token

2. **Suspicious Activity Detection**
   - Login from new location → Email notification
   - API rate limiting
   - Captcha challenges

3. **2FA (MFA)**
   - Requires secondary authentication
   - Protects sensitive actions
   - Different token format

### Client-Side Protections

1. **BetterDiscord/Mods Detection**
   - Discord detects client modifications
   - May ban accounts using mods
   - Warns users of risks

2. **Secure Storage** (Limited)
   - LevelDB provides some obfuscation
   - Not encrypted by default
   - Accessible with user permissions

### System-Side Protections

1. **Antivirus/EDR**
   - Signature-based detection
   - Behavioral analysis
   - File access monitoring

2. **File Integrity Monitoring**
   - Detect unauthorized access to Discord files
   - Alert on mass file reading
   - Process genealogy tracking

### User-Side Best Practices

1. **Enable 2FA**
   - Use authenticator app
   - Backup codes in safe location
   - Protects against token theft

2. **Regular Password Changes**
   - Invalidates stolen tokens
   - Use unique passwords
   - Password manager recommended

3. **Monitor Sessions**
   - Check active sessions in settings
   - Log out unknown devices
   - Review login locations

4. **Avoid Suspicious Links**
   - No unofficial Discord apps
   - No "free Nitro" scams
   - Verify URLs before clicking

---

## Detection Indicators

### File System Indicators
```
- Access to Discord Local Storage while app closed
- Reading of .log and .ldb files
- Python/script execution with Discord path access
- Mass file copying from AppData
```

### Network Indicators
```
- Discord webhook traffic with token data
- API calls from unusual locations
- Multiple /users/@me requests
- Failed authentication attempts
```

### Behavioral Indicators
```
- Sudden mass DM sending
- Messages sent while user offline
- Account settings changes
- Unusual API usage patterns
```

---

## Token Security Analysis

### Strengths

- ✅ Long, complex format
- ✅ Cryptographic signature (HMAC)
- ✅ Timestamp-based rotation
- ✅ User ID embedded (prevents guessing)

### Weaknesses

- ❌ Stored in plaintext
- ❌ No client-side encryption
- ❌ Accessible with user permissions
- ❌ Long validity period
- ❌ No device binding

### Comparison to Other Platforms

| Platform | Storage | Encryption | Rotation | Device Binding |
|----------|---------|------------|----------|----------------|
| Discord | Plaintext | None | Periodic | No |
| Telegram | Encrypted | Yes | On logout | Yes |
| WhatsApp | Encrypted | Yes | Frequent | Yes |
| Slack | Plaintext | Partial | On logout | No |

---

## Mitigation Recommendations

### For Users:

1. **Enable 2FA immediately**
   - Protects against token theft impact
   - Use Google Authenticator or Authy
   - Store backup codes securely

2. **Regularly log out**
   - Invalidates current tokens
   - Forces re-authentication
   - Reduces exposure window

3. **Monitor account activity**
   - Check user settings → Devices
   - Review login locations
   - Immediately deauthorize unknowns

4. **Use official clients only**
   - Avoid BetterDiscord/client mods
   - Download from official discord.com
   - Keep app updated

5. **Security software**
   - Updated antivirus
   - Regular system scans
   - Monitor file access

### For Discord (Platform):

1. **Implement client-side encryption**
   - Encrypt tokens in local storage
   - Use OS-level key storage (Keychain/DPAPI)
   - Similar to browser cookie encryption

2. **Shorter token validity**
   - More frequent rotation
   - Re-authentication prompts
   - Balance security vs UX

3. **Device binding**
   - Tie tokens to hardware ID
   - Require re-auth on new device
   - Similar to banking apps

4. **Enhanced monitoring**
   - Better anomaly detection
   - Immediate user notification
   - Automatic token revocation

### For Developers:

1. **Educate users**
   - In-app security tips
   - Phishing awareness
   - 2FA promotion

2. **Implement monitoring**
   - Detect mass token requests
   - Rate limit validation endpoints
   - Alert on suspicious patterns

---

## Legal and Ethical Considerations

### Laws Violated by Token Theft

- **Computer Fraud and Abuse Act (CFAA)** - USA
- **General Data Protection Regulation (GDPR)** - EU
- **Computer Misuse Act** - UK
- **Cybercrime laws** - Various countries

### Penalties

- Criminal charges
- Fines up to $500,000
- Prison sentences up to 20 years
- Civil lawsuits
- Permanent records

### Ethical Issues

- Privacy violation
- Identity theft
- Harassment potential
- Financial fraud
- Reputation damage

---

## Educational Use Cases

This information is valuable for:

- **Security Researchers:** Understanding authentication weaknesses
- **Incident Responders:** Investigating account compromises
- **Discord Security Team:** Improving platform security
- **Users:** Understanding risks and protection
- **Students:** Learning about token-based authentication

---

## References

- [Discord API Documentation](https://discord.com/developers/docs/intro)
- [LevelDB GitHub Repository](https://github.com/google/leveldb)
- [Discord Security Best Practices](https://discord.com/safety/360043857751-Four-steps-to-a-super-safe-account)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

**Last Updated:** December 2025
**Purpose:** Educational and defensive security research only
**Warning:** Unauthorized access to Discord accounts is illegal and violates Terms of Service

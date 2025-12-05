# Contributing to InfoSec Research Toolkit

Thank you for your interest in contributing to this educational security research project! This document provides guidelines for contributing code, documentation, and other improvements.

## 🎯 Types of Contributions

We welcome various types of contributions:

- **Code Implementations:** New tools in any supported language
- **Documentation:** README files, code comments, tutorials
- **Bug Fixes:** Corrections to existing code
- **Examples:** Usage examples and integration guides
- **Tests:** Unit tests and integration tests
- **Translations:** Documentation in other languages

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/make-u-own-stealer.git
cd make-u-own-stealer
```

### 2. Choose Your Contribution

Decide what you want to contribute:
- Pick a language (Python, C/C++, Rust, Go, PowerShell, Bash)
- Pick a category (cookies, wallets, discord, telegram, etc.)
- Check if an implementation already exists

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# Example: git checkout -b feature/rust-cookie-extraction
```

## 📝 Contribution Guidelines

### Code Quality

- **Clean Code:** Write readable, maintainable code
- **Comments:** Add clear comments explaining complex logic
- **Documentation:** Include README files for new features
- **Error Handling:** Implement proper error handling
- **Security:** Follow security best practices

### Language-Specific Guidelines

#### Python
```python
# Use type hints
def extract_cookies(browser: str) -> dict:
    """Extract cookies from specified browser.

    Args:
        browser: Browser name (chrome, firefox, etc.)

    Returns:
        Dictionary containing extracted cookies
    """
    pass

# Follow PEP 8
# Use meaningful variable names
# Add docstrings to functions
```

#### Rust
```rust
// Use idiomatic Rust
// Minimize unsafe code
// Add comprehensive error handling
// Include documentation comments

/// Extracts cookies from the specified browser.
///
/// # Arguments
/// * `browser` - Browser name to extract from
///
/// # Returns
/// Result containing extracted cookies or error
pub fn extract_cookies(browser: &str) -> Result<Cookies, Error> {
    // Implementation
}
```

#### Go
```go
// Follow Go conventions
// Use go fmt
// Add godoc comments
// Implement error handling

// ExtractCookies extracts cookies from the specified browser.
// Returns error if extraction fails.
func ExtractCookies(browser string) (map[string]string, error) {
    // Implementation
}
```

#### C/C++
```c
// Use consistent style
// Check return values
// Free allocated memory
// Add header comments

/**
 * Extract cookies from specified browser
 * @param browser Browser name
 * @param cookies Output buffer for cookies
 * @return 0 on success, error code on failure
 */
int extract_cookies(const char* browser, cookies_t* cookies);
```

### Documentation Requirements

Each contribution should include:

1. **README.md** in the category folder
   - Purpose and features
   - Usage examples
   - Requirements
   - Disclaimers

2. **Code Comments**
   - Function/method documentation
   - Complex logic explanation
   - Security considerations

3. **Examples** (if applicable)
   - Basic usage example
   - Common use cases
   - Integration examples

### Security and Ethics

**CRITICAL:** All contributions must follow these rules:

- ✅ **Educational Purpose:** Code must have clear educational value
- ✅ **Disclaimers:** Include warnings about authorized use only
- ✅ **No Hardcoded Secrets:** Never include real credentials or tokens
- ✅ **Responsible:** Follow responsible disclosure practices
- ❌ **No Malware:** No actual malware or malicious payloads
- ❌ **No Evasion for Malice:** Don't optimize for malicious evasion
- ❌ **No Personal Data:** Don't include real user data

### Testing

- Test your code in isolated, safe environments
- Include unit tests where applicable
- Verify cross-platform compatibility (if relevant)
- Test edge cases and error conditions

## 📋 Submission Process

### 1. Make Your Changes

```bash
# Add your implementation
mkdir -p Rust/cookies
touch Rust/cookies/chrome_extractor.rs
touch Rust/cookies/README.md

# Write your code and documentation
```

### 2. Test Thoroughly

```bash
# Run tests
pytest  # Python
cargo test  # Rust
go test ./...  # Go
```

### 3. Commit Your Changes

```bash
git add .
git commit -m "Add Rust Chrome cookie extractor

- Implements cookie extraction for Chrome on Linux
- Includes comprehensive error handling
- Adds documentation and examples"
```

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 5. Create Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template:

```markdown
## Description
Brief description of your changes

## Type of Change
- [ ] New implementation
- [ ] Bug fix
- [ ] Documentation
- [ ] Examples

## Language
- [ ] Python
- [ ] C/C++
- [ ] Rust
- [ ] Go
- [ ] PowerShell
- [ ] Bash

## Category
- [ ] Cookies
- [ ] Wallets
- [ ] Discord
- [ ] Telegram
- [ ] Exfiltration
- [ ] Evasion
- [ ] Other: _____

## Testing
Describe how you tested your changes

## Disclaimer
- [ ] I confirm this is for educational purposes only
- [ ] I have included appropriate disclaimers
- [ ] I have not included any real credentials or personal data
- [ ] I understand this code should only be used with authorization
```

## 🔍 Code Review Process

1. **Initial Review:** Maintainers review for basic requirements
2. **Technical Review:** Code quality, security, and functionality
3. **Testing:** Verification in test environments
4. **Approval:** Merge when all requirements are met

## ✅ Checklist

Before submitting, ensure:

- [ ] Code follows language conventions
- [ ] Documentation is complete
- [ ] README includes disclaimers
- [ ] No hardcoded secrets or credentials
- [ ] Tested in safe environment
- [ ] Commit messages are clear
- [ ] PR template is filled out
- [ ] Code has educational value
- [ ] Ethical guidelines are followed

## 🌟 Priority Contributions

We especially need:

1. **Rust implementations** - All categories
2. **C/C++ implementations** - All categories
3. **Go implementations** - All categories
4. **PowerShell scripts** - Windows-specific tools
5. **Bash scripts** - Unix/Linux tools
6. **Cross-platform examples**
7. **Integration guides**
8. **Test suites**

## 💬 Communication

- **Questions:** Open a GitHub Issue
- **Discussion:** Join our Telegram channel
- **Ideas:** Start a GitHub Discussion
- **Bugs:** Report via GitHub Issues

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

## 🙏 Recognition

All contributors will be:
- Listed in the README acknowledgments
- Credited in their contributed files
- Recognized in release notes

## ❓ Need Help?

- Check existing implementations for examples
- Review language-specific READMEs
- Ask in GitHub Discussions
- Contact maintainers on Telegram

---

Thank you for contributing to security education! 🎓🔒

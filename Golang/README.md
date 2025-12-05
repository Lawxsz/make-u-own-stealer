# 🐹 Go Security Research Tools

Cross-platform security research implementations in Go for simplicity and efficiency.

## Categories

### 🍪 Cookies
Browser cookie extraction with Go's standard library.

### 💰 Wallets
Cryptocurrency wallet analysis with easy deployment.

### 💬 Discord
Discord security testing with concurrent goroutines.

### 📱 Telegram
Telegram session analysis with robust parsing.

### 📡 Exfiltration
Network-based exfiltration using Go's networking capabilities.

### 🛡️ Evasion
Evasion techniques leveraging Go's compilation model.

## Why Go?
- Simple syntax and fast development
- Excellent cross-compilation
- Built-in concurrency
- Single binary deployment
- Strong standard library
- Great networking support

## Requirements
- Go 1.21+ (install from [golang.org](https://golang.org/))

## Building
```bash
# Build for current platform
go build -o bin/ ./...

# Cross-compile for Windows
GOOS=windows GOARCH=amd64 go build -o bin/tool.exe

# Cross-compile for Linux
GOOS=linux GOARCH=amd64 go build -o bin/tool
```

## Running
```bash
go run main.go
```

## ⚠️ Disclaimer
All code is for educational and authorized security testing only. Follow all applicable laws and regulations.

## Contributing
Go contributions welcome! Please ensure:
- Follow Go conventions and style
- Use `go fmt` and `go vet`
- Include examples and documentation
- Error handling with proper context
- Use modules for dependency management

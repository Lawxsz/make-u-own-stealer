# 🧪 Testing Environments and Scripts

Test environments, unit tests, and integration tests for security research tools.

## Purpose
This directory contains:
- Unit tests for individual modules
- Integration tests for complete workflows
- Mock environments for safe testing
- Test fixtures and sample data
- Automated testing scripts

## Structure

```
tests/
├── unit/           # Unit tests for individual functions
├── integration/    # Integration tests for complete flows
├── fixtures/       # Test data and mock files
├── environments/   # Docker/VM test environments
└── results/        # Test results and reports
```

## Running Tests

### Python Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=../Python --cov-report=html
```

### Rust Tests
```bash
# Run tests
cargo test

# Run tests with output
cargo test -- --nocapture
```

### Go Tests
```bash
# Run all tests
go test ./...

# Run with coverage
go test -cover ./...
```

### C/C++ Tests
```bash
# Using CMake and CTest
mkdir build && cd build
cmake ..
make
ctest
```

## Test Environments

### Docker Environments
Isolated environments for safe testing:
```bash
docker-compose up -d test-env
```

### Virtual Machines
VM configurations for platform-specific testing.

## Best Practices
- Always test in isolated environments
- Use mock data, never real credentials
- Test edge cases and error conditions
- Maintain high test coverage
- Automated testing in CI/CD

## ⚠️ Security Note
Never include real credentials, tokens, or sensitive data in test fixtures.

## Contributing
When contributing code, please include:
- Unit tests for new functions
- Integration tests for new features
- Updated test documentation
- Any required test fixtures

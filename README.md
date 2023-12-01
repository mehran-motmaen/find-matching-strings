# StringMatcher App

This is a Python application for matching strings using the StringMatcher class.

## Prerequisites

- Docker installed on your machine

## Running the Application and Tests

### Build the Docker Image

```bash
docker build -t string-matcher-app .
```

### Run Tests

```bash
docker run string-matcher-app
```

### Run the Application

If you want to run the StringMatcher application:

```bash
docker run string-matcher-app python src/main.py
```

### Configuration

You can configure the input strings for testing by modifying the string_list in tests/test.py.

### Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the StringMatcher App. Your feedback
and collaboration are appreciated.

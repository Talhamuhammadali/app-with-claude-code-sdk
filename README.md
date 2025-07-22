# Python Project

## Description

A Python project with basic structure and dependencies.

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Local
```bash
python main.py
```

### Docker
```bash
# Build the image
docker build -t python-app .

# Run the container
docker run -it python-app
```

## Development

### Requirements

- Python 3.8+

### Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

## License

MIT License
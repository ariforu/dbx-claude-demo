# Claude API Demo

A simple Python project demonstrating how to use Claude via the Anthropic API in Databricks.

## Setup

### Using pyenv (recommended)

1. Clone this repository
2. Set up Python environment with pyenv:
   ```bash
   # Install Python 3.11.8 if not already installed
   pyenv install 3.11.8
   
   # Set local Python version for this project
   cd claude_demo
   pyenv local 3.11.8
   
   # Create and activate virtual environment
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root by copying the example:
   ```bash
   cp .env.example .env
   ```

### Without pyenv

1. Clone this repository
2. Create and activate a virtual environment (Python 3.8+ recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root by copying the example:
   ```bash
   cp .env.example .env
   ```
5. Get your API key from [Anthropic Console](https://console.anthropic.com/) and add it to the `.env` file

## Usage

### Basic Example

Run the basic example:

```bash
python src/main.py
```

This will prompt you to enter a question, which will be sent to Claude. The response will be displayed in the terminal.

## Available Models

- Goto DBX console and visit "Serving" section to see the available models/gateway.Try the DBX managed LLM models(e.g. databricks-claude-3-7-sonnet) from your "paid" Databricks account(for unified DBU based billing) or register it like external provider if you're testing on Free account !

## Documentation

For more information on using the Anthropic API, see the [official documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api).

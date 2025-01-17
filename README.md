# GPT-Based Smart Assistant (Desktop Application)

This is a desktop-based smart assistant powered by OpenAI's GPT model. The application provides intelligent, conversational assistance directly on your local machine.

## Prerequisites

To use this application, you'll need an OpenAI API key. **For security reasons, the API key must not be hardcoded into the application or exposed to the user.**

### Steps to Obtain an API Key

1. Sign up or log in to your [OpenAI account](https://platform.openai.com/signup/).
2. Navigate to the **API Keys** section in your OpenAI dashboard.
3. Generate a new API key and store it securely.

## Setting Up the API Key

### 1. Storing the API Key Securely
For desktop applications, the API key must be stored securely to prevent unauthorized access. Use one of the following methods:

#### A. Environment Variables
Set an environment variable on your operating system:
- **Windows**:
  ```powershell
  $env:OPENAI_API_KEY="your-secret-key-here"

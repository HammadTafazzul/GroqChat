# Groq-LangChain-QA: A Question Answering Demo with Groq and LangChain

This project demonstrates a simple question-answering application built using LangChain, the Groq language model API, and Streamlit. It allows users to input a question, which is then passed to the Groq LLM (specifically the `llama3-8b-8192` model) via a LangChain chain. The LLM's response is then displayed in the Streamlit application.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [LangSmith Tracing (Optional)](#langsmith-tracing-optional)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project provides a basic example of how to build a user-friendly question-answering application using LangChain, Groq, and Streamlit. It showcases the core components needed for interacting with LLMs and building simple web applications around them.  It uses the `llama3-8b-8192` model from Groq.

## Features

* **Interactive Question Answering:** Users can input questions through a Streamlit web interface.
* **Groq LLM Integration:** Leverages the Groq API for powerful language model capabilities.
* **LangChain Orchestration:** Uses LangChain to manage prompts, LLM interaction, and output parsing.
* **Streamlit UI:** Provides a simple and intuitive user interface for interacting with the application.
* **Clear Prompting:** Employs a `ChatPromptTemplate` to structure prompts for the LLM.
* **Secure API Key Management:** Uses environment variables to store and access the Groq API key.
* **Optional LangSmith Tracing:** Includes setup for LangSmith tracing for monitoring and debugging.

## Installation

1. **Clone the repository:**
```bash
git clone [invalid URL removed]  # Replace with your repo URL
cd Groq-LangChain-QA
```
2. **Create a virtual environment (recommended):**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the required packages:**
```bash
pip install -r requirements.txt
```

4. **Create a .env file: See the Environment Variables section for details.** 

## Usage

1. Set up your environment variables: Make sure you have created the .env file and populated it with the necessary API keys (see Environment Variables).
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your browser: Streamlit will provide a URL (usually http://localhost:8501) that you can use to access the application.
4. Enter your question: Type your question into the text box and press Enter.
5. View the response: The LLM's response will be displayed below the input box.

## Project Structure

```bash
Groq-LangChain-QA/
├── app.py           # Main Streamlit application
├── requirements.txt  # Project dependencies
├── .gitignore        # Files to ignore by Git
├── .env             # Environment variables (not committed to repo)
└── README.md         # This file
```
## Environment Variables

Create a .env file in the root directory of the project and add the following environment variables: 
```bash
GROQ_API_KEY="your_groq_api_key"
# Optional for LangSmith tracing:
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="your_langchain_api_key"
```
Important:  Do not commit your .env file to version control, as it contains sensitive information.

## LangSmith Tracing (Optional)
To enable LangSmith tracing for debugging and monitoring, set the LANGCHAIN_TRACING_V2 and LANGCHAIN_API_KEY environment variables in your .env file.  You'll need a LangSmith account.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
   
## Contact
Hammad Tafazzul
hammad.tafazzul1@gmail.com

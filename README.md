# Agentic-Chatbot

An “agentic” AI chatbot framework built in Python.  
This repository contains the core code, configuration, and dependencies for running an autonomous, tool-enabled chatbot agent.

---

## 🚀 Features

- Modular agent architecture  
- Ability to call external tools / APIs  
- Conversational interface (Web / Streamlit / etc.)  
- Extensible — you can plug in new agents, tools, and functions  

---

## 🛠 Setup & Installation

### Prerequisites

- Python 3.8+  
- (Optional) Virtual environment tool — `venv` / `conda` / `poetry`  
- Any external API keys or credentials needed (e.g. for language models, embeddings, vector DBs)

### Installation Steps

# 1. Clone the repo
    git clone https://github.com/abhimanyu726/Agentic-Chatbot.git
    cd Agentic-Chatbot

# 2. Create & activate a virtual environment
    python -m venv venv
### On Linux / macOS:
    source venv/bin/activate
### On Windows:
    venv\Scripts\activate

# 3. Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

# 4. Run the application
python app.py

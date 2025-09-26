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
streamlit run app.py

# 🔧 Usage

Once your app is running, you can:

- Send user queries / messages
- Internally, the system will route the query to the appropriate sub-agent or tool
- The sub-agent can perform reasoning, fetch / retrieve information, call APIs, or generate a response
- The response is returned to the user

You can extend the system by:
- Adding new tools (e.g. weather API, calculator, web search)
- Adding new agent logic or branching strategies
- Integrating new memory or retrieval systems (vector DB, embedding models)

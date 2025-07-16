# 🧠 MCP Assistant

An intelligent desktop AI assistant built using:
- LangChain
- Ollama + Mistral
- Whisper (STT)
- pyttsx3 (TTS)
- pywhatkit (WhatsApp)
- SMTP (Email)
- CLI & Voice Modes

## 📦 Features
- Open apps
- Google search
- Send emails
- WhatsApp messaging
- Brainstorming
- Summarization
- File writer
- Shutdown system
- CLI and Voice Support

## 🚀 Setup

```bash
git clone https://github.com/your-username/mcp-assistant.git
cd mcp-assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py  # or python cli.py

extra modules
pip install langchain
pip install -U langchain-community
pip install -U langchain-ollama
pip install git+https://github.com/openai/whisper.git
pip install sounddevice
pip install scipy
pip install pyttsx3
pip install python-dotenv
pip install pyautogui
pip install pywhatkit

# 🧠 MCP Assistant (Your Local JARVIS)

This is a free, local JARVIS-like AI assistant that:
- Listens to your voice
- Thinks using a local LLM (like Mistral or Phi-3)
- Automates tasks on your PC
- Talks back like a real assistant

## 🚀 Features
- 🎙️ Voice input via Whisper
- 🧠 Brain powered by Ollama + LangChain
- 🖥️ Automates tasks using `pyautogui`, `os`, `keyboard`
- 🗣️ Speaks responses using TTS

## 🛠️ Setup

### 1. Install Python Dependencies
```bash
ollama pull mistral

for test_llm : pip install langchain
pip install --upgrade pip setuptools wheel
pip install langchain==0.1.16 langchain-core==0.1.40 langchain-community==0.3.27

for test_llm1 : pip install lahnchain-ollama

for main py : pip install pywhatkit
pip install git+https://github.com/openai/whisper.git (for speech-to-text)
pip install sounddevice
pip install scipy
pip install pyttsx3
pip install langchain
pip install -U langchain-community
pip install -U langchain-ollama
pip install python-dotenv
pip install pyautogui
pip install pywhatkit




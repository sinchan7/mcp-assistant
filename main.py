from core.brain import process_command
from voice.stt import listen
from voice.tts import speak

def main():
    speak("Hello, I'm JARVIS. How can I help you?")
    while True:
        try:
            command = listen()
            print(f"You said: {command}")
            response = process_command(command)
            speak(response)
        except KeyboardInterrupt:
            speak("Shutting down Meeeee.")
            break

if __name__ == "__main__":
    main()



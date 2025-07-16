import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile

model = whisper.load_model("base")

def listen():
    duration = 5
    samplerate = 16000
    print("🎤 Listening...")

    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav.write(f.name, samplerate, np.squeeze(audio))
        result = model.transcribe(f.name)
        return result["text"]

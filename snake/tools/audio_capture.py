import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100

def record(seconds, path="output.wav"):
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(path, fs, recording)
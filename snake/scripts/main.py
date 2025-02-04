from tools.audio_decode import transcribe
from tools.audio_capture import record

def main():
    path = "output.wav"
    print("Audio recording")
    record(10, path)
    print("Decoding recording")
    text = transcribe(path)
    print(text)

if __name__ == "__main__":
    main()
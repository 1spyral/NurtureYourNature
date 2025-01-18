from audio_decode import transcribe
from audio_capture import record

def main():
    path = "output.wav"
    print("Audio recording")
    record(5, path)
    print("Decoding recording")
    text = transcribe(path)
    print(text)

if __name__ == "__main__":
    main()
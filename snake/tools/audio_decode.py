import whisper

model = whisper.load_model("base")
options = whisper.DecodingOptions()

print("Whisper model loaded")

def transcribe(path):
    result = model.transcribe(path)
    return result["text"]

def decode(path):
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    result = whisper.decode(model, mel, options)

    return result.text
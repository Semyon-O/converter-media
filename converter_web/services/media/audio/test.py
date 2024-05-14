from abstract_audio_strategy import AudioConversionContext
import converters

if __name__ == "__main__":
    audio = AudioConversionContext(converters.OGGStrategy())
    audio.convert("audio/record.mp3")
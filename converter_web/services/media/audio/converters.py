import os

from abstract_audio_strategy import AudioConverterStrategy
from pydub import AudioSegment


class WAVStrategy(AudioConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        audio = AudioSegment.from_file(input_file)
        audio.export(f"{name}_converted.wav", format="wav")


class MP3Strategy(AudioConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        audio = AudioSegment.from_file(input_file)
        audio.export(f"{name}_converted.mp3", format="mp3")


class OGGStrategy(AudioConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        audio = AudioSegment.from_file(input_file)
        audio.export(f"{name}_converted.ogg", format="ogg")

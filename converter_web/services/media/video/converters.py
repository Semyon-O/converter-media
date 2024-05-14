import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from .abstract_video_strategy import VideoConverterStrategy


class MP4VideoConverter(VideoConverterStrategy):

    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        video = VideoFileClip(input_file)
        output_file = input_file.replace(extension, '_converted.mp4')
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        return output_file


class AVIVideoConverter(VideoConverterStrategy):
    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        video = VideoFileClip(input_file)
        output_file = input_file.replace(extension, '_converted.avi')
        video.write_videofile(output_file, codec='mpeg4', audio_codec='pcm_s16le')
        return output_file


class GIFVideoConverter(VideoConverterStrategy):
    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        video = VideoFileClip(input_file)
        output_file = input_file.replace(extension, '_converted.gif')
        video.write_gif(output_file)
        return output_file


class WebMVideoConverter(VideoConverterStrategy):
    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        video = VideoFileClip(input_file)
        output_file = input_file.replace(extension, '_converted.webm')
        video.write_videofile(output_file, codec='libvpx', audio_codec='libvorbis')
        return output_file


class MOVVideoConverter(VideoConverterStrategy):
    def convert(self, input_file):
        name, extension = os.path.splitext(input_file)
        video = VideoFileClip(input_file)
        output_file = input_file.replace(extension, '_converted.mov')
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        return output_file


class VideoConversionContext:
    def __init__(self, strategy: VideoConverterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: VideoConverterStrategy):
        if isinstance(strategy, VideoConverterStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Strategy must be an instance of VideoConverterStrategy")

    def convert_video(self, input_file):
        return self.strategy.convert(input_file)
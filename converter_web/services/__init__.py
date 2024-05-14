from moviepy.editor import VideoFileClip


def convert_video(input_file, output_format):
    try:
        # Определяем выходное имя файла с новым форматом
        output_file = input_file.replace('.mp4', f'.{output_format}')

        # Загружаем видеофайл
        video = VideoFileClip(input_file)

        # Сохраняем конвертированный файл в указанном формате
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')

        return output_file  # Возвращаем путь к конвертированному файлу

    except Exception as e:
        return f"Ошибка конвертации: {str(e)}"


converted_file_path = convert_video(r"../video/Demo.mp4", "gif")
print(f"Конвертированный файл: {converted_file_path}")
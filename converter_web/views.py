from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render
from .services.media.video.abstract_video_strategy import VideoConversionContext
from .services.media.photo.abstract_photo_strategy import PhotoConversionContext
from .services.media.video import converters as video_conv
from .services.media.photo import converters as photo_conv
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    # Дополнительные действия после выхода
    return HttpResponseRedirect('/')


def convert_video(request):
    if request.method == 'POST':
        output_format = request.POST.get('output_format')  # Получаем выбранный формат из формы
        uploaded_file = request.FILES['video_file']  # Получаем загруженный файл

        print(output_format)

        if not request.COOKIES.get("sessionid", False) and uploaded_file.size > 20971520:
            return render(request, 'index.html')

        input_file_path = f'input_videos/{str(uploaded_file)}'
        with default_storage.open(input_file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)


        formats_strategy = {
            "mp4": video_conv.MP4VideoConverter(),
            "webm": video_conv.WebMVideoConverter(),
            "mov": video_conv.MOVVideoConverter(),
            "avi": video_conv.AVIVideoConverter(),
            "gif": video_conv.GIFVideoConverter(),
        }

        choosed_format_strategy = formats_strategy.get(output_format)

        convert_context = VideoConversionContext(choosed_format_strategy)
        updated_file = convert_context.convert_video(f"input_videos/{str(uploaded_file)}")

        response = FileResponse(default_storage.open(updated_file, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{str(updated_file).split("/")[1]}"'
        return response

    return HttpResponse("Invalid request method")


def convert_photo(request):
    if request.method == 'POST':
        output_format = request.POST.get('output_format')  # Получаем выбранный формат из формы
        uploaded_file = request.FILES['video_file']  # Получаем загруженный файл

        print(output_format)

        # if not request.COOKIES.get("sessionid", False) and uploaded_file.size > 20971520:
        #     return render(request, 'index.html')

        input_file_path = f'input_videos/{str(uploaded_file)}'
        with default_storage.open(input_file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        formats_strategy = {
            "jpg": photo_conv.JPEGConverter(),
            "png": photo_conv.PNGConverter(),
            "tiff": photo_conv.TIFFConverter(),
            "bmp": photo_conv.BMPConverter(),
        }

        choosed_format_strategy = formats_strategy.get(output_format)

        convert_context = PhotoConversionContext(choosed_format_strategy)
        updated_file = convert_context.convert(f"input_videos/{str(uploaded_file)}")

        response = FileResponse(default_storage.open(updated_file, 'rb'), content_type=f'image/{output_format}')
        response['Content-Disposition'] = f'attachment; filename="{str(updated_file).split("/")[1]}"'
        return response

    return HttpResponse("Invalid request method")


def convert_audio(request):
    ...


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'authed_user.html')

    return render(request, 'login.html')


def register_view(request):
    # Логика для страницы регистрации (register)

    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password2 == password1:
            user = User.objects.create_user(username=username, email="-", password=password1)
            login(request, user)
            return render(request, 'authed_user.html')
        else:
            return render(request, 'register.html')

    return render(request, 'register.html')


def video_convert_view(request):
    return render(request, 'video_converter_page.html')


def audio_convert_view(request):
    return render(request, 'audio_converter_page.html')


def photo_convert_view(request):
    return render(request, 'photo_converter_page.html')
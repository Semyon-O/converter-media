"""
URL configuration for full_converter_video project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from converter_web import views as converter_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', converter_views.index),
    path('convert/', converter_views.convert_video, name='convert'),
    path('make_convert_photo/', converter_views.convert_photo, name='make_convert_photo'),
    path('login_page/', converter_views.login_view, name='login_view'),
    path('register_page/', converter_views.register_view, name='register_view'),
    path('logout/', converter_views.logout_view, name='logout'),

    path('video_convert/', converter_views.video_convert_view, name='video_convert_view'),
    path('audio_convert/', converter_views.audio_convert_view, name='audio_convert_view'),
    path('photo_convert/', converter_views.photo_convert_view, name='photo_convert_view')
]

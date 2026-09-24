from django.shortcuts import render
from .models import Song, Photo, Concert

def home(request):
    return render(request, 'core/home.html')

def songs(request):
    all_songs = Song.objects.all()
    return render(request, 'core/songs.html', {'songs': all_songs})

def photos(request):
    all_photos = Photo.objects.all()
    return render(request, 'core/photos.html', {'photos': all_photos})

def concerts(request):
    all_concerts = Concert.objects.all()
    return render(request, 'core/concerts.html', {'concerts': all_concerts})
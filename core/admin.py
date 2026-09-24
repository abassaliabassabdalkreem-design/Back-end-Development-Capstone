from django.contrib import admin
from .models import Song, Photo, Concert

admin.site.register(Song)
admin.site.register(Photo)
admin.site.register(Concert)
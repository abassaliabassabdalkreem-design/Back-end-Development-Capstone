from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Concert(models.Model):
    venue = models.CharField(max_length=200)
    date = models.DateField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.venue} - {self.city}"
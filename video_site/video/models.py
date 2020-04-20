from django.db import models


# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=30)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='uploads')
    thumbnail_file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.title

from django.db import models

class UserMedia(models.Model):
    name_code = models.CharField(max_length=100) # The "Name" you will type to unlock
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    image_file = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name_code} - {self.title}"
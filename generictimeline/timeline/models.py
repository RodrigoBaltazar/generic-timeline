from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    approved = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='')

    def __str__(self):
        return self.name

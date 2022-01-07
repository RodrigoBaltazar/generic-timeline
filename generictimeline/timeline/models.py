from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    filepath = models.CharField(max_length=200)
    approved = models.DateTimeField()

    def __str__(self):
        return self.name

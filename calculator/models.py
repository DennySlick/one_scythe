from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=25)
    pts = models.IntegerField()

    def __str__(self):
        return ":".join([self.nickname, str(self.pts)])

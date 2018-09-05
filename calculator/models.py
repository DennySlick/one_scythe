from django.db import models
from django.utils import timezone

class Player(models.Model):
    nickname = models.CharField(max_length=25)
    pts = models.IntegerField()

    def __str__(self):
        return " : ".join([self.nickname, str(self.pts)])

class GameMode(models.Model):
    line = models.CharField(max_length=15)

    def __str__(self):
        return self.line

class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    mode = models.ForeignKey(
        'GameMode',
        on_delete=models.CASCADE,
    )
    players = models.ManyToManyField(Player, related_name='games')

    def __str__(self):
        return (str(self.mode) + " #" + str(self.id))

from django.db import models
from django.utils import timezone


class Player(models.Model):
    nickname = models.CharField(max_length=25)
    pts = models.IntegerField(default=1000)

    class Meta:
        ordering = ['-pts', 'nickname']

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
    players = models.ManyToManyField(
        Player,
        related_name='games',
        blank=True,
        through='PlayerInGame',
    )

    SENTINEL = 'Sentinel'
    SCOURGE = 'Scourge'
    DRAW = 'Draw'
    WINNER_CHOICES = (
        (SENTINEL, 'Sentinel'),
        (SCOURGE, 'Scourge'),
        (DRAW, 'Draw'),
    )
    winner = models.CharField(
        max_length=10,
        choices=WINNER_CHOICES,
        default=DRAW,
    )
    cost = models.IntegerField(default=25)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return (str(self.mode) + " #" + str(self.id))


class PlayerInGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playeringame_set')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='playeringame_set')

    pts_start = models.IntegerField(default=None)
    pts_dif = models.IntegerField(default=None)

    SENTINEL = 'Sentinel'
    SCOURGE = 'Scourge'
    SIDE_CHOICES = (
        (SENTINEL, 'Sentinel'),
        (SCOURGE, 'Scourge'),
    )
    side = models.CharField(
        max_length=10,
        choices=SIDE_CHOICES,
        default=SENTINEL,
    )

    class Meta:
        ordering = ['game', '-side', 'player']

    def get_points(thePlayer):
        return thePlayer.pts

    def save(self):
        if self.player != None and self.pts_start == None:
            self.pts_start = self.player.pts
        if self.game != None and self.pts_dif == None:
            self.pts_dif = self.game.cost
            if self.game.winner == self.side:
                self.player.pts += self.pts_dif
            elif self.game.winner != 'Draw':
                self.player.pts -= self.pts_dif
            self.player.save()

        super(PlayerInGame, self).save()

    def __str__(self):
        return (str(self.game) + " | " + str(self.player)) + " | " + self.side

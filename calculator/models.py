from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

import datetime

DEBUG_OUTPUT = True
def debug_output(line):
    if DEBUG_OUTPUT:
        date = datetime.datetime.now()
        date = date.strftime('[%d/%b/%Y %H:%M:%S]')
        print(str(date) + " DEBUG_OUTPUT: \"" + line + "\"")

class Player(models.Model):
    nickname = models.CharField(max_length=25)
    pts = models.IntegerField(default=1000)

    class Meta:
        ordering = ['-pts', 'nickname']

    def __str__(self):
        return " | ".join([self.nickname, str(self.pts)])


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
    cost = models.IntegerField(default=0)
    COST_CONST = 25

    avg_sentinel = models.IntegerField(default=0)
    avg_scourge = models.IntegerField(default=0)
    count_players_sentinel = models.IntegerField(default=0)
    count_players_scourge = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def get_game_cost(self):
        if self.avg_sentinel == 0 and self.avg_scourge == 0 and self.playeringame_set:
            for game_info in self.playeringame_set.all():
                if game_info.side == 'Sentinel':
                    self.avg_sentinel += game_info.pts_start
                    self.count_players_sentinel += 1
                elif game_info.side == 'Scourge':
                    self.avg_scourge += game_info.pts_start
                    self.count_players_scourge += 1
            if self.count_players_sentinel != 0 and self.count_players_scourge != 0:
                self.avg_sentinel /= self.count_players_sentinel
                self.avg_scourge /= self.count_players_scourge

                if self.cost == 0 and self.winner != 'Draw':
                    if self.winner == 'Sentinel':
                        self.cost = int(self.COST_CONST * self.avg_scourge / self.avg_sentinel)
                    elif self.winner == 'Scourge':
                        self.cost = int(self.COST_CONST * self.avg_sentinel / self.avg_scourge)
                    for game_info in self.playeringame_set.all():
                        game_info.save()
        else:
            pass

    def save(self, *args, **kwargs):
        self.get_game_cost()
        return super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.mode) + " #" + str(self.id)) + " | Avg: " + str(int( (self.avg_sentinel + self.avg_scourge)/2))

class PlayerInGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playeringame_set')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='playeringame_set')

    pts_start = models.IntegerField(default=None)
    pts_dif = models.IntegerField(default=0)

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

    def get_pts_start(self):
        if self.player != None and self.pts_start == None:
            self.pts_start = self.player.pts
        else:
            pass

    def change_player_pts(self):
        if (int(self.pts_dif) >= 0):
            debug_output("CHANGE PLAYER PTS: " + str(self.player) + " +" + str(self.pts_dif))
        else:
            debug_output("CHANGE PLAYER PTS: " + str(self.player) + " " + str(self.pts_dif))
        self.player.pts += self.pts_dif
        self.player.save()

    def get_pts_changes(self):
        debug_output("GET PTS CHANGES: " + str(self))
        if self.game != None and self.pts_dif == 0:
            debug_output("TRY PTS CHANGES: " + str(self))
            if self.game.cost != 0 and self.game.winner != 'Draw':
                if self.game.winner == self.side:
                    self.pts_dif = self.game.cost
                #elif self.game.winner == 'Draw':
                #    self.pts_dif = 0
                else:
                    self.pts_dif = -(self.game.cost)
                self.change_player_pts()
            else:
                debug_output("GAME COST = 0: " + str(self))
        else:
            debug_output("CAN'T CHANGE PTS")
            pass

    def save(self):
        self.get_pts_start()
        self.get_pts_changes()
        super(PlayerInGame, self).save()


    def __str__(self):
        return (str(self.game) + " ][ " + str(self.player)) + " | " + self.side


@receiver(post_save, sender=Game)
def game_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    debug_output("GAME CHANGED: " + str(instance))


@receiver(post_save, sender=PlayerInGame)
def playeringame_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    debug_output("PlayerInGame CHANGED: " + str(instance))

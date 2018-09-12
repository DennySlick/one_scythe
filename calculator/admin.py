from django.contrib import admin

from .models import Player, GameMode, Game, PlayerInGame

class PlayerInGameInline(admin.TabularInline):
    model = PlayerInGame
    extra = 0
    exclude = ['pts_start', 'pts_dif']

class GameAdmin(admin.ModelAdmin):
    inlines = (PlayerInGameInline,)
    exclude = ['cost', 'avg_sentinel', 'avg_scourge', 'count_players_sentinel', 'count_players_scourge']

    #def save_model(self, request, obj, form, change):
    #    if obj.playeringame_set:
    #        #form.cleaned_data['players'] = obj.copy_holidays_from.players.all()
    #        print("PLAYERINGAME_SET")
    #        print(obj.playeringame_set.all())
    #        if obj.avg_sentinel == 0 and obj.avg_scourge == 0:
    #            for game_info in obj.playeringame_set.all():
    #                if game_info.side == 'Sentinel':
    #                    obj.avg_sentinel += game_info.pts_start
    #                    obj.count_players_sentinel += 1
    ##                    obj.avg_scourge += game_info.pts_start
    #                    obj.count_players_scourge += 1
    #            if obj.count_players_sentinel != 0 and obj.count_players_scourge != 0:
    #                obj.avg_sentinel /= obj.count_players_sentinel
    #                obj.avg_scourge /= obj.count_players_scourge
#
#                    if obj.cost == 0 and obj.winner != 'Draw':
#                        if obj.winner == 'Sentinel':
#                            obj.cost = int(obj.COST_CONST * obj.avg_scourge / obj.avg_sentinel)
#                        elif obj.winner == 'Scourge':
#                            obj.cost = int(obj.COST_CONST * obj.avg_sentinel / obj.avg_scourge)
#                        for game_info in obj.playeringame_set.all():
#                            game_info.save()
#        else:
#            print("NO SET")
#
#        super(GameAdmin, self).save_model(request, obj, form, change)

class PlayerAdmin(admin.ModelAdmin):
    inlines = (PlayerInGameInline,)
    exclude = ['wins', 'loses']
    list_display = ('nickname', 'pts')


admin.site.register(Player, PlayerAdmin)
admin.site.register(GameMode)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerInGame)

from django.contrib import admin

from .models import Player, GameMode, Game, PlayerInGame

class PlayerInGameInline(admin.TabularInline):
    model = PlayerInGame
    extra = 0
    exclude = ['pts_start', 'pts_dif']

class GameAdmin(admin.ModelAdmin):
    inlines = (PlayerInGameInline,)

class PlayerAdmin(admin.ModelAdmin):
    inlines = (PlayerInGameInline,)
    list_display = ('nickname', 'pts')


admin.site.register(Player, PlayerAdmin)
admin.site.register(GameMode)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerInGame)

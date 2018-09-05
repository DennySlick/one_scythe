from django.contrib import admin


from .models import Player, GameMode, Game
from .forms import PlayerAdminForm

class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('players',)

class PlayerAdmin(admin.ModelAdmin):
    form = PlayerAdminForm
    list_display = ('nickname', 'pts')

admin.site.register(Player, PlayerAdmin)
admin.site.register(GameMode)
admin.site.register(Game, GameAdmin)


##########################test

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Player, Game

class PlayerAdminForm(forms.ModelForm):
    games = forms.ModelMultipleChoiceField(
        queryset=Game.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Games'),
            is_stacked=False
        )
    )

    class Meta:
        model = Player
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PlayerAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['games'].initial = self.instance.games.all()

    def save(self, commit=True):
        player = super(PlayerAdminForm, self).save(commit=False)

        if commit:
            player.save()

        if player.pk:
            player.games = self.cleaned_data['games']
            self.save_m2m()

        return player


class GameAdminForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=Player.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Players'),
            is_stacked=False
        )
    )

    class Meta:
        model = Game
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GameAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['players'].initial = self.instance.games.all()

    def save(self, commit=True):
        game = super(GameAdminForm, self).save(commit=False)

        if commit:
            game.save()

        if game.pk:
            game.players = self.cleaned_data['players']
            self.save_m2m()

        return game

from django.shortcuts import render
from .models import Player, Game

def balance_calculator(request):
    return render(request, 'calculator/balance_calculator.html', {})

def players_list(request):
    players = Player.objects.all().order_by('-pts');
    return render(request, 'calculator/players_list.html', { 'players': players })

def games_list(request):
    games = Game.objects.all().order_by('-date');
    return render(request, 'calculator/games_list.html', { 'games': games })

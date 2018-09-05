from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Game

def balance_calculator(request):
    return render(request, 'calculator/balance_calculator.html', {})

def players_list(request):
    players = Player.objects.all().order_by('-pts');
    return render(request, 'calculator/players_list.html', { 'players': players })

def games_list(request):
    games = Game.objects.all().order_by('-date');
    return render(request, 'calculator/games_list.html', { 'games': games })

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'calculator/player_detail.html', { 'player': player })

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'calculator/game_detail.html', { 'game': game })

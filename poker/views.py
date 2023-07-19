from django.shortcuts import render, redirect
from .models import *
from .forms import UpdatePokerPlayer
from django.contrib import messages


def show_poker_page(request):
    seasons_data = PokerSeason.objects.all().select_related()
    seasons = {}
    
    for season in seasons_data:
        seasons[season] = []
        players = PokerPlayer.objects.filter(pokerplayergameperformance__game__season=season).distinct()
        for player in players:
            balance = 0
            for game in player.pokerplayergameperformance_set.all():
                balance += game.chips
            seasons[season].append((player, balance))
        seasons[season].sort(key=lambda x: x[1], reverse=True)


    return render(request, "poker/show_poker_page.html", {"seasons_data": seasons})

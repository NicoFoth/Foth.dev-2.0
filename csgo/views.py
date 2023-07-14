from django.shortcuts import render, redirect
from .models import *
from .forms import SelectPlayers
from .generate_team import generate
from django.contrib import messages

def show_csgo_stats(request):
    seasons = {}
    seasons_query = CSSeason.objects.all()

    for season in seasons_query:
        seasonplayerelos = CSPlayerSeasonElo.objects.filter(season=season).select_related()
        seasons[season] = []
        for seasonplayerelo in seasonplayerelos:
            seasons[season].append((seasonplayerelo.player.name, seasonplayerelo.elo))

        
            

    return render(request, "csgo/show_csgo_stats.html", {"seasons": seasons})

def select_players(request):

    if request.method == "POST":

        form = SelectPlayers(request.POST)
        if form.is_valid():
            selected_players = form.clean()

            player_dict = {}
            queryset = None

            for dict in selected_players:
                queryset = selected_players[dict]

            for item in queryset:
                player_dict[item.name] = item.elo

            if len(player_dict) >= 4:
            
                team_a, team_b = generate(player_dict)
            
                return render(request, "csgo/show_teams.html", {"team_a": team_a, "team_b": team_b})
            
            else:

                messages.warning(request, "Bitte wählen Sie mindestens 4 Spieler aus!")
                
                return redirect("select_players")

    else:

        selectform = SelectPlayers()
        
        return render(request, "csgo/select_players.html", {"selectform": selectform})


def player_profile(request, steam_id):


    return render(request, 'csgo/player_profile.html', {"player": ()})
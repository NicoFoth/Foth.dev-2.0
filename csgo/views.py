from django.shortcuts import render, redirect
from django.db.models import Count
from .models import *
from .forms import SelectPlayers
from .generate_team import generate
from django.contrib import messages

def cs_overview(request):
    seasons = {}
    seasons_query = CSSeason.objects.all()

    for season in seasons_query:
        seasonplayerelos = CSPlayerSeasonElo.objects.filter(season=season).select_related().order_by("-elo")
        seasons[season] = []
        for seasonplayerelo in seasonplayerelos:
            seasons[season].append((seasonplayerelo.player.name, seasonplayerelo.elo))

    return render(request, "csgo/cs_overview.html", {"seasons": seasons})


def season_overview(request, season_id):
    season_object = CSSeason.objects.get(pk=season_id)
    ranked_players = CSPlayerMatch.objects.filter(match__season=season_id).values('player').annotate(game_count=Count('player')).filter(game_count__gte=10).values_list('player', flat=True)
    seasonplayerelos = CSPlayerSeasonElo.objects.filter(season=season_object, player__in=ranked_players).select_related().order_by("-elo")
    unrankedplayers = CSPlayerMatch.objects.filter(match__season=season_id).exclude(player__in=ranked_players)
    return render(request, "csgo/season_overview.html", {"season": season_object, "seasonplayerdata": seasonplayerelos, "unrankedplayers": unrankedplayers})

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
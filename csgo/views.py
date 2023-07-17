from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Case, When
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
            seasons[season].append((seasonplayerelo.player, seasonplayerelo.elo))

    return render(request, "csgo/cs_overview.html", {"seasons": seasons})


def season_overview(request, season_id):
    season_object = CSSeason.objects.get(pk=season_id)
    season_player_elos = CSPlayerSeasonElo.objects.filter(season=season_object).select_related().order_by("-elo")

    ranked_match_counts = CSPlayerMatch.objects.filter(match__season=season_object).annotate(matchCount=Count('match')).filter(matchCount__gte=10)

    ranked_players = CSPlayerSeasonElo.objects.filter(season=season_object, player__pk__in=ranked_match_counts.values_list("player", flat=True).distinct())

    unranked_players = CSPlayerSeasonElo.objects.filter(season=season_object).exclude(player__pk__in=ranked_match_counts.values_list("player", flat=True).distinct())

    matches = CSMatch.objects.filter(season=season_id).order_by("-date")

    return render(request, "csgo/season_overview.html", {"season": season_object, "ranked_players": ranked_players, "unranked_players": unranked_players, "matches": matches})


def match_overview(request, match_id):
    match_object = CSMatch.objects.get(pk=match_id)
    match_players = CSPlayerMatch.objects.filter(match=match_object).select_related().order_by("kills")

    return render(request, "csgo/match_overview.html", {"match": match_object, "match_players": match_players})


def player_profile(request, player_id):
    player_object = CSPlayer.objects.get(pk=player_id)
    player_matches = CSPlayerMatch.objects.filter(player=player_object).select_related().order_by("-match__date")
    season_elos = CSPlayerSeasonElo.objects.filter(player=player_object).select_related().order_by("-season__date")

    player_stats = CSPlayerMatch.objects.filter(player=player_object).select_related().aggregate(
        kills=Sum('kills'), deaths=Sum('deaths'), assist= Sum('assists'),
        kd=Sum('kills')/Sum('deaths'), headshots=Sum('headshotKills'),
        enemiesFlashed=Sum('enemiesFlashed'), utilityDamage=Sum('utilityDamage'),
        matchCount=Count('match'), winCount=Count(Case(When(win=True, then=1))))

    return render(request, "csgo/player_profile.html", {"player": player_object, "player_matches": player_matches, "season_elos": season_elos, "player_stats": player_stats})


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

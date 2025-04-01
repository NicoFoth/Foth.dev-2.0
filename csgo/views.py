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

    # Get players with 10 or more matches in the season
    ranked_match_counts = CSPlayerMatch.objects.filter(match__season=season_object).annotate(matchCount=Count('match')).filter(matchCount__gte=10)
    ranked_player_ids = ranked_match_counts.values_list("player", flat=True).distinct()

    # Get ranked players with their stats
    ranked_players = CSPlayerMatch.objects.filter(
        match__season=season_object,
        player__pk__in=ranked_player_ids
    ).values('player').annotate(
        kills=Sum('kills'),
        deaths=Sum('deaths'),
        assists=Sum('assists'),
        matchCount=Count('match'),
        winCount=Count(Case(When(win=True, then=1)))
    ).order_by('-kills')

    # Calculate derived stats for ranked players
    for player in ranked_players:
        player['kd_ratio'] = round(player['kills'] / player['deaths'], 2) if player['deaths'] > 0 else float('inf')
        player['win_rate'] = round((player['winCount'] / player['matchCount']) * 100, 1) if player['matchCount'] > 0 else 0
        player['name'] = CSPlayer.objects.get(pk=player['player']).name
        player['id'] = player['player']

    # Get unranked players with their stats
    unranked_players = CSPlayerMatch.objects.filter(
        match__season=season_object
    ).exclude(
        player__pk__in=ranked_player_ids
    ).values('player').annotate(
        kills=Sum('kills'),
        deaths=Sum('deaths'),
        assists=Sum('assists'),
        matchCount=Count('match'),
        winCount=Count(Case(When(win=True, then=1)))
    ).order_by('-kills')

    # Calculate derived stats for unranked players
    for player in unranked_players:
        player['kd_ratio'] = round(player['kills'] / player['deaths'], 2) if player['deaths'] > 0 else float('inf')
        player['win_rate'] = round((player['winCount'] / player['matchCount']) * 100, 1) if player['matchCount'] > 0 else 0
        player['name'] = CSPlayer.objects.get(pk=player['player']).name
        player['id'] = player['player']

    matches = CSMatch.objects.filter(season=season_id).order_by("-date")

    return render(request, "csgo/season_overview.html", {
        "season": season_object,
        "ranked_players": ranked_players,
        "unranked_players": unranked_players,
        "matches": matches
    })


def match_overview(request, match_id):
    match_object = CSMatch.objects.get(pk=match_id)
    match_players = CSPlayerMatch.objects.filter(match=match_object).select_related().order_by("kills")

    return render(request, "csgo/match_overview.html", {"match": match_object, "match_players": match_players})


def player_profile(request, player_id):
    player_object = CSPlayer.objects.get(pk=player_id)
    player_matches = CSPlayerMatch.objects.filter(player=player_object).select_related().order_by("-match__date")
    season_elos = CSPlayerSeasonElo.objects.filter(player=player_object).select_related().order_by("-season__date")

    # Get base stats
    player_stats = CSPlayerMatch.objects.filter(player=player_object).select_related().aggregate(
        kills=Sum('kills'),
        deaths=Sum('deaths'),
        assists=Sum('assists'),
        headshots=Sum('headshotKills'),
        enemiesFlashed=Sum('enemiesFlashed'),
        utilityDamage=Sum('utilityDamage'),
        matchCount=Count('match'),
        winCount=Count(Case(When(win=True, then=1)))
    )
    
    # Calculate derived stats
    player_stats['kd_ratio'] = round(player_stats['kills'] / player_stats['deaths'], 2) if player_stats['deaths'] > 0 else float('inf')
    player_stats['win_rate'] = round((player_stats['winCount'] / player_stats['matchCount']) * 100, 1) if player_stats['matchCount'] > 0 else 0
    
    # Get season stats
    player_seasons = CSPlayerMatch.objects.filter(player=player_object).values("match__season").annotate(
        kills=Sum('kills'),
        deaths=Sum('deaths'),
        assists=Sum('assists'),
        headshots=Sum('headshotKills'),
        enemiesFlashed=Sum('enemiesFlashed'),
        utilityDamage=Sum('utilityDamage'),
        matchCount=Count('match'),
        winCount=Count(Case(When(win=True, then=1)))
    ).order_by("match__season__startDate")

    # Calculate derived stats for each season
    for season in player_seasons:
        season['kd_ratio'] = round(season['kills'] / season['deaths'], 2) if season['deaths'] > 0 else float('inf')
        season['win_rate'] = round((season['winCount'] / season['matchCount']) * 100, 1) if season['matchCount'] > 0 else 0

    return render(request, "csgo/player_profile.html", {
        "player": player_object,
        "player_matches": player_matches,
        "season_elos": season_elos,
        "player_stats": player_stats,
        "player_seasons": player_seasons
    })


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

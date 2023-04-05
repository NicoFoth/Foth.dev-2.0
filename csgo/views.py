from django.shortcuts import render, redirect
from .models import CsgoPlayer
from .forms import SelectPlayers
from .generate_team import generate
from django.contrib import messages

def show_csgo_stats(request):
    
    player_data = CsgoPlayer.objects.order_by("-elo")

    player_list_ranked = []
    player_list_unranked = []

    for player in player_data:
        if player.played_matches >= 10:
            player_list_ranked.append(player)
        else:
            player_list_unranked.append(player)

    unranked_matches_for_rank = [10-int(player.played_matches) for player in player_list_unranked]

    player_data_unranked = zip(player_list_unranked, unranked_matches_for_rank)

    return render(request, "csgo/show_csgo_stats.html", {"player_data_ranked": player_list_ranked, "player_data_unranked": player_data_unranked, "unranked_matches": unranked_matches_for_rank})

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

    player_details = CsgoPlayer.objects.get(steam_id=steam_id)

    return render(request, 'csgo/player_profile.html', {"player": player_details})
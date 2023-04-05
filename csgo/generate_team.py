
def generate(players):

    sorted_dict = dict(sorted(players.items(), key=lambda item: item[1]))

    team_a = []
    team_b = []
    player_names_sorted = list(sorted_dict.keys())

    team_a.append(player_names_sorted[0])
    team_a.append(player_names_sorted[-1])
    team_b.append(player_names_sorted[1])
    team_b.append(player_names_sorted[-2])
    
    for _ in range(2):
        player_names_sorted.pop(0)
        player_names_sorted.pop(-1)

    if len(sorted_dict) % 2 == 0:
    
        for _ in range((len(player_names_sorted)//2)):
            current_elo = [0, 0]
            for name in team_a:
                current_elo[0] += sorted_dict[name]
            for name in team_b:
                current_elo[1] += sorted_dict[name]

            if current_elo[0] < current_elo[1]:
                team_a.append(player_names_sorted[0])
                team_b.append(player_names_sorted[1])
                player_names_sorted.pop(0)
                player_names_sorted.pop(0)
       
            else:
                team_b.append(player_names_sorted[0])
                team_a.append(player_names_sorted[1])
                player_names_sorted.pop(0)
                player_names_sorted.pop(0)

    else:

        for _ in range(len(player_names_sorted)):
            current_elo = [0, 0]

            for name in team_a:
                current_elo[0] += sorted_dict[name]
            for name in team_b:
                current_elo[1] += sorted_dict[name]

            if current_elo[0] < current_elo[1]:
                team_a.append(player_names_sorted[0])
            else:
                team_b.append(player_names_sorted[0])
            
            player_names_sorted.pop(0)


    return team_a, team_b
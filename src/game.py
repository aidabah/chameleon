def set_up_players ():
    player_amt = int(input("How many players? "))
    player_names = []
    while len(player_names) < player_amt:
        player_names.append(input("What is your name? "))
    return player_names

set_up_players()

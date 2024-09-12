import random

def set_up_players ():
    player_amt = int(input("How many players? "))
    player_names = []
    while len(player_names) < player_amt:
        player_names.append(input("What is your name? "))
    return player_names

players = set_up_players()

def choose_chameleon (players):
    chameleon = random.choice(players)
    
    print(chameleon)
    return chameleon

choose_chameleon(players)


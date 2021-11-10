# CCC - 2003 - S3
# Snakes and Ladders

#   SNAKES:
#   54 - 19
#   90 - 48
#   99 - 77

#   LADDERS:
#   9 - 34
#   40 - 64
#   67 - 86

player_pos = 1  # default position
snakes_ladders = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}    # Dictionary to store snakes, ladders and  final pos as key value pairs
game_on = True

def playgame():
    global player_pos
    global game_on
    user_input = int(input())
    temp = player_pos   
    if user_input != 0:
        player_pos = player_pos + user_input
        if player_pos in snakes_ladders.keys():
            player_pos = snakes_ladders[player_pos]
    elif user_input == 0:
        game_on = False
        print("You Quit!")
        return
    if player_pos > 100 or user_input < 2 or user_input > 12:
        player_pos = temp
        print("You are now on square", player_pos)
    elif player_pos == 100:
        game_on = False
        print("You are now on square 100")
        print("You Win!")

    else:
        print("You are now on square",player_pos)


while game_on:
    playgame()

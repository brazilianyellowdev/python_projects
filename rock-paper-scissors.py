import random

def play():
    user = input("Write:\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's '])

    if user == computer:
        return 'It\'s a tie !'

    # r > s, p > r, s > p
    if is_win(user, computer):
        return 'You won!'

    return 'You lost... So sad :( '

def is_win(player, opponent):
    #return True if player wins
    # r > s, p > r, s > p 
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True 

print(play())
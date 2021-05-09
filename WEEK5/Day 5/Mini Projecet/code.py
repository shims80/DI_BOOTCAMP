# Mini-Project #1: Rock, Paper, Scissors
import random
import math


def play():
    user = input(
        "what's your choise? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def is_win(player, opponent):
    # returen true is the player beats the opponent
    # wining conditions : r > s, s> p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):
    # play against the computer until someone wins of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/1)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print(' you and the computer have both chosen {}.IT\'S A TIE\n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('you chose {} and computer chose {} YOU WON :)!\n'.format(
                user, computer))
        else:
            computer_wins += 1
            print(
                'you chose {} and computer chose {} YOU LOST :(\n'.format(user, computer))
        
    if player_wins > computer_wins:
        print('you have won the best of {} games!'.format(n))
    else:
        print('computer won the best of {} games'.format(n))


if __name__ == '__main__':
    play_best_of(3)

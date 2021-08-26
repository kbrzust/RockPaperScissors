import random


def play():
    user = input("Wpisz 'p' jeśli wybierasz papier, 'k' jeśli kamień lub 'n' jeśli nożyce\n")
    computer = random.choice(['p', 'k', 'n'])

    if user == computer:
        return 'Remis, spróbuj jeszcze raz'

    if is_win(user, computer):
        return 'Wygrałes, gratulacje'

    return 'Przegrałeś '


def is_win(player, opponent):
    player_wins_with_rock = (player == 'k' and opponent == 'n')
    player_wins_with_paper = (player == 'p' and opponent == 'k')
    player_wins_with_scissors = (player == 'n' and opponent == 'p')


print(play())

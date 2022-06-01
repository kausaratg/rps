import random
print('Rock paper Scissors game')
# r > s, p> r, s> p
value = ['r', 's', 'p']
def rps(check):
    computer = ''
    player = ''
    while (computer == player) or (player not in check):
        computer = random.choice(check)
        player = input("Enter your choice('r' for rock, 'p' for paper, 's' for scissors): ")
        if player in check:
            if computer == player:
                print(f'computer: {computer}')
                print(f'player: {player}')
                print('It is a tie')
            elif (computer =='r' and player =='s') or (computer == 'p' and player=='r') or (computer == 's' and player == 'p') :
                print(f'computer: {computer}')
                print(f'player: {player}')
                print('computer win')
            elif (computer == 's' and player == 'r') or (computer == 'p' and player == 'r') or (computer == 's' or player== 'p'):
                print(f'computer: {computer}')
                print(f'player: {player}')
                print('player win')
        else:
            print('invalid input')


rps(value)
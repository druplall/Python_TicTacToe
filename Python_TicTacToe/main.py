# Tic Tac Toe 
# The board will be displayed as such:
# 7 8 9
# 6 5 4
# 3 2 1

print('Welcome to Deo Tic Tac Toe implementation !')
firstPlayer = None
secondPlayer = None
grid = ['9','8','7','6','5','4','3','2','1']

def player_selection():
    print('\n')
    global firstPlayer, secondPlayer
    firstPlayer = input("Player 1: Do you want to be X or O ? ")
    if firstPlayer == 'X':
        secondPlayer = 'O'
    else:
        firstPlayer = 'O'
        secondPlayer = 'X'

def get_user_input(firstplayer,secondplayer):
    position = input('Player 1: Please enter a postion between 0-9: ')
    if position.isdigit():
        loadgrid(position)
    else:
        endgame = input('Do you want to quit ? Type Y or N: ')
        if endgame == 'Y':
            return True
        else:
            return False

def loadgrid(p):
    global grid
    for i in grid:
        if i % 3 == 0:
            print('|{}|{}|{}|'.format(grid.index('9'),grid.index('8'),grid.index('7'))

                  
player_selection()

while (True):
    print('First Player is {}'.format(firstPlayer))
    if get_user_input(firstPlayer, secondPlayer) == True:
        break


#print(firstPlayer)
#print(secondPlayer)

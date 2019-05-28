import random
print('hello')
def display_board(board):
    print(board[7]+ '   |   ' + board[8] +'   |   ' + board[9])
    print("__________________")
    print(board[4] +'   |   ' + board[5] +'   |   ' + board[6])
    print("__________________ ")
    print(board[1] +'   |    ' + board[2]+'  |   ' + board[3])

def player_input():
    marker= ''
    while marker!='X' and marker!='O':
        marker=input("player 1, choose your marker")
    Player1=marker
    if Player1=='X':
        Player2='O'
    else:
        Player2='X'
    return (Player1,Player2)


def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return (board[1]==board[2]==board[3]==mark or
    board[4] == board[5] == board[6] == mark or
    board[7] == board[8] == board[9] == mark or
    board[1] == board[5] == board[9] == mark or
    board[3] == board[5] == board[7] == mark or
    board[1] == board[4] == board[7] == mark or
    board[2] == board[5] == board[8] == mark   or
    board[3] == board[6] == board[9] == mark)

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return'Player 1'
    else:
        return ' Player 2'

def space_check(board,position):
    return board[position]==' '
def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
         position=int(input("please choose position"))
    return position


def replay():
    choice=input("play again? yes or no")
    return choice=='yes'




print('Welcome to tic tac toe')
while True:
    the_board=[' ']*10
    choose_first()
    player1_marker, player2_marker = player_input()
    turn=choose_first()
    print(turn+'will go first')
    play_game=input("ready to play ?Y:N")
    if play_game=='y':
        gameon=True
    else :
        gameon=False
    while gameon:
        if turn=='Player 1':
            display_board(the_board)
            position=player_choice(the_board )
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("player1 won")
                gameon=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print("game tie")
                    gameon=False
                else:
                    turn=player2_marker

        else:

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("player2 won")
                gameon = False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print("game tie")
                    gameon = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
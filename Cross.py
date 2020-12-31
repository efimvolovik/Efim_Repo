game_board = list(range(1,10))
#def roll_board(game_board):
#   print("_" * 13)
#   for i in range(3):
#   print ("|", game_board[0+i*3], "|", game_board[1+i*3], "|", game_board[2+i*3], "|")
#       print ("|", game_board[0+1+3], game_board[4+5+6], game_board[7+8+9])
#        print ("|", * 13)
def roll_board(game_board):
    print("-" * 13)
    for i in range(3):
        print ("|", game_board [0+i*3], "|", game_board [1+i*3], "|", game_board [2+i*3], "|")
        print ("-" * 13)
def rool_input(player_roll):
    valid = False
    while not valid:
        player_answer = input("Okay , " + player_roll +" , You roll" "?")
        try:
            player_answer = input(player_answer)
        except :
            print ("Invalid Input")
            continue
    if player_answer >=1 and player_answer <= 9:
        if (str(roll_board[player_answer-1]) not in "XO"):
            game_board[player_answer-1] = player_roll
            valid = True
        else:
            print("Invalid Input :-(")
    else:
        print("Invalid Input :-(")
def win(game_board):
    combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for everyone in win:
        if game_board[everyone[0]] ==game_board[everyone[1]] == game_board[everyone[2]]:
            return game_board[everyone[0]]
        return False
def general(game_board):
    counter = 0
    youwin = False
    while not youwin:
        roll_board(game_board)
        if counter % 2==0:
            rool_input("X")
        else:
            rool_input("0")
        counter +=1
        if counter >4:
            tmp = win(game_board)
        if tmp:
            print(tmp,":-)")
            youwin = True
            break
    roll_board(game_board)
general(game_board)
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]


# the function that get the position from the player:


def player_input(player):
    global board
    while True:
        print(player, "turn")
        user_choisse_x = int(input("please enter row btw 0-2: "))
        user_choisse_y = int(input("please enter coulum btw 0-2: "))
        if 2 >= user_choisse_x >= 0 and 2 >= user_choisse_y >= 0:
            if board[user_choisse_x][user_choisse_y] == '':
                board[user_choisse_x][user_choisse_y] = player
                break

# the function that check the winner :


def check_win(player):
    global board
    if board[0][0] == board[0][1] == board[0][2] != "" or board[1][0] == board[1][1] == board[1][2] != "" or board[2][0] == board[2][1] == board[2][2] != "" or board[0][0] == board[1][0] == board[2][0] != "" or board[0][1] == board[1][1] == board[2][1] != "" or board[0][2] == board[1][2] == board[2][2] != "" or board[0][0] == board[1][1] == board[2][2] != "" or board[2][0] == board[1][1] == board[0][2] != "":
        print(player, "winner")
        board = [["", "", ""],
                 ["", "", ""],
                 ["", "", ""]]

    # The main function, which calls all the functions created above:


def play():
    global board
    while True:
        player_input("x")
        check_win("x")
        for i in board:
            print(i)
        player_input("o")
        check_win("o")
        for i in board:
            print(i)


play()

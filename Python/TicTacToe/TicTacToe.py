from past.builtins import raw_input

user = True  # when true it refers to x, otherwise o
cells_left = 9  # if turns_left == 0 and no one is a winner then its a draw!

# we only have to do the changes in playing board
playing_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board():
    game_board = [
        [playing_board[0][0], '|', playing_board[0][1], '|', playing_board[0][2]],
        ['-', '+', '-', '+', '-'],
        [playing_board[1][0], '|', playing_board[1][1], '|', playing_board[1][2]],
        ['-', '+', '-', '+', '-'],
        [playing_board[2][0], '|', playing_board[2][1], '|', playing_board[2][2]]
    ]
    for rows in game_board:
        for row in rows:
            print(f"{row}", end=" ")
        print(" ")


def isnum(user_input):
    # checking if it is no. or not, if not then user hav to input the value until it it not a no.
    if not user_input.isnumeric():
        print("This is not a valid no.")
        return False
    else:
        return True


def inrange(user_input):
    # we already check the no condition in isnum() so we know its a int type
    # now we can cast it into integer
    usr_input = int(user_input)
    if usr_input > 9 or usr_input < 1:
        print("not in range( 1-9 )")
        return False
    return True


def check_input(user_input):
    # check if it is a number
    if not isnum(user_input):
        return False
    # check if the input no is btw 1-9
    if not inrange(user_input):
        return False

    return True


def playthemove(coordinates, player):
    row = coordinates[0]
    col = coordinates[1]
    playing_board[row][col] = player


# check the input position is already taken or not in the board
def istaken(cordinates, player):
    row = cordinates[0]
    col = cordinates[1]
    if playing_board[row][col] != ' ':
        # that means its taken so return true
        # print("Its already taken")
        return True
    else:
        return False


def coordinates(pos):
    row = int(pos / 3)
    col = pos
    if col > 2:
        col = int(col % 3)
    return row, col


def current_player(user):  # it keeps track of who is going to play next
    if user:
        return "x"
    else:
        return "o"


def check_row(player):
    for row in playing_board:
        complete_row = True
        for val in row:
            if val != player:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_col(player):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if playing_board[row][col] != player:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diagonal(player):
    # left diagonal
    if playing_board[0][0] == player and playing_board[1][1] == player and playing_board[2][2] == player:
        return True
    # right diagonal
    elif playing_board[0][2] == player and playing_board[1][1] == player and playing_board[2][0] == player:
        return True
    else:
        return False


def check_winner(player):
    if check_row(player) or check_col(player) or check_diagonal(player):
        print(f"{player.capitalize()} wins!!")
        return True
    return False


while cells_left != 0:
    player = current_player(user)
    print_board()
    user_input = raw_input("Enter a no from 1 to 9: ")
    if not check_input(user_input):
        print("Enter a valid no.")
        continue
    pos = int(user_input) - 1
    # we now check the given output is taken or not
    # if not we play the given move by the user
    if istaken(coordinates(pos), player):
        print("input a blank one")
        continue
    playthemove(coordinates(pos), player)
    if check_winner(player):
        print_board()
        break
    cells_left -= 1  # after every move minus 1 cell from turns_left

    if cells_left == 0:
        print("its a Draw!")  # if no cell left then its a draw
    user = not user

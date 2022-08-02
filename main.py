"""Tic Tac Toe 6x6"""

import itertools


def draw_board(board: list) -> None:
    """ Draw actual board"""

    print("-" * size)
    for i in range(6):
        print("|",
              "".join('{:3}'.format(board[0 + i*6])), "|",
              "".join('{:3}'.format(board[1 + i*6])), "|",
              "".join('{:3}'.format(board[2 + i*6])), "|",
              "".join('{:3}'.format(board[3 + i*6])), "|",
              "".join('{:3}'.format(board[4 + i*6])), "|",
              "".join('{:3}'.format(board[5 + i*6])), "|")
        print("-" * size)


def take_input(board: list, player_token: str) -> None:
    """ Take user input"""
    tokens = "XO"
    valid = False
    while not valid:
        player_answer = input("Where to put " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Incorrect number.Try again")
            continue
        if player_answer in range(1, size+1):
            x = size - (size - player_answer) % 6
            while 1:
                if str(board[-1+x]) not in tokens:
                    board[- 1 + x] = player_token
                    valid = True
                    break
                else:
                    if x <= 6:
                        print("This cell is already taken, choose another one")
                        break
                x -= 6


def win_coordinates() -> list:
    """Get win coordinates list"""
    board = make_board()
    coordinates = list(itertools.combinations(board, 4))  # all possible sublists
    win_coords = []
    for coord in coordinates:
        for _ in range(len(coord)):
            if any([
                    coord[3] - coord[0] == 3,  # for horizontal
                    (coord[3]-coord[2]) == (coord[2] - coord[1]) == (coord[1]-coord[0]) == 6  # for vertical
                    ]):
                win_coords.append(coord)
    win_coords = list(set(win_coords))
    return win_coords


def make_board() -> list:
    """ Create a board"""
    return [_ for _ in range(1, size + 1)]


def check_win(board: list, win_coords: list) -> bool:
    """ Check if there is a winner (4 in a row)"""

    for each in win_coords:
        if board[each[0]] == board[each[1]] == board[each[2]] == board[each[3]]:
            return board[each[0]]
    return False


def main(board: list, win_coords: list) -> None:
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(board, "X")
        else:
            take_input(board, "O")
        counter += 1
        if counter > 6:  # Time to check if there is a winner
            winner = check_win(board, win_coords)
            if winner:
                print("\n", winner, " wins!")
                break
        if counter == size:
            print("Draw!")
            break
    draw_board(board)


if __name__ == "__main__":
    size = 36
    initial_board = make_board()
    win_coordinates = win_coordinates()

    main(initial_board, win_coordinates)

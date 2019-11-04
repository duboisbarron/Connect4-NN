# packages for
from colorama import Fore, Back, Style, init
from random import randint
init()
# print(Fore.RED + 'hello')



'''
JUST HAVE EMPTY LISTS THAT WE 
'''
class Connect4:
    rows = 6
    columns = 7

    def __init__(self):
        self.board = self.new_board()
        self.turn = "B" if randint(0, 1) == 1 else "R"

    def make_column(self):
        return [None for i in range(self.rows)]

    def new_board(self):
        return [self.make_column() for i in range(self.columns)]

    def get_col(self, col):
        return self.board[col]

    def get_row(self, row):
        return [self.board[j][row] for j in range(self.columns)]

    def get_chip(self, row, col):
        return self.board[col][row]


    def print_board(self):
        board = self.board

        # print(chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175))
        for i in range(len(board[0])):
            row_string = "|"
            for j in range(len(board)):
                if(board[j][i] == None):
                    row_string += " |"
                else:
                    row_string += board[j][i] + "|"
            self.prCyan(row_string)

        # print(chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175) + chr(175))



    def is_tie_condition(self):
        # everything will be true
        # if total length of all the arrays is 7*6 then it's a tie
            x = True
            for col in range(self.columns-1):
                # print(col)
                if not self.is_column_full(col):
                    x = False

            return x

            # check if every single column is full... do this after you check for win conditions since the checks happen within drop_chip


    def flip_turn(self):
        if self.turn == "B":
            self.turn = "R"
        else:
            self.turn = "B"


    def drop_chip(self, col):

        # instead of having an array of values preset...
        # just have a list that you append to in drop_chip
        # only print_board is what really matters to a human
        # if everything else works it's much more memory efficient - wider loops


        col_to_drop_in = self.board[col]
        col_to_drop_in.reverse()
        index = 0
        # print(col_to_drop_in)
        for row in col_to_drop_in:
            if row == None:
                col_to_drop_in[index] = self.turn
                break
            index += 1
        col_to_drop_in.reverse()
        # print(self.rows - index - 1, col)
        self.board[col] = col_to_drop_in

        if self.check_win_conditions(self.rows - index - 1, col, self.turn):
            # print("GAME OVER")
            self.turn = self.turn + "_WINS"
        elif self.is_tie_condition():
            # print("GAME IS A TIE")
            self.turn = "TIE"
        else:
            self.flip_turn()
    #         check win condition

    def prCyan(self, skk):
        print("\033[96m {}\033[00m".format(skk))

    # return True if column col is full, False otherwise
    # list.index(el) throws ValueError if el not in list
    def is_column_full(self, col):
        # print('calling is_column full')
        # print(col)
        # print(col)
        # print(col)
        # print(col)
        try:
            x = self.board[col].index(None)
        except ValueError:
            x = -1
        return x == -1

    # return array of booleans indicating if you can make a move in given column
    def available_moves(self):
        return [not self.is_column_full(col) for col in range(self.columns)]

    def win_down(self, row, col):

        if row + 3 < self.rows:
            # print("row - 3 >= 0")
        #     dont have to deal with negative indices
            return self.get_chip(row, col) == self.get_chip(row+1, col) == \
                   self.get_chip(row+2, col) == self.get_chip(row+3, col)

        return False

    def win_horizontal(self, row, turns):

        for i, chip in enumerate(self.get_row(row)):
            if chip == turns:
                try:
                    if self.get_chip(row, i) == self.get_chip(row, i+1) == self.get_chip(row, i+2) == self.get_chip(row, i+3):
                        return True
                except IndexError as e:
                    return False

    def check_win_conditions(self, row, col, chip):
        return self.win_horizontal(row, chip) or self.win_down(row, col)
               #  or
               # self.win_horizontal(row)

    # return the list of diagonal values going bottom left to top right
    # given a chip position (row, col)
    # (0, 6) should return (0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)
    def get_forward_diag(self, row, col):

        if row == 5 and col == 0:
            print("sdf")
            arr = [self.get_chip(row, col)]
            for x in range(self.columns-1):
                # row-1 and col + 1
                chip_to_append = self.get_chip(row-1,x)
                print(chip_to_append)
                arr.append(self.get_chip(row-1, x+1))
                # print(arr)
            return arr



# p1 = Connect4()
#
# p1.drop_chip(0)
# p1.print_board()
# print(p1.get_forward_diag(5, 0))
#
#
# p1.drop_chip(1)
# p1.drop_chip(1)
# p1.print_board()
# print(p1.get_forward_diag(5, 0))

# p1.print_board()



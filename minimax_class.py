from connect4 import Connect4
from copy import deepcopy


class Minimax:
    maxdepth = 0
    heuristic_function = None
    player_chip = None

    def __init__(self, maxdepth, heuristic_function, chip_color):
        self.maxdepth = maxdepth
        self.heuristic_function = heuristic_function
        self.player_chip = chip_color
        self.win_string = self.player_chip + '_WINS'
        self.lose_string = 'B_WINS' if self.player_chip == 'R' else 'R_WINS'

    def find_move(self, game):
        return self.minimax(game, self.maxdepth, True)

    def minimax(self, game, depth, maximizingPlayer):
        # print('calling minimax')

        # if the node is a terminal node (depth is at zero or the state of the game is gameover
        if depth == 0 or game.turn == 'B_WINS' or game.turn == 'R_WINS':

            if game.turn == self.win_string:
                return None, 999999999999

            elif game.turn == self.lose_string:
                return None, -999999999999

            else:

                board_score = self.heuristic_function(game, self.player_chip)

                return None, board_score
        if maximizingPlayer:
            value = -999999999999
            best_move = 0
            for valid_move in game.available_moves():
                child_game = Connect4(deepcopy(game.board), deepcopy(game.turn))

                last_move = child_game.drop_chip(valid_move)
                value_this_move = self.minimax(child_game, depth - 1, not maximizingPlayer)[1]

                if value_this_move > value:
                    value = value_this_move
                    best_move = valid_move

            return best_move, value

        else:
            value = 999999999999
            best_move = 0
            for valid_move in game.available_moves():
                # print(valid_move)
                child_game = Connect4(deepcopy(game.board), deepcopy(game.turn))

                last_move = child_game.drop_chip(valid_move)
                value_this_move = self.minimax(child_game, depth - 1, not maximizingPlayer)[1]

                if value_this_move < value:
                    value = value_this_move
                    best_move = valid_move
            return best_move, value
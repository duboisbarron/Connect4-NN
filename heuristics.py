from connect4 import Connect4


twoinarowconditions = [

    ['R', 'R', None, None],
    ['R', None, 'R', None],
    ['R', None, None, 'R'],
    [None, 'R', 'R', None],
    [None, 'R', None, 'R'],
    [None, None, 'R', 'R'],
#     blues
    ['B', 'B', None, None],
    ['B', None, 'B', None],
    ['B', None, None, 'B'],
    [None, 'B', 'B', None],
    [None, 'B', None, 'B'],
    [None, None, 'B', 'B'],


]



def count_2s_that_can_win(game, lastMove):
    row = lastMove[0]
    column = lastMove[1]
    # game.print_board()
    chip = game.get_chip(row, column)
    # print(chip)



    up_to_7_horiz = game.get_up_to_7_horizontal(lastMove[0], lastMove[1])
    up_to_7_vert = game.get_up_to_7_vertical(row, column)
    up_to_7_forward_slash = game.win_diagonal_forward_slash(row, column)
    up_to_7_backward_slash = game.win_diagonal_backward_slash(row, column)
    # print(up_to_7_backward_slash)

    all_possible_ways = [up_to_7_horiz, up_to_7_vert, up_to_7_forward_slash, up_to_7_backward_slash]
    total_num_conversions = 0
    for way in all_possible_ways:

        possible_conversions_this_way = 0
        for index, chip in enumerate(way):
            try:
                arr = [way[index], way[index+1], way[index+2], way[index+3]]
                if arr in twoinarowconditions:

                    # print('the last move taken can convert into a win')
                    # print(arr)
                    possible_conversions_this_way += 1
            except:
                continue
        total_num_conversions += possible_conversions_this_way
    # print(total_num_conversions)

    return total_num_conversions
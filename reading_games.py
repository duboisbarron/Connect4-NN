import numpy as np
import matplotlib.pyplot as plt
import os

#parameters to change 
folder = './saved_games/'
game_num_to_plot = 0
round_to_plot = 9 

# Get a list of all files in the load folder. (not including hidden files)
games = [f for f in os.listdir(folder) if not f.startswith('.')]
print(games)

current_game = np.load(folder + games[game_num_to_plot])

print('Total Games = {}'.format(len(games)))
print('current_game shape = {}'.format(current_game.shape))

# Find Last Round
for round in range(current_game.shape[0]):
    current_game_abs = np.abs(current_game[round])
    current_game_sum = np.sum(current_game_abs)
    
    print('Round {}, Absolute Sum = {}'.format(round, current_game_sum))
    
    if current_game_sum == 0:
        round -= 1
        break

print('Final Round = {}'.format(round))
final_board = current_game[round]

print(final_board)

def plot_board(board):
    ''' This function reads a saved board and plots Red and Yellow tokens in 
    their correct positions.

    Input: Numpy Array of Shape(6,7) containing:

    1 represents black tokens
    -1 represents red tokens
    0 represents an open space

    Returns:
    Shows a plot of the current board
    '''
    
    # Create New Figure
    plt.figure() 
    
    # Iterate over all board rows
    for row in range(board.shape[0]):
        
        # Iterate over all board rows
        for col in range(board.shape[1]):
            
            # Plot all tokens that = 1 as yellow
            if board[5-row][col] == 1:
                plt.scatter(col, row, c='Black', s=500, edgecolors='black')
            
            # Plot all tokens that = -1 as red
            if board[5-row][col] == -1:
                plt.scatter(col, row, c='Red', s=500, edgecolors='black')
    
    plot_margin = 0.4                         # Padding around edges
    plt.grid()                                # Turn on grid
    plt.ylim(-plot_margin, 5 + plot_margin)   # Set Y Limits
    plt.xlim(-plot_margin, 6 + plot_margin)   # Set X Limits
    plt.show()                                # Show Plot

# Plot Board
plot_board(final_board)
# Assign the final board
final_board = current_game[round + 1]

# Plot Board
plot_board(final_board)

# Assign the final board
final_board = current_game[round - 1]

# Plot Board
plot_board(final_board)
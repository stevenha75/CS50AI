"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board. Given X goes first.
    """
    num_of_O = 0
    num_of_X = 0
    
    # Count the num_of_O & num_of_X
    # Loop through the board where each row is a row on the board
    for row in board:
        # Each col represents a move
        for col in row:
            if col == O:
                num_of_O += 1
            elif col == X:
                num_of_X += 1
    
    # Calculate who's turn it is given X goes first
    if num_of_X == num_of_O:
        return X
    else: 
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    where i is the row of the move & j corresponds to to cell
    """
    actions = set()
    
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == EMPTY:
                actions.add((row_index, col_index))
                
    return actions
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if action is possible
    if action not in actions():
        raise Exception("Invalid Action")
    
    # create a copy of the board to return later
    board_copy = copy.deepcopy(board)
    
    # index into the action's row and col and execute action
    board_copy[action[0]][action[1]] = player(board)
    
    return board_copy
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

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
    if action not in actions(board):
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
    # looping through the rows
    for i in range(3):
        # check for 3 horizontally
        if ((board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY)):
            return board[i][0]
        # check for 3 vertically
        if ((board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY)):
            return board[0][i]
    
    # check for 3 in a row diagonally
    if (((board[0][0] == board[1][1] == board[2][2]) or 
         (board[2][0] == board[1][1] == board[0][2])) and 
        (board[1][1] != EMPTY)):
        return board[1][1]
    
    # if there are no winners return None
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check for a winner and terminate the game
    if winner(board) != None:
        return True
    
    # If there is no winner -> check for actions
    if len(actions(board)) == 0:
        return True
    
    return False    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    the move should return a tuple (i, j) that is one of the allowable moves
    """
    # if the board is terminal, there are no more actions to take
    if terminal(board):
        return None
    
    # X plays and tries to pick the highest utility states against the minimiser (O)
    if player(board) == X:
        score = -math.inf
        optimal_action = None
        
        # looping through actions and finding the best of all minimum utils
        # that are selected from max utils
        for action in actions(board):
            min_util = min_val(result(board, action))
            
            if min_util > score:
                score = min_util
                optimal_action = action
        
        return optimal_action
    
    # O plays and tries to pick the lowest utility action states against maximiser
    elif player(board) == O:
        score = math.inf
        optimal_action = None
        
        # looping through actions and finding the worst of all maximum utils
        # that are selected from min utils
        for action in actions(board):
            max_util = max_val(result(board, action))
            
            if max_util < score:
                score = max_util
                optimal_action = action 
        
        return optimal_action
    

def max_val(board):
    """
    returns the max utility out of all min utilities
    """    
    # base case: if we have reached the final state, return the utility of 
    # that board
    if terminal(board):
        return utility(board)
    
    util = -math.inf
    # looping through the actions and finding max out of 
    # every min state 
    for action in actions(board):
        util = max(util, min_val(result(board, action)))
    
    return util
        
    
def min_val(board):
    """
    returns the min utility out of all max utilities.
    """
    # base case: if we have reached the final state, return the utility of 
    # that board
    if terminal(board):
        return utility(board)
    
    util = math.inf
    # looping through the actions and finding min out of 
    # every max state 
    for action in actions(board):
        util = min(util, max_val(result(board, action)))
    
    return util
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
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)
    if count_X > count_O: 
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allowed_actions = set()
    for i in range(3):
        for j in range(3):
            state = board[i][j]
            if state == EMPTY:
                allowed_actions.add((i,j))
    return allowed_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    allowed_actions = actions(board)
    user = player(board)
    if action not in allowed_actions:
        raise Exception('Not allowed movement')
    i, j = action
    new_board[i][j] = user
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    for row in board:
        winner = row[0]
        if row[0] == row[1] == row[2] and row[0] is not None:
            return winner
    # Cols
    for col in range(3):
        winner = board[0][col]
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return winner
    # Diag
    winner = board[1][1]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return winner
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return winner
    
    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    count_empty = sum(row.count('O') for row in board)
    if win == None: 
        return False
    elif count_empty == 0: 
        return False
    else: 
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    score = 0
    print(win)
    if win == X:
        score += 1
    if win == O:
        score -= 1
    return score


def minimax(board):
    if terminal(board):
        return None  # El juego ha terminado

    current_player = player(board)

    # X
    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    # O
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

# Función que calcula el valor mínimo (para el jugador 'O')
def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value

# Función que calcula el valor máximo (para el jugador 'X')
def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value
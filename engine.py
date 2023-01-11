""" Chess Engine """
import math
import chess
import opening
# Initial chess board
BOARD = chess.Board()
# Use legal moves to count mobility

def count_doubled(board, colour):
    """ Function counts doubled pawns """
    pass


def evaluate_position(board, colour, legal_moves):
    """ Evaluation function for chess game """
    white = chess.WHITE
    black = chess.BLACK
    pieces = {}
    # Counting pieces depeneding on colour
    wking = bin(board.occupied_co[white] & board.kings).count('1')
    wqueen = bin(board.occupied_co[white] & board.queens).count('1')
    wrook = bin(board.occupied_co[white] & board.rooks).count('1')
    wknight = bin(board.occupied_co[white] & board.knights).count('1')
    wbishop = bin(board.occupied_co[white] & board.bishops).count('1')
    wpawn = bin(board.occupied_co[white] & board.pawns).count('1')
    bking = bin(board.occupied_co[black] & board.kings).count('1')
    bqueen = bin(board.occupied_co[black] & board.queens).count('1')
    brook = bin(board.occupied_co[black] & board.rooks).count('1')
    bknight = bin(board.occupied_co[black] & board.knights).count('1')
    bbishop = bin(board.occupied_co[black] & board.bishops).count('1')
    bpawn = bin(board.occupied_co[black] & board.pawns).count('1')

    material_score = 200  * (wking - bking) \
                      + 9 * (wqueen - bqueen) \
                      + 5 * (wrook - brook) \
                      + 3.3 * (wbishop - bbishop) \
                      + 3.2 * (wknight - bknight) \
                      + 1 * (wpawn - bpawn)
                      
    # Assigning piece square scores 
    """
    pawnsq = sum([opening.WPAWN_SCORE[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-opening.BPAWN_SCORE[i] for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([opening.WKNIGHT_SCORE[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-opening.BKNIGHT_SCORE[i] for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([opening.WBISHOP_SCORE[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-opening.BBISHOP_SCORE[i] for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([opening.WROOK_SCORE[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-opening.BROOK_SCORE[i] for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([opening.WQUEEN_SCORE[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-opening.BQUEEN_SCORE[i] for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([opening.WKING_SCORE[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-opening.BKING_SCORE[i] for i in board.pieces(chess.KING, chess.BLACK)])
    """
    mobility_score = 0.01 * legal_moves
    #print("Score")
    #print(material_score)
    # Totalling Evaluation score 
    evaluation = (mobility_score + material_score) * colour
    #evaluation = material_score + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
    return evaluation 

def negamax(depth, board, alpha, beta, colour):
    """ Negamax decision tree """
    if board.is_game_over():
        return eval(board.result())  * 10000 * colour + depth
    
    elif depth == 0:
        return evaluate_position(board, colour, board.legal_moves.count())
    
    value = -math.inf
    temp = board
    #print(board)
    for move in board.legal_moves:
        temp.push(move)
        value = max(value, -negamax(depth - 1, temp, -beta, -alpha, -colour))
        alpha = max(alpha, value)
        temp.pop()
        if alpha >= beta:
            break

    return value


def generate_top_moves(board, colour):
    """ Generates a list of top moves """
    scores = []
    for move in board.legal_moves:
        board.push(move)
        scores.append({'move': move, 'score': negamax(3, board, -math.inf, math.inf, -colour)})
        board.pop()

    newlist = sorted(scores, key=lambda k: k['score'], reverse=True)
    return newlist[-3:][::-1]

# Testing Function
def test(user_move):
    """ function used for testing game board and evaluation """
    colour = 1
    user_move = "temp"
    while user_move != "quit":
        print("Enter your move:")
        user_move = input()

        if user_move == 'eval':
            print(generate_top_moves(BOARD, colour))
            continue

        if user_move == 'legal':
            for move in BOARD.legal_moves:
                print(move)
                continue
        try:
            BOARD.push_san(user_move)
        except AttributeError:
            print("Invalid move!")
        print(BOARD)
        
        colour *= -1
        print(colour)

if __name__ == "__main__":
    test("move")
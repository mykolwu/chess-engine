import time 
import chess
import engine

board = chess.Board()
start = time.process_time()
#for i in range(0, 1000):
    #engine.evaluate_position(board, 1, board.legal_moves.count())
engine.generate_top_moves(board, 1)
#print(time.process_time() - start)

# Test1: Testing for scholar's mate
scholar_board = chess.Board()
scholar_board.push_san("e4")
scholar_board.push_san("e5")
scholar_board.push_san("Bc4")
scholar_board.push_san("Nc6")
scholar_board.push_san("Qf3")
print(engine.generate_top_moves(scholar_board, -1))
scholar_board.push_san("a6")
print(engine.generate_top_moves(scholar_board, 1))
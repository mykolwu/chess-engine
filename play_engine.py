""" Module for playing the game """
import chess
import chess.pgn
import engine

def start_game(colour):
    """ Start a new game against the engine """
    game = chess.pgn.Game()
    game.headers["Event"] = "Engine Testing Phase"
    game.headers["White"] = "Michael Wu"
    game.headers["Black"] = "Chess Engine"

    turn = 1
    board = chess.Board()
    print('(っ◕‿◕)っ  Chess (っ◕‿◕)っ ')
    print("Good Luck!")
    print(board)
    print("\n")

    while turn == 1:
        try:
            move = input("Your move:")
            uci = board.push_san(move)
            node = game.add_variation(uci)
            print(board)
            print("\n")
            turn+=1

        except ValueError:
            print("Illegal move!")
            continue
        

    while not board.is_checkmate():
        if turn % 2 == 1:
            move = input("Your move:")
            #top_moves = engine.generate_top_moves(board, colour)
            #print("Top moves:")
            #print(top_moves)
            try:
                uci = board.push_san(move)
                node = node.add_variation(uci)
                print(board)
                print("\n")

            except ValueError:
                print("Illegal move!")
                continue
        else:
            """
            print("Thinking...")
            """
            top_moves = engine.generate_top_moves(board, -colour)
            print("Top moves:")
            print(top_moves)
            board.push(top_moves[0]['move'])
            node = node.add_variation(top_moves[0]['move'])
            print(board)
            print("\n")
            print("Engine's move:" + str(top_moves[0]['move']) + "\n")

        turn += 1

    if turn % 2 == 1:
        print("You lost!")

    else:
        print("You win!")

    game.headers["Result"] = board.result()
    return game

print(start_game(1))
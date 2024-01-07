import chess
import chess.svg
import chess.pgn
from IPython.display import display
from io import StringIO

board = chess.Board()                       
pgn = open("./games/game.pgn")
first_game = chess.pgn.read_game(pgn)

board = first_game.board()
for move in first_game.mainline_moves():
    board.push(move)
    
display(board)
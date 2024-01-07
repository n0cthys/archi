import chess
import chess.svg
import chess.pgn

# Chess game data
moves_data = 'c4 e5 b3 Nf6 Bb2 Nc6 d3 d5 Nf3 d4 Nbd2 Be7 g3 O-O Bg2 Bf5 O-O Re8 Re1 Qd7 a3 a5 Nf1 Rad8 Nh4 Bh3 Bh1 Bc5 Ng2 g5 f3 Qf5 g4 Qd7 Ng3 Bxg4 fxg4 Qxg4 e4 Qh3 Qf3 Ng4'

board = chess.Board()
display(board)


'''# Apply moves to the board
for move in moves_data.split():
    board.push_uci(move)

svg_board = chess.svg.board(board=board)'''
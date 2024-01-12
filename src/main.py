# from basegame import createbasegame

# chess libs
import io
import chess
import chess.pgn
from chess import Board
from chess.pgn import read_game
from IPython.display import display

# "basic" libs
import tkinter as ttk

board = Board()
pgn_file = open("games/ChessCom_erik_200910.pgn")
game = read_game(pgn_file)

pgn = io.StringIO("1. e4 e5 2. Nf3 *")
game = chess.pgn.read_game(pgn)


'''board = game.board()
for move in game.mainline_moves():
    board.push(move)'''

import tkinter as tk
import chess
import chess.svg
from tkinter import Canvas, Entry, Button, Label

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Chess Board App")

        # Chessboard canvas
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack(side=tk.TOP, padx=10, pady=10)

        # Entry widget for FEN input
        self.fen_entry = Entry(self.root, width=40)
        self.fen_entry.pack(side=tk.TOP, pady=5)

        # Button to update chessboard
        update_button = Button(self.root, text="Update Chessboard", command=self.update_chessboard)
        update_button.pack(side=tk.TOP, pady=5)

        # Label to display current FEN
        self.fen_label = Label(self.root, text="Current FEN:")
        self.fen_label.pack(side=tk.TOP, pady=5)

        # Initial chessboard state
        self.board = chess.Board()

        # Draw initial chessboard
        self.draw_chessboard()

    def draw_chessboard(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw chessboard using python-chess SVG
        svg_data = chess.svg.board(board=self.board)
        self.chessboard_image = tk.PhotoImage(data=svg_data)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.chessboard_image)

        # Display current FEN
        self.fen_label.config(text="Current FEN: " + self.board.fen())

    def update_chessboard(self):
        # Update chessboard based on the provided FEN
        fen = self.fen_entry.get()
        try:
            self.board.set_fen(fen)
            self.draw_chessboard()
        except ValueError:
            self.fen_label.config(text="Invalid FEN format")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()


display(board)
# inicializal egy kulon kattintgathato tablat
# createbasegame()


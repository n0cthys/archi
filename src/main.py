# TOKEN
token = "lip_9DZ5qcYJMGkmqI50D1wZ"

from io import BytesIO
from PIL import Image
import berserk
import chess.pgn
import chess.svg
import cairosvg

client = berserk.Client()
session = berserk.TokenSession(token)
client = berserk.Client(session)

# basic txt formaban
games = client.games.export_by_player(username = "Nocthys")
gms = ' '.join([str(elem) for elem in list(games)]) 
file_path = "game.txt"
with open(file_path, "w") as file:
    file.write(gms)

"""gamesPNG = client.games.export_by_player(username = "Nocthys", as_pgn=True)
# image = Image.open(BytesIO(gamesPNG))
# image.save("downloaded_image.png")
gamesPNG.save("downloaded_image.png")
image.show()"""
    
gamesPNG = client.games.export_by_player(username = "Nocthys", as_pgn=True)

for pgn in gamesPNG:
    game = chess.pgn.read_game(BytesIO(pgn.encode('utf-8')))
    board = game.board()
    svg = chess.svg.board(board=board, size=400)
    png_bytes = cairosvg.svg2png(bytestring=svg)

    # Now you can save png_bytes to a file or use it as needed
    with open('game.png', 'wb') as f:
        f.write(png_bytes)
'''import chess
import chess.svg
import chess.pgn
from IPython.display import display
from io import StringIO

pgn_string = "1. e4 e6 2. d4 d5 3. e5 c5 4. Nf3 Nc6 5. Bb5 cxd4 6. Nxd4 Bd7 7. Nxc6 Bxc6 8. Bxc6+ bxc6 9. c3 f6 10. exf6 Nxf6 11. Bg5 Be7 12. Qe2 Qd7 13. O-O O-O 14. Re1 Ne4 15. Bxe7 Qxe7 16. f3 Qc5+ 17. Qe3 Qxe3+ 18. Rxe3 Nc5 19. b4 Na4 20. Rxe6 Rac8 21. Nd2 Nxc3 22. Rc1 Nxa2 23. Rcxc6 Nxb4 24. Rcd6 Rc1+ 25. Kf2 Nd3+ 26. Ke3 Nb4 27. Re7 Re1+ 0-1"
pgn = StringIO(pgn_string) 
  
# Reading the game 
game = chess.pgn.read_game(pgn) 
board = chess.Board()
display(board)


# Apply moves to the board
for move in moves_data.split():
    board.push_uci(move)

svg_board = chess.svg.board(board=board)'''

from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
	data = get_leaderboards().json
	categories = data.keys()

	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
	data = get_player_stats(username).json
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
	for category in categories:
		print('Category:', category)
		print(f'Current: {data[category]["last"]["rating"]}')
		print(f'Best: {data[category]["best"]["rating"]}')
		print(f'Best: {data[category]["record"]}')

def get_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	printer.pprint(game)

get_most_recent_game('Tenebris-Noctis')
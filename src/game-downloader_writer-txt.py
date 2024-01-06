# TOKEN
token = "lip_9DZ5qcYJMGkmqI50D1wZ"
file_path = "./games/game.txt"

import berserk

client = berserk.Client()
session = berserk.TokenSession(token)
client = berserk.Client(session)

gms = client.games.export_by_player(username="Nocthys")
games = ' '.join([str(elem) for elem in list(gms)])

with open(file_path, "w") as file:
    file.write(games)
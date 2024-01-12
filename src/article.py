import requests
import json
import chess.pgn
import io
import pandas as pd
import math
import numpy as np
import time

pd.set_option('display.max_rows', 50)
def get_data_by_month(username, year, month):

    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}"

    data = requests.get(url)
    if data.status_code != 200:
        raise Exception("The following response was returned: " + str(data.status_code))
    else:
        data = json.loads(data.text)
        games = data["games"]
        
    all_games=[]
    for game in games:
        pgn = (game['pgn'])
        pgn = io.StringIO(pgn)
        game = chess.pgn.read_game(pgn)
        all_games.append(game)
                
    game_list = []
    for g in all_games:
        moves = (g.mainline_moves())
        moves = [str(x) for x in moves]
        
        white = (g.headers['White'])
        if white.lower() == username.lower():
            playing_as_white = 1
        else:
            playing_as_white = 0
        
        if len(moves)>1:
            move_made = (moves[1])
        else:
            move_made = ""
        
        game = {"date": (g.headers["Date"]), "player_white": white, "player_black": (g.headers['Black']), "playing_as_white" : playing_as_white, "result": (g.headers['Result']), "termination": (g.headers['Termination']), "moves": moves, "no_of_moves": (math.ceil(len(moves)/2)), "first_move": (moves[0]), "response": move_made}
    
        
        game_list.append(game)
    game_list = pd.DataFrame(game_list)
    return game_list
this_year = [("2021", "01"),  ("2021", "02"), ("2021", "03"), ("2021", "04"), ("2021", "05")]
all_months = []
for date in this_year:
    year = date[0]
    month = date[1]
    
    df = get_data_by_month("", year, month)
    all_months.append(df)
    time.sleep(10)
    print("Sleeping")
def combine_months(dfs):
    df = pd.concat(dfs, ignore_index=True)
    return df
all_months = combine_months(all_months)
def drop_not_required_columns(df):
    # For now I am not interested in these columns
    df = df.drop(["player_white", "player_black", "moves", "termination"], axis =1)
    return df
all_months = drop_not_required_columns(all_months)
def create_wins_column(df):
    
    conditions = \
    [(df["playing_as_white"] == 1) & (df["result"] == "1-0"), 
     (df["playing_as_white"] == 1) & (df["result"] == "0-1"), 
     (df["playing_as_white"] == 0) & (df["result"] == "1-0"), 
     (df["playing_as_white"] == 0) & (df["result"] == "0-1"), 
     (df["playing_as_white"] == 1) & (df["result"] == "1/2-1/2"),
     (df["playing_as_white"] == 0) & (df["result"] == "1/2-1/2")]
    
    values = ["Win", "Loss", "Loss", "Win", "Draw", "Draw"]
                
    df['my_result'] = np.select(conditions, values)    

    return df    

all_months = create_wins_column(all_months)
def column_by_month(df):
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = pd.DatetimeIndex(df["date"]).month    
    return df
all_months = column_by_month(all_months)
all_months.info()
# see my most common opening
all_months[all_months["playing_as_white"]==1].groupby(["first_move", "my_result"])["my_result"].count()
#those of my opponents
pd.set_option('display.max_rows', None)
all_months[all_months["playing_as_white"]==0].groupby(["first_move", "my_result"])["my_result"].count()
#zooming in on these openings and how I respond
all_months[(all_months["playing_as_white"]==0) & ((all_months["first_move"]=="e2e4") | (all_months["first_move"]=="d2d4"))].groupby(["first_move", "response", "my_result"])["my_result"].count()
all_months.groupby(["month", "my_result"])["my_result"].count()
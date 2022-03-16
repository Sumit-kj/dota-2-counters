import json

import uvicorn
from fastapi import FastAPI
import alias as al

app = FastAPI()


def create_counter_dict():
    """
    This function reads the counter data from csv and converts it into a dictionary of hero, counters
    :return: The dict of hero  counter
    """
    with open('counters.json', 'r') as fp:
        h_c_dict = json.load(fp)
        return h_c_dict


def get_counter_tally(opp_picks, h_c_dict):
    """
    This function gives tally of counters to the opponent's pick
    :param opp_picks: The list of picks by opponent
    :param h_c_dict: the counter dict for hero
    :return: a dict containing the tally to each counter for each pick
    """
    c_d = {}
    for pick in opp_picks:
        for counter in h_c_dict[pick]['bad_against']:
            if counter in c_d.keys():
                c_d[counter] += 1
            else:
                if counter not in opp_picks:
                    c_d[counter] = 1
        for counter in h_c_dict[pick]['good_against']:
            if counter in c_d.keys():
                c_d[counter] -= 1
            else:
                if counter not in opp_picks:
                    c_d[counter] = -1
    return c_d


def get_counter_tally_sorted(c_t_dict):
    """
    This function checks if the counter to picks are already countered
    :param c_t_dict: The counter Tally dict
    :return: The tally for each
    """
    return {k: v for k, v in sorted(c_t_dict.items(), key=lambda item: item[1], reverse=True)}


@app.get('/get_counters')
async def get_counter_picks(picks: str = ''):
    if picks == '':
        return {
            "status": "Error",
            "message": "please provide comma separated picks of opponents, like ?pick=ES,WW,BB,ES,PA. It can have up to"
                       " 5 comma separated values. The Alias are mentioned in README.md @ "
                       "https://github.com/Sumit-kj/dota-2-counters/blob/master/README.md ."
        }
    opponent_picks = [al.alias[x.strip().upper()] for x in picks.split(',')]
    if len(opponent_picks) > 5:
        return {
            "status": "Error",
            "message": "please provide up to 5 picks of opponents, like ?pick=ES,WW,BB,ES,PA.  The Alias are mentioned "
                       "in README.md @ "
                       "https://github.com/Sumit-kj/dota-2-counters/blob/master/README.md ."
        }
    hero_counter_dict = create_counter_dict()
    result = get_counter_tally(opponent_picks, hero_counter_dict)
    result = get_counter_tally_sorted(result)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)

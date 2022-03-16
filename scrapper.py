import json

import requests
from bs4 import BeautifulSoup
from heroes import heroes_list as heroes


def get_counter_countering_lists(h):
    url = "https://dota2.fandom.com/wiki/" + h + "/Counters"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    bad_against_list = []
    div_bad_against = soup.findAll('div', attrs={"style": "margin-bottom:5px; box-shadow:0px 0px 2px 4px red;"})
    for div in div_bad_against:
        img_bad_against = div.contents[0].attrs['title']
        bad_against_list.append(img_bad_against)

    good_against_list = []
    div_good_against = soup.findAll('div', attrs={"style": "margin-bottom:5px; box-shadow:0px 0px 2px 4px chartreuse;"})
    for div in div_good_against:
        img_good_against = div.contents[0].attrs['title']
        good_against_list.append(img_good_against)
    return bad_against_list, good_against_list


def get_good_bad_for_all_heroes():
    good_bad_dict = {}
    for index, hero in enumerate(heroes):
        good, bad = get_counter_countering_lists(hero)
        good_bad_dict[hero] = {}
        good_bad_dict[hero] = {
            'good_against': good,
            'bad_against': bad
        }
        print(str((index+1)/len(heroes)*100), '%, Done for', hero)
    out_file = open('counters.json', "w")
    json.dump(good_bad_dict, out_file, indent=4)
    out_file.close()


get_good_bad_for_all_heroes()
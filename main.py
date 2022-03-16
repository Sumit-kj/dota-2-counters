import json

import matplotlib.pyplot as plt
import alias as al
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


def create_counter_dict():
    """
    This function reads the counter data from csv and converts it into a dictionary of hero, counters
    :return: The dict of hero  counter
    """
    with open('counters.json', 'r') as fp:
        h_c_dict = json.load(fp)
        return h_c_dict


def get_opponents_pick(h_c_dict):
    """
    This function takes opponent's pick as input
    :return: this function returns the input from user
    """

    opp_picks = []
    i = 0
    while i < 5:
        pick_message = 'Enter pick ' + str(i + 1) + ": "
        pick = str(input(pick_message)).upper()
        try:
            if al.alias[pick] in opp_picks:
                raise Exception('Same hero present!')
            opp_picks.append(al.alias[pick])

            counter_tally_dict = get_counter_tally(opp_picks, h_c_dict)
            counter_tally_dict = get_counter_tally_sorted(counter_tally_dict)
            # counter_tally_dict = get_counter_to_counter_tally(opp_picks, counter_tally_dict, h_c_dict)
            plot = plot_counter_bar_plot(counter_tally_dict)
            # plot.show()
            plot.draw()
            plot.pause(0.001)
            input('Press Enter to continue')
            if i != 4:
                plot.close('all')
            i += 1
        except KeyError:
            print('Enter the hero again!')
        except Exception as e:
            print(e)
    return opp_picks


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


def plot_counter_bar_plot(data):
    """
    This function plots bar plot for the counters
    :return: None
    """
    counters = list(data.keys())[:30]
    values = list(data.values())[:30]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(counters, values)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')
    ax.set_title('Counters',
                 loc='left', )
    return plt


if __name__ == '__main__':
    hero_counter_dict = create_counter_dict()
    opponents_picks = get_opponents_pick(hero_counter_dict)

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import os

FACECOLORS = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:grey', 'tab:yellow']

current_path_str = os.path.dirname(__file__)
SAVE_DIR = os.path.dirname(current_path_str)
RESULTS_DIR = os.path.join(SAVE_DIR, 'outputs/cpu_scheduling/')
if not os.path.isdir(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)


def plot_gantt_chart(algorithm_name, processes_list, processes_scheduled_list):
    fig, gnt = plt.subplots()

    y_lim = 15 + 10 * len(processes_list)
    gnt.set_ylim(0, y_lim + 5)
    x_lim = sum(list(map(lambda p: p['burst_time'], processes_list)))
    gnt.set_xlim(0, x_lim + 5)

    gnt.set_xlabel('burst cycles')
    gnt.set_ylabel('process')

    y_labels = list(map(lambda p: p['name'], processes_scheduled_list))
    y_labels.reverse()
    ytick = 15
    y_ticks = []
    for _ in y_labels:
        y_ticks.append(ytick)
        ytick += 10

    gnt.set_yticks(y_ticks)
    gnt.set_yticklabels(y_labels)

    loc = plticker.MultipleLocator(base=5)  # this locator puts ticks at regular intervals
    gnt.xaxis.set_major_locator(loc)

    gnt.grid(True) # Setting graph attribute

    y_pos = 10 * len(processes_list)
    for index, process_scheduled in enumerate(processes_scheduled_list):
        gnt.broken_barh(process_scheduled['coordinates'], (y_pos, 9), facecolors=FACECOLORS[index])
        y_pos -= 10

    file_name = algorithm_name + ".png"
    plt.savefig(RESULTS_DIR + file_name)
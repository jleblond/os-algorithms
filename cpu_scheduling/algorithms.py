from . import visualizations


def sort_processes_list_by_priority(processes_list):
    return sorted(processes_list, key=lambda p: p['priority'], reverse=False)



def fcfs(processes_list):
    start_point = 0
    list_processes_scheduled = []

    sorted_processes_list = sort_processes_list_by_priority(processes_list)
    x_pos = start_point

    for process in sorted_processes_list:
        process_information = {'name': process['name'],
                               'waiting_time': x_pos,
                               'coordinates': [(x_pos, process['burst_time'])]
                               }
        list_processes_scheduled.append(process_information)
        x_pos += process['burst_time']

    visualizations.plot_gantt_chart(processes_list, list_processes_scheduled)

    # Print information
    print("*** FCFS Algorithm for CPU Scheduling ***")
    print(str(processes_list))

    print('Results: ')
    print(str(list_processes_scheduled))
    sum_waiting_times = sum(list(map(lambda p: p['waiting_time'], list_processes_scheduled)))
    average_waiting_time = sum_waiting_times/len(sorted_processes_list)
    print("Average waiting time is: " + str(average_waiting_time))

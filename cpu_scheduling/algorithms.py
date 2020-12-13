import math

from . import printing

# COMPUTING HELPERS

def find_process_for(processes_list, key, value):
    return next(process for process in processes_list if process[key] == value)

def sort_processes_list_by(processes_list, order_by_key):
    return sorted(processes_list, key=lambda p: p[order_by_key], reverse=False)

def simple_cpu_scheduling_algorithm(algorithm_name, sorting_by_key, processes_list, start_point = 0):
    list_processes_scheduled = []
    x_pos = start_point

    sorted_processes_list = processes_list
    if sorting_by_key != None:
        sorted_processes_list = sort_processes_list_by(processes_list, sorting_by_key)

    for process in sorted_processes_list:
        wait_time = x_pos - process['arrival_time']
        turnaround_time = (x_pos + process['burst_time']) - process['arrival_time']
        # print(str(process['name']) +  '  --- x_pos: '+ str(x_pos) + ' / wait_time: ' + str(wait_time))
        process_information = {'name': process['name'],
                               'first_execution_time': x_pos,
                               'waiting_time': wait_time,
                               'turnaround_time': turnaround_time,
                               'coordinates': [(x_pos, process['burst_time'])]
                               }
        list_processes_scheduled.append(process_information)
        x_pos += process['burst_time']

    printing.print_algorithm_results(algorithm_name, processes_list, list_processes_scheduled)

# MAIN ALGORITHMS

def fcfs(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('FCFS', 'arrival_time', processes_list, start_point)

def sjf(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('SJF', 'burst_time', processes_list, start_point)

def priority(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('PRIORITY', 'priority', processes_list, start_point)

def shortest_remaining_time_first(processes_list, start_point = 0):
    t = start_point
    sorted_processes_list = sort_processes_list_by(processes_list.copy(), 'arrival_time')
    list_processes_computated = sorted_processes_list.copy()

    total_time = start_point
    for process in list_processes_computated:
        total_time += process['burst_time']
        process['burst_time_left'] = process['burst_time']
        process['coordinates'] = []

    p_index = 0
    while t <= total_time:
        filtered_processes = list(filter(lambda p: (p['arrival_time'] <= t and p['burst_time_left'] > 0) , list_processes_computated))
        list_processes_copy = sorted(filtered_processes, key=lambda p: p['burst_time_left'], reverse=False)
        if list_processes_copy != []:
            executing_process = list_processes_copy[0]

            if executing_process['burst_time_left'] == 0:
                list_processes_copy.remove(executing_process)
            if executing_process['arrival_time'] <= t and executing_process['burst_time_left'] > 0:
                process_from_computated_list = find_process_for(list_processes_computated, 'name', list_processes_copy[p_index]['name'])
                process_from_computated_list['coordinates'].append((t, 1))
                list_processes_copy[p_index]['burst_time_left'] -= 1

        t += 1

    for process in list_processes_computated:
        # coor_end_x = 0  # start - for each process
        # sum_waiting_time = 0
        # for coordinates in process['coordinates']:
        #     coor_start_x = coordinates[0]
        #     sum_waiting_time += math.fabs(coor_end_x - coor_start_x)
        #     coor_end_x = sum(list(coordinates))
        # process['waiting_time'] = sum_waiting_time

        process['turnaround_time'] = sum(list(process['coordinates'][-1])) - process['arrival_time']

    printing.print_algorithm_results('Shortest-remaining-time-First', processes_list, list_processes_computated)



def round_robin(processes_list, quantum, start_point = 0):
    processes_list_length = len(processes_list)
    t = start_point
    sorted_processes_list = sort_processes_list_by(processes_list, 'arrival_time')

    total_time = start_point
    for process in sorted_processes_list:
        total_time += process['burst_time']
        process['burst_time_left'] = process['burst_time']
        process['coordinates'] = []

    p_index = 0
    while t <= total_time:
        filtered_list = list(filter(lambda p: (p['arrival_time'] <= t and p['burst_time_left'] > 0), sorted_processes_list))
        if filtered_list != []:
            executing_process = processes_list[p_index]
            while(executing_process['name'] not in list(map(lambda p: p['name'], filtered_list))):
                p_index = p_index + 1 if (p_index < processes_list_length-1) else 0
                executing_process = processes_list[p_index]

            if executing_process['burst_time_left'] > 0:
                if executing_process['burst_time_left'] >= quantum:
                    current_quantum = quantum
                else:
                    current_quantum = executing_process['burst_time_left']

                process_to_compute = find_process_for(sorted_processes_list, 'name', executing_process['name'])
                process_to_compute['coordinates'].append((t, current_quantum))
                process_to_compute['burst_time_left'] -= current_quantum
                t += current_quantum
                p_index = p_index + 1 if (p_index < processes_list_length - 1) else 0
            else:
                t += 1
        else:
            break

    for process in sorted_processes_list:
        coor_end_x = 0  # start - for each process
        sum_waiting_time = 0
        for coordinates in process['coordinates']:
            coor_start_x = coordinates[0]
            sum_waiting_time += math.fabs(coor_end_x - coor_start_x)
            coor_end_x = sum(list(coordinates))
        process['waiting_time'] = sum_waiting_time

        process['turnaround_time'] = sum(list(process['coordinates'][-1])) - process['arrival_time']


    printing.print_algorithm_results('ROUND-ROBIN', processes_list, sorted_processes_list)

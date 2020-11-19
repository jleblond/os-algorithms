from . import printing


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
        process_information = {'name': process['name'],
                               'waiting_time': x_pos,
                               'coordinates': [(x_pos, process['burst_time'])]
                               }
        list_processes_scheduled.append(process_information)
        x_pos += process['burst_time']

    printing.print_algorithm_results(algorithm_name, processes_list, list_processes_scheduled)



def fcfs(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('FCFS', 'arrival_time', processes_list, start_point)

def sjf(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('SJF', 'burst_time', processes_list, start_point)

def priority(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('PRIORITY', 'priority', processes_list, start_point)


def round_robin(processes_list, quantum, start_point = 0):
    list_processes_scheduled = []
    x_pos = start_point
    sorted_processes_list = sort_processes_list_by(processes_list, 'arrival_time')


    total_time = start_point
    for process in sorted_processes_list:
        total_time += process['burst_time']
        process['burst_time_left'] = process['burst_time']
        process['coordinates'] = []

    p_index = 0

    while x_pos < total_time:
        executing_process = sorted_processes_list[p_index]
        if executing_process['burst_time_left'] > 0:
            if executing_process['burst_time_left'] > quantum:
                current_quantum = quantum
            else:
                current_quantum = executing_process['burst_time_left']

            sorted_processes_list[p_index]['coordinates'].append((x_pos, current_quantum))
            print(str(sorted_processes_list[p_index]))
            sorted_processes_list[p_index]['burst_time_left'] -= current_quantum

        x_pos += current_quantum

        while True:
            # go to next process
            if p_index < len(sorted_processes_list) - 1:
                next_index = p_index + 1
            else:
                next_index = 0

            if sorted_processes_list[next_index]['arrival_time'] <= x_pos:
                p_index = next_index

            if (sorted_processes_list[next_index]['burst_time_left'] > 0):
                break


    print(str(sorted_processes_list))
    #printing.print_algorithm_results('ROUND-ROBIN', processes_list, list_processes_scheduled)

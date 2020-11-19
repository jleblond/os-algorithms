from . import printing


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
    simple_cpu_scheduling_algorithm('FCFS', None, processes_list, start_point)

def sjf(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('SJF', 'burst_time', processes_list, start_point)

def priority(processes_list, start_point = 0):
    simple_cpu_scheduling_algorithm('PRIORITY', 'priority', processes_list, start_point)
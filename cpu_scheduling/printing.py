from . import visualizations

def print_algorithm_results(algorithm_name, processes_list, list_processes_scheduled):
    print("*** " + algorithm_name + " algorithm for CPU Scheduling ***")
    print(str(processes_list))

    print('Results: ')
    print(str(list_processes_scheduled))
    sum_waiting_times = sum(list(map(lambda p: p['waiting_time'], list_processes_scheduled)))
    average_waiting_time = sum_waiting_times/len(processes_list)
    print("Average waiting time is: " + str(average_waiting_time))

    visualizations.plot_gantt_chart(algorithm_name, processes_list, list_processes_scheduled)

from . import visualizations


def sort_processes_list_by_priority(processes_list):
    return sorted(processes_list, key=lambda p: p['priority'], reverse=False)



def fcfs(processes_list):
    start_point = 0
    list_processes_scheduled = []

    sorted_processes_list = sort_processes_list_by_priority(processes_list)
    for process in sorted_processes_list:
        process_information = {'name': process['name'],
                               'coordinates': [(start_point, process['burst_time'])]
                               }
        list_processes_scheduled.append(process_information)

    visualizations.plot_gantt_chart(processes_list, list_processes_scheduled)


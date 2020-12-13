from disk_scheduling import disk
from threads import laws
from cpu_scheduling import cpu_scheduler, visualizations

# processes = [
#     {'name': 'P1', 'burst_time': 20, 'arrival_time': 0},
#     {'name': 'P2', 'burst_time': 25, 'arrival_time': 15},
#     {'name': 'P3', 'burst_time': 10, 'arrival_time': 30},
#     {'name': 'P4', 'burst_time': 15, 'arrival_time': 45},
# ]
# quantum = 10
# process_scheduler = cpu_scheduler.CpuScheduler(processes, quantum)
# process_scheduler.compute()


# processes = [
#     {'name': 'P0', 'burst_time': 20, 'arrival_time': 0, 'priority': 3},
#     {'name': 'P1', 'burst_time': 15, 'arrival_time': 0, 'priority': 1},
#     {'name': 'P2', 'burst_time': 21, 'arrival_time': 0, 'priority': 3},
#     {'name': 'P3', 'burst_time': 7, 'arrival_time': 0, 'priority': 5},
#     {'name': 'P4', 'burst_time': 12, 'arrival_time': 0, 'priority': 2},
# ]
# quantum = 3
# process_scheduler = cpu_scheduler.CpuScheduler(processes, quantum)
# process_scheduler.compute()


processes = [
    {'name': 'P1', 'burst_time': 8, 'arrival_time': 0},
    {'name': 'P2', 'burst_time': 4, 'arrival_time': 1},
    {'name': 'P3', 'burst_time': 9, 'arrival_time': 2},
    {'name': 'P4', 'burst_time': 5, 'arrival_time': 3},
]
quantum = 3
process_scheduler = cpu_scheduler.CpuScheduler(processes, quantum)
process_scheduler.compute()


# laws.amdahls_law(0.25, 2)
#
first_problem = disk.Disk(requests_queue=[1, 3, 7, 4, 10, 12, 8],
                          head_cylinder=5, lower_cylinder=0, upper_cylinder=14,
                          is_moving_towards_0=True)
first_problem.compute()
#
#
# second_problem = disk.Disk(requests_queue = [98, 183, 32, 122, 14, 124, 65, 67],
#                            head_cylinder = 53, lower_cylinder = 0, upper_cylinder = 199,
#                            is_moving_towards_0 = False)
# second_problem.compute()
#
#
# third_problem = disk.Disk(requests_queue = [82, 170, 43, 140, 24, 16, 190],
#                            head_cylinder = 50, lower_cylinder = 0, upper_cylinder = 199,
#                            is_moving_towards_0 = False)
# third_problem.compute()


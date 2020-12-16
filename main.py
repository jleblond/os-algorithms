from disk_scheduling import disk
from threads import laws
from cpu_scheduling import cpu_scheduler, visualizations

# processes = [
#     {'name': 'P1', 'burst_time': 23, 'arrival_time': 0},
#     {'name': 'P2', 'burst_time': 12, 'arrival_time': 3},
#     {'name': 'P3', 'burst_time': 15, 'arrival_time': 1},
#     {'name': 'P4', 'burst_time': 8, 'arrival_time': 2},
# ]
# quantum = 4
# process_scheduler = cpu_scheduler.CpuScheduler(processes, quantum)
# process_scheduler.compute()


processes = [
    {'name': 'P1', 'burst_time': 2, 'arrival_time': 0, 'priority': 2},
    {'name': 'P2', 'burst_time': 1, 'arrival_time': 0, 'priority': 3},
    {'name': 'P3', 'burst_time': 8, 'arrival_time': 0, 'priority': 1},
    {'name': 'P4', 'burst_time': 5, 'arrival_time': 0, 'priority': 2},
]
quantum = 1
process_scheduler = cpu_scheduler.CpuScheduler(processes, quantum)
process_scheduler.compute()


# laws.amdahls_law(0.25, 2)
#
# first_problem = disk.Disk(requests_queue=[11, 3, 17, 4, 10, 12, 8, 9, 22, 13],
#                           head_cylinder=8, lower_cylinder=0, upper_cylinder=23,
#                           is_moving_towards_0=False)
# first_problem.compute()

# first_problem = disk.Disk(requests_queue=[11, 3, 17, 4, 10, 12, 8, 9, 22, 13],
#                           head_cylinder=8, lower_cylinder=0, upper_cylinder=23,
#                           is_moving_towards_0=False)
# first_problem.compute()

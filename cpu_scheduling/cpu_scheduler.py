from . import algorithms

class CpuScheduler:
    def __init__(self, processes_list):
        self.original_processes_list = processes_list
        self.processes_list = processes_list.copy()

    # def add_process(self, process_name, burst_time, priority):
    #     process = {'name': process_name, 'burst_time': burst_time, 'priority': priority}
    #     self.processes_list.append(process)

    def find_process_for(self, key, value):
        return next(process for process in self.processes_list if process[key] == value)

    def compute(self):
        algorithms.fcfs(self.processes_list)


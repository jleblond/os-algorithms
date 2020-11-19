from . import algorithms

class CpuScheduler:
    def __init__(self, processes_list, quantum=None):
        self.original_processes_list = processes_list
        self.processes_list = processes_list.copy()
        self.quantum = quantum

    # def add_process(self, process_name, burst_time, priority):
    #     process = {'name': process_name, 'burst_time': burst_time, 'priority': priority}
    #     self.processes_list.append(process)

    def compute(self):
        # algorithms.fcfs(self.processes_list)
        # algorithms.sjf(self.processes_list)
        # algorithms.priority(self.processes_list)
        if self.quantum != None:
            algorithms.round_robin(self.processes_list, self.quantum)



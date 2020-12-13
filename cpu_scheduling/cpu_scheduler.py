from . import algorithms

class CpuScheduler:
    def __init__(self, processes_list, quantum=None):
        self.original_processes_list = processes_list
        self.processes_list = processes_list.copy()
        self.quantum = quantum
        self.errors_message_str = ''

    @staticmethod
    def element_missing_error_message(el, algorithm_name):
        msg = '!!!!!!!!!!!!!!!!!!!!!\n'
        msg += '** ' + str(el) + ' is missing \n'
        msg += '** ' + algorithm_name + ' algorithm NOT COMPUTED\n'
        msg += '!!!!!!!!!!!!!!!!!!!!!\n'
        return msg

    def compute(self):
        if list(filter(lambda p: 'burst_time' in p, self.processes_list)) == []:
            print('*** BURST TIME IS MISSING ***')
            return

        if list(filter(lambda p: 'arrival_time' in p, self.processes_list) )!= []:
            algorithms.fcfs(self.processes_list)
            algorithms.shortest_remaining_time_first(self.processes_list)
        else:
            self.errors_message_str += CpuScheduler.element_missing_error_message('arrival_time', 'FCFS & SRTF')


        algorithms.sjf(self.processes_list)

        if list(filter(lambda p: 'priority' in p, self.processes_list)) != []:
            algorithms.priority(self.processes_list)
        else:
            self.errors_message_str += CpuScheduler.element_missing_error_message('priority', 'PRIORITY')


        if self.quantum != None:
            algorithms.round_robin(self.processes_list, self.quantum)
        else:
            self.errors_message_str += CpuScheduler.element_missing_error_message('[scheduler quantum is None]', 'ROUND-ROBIN')

        print()
        print(self.errors_message_str)
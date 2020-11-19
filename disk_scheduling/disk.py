from . import algorithms

class Disk:
    def __init__(self, requests_queue, head_cylinder, lower_cylinder, upper_cylinder, is_moving_towards_0):
        self.requests_queue = requests_queue

        self.head_cylinder = head_cylinder
        self.lower_cylinder = lower_cylinder
        self.upper_cylinder = upper_cylinder

        self.is_moving_towards_0 = is_moving_towards_0

    def request_queue_copy(self):
        return self.requests_queue.copy()

    def compute(self):
        algorithms.fcfs(self.request_queue_copy(), self.head_cylinder)

        algorithms.sstf(self.request_queue_copy(), self.head_cylinder)

        algorithms.scan(self.request_queue_copy(),
                        self.head_cylinder,
                        self.lower_cylinder, self.upper_cylinder,
                        self.is_moving_towards_0)

        algorithms.c_look(self.request_queue_copy(), self.head_cylinder, self.is_moving_towards_0)




def print_cylinders_diff(first_cylinder, second_cylinder, diff):
    print("Cylinders: " + str(first_cylinder) + " to " + str(second_cylinder) + " -> |diff| = " + str(diff))

def print_disk_scheduling_algorithm_info(algo_name, requests_queue, head_cylinder, is_moving_towards_0):
    print()
    print("*** Computing " + str(algo_name) +"*** ")
    print("_ requests queue: " + str(requests_queue))
    print('_ head points to cylinder: ' + str(head_cylinder) )
    if is_moving_towards_0 != None:
        print('_ is_moving_towards_0: ' + str(is_moving_towards_0))

def print_disk_scheduling_algorithm_sum(sum):
    print('Total head movements: ' + str(sum))
    print()
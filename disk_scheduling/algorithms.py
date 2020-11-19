import math
from custom_helpers import computation_helper, print_helper


def fcfs(list, start_at):
    """
    FCFS (First Come First Served)
    :param start_at: The head points to that cylinder
    :param list:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("FCFS", list, start_at, None)

    sum = 0
    for i, v in enumerate(list):
        prev = start_at if i == 0 else list[i-1]
        diff = int(math.fabs(list[i] - prev))
        # print("Step " + str(i) + " -  request: " + str(v) + " diff: " + str(diff))
        sum += diff

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


def sstf(list):
    """
    SSTF (Shortest Seek Time First)
    Shortest Seek Time First selects the request with the minimum seek time from the current head position
    SSTF scheduling is a form of SJF scheduling; may cause starvation of some requests
    :param list:
    :return: Total head movements
    """
    return


def scan(list, start_at, lower_cylinder, upper_cylinder, is_moving_towards_0):
    """
    SCAN
    The disk arm starts at one end of the disk, and moves toward the other end, servicing requests until
    it gets to the other end of the disk, where the head movement is reversed and servicing continues.
    Sometimes called the elevator algorithm.
    :param start_at: The head points to that cylinder
    :param list:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("SCAN", list, start_at, is_moving_towards_0)

    lower_value = lower_cylinder
    upper_value = upper_cylinder

    sum = 0
    list.append(start_at)
    list.sort()
    starting_index = list.index(start_at)
    current_index = starting_index

    if is_moving_towards_0:
        while current_index >= 0:
            next_cylinder = lower_value if current_index == 0 else list[current_index - 1]
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], next_cylinder)
            current_index -= 1

        current_index = starting_index + 1
        sum += computation_helper.abs_diff_between_cylinders(list[current_index], 0)
        current_index += 1

        while current_index < len(list):
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], list[current_index - 1])
            current_index += 1
    else:
        while current_index < len(list):
            next_cylinder = upper_value if current_index == (len(list)-1) else list[current_index+1]
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], next_cylinder)
            current_index += 1

        current_index = starting_index - 1
        sum += computation_helper.abs_diff_between_cylinders(upper_value, list[current_index])

        while current_index > 0:
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], list[current_index - 1])
            current_index -= 1

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum

def c_scan(list):
    """
    C-SCAN
    The head moves from one end of the disk to the other, servicing requests as it goes. When it reaches the other end,
    however, it immediately returns to the beginning of the disk, without servicing any requests on the return trip.
    :param list:
    :return: Total head movements
    """
    return


def look(list, start_at, is_moving_towards_0):
    """
    LOOK
    Similar to SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param list:
    :return: Total head movements
    """


def c_look(list, start_at, is_moving_towards_0):
    """
    C-LOOK
    Similar to C-SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param list:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("C-LOOK", list, start_at, is_moving_towards_0)

    list.sort()
    lower_value = list[0]
    upper_value = list[len(list) - 1]

    sum = 0
    list.append(start_at)
    list.sort()
    starting_index = list.index(start_at)
    current_index = starting_index

    if is_moving_towards_0:
        while current_index > 0:
            next_cylinder = lower_value if current_index == 0 else list[current_index - 1]
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], next_cylinder)
            current_index -= 1

        # current index will be 0 here
        list_last_index = len(list) - 1
        sum += computation_helper.abs_diff_between_cylinders(list[current_index], list[list_last_index])
        current_index = list_last_index

        while current_index > starting_index + 2:
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], list[current_index - 1])
            current_index -= 1
    else:
        while current_index < len(list)-1:
            next_cylinder = upper_value if current_index == (len(list) - 1) else list[current_index + 1]
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], next_cylinder)
            current_index += 1

        current_index = 0
        sum += computation_helper.abs_diff_between_cylinders(upper_value, list[current_index])

        while current_index < starting_index -1 :
            sum += computation_helper.abs_diff_between_cylinders(list[current_index], list[current_index + 1])
            current_index += 1

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


import math
from custom_helpers import computation_helper, print_helper


def fcfs(requests_queue, start_at):
    """
    FCFS (First Come First Served)
    :param start_at: The head points to that cylinder
    :param requests_queue:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("FCFS", requests_queue, start_at, None)

    sum = 0
    for i, v in enumerate(requests_queue):
        prev = start_at if i == 0 else requests_queue[i-1]
        diff = int(math.fabs(requests_queue[i] - prev))
        # print("Step " + str(i) + " -  request: " + str(v) + " diff: " + str(diff))
        sum += diff

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


def sstf(requests_queue, start_at):
    """
    SSTF (Shortest Seek Time First)
    Shortest Seek Time First selects the request with the minimum seek time from the current head position
    SSTF scheduling is a form of SJF scheduling; may cause starvation of some requests
    :param requests_queue:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("SSTF", requests_queue, start_at, None)
    k = start_at
    sum = 0
    while(requests_queue):
        closest_value = computation_helper.closest_value_from_list_to_k(requests_queue, k)
        sum += computation_helper.abs_diff_between_cylinders(k, closest_value)
        k = closest_value
        requests_queue.remove(closest_value)

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


def scan(requests_queue, start_at, lower_cylinder, upper_cylinder, is_moving_towards_0):
    """
    SCAN
    The disk arm starts at one end of the disk, and moves toward the other end, servicing requests until
    it gets to the other end of the disk, where the head movement is reversed and servicing continues.
    Sometimes called the elevator algorithm.
    :param start_at: The head points to that cylinder
    :param requests_queue:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("SCAN", requests_queue, start_at, is_moving_towards_0)

    lower_value = lower_cylinder
    upper_value = upper_cylinder

    sum = 0
    requests_queue.append(start_at)
    requests_queue.sort()
    starting_index = requests_queue.index(start_at)
    current_index = starting_index

    if is_moving_towards_0:
        while current_index >= 0:
            next_cylinder = lower_value if current_index == 0 else requests_queue[current_index - 1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index -= 1

        current_index = starting_index + 1
        sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], lower_value)
        current_index += 1

        while current_index < len(requests_queue):
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], requests_queue[current_index - 1])
            current_index += 1
    else:
        while current_index < len(requests_queue):
            next_cylinder = upper_value if current_index == (len(requests_queue)-1) else requests_queue[current_index+1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index += 1

        current_index = starting_index - 1
        sum += computation_helper.abs_diff_between_cylinders(upper_value, requests_queue[current_index])

        while current_index > 0:
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], requests_queue[current_index - 1])
            current_index -= 1

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum

def c_scan(requests_queue, start_at, lower_cylinder, upper_cylinder, is_moving_towards_0):
    """
    C-SCAN
    The head moves from one end of the disk to the other, servicing requests as it goes. When it reaches the other end,
    however, it immediately returns to the beginning of the disk, without servicing any requests on the return trip.
    :param requests_queue:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("C-SCAN", requests_queue, start_at, is_moving_towards_0)

    requests_queue.sort()
    lower_value = lower_cylinder
    upper_value = upper_cylinder

    sum = 0
    requests_queue.append(start_at)
    requests_queue.sort()
    starting_index = requests_queue.index(start_at)
    current_index = starting_index

    if is_moving_towards_0:
        while current_index > 0:
            next_cylinder = lower_value if current_index == 0 else requests_queue[current_index - 1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index -= 1

        # current index will be 0 here
        sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index],
                                                             lower_value)

        list_last_index = len(requests_queue) - 1
        sum += computation_helper.abs_diff_between_cylinders(lower_value,
                                                             requests_queue[list_last_index])
        current_index = list_last_index

        while current_index > starting_index + 1:
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index],
                                                                 requests_queue[current_index - 1])
            current_index -= 1
    else:
        while current_index < len(requests_queue) - 1:
            next_cylinder = upper_value if current_index == (len(requests_queue) - 1) else requests_queue[
                current_index + 1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index += 1

        # current index will be last one
        sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index],
                                                             upper_value)

        sum += computation_helper.abs_diff_between_cylinders(lower_value, upper_value)

        current_index = 0
        sum += computation_helper.abs_diff_between_cylinders(lower_value, requests_queue[current_index])

        while current_index < starting_index - 1:
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index],
                                                                 requests_queue[current_index + 1])
            current_index += 1

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


def look(v, start_at, is_moving_towards_0):
    """
    LOOK
    Similar to SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param requests_queue:
    :return: Total head movements
    """


def c_look(requests_queue, start_at, is_moving_towards_0):
    """
    C-LOOK
    Similar to C-SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param requests_queue:
    :return: Total head movements
    """
    print_helper.print_disk_scheduling_algorithm_info("C-LOOK", requests_queue, start_at, is_moving_towards_0)

    requests_queue.sort()
    lower_value = requests_queue[0]
    upper_value = requests_queue[len(requests_queue) - 1]

    sum = 0
    requests_queue.append(start_at)
    requests_queue.sort()
    starting_index = requests_queue.index(start_at)
    current_index = starting_index

    if is_moving_towards_0:
        while current_index > 0:
            next_cylinder = lower_value if current_index == 0 else requests_queue[current_index - 1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index -= 1

        # current index will be 0 here
        list_last_index = len(requests_queue) - 1
        sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], requests_queue[list_last_index])
        current_index = list_last_index

        while current_index > starting_index + 2:
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], requests_queue[current_index - 1])
            current_index -= 1
    else:
        while current_index < len(requests_queue)-1:
            next_cylinder = upper_value if current_index == (len(requests_queue) - 1) else requests_queue[current_index + 1]
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], next_cylinder)
            current_index += 1

        current_index = 0
        sum += computation_helper.abs_diff_between_cylinders(upper_value, requests_queue[current_index])

        while current_index < starting_index -1 :
            sum += computation_helper.abs_diff_between_cylinders(requests_queue[current_index], requests_queue[current_index + 1])
            current_index += 1

    print_helper.print_disk_scheduling_algorithm_sum(sum)
    return sum


import math


def fcfs(start_at, list):
    """
    FCFS (First Come First Served)
    :param list:
    :return:
    """
    print("Computing FCFS for " + str(list) + ' when the head points to cylinder ' + str(start_at))
    sum = 0
    for i, v in enumerate(list):
        if i == 0:
            prev = start_at
        else:
            prev = list[i-1]
        diff = int(math.fabs(list[i]-prev))
        sum += diff
        print("Step " + str(i) + " -  request: " + str(v) + " diff: " + str(diff))
    print('Total head movements: ' + str(sum))
    return sum

def sstf(list):
    """
    SSTF (Shortest Seek Time First)
    Shortest Seek Time First selects the request with the minimum seek time from the current head position
    SSTF scheduling is a form of SJF scheduling; may cause starvation of some requests
    :param list:
    :return:
    """
    return

def scan(start_at, list, is_moving_towards_0):
    """
    SCAN
    The disk arm starts at one end of the disk, and moves toward the other end, servicing requests until
    it gets to the other end of the disk, where the head movement is reversed and servicing continues.
    Sometimes called the elevator algorithm.
    :param list:
    :return:
    """
    print("Computing SCAN for " + str(list) + ' when the head points to cylinder '
          + str(start_at) + ' and is_moving_towards_0 is ' + str(is_moving_towards_0))

    sum = 0
    list.append(start_at)
    list.sort()
    starting_index = list.index(start_at)
    current_index = starting_index

    print('Sorted list: ' + str(list))
    if is_moving_towards_0:
        while current_index >= 0:
            next_cylinder = 0 if current_index == 0 else list[current_index -1 ]
            diff = int(math.fabs(list[current_index] - next_cylinder))
            print("Index " + str(current_index) + " -  cylinder: " + str(next_cylinder) + " diff: " + str(diff))
            sum += diff
            current_index -= 1

        current_index = starting_index + 1
        diff = int(math.fabs(list[current_index] - 0))
        print("Index " + str(current_index) + " -  cylinder: " + str(list[current_index]) + " diff: " + str(diff))
        sum += diff
        current_index += 1

        while current_index < len(list):
            diff = int(math.fabs(list[current_index] - list[current_index-1]))
            print("Index " + str(current_index) + " -  cylinder: " + str(list[current_index]) + " diff: " + str(diff))
            sum += diff
            current_index += 1
    else:
        print('**INCOMPLETE** TODO: moving towards opposite of 0')

    print('Total head movements: ' + str(sum))
    return sum


def c_scan(list):
    """
    C-SCAN
    The head moves from one end of the disk to the other, servicing requests as it goes. When it reaches the other end,
    however, it immediately returns to the beginning of the disk, without servicing any requests on the return trip.
    :param list:
    :return:
    """
    return


def look(list):
    """
    LOOK
    Similar to SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param list:
    :return:
    """
    return


def c_look(list):
    """
    C-LOOK
    Similar to C-SCAN
    Arm only goes as far as the last request in each direction, then reverses direction immediately,
    without first going all the way to the end of the disk.
    :param list:
    :return:
    """
    return
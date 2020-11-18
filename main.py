from disk_scheduling import algorithms

start_at = 5
arr = [1, 3, 7, 4, 10, 12, 8]
is_moving_towards_0 = True  # moving towards 0

algorithms.fcfs(start_at, arr)
algorithms.scan(start_at, arr, is_moving_towards_0)


start_at_2 = 53
arr_2 = [98, 183, 32, 122, 14, 124, 65, 67]
is_moving_towards_0 = False  # moving towards end

algorithms.fcfs(start_at_2, arr_2)
algorithms.scan(start_at_2, arr_2, is_moving_towards_0)

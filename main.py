from disk_scheduling import disk
from threads import laws


# laws.amdahls_law(0.25, 2)

first_problem = disk.Disk(requests_queue=[1, 3, 7, 4, 10, 12, 8],
                          head_cylinder=5, lower_cylinder=0, upper_cylinder=14,
                          is_moving_towards_0=True)
first_problem.compute()


# second_problem = disk.Disk(requests_queue = [98, 183, 32, 122, 14, 124, 65, 67],
#                            head_cylinder = 53, lower_cylinder = 0, upper_cylinder = 199,
#                            is_moving_towards_0 = False)
# second_problem.compute()


# third_problem = disk.Disk(requests_queue = [82, 170, 43, 140, 24, 16, 190],
#                            head_cylinder = 50, lower_cylinder = 0, upper_cylinder = 199,
#                            is_moving_towards_0 = False)
# third_problem.compute()


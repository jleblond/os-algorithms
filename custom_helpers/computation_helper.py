import math
from custom_helpers import print_helper

def abs_diff_between_cylinders(first_cylinder, second_cylinder):
    diff = int(math.fabs(second_cylinder - first_cylinder))
    print_helper.print_cylinders_diff(first_cylinder, second_cylinder, diff)
    return diff
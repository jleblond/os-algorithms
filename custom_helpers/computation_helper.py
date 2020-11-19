import math
from custom_helpers import print_helper

def abs_diff_between_cylinders(first_cylinder, second_cylinder):
    diff = int(math.fabs(second_cylinder - first_cylinder))
    print_helper.print_cylinders_diff(first_cylinder, second_cylinder, diff)
    return diff

def closest_value_from_list_to_k(queue, k):
    list_of_diffs_with_k = list(map(lambda v: int(math.fabs(k-v)), queue))
    min_diff_with_k = min(list_of_diffs_with_k)
    index_with_min_diff = list_of_diffs_with_k.index(min_diff_with_k)
    closest_value = queue[index_with_min_diff]
    return closest_value
#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Union, Tuple


#
# Complete the 'applicationPairs' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER deviceCapacity
#  2. 2D_INTEGER_ARRAY foregroundAppList
#  3. 2D_INTEGER_ARRAY backgroundAppList
#

def applicationPairs(device_capacity: int, foreground_app_list: List[List[int]], background_app_list: [List[List[int]]]) -> Union[List[List[int]], List[Tuple]]:
    """
    Find optimal pairs of foreground and background processes, having ram summation as much as the device capacity.

    :param device_capacity: int
    :param foreground_app_list: List of [id - memory] pairs
    :param background_app_list: List of [id - memory] pairs
    :return: List of [foreground_id, background_id] pairs
    """
    foreground_app_list = sort_apps(foreground_app_list)
    background_app_list = sort_apps(background_app_list)
    optimal_solution_list = []
    max_memory_usage = -1
    for foreground_app in foreground_app_list:
        foreground_app_id, foreground_app_memory = foreground_app
        for background_app in background_app_list:
            background_app_id, background_app_memory = background_app
            memory_usage = foreground_app_memory + background_app_memory
            if memory_usage <= device_capacity:
                if memory_usage > max_memory_usage:
                    optimal_solution_list = [[foreground_app_id, background_app_id]]
                    max_memory_usage = memory_usage
                elif memory_usage == max_memory_usage:
                    optimal_solution_list.append([foreground_app_id, background_app_id])

    if optimal_solution_list:
        return optimal_solution_list
    else:
        return [()]


def sort_apps(app_list: List[List[int]]) -> List[List[int]]:
    return list(sorted(app_list, reverse=True, key=lambda app: app[1]))


if __name__ == '__main__':
    ram = 28
    foreground_apps = [[1, 8], [2, 7], [3, 14]]
    background_apps = [[1, 5], [2, 10], [3, 14]]
    print(sort_apps(foreground_apps))

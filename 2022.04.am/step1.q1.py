#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


#
# Complete the 'sortBoxes' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY boxList as parameter.
#

def sortBoxes(boxList: List[str]) -> List[str]:
    """
    Sort boxes according to their id and version.

    Older generation boxes come first(boxes not having their version in numeric)
    box_naming_convention: id - version

    :param boxList: box list
    :return: Sorted box list
    """
    old_boxes, new_boxes = divide_boxes(boxList)
    old_boxes = sort_according_to_id(old_boxes)
    old_boxes = sort_according_to_version_code(old_boxes)

    return old_boxes + new_boxes


def divide_boxes(boxList: List[str]) -> (List[str], List[str]):
    """
    Divide boxes into old and new generation lsits

    :param boxList: box list
    :return: (Old generation box list, new generation box list)
    """
    old_boxes = []
    new_boxes = []
    for box in boxList:
        version_code = get_version_code(box)
        is_old_generation = bool(re.match('[0-9 ]+', version_code))
        if is_old_generation:
            new_boxes.append(box)
        else:
            old_boxes.append(box)

    return old_boxes, new_boxes


def sort_according_to_id(boxes: List[str]) -> List[str]:
    return list(sorted(boxes, key=lambda box: box.split()[0]))


def sort_according_to_version_code(boxes: List[str]) -> List[str]:
    return list(sorted(boxes, key=lambda box: get_version_code(box)))


def get_id(box: str) -> str:
    return box.split()[0]


def get_version_code(box: str) -> str:
    first_space_index = box.find(" ")
    version_code = box[first_space_index + 1:]
    return version_code


if __name__ == '__main__':
    print(divide_boxes(["mi2 jog mid pet", "wz3 34 54 398", "a1 alps cow bar", "x4 45 21 7"]))

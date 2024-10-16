#!/usr/bin/env python3
"""
A module that sum a lsi of float numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that take a list of float as a parameter and
    return their sum.

    Args:
        input_list(list): A list of float as a parameter.
    """
    return sum(input_list)

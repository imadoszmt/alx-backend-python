#!/usr/bin/env python3
"""
A module that sum a list of mixed numbers of floats and integers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that takes a list of mixed integers and floats
    and return their sum as a float.

    Args:
        mxd_lst(int and float): A List of integers and floats.
    """
    return sum(mxd_lst)

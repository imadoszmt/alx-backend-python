#!/usr/bin/env python3
"""
A module that take a string and int/float and return a tuple
"""


from typing import List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes string and numbers and return a tuple.

    Args:
        k (str): A string as first element of the tuple.
        v (Union[int, float]): A number as second element of the tuple.
    """
    return (k, float(v**2))

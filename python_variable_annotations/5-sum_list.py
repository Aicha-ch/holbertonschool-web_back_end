#!/usr/bin/env python3
""" Complex types list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ type-annotated function sum_list """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
#!/usr/bin/env python3
"""Define Coroutine async_comprehension"""

from typing import List
import asyncio


async_gen = __import__ ('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
""" return 10 random numbers"""
 return [n async for n in async_generator()]

#!/usr/bin/env python3
"""
async generator
"""


import random
import asyncio


async def async_generator():
    """ coroutine looping 10 times, wait 1 second
    and then yield a random number between 0 and 10"""
    for loop in range(10):
        n = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield n

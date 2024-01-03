#!/usr/bin/env python3
"""
async generator
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ coroutine looping 10 times, wait 1 second
    and then yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

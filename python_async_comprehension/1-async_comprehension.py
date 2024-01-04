#!/usr/bin/env python3
"""Define Coroutine async_comprehension"""

import asyncio
async_gen = __import__ ('0-async_generator').async_generator


async def async_comprehension():
    """return 10 random numbers"""
    _list = []
    async for x in async_generator():
        _list.append(x)
    return _list




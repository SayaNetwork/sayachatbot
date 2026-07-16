"""
sitecustomize.py - Python 3.14 asyncio compatibility hook

This file is automatically loaded by Python before user modules.
It patches pyrogram.sync to handle Python 3.14's stricter asyncio.get_event_loop() behavior.
"""
import sys
import asyncio

# Store original function
_original_get_event_loop = asyncio.get_event_loop

def patched_get_event_loop():
    """
    Patched get_event_loop() that creates a new event loop if none exists.
    This maintains Python 3.10-3.13 behavior on Python 3.14+.
    """
    try:
        return _original_get_event_loop()
    except RuntimeError:
        # No event loop in current thread, create one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

# Apply patch
asyncio.get_event_loop = patched_get_event_loop

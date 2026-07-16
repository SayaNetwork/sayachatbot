#!/usr/bin/env python3
"""
Entrypoint wrapper to satisfy platforms that expect /app/bot.py
This simply runs the package module entrypoint ANNIECHATBOT (same as `python3 -m ANNIECHATBOT`).
"""
import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from ANNIECHATBOT.__main__ import jarvis_boot
from ANNIECHATBOT import LOGGER


if __name__ == "__main__":
    try:
        asyncio.run(jarvis_boot())
        LOGGER.info("Stopping app Bot...")
    except Exception as e:
        LOGGER.error(e)
        raise SystemExit(1)

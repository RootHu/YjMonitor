import sys
import asyncio


if sys.platform == 'win32':
    asyncio.set_event_loop(asyncio.ProactorEventLoop())


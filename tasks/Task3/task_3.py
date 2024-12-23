# Task 3
#   * Integrate AbortController or other Cancallable approach


import asyncio

class AbortController:
    def __init__(self):
        self._cancel_event = asyncio.Event()
        self._cancelled = False

    async def abort(self):
        if not self._cancelled:
            self._cancelled = True
            self._cancel_event.set()

    async def wait_for_abort(self):
        await self._cancel_event.wait()

    def is_aborted(self):
        return self._cancelled




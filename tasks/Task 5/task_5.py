# Task 5 (Observable/EventEmitter/Alternative) -- Reactive message based communication between entities
import asyncio
from collections import defaultdict

class AsyncEventEmitter:
    def __init__(self):
        self.events = defaultdict(list)

    async def subscribe(self, event_name, callback):
        if callback not in self.events[event_name]:
            self.events[event_name].append(callback)

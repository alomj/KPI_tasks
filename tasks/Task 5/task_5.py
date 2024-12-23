# Task 5 (Observable/EventEmitter/Alternative) -- Reactive message based communication between entities
import asyncio
from collections import defaultdict


class AsyncEventEmitter:
    def __init__(self):
        self.events = defaultdict(list)

    async def subscribe(self, event_name, callback):
        if callback not in self.events[event_name]:
            self.events[event_name].append(callback)

    async def unsubscribe(self, event_name, callback):
        if callback in self.events[event_name]:
            self.events[event_name].remove(callback)
            if not self.events[event_name]:
                del self.events[event_name]

    async def emit(self, event_name, *args, **kwargs):
        if event_name in self.events:
            await asyncio.gather(
                *(callback(*args, **kwargs) for callback in self.events[event_name])
            )


async def on_data_received(data):
    await asyncio.sleep(1)
    print(f"Data received: {data}")


async def on_error_occurred(error):
    await asyncio.sleep(1)
    print(f"Error occurred: {error}")


async def run_event_emitter():
    emitter = AsyncEventEmitter()

    await emitter.subscribe("data", on_data_received)
    await emitter.subscribe("error", on_error_occurred)

    print("Emitting 'data' event...")
    await emitter.emit("data", "This is some async data!")

    await emitter.emit("error", "Something went async wrong...")
    await emitter.unsubscribe("error", on_error_occurred)

    print("Emitting 'data' again...")
    await emitter.emit("data", "More async data!")

    print("Emitting 'error' again...")
    await emitter.emit("error", "You should not see this whoomp(.")


if __name__ == "__main__":
    asyncio.run(run_event_emitter())

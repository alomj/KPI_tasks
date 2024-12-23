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


async def cancellable_task(controller: AbortController, task_id: int):
    try:
        for i in range(10):
            if controller.is_aborted():
                print(f"Task {task_id} aborted!")
                break
            print(f"Task {task_id} working... step {i}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"Task {task_id} was cancelled via asyncio.")
    finally:
        print(f"Task {task_id} is exiting.")


async def main():
    controller = AbortController()
    task1 = asyncio.create_task(cancellable_task(controller, 1))
    task2 = asyncio.create_task(cancellable_task(controller, 2))

    await asyncio.sleep(3)

    print("Sending abort signal!")
    await controller.abort()

    await asyncio.gather(task1, task2, return_exceptions=True)

asyncio.run(main())

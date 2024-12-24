# Task 3
#   * Integrate AbortController or other Cancallable approach


import asyncio

async def cancellable_task(task_id: int):
    try:
        for i in range(10):
            print(f"Task {task_id} working... step {i}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"Task {task_id} was cancelled via asyncio.")
    finally:
        print(f"Task {task_id} is exiting.")


async def main():
    task1 = asyncio.create_task(cancellable_task(1))
    task2 = asyncio.create_task(cancellable_task(2))

    await asyncio.sleep(3)

    print("Sending abort signal!")
    task1.cancel()
    task2.cancel()

    await asyncio.gather(task1, task2, return_exceptions=True)

asyncio.run(main())

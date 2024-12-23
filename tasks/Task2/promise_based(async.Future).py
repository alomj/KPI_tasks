''' Task 2
  * Prepare promise based alternative
  * Write use cases for the promise based solution
  * Write use cases for the async-await
  * Add new on-demend feature during review
    e.g.: Add support for parallelism'''

import asyncio


async def async_long_running_task(name, future):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    result = f"Result of {name}"
    future.set_result(result)
    print(f"Task {name} completed")


async def promise_based_solution_with_future():
    loop = asyncio.get_event_loop()

    futures = [asyncio.Future() for _ in range(5)]

    tasks = [
        loop.create_task(async_long_running_task(f"Task-{i}", futures[i]))
        for i in range(5)
    ]

    results = await asyncio.gather(*[future for future in futures])
    return results


async def test_promise_based_solution_with_future():
    results = await promise_based_solution_with_future()
    assert len(results) == 5, "Number of results should match the number of tasks"
    assert results == [f"Result of Task-{i}" for i in range(5)], "Results do not match expected values"
    print("Promise-based solution with Future test passed!")


if __name__ == "__main__":
    print("Testing promise-based solution with asyncio.Future...")
    asyncio.run(test_promise_based_solution_with_future())
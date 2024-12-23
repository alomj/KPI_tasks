''' Task 2
  * Prepare promise based alternative
  * Write use cases for the promise based solution
  * Write use cases for the async-await
  * Add new on-demend feature during review
    e.g.: Add support for parallelism'''


import asyncio


async def long_running_task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    result = f"Result of {name}"
    print(f"Task {name} completed")
    return result


async def test_async_await():
    tasks = [long_running_task(f"Task-{i}") for i in range(5)]
    results = await asyncio.gather(*tasks)

    assert len(results) == 5, "Number of results should match the number of tasks"
    assert results == [f"Result of Task-{i}" for i in range(5)], "Results do not match expected values"
    print("All asyncio tests passed!")


if __name__ == "__main__":
    asyncio.run(test_async_await())
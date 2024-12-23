''' Task 2
  * Prepare promise based alternative
  * Write use cases for the promise based solution
  * Write use cases for the async-await
  * Add new on-demend feature during review
    e.g.: Add support for parallelism'''

import asyncio

PARALLEL_LIMIT = 3
semaphore = asyncio.Semaphore(PARALLEL_LIMIT)


async def parallel_long_running_task(name):
    async with semaphore:
        print(f"Task {name} started")
        await asyncio.sleep(2)
        result = f"Result of {name}"
        print(f"Task {name} completed")
        return result


async def test_parallelism():
    tasks = [parallel_long_running_task(f"Task-{i}") for i in range(5)]
    results = await asyncio.gather(*tasks)

    assert len(results) == 5, "Number of results should match the number of tasks"
    assert results == [f"Result of Task-{i}" for i in range(5)], "Results do not match expected values"
    print("All tests passed with parallelism!")


if __name__ == "__main__":
    print("Testing solution with parallelism support...")
    asyncio.run(test_parallelism())

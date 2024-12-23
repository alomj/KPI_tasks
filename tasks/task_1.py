'''  Task 1
  * Choose array fn (map/filter/filterMap/some/find/findIndex)
  * Prepare its callback based async counterpart
  * Prepare demo cases for the usage
  * Add new on-demend feature during review
    e.g.: Add support for debounce (if the task took less then X time to
    complete -- add an additional execution delya)'''

import asyncio


async def async_map(array, callback, debounce_time=None):
    async def wrapped_callback(item):
        results = await callback(item)
        if debounce_time is not None:
            await asyncio.sleep(debounce_time)
        return results

    return await asyncio.gather(*[wrapped_callback(item) for item in array])


async def multiply_by_two(x):
    await asyncio.sleep(1)
    return x * 2


async def main():
    array = [1, 2, 3, 4, 5]
    print("Without debounce:")
    results = await async_map(array, multiply_by_two)
    print("Results:", results)

    print("\nWith debounce:")
    results_with_debounce = await async_map(array, multiply_by_two, debounce_time=0.5)
    print("Results:", results_with_debounce)


asyncio.run(main())

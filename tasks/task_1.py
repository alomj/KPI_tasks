'''  Task 1
  * Choose array fn (map/filter/filterMap/some/find/findIndex)
  * Prepare its callback based async counterpart
  * Prepare demo cases for the usage
  * Add new on-demend feature during review
    e.g.: Add support for debounce (if the task took less then X time to
    complete -- add an additional execution delya)'''

import asyncio

async def async_map(array, callback):
    results = []
    for item in array:
        result = await callback(item)
        results.append(result)
    return results


async def multiply_by_two(x):
    await asyncio.sleep(1)
    return x * 2


async def main():
    array = [1, 2, 3, 4, 5]
    results = await async_map(array, multiply_by_two)
    print("Results:", results)

asyncio.run(main())
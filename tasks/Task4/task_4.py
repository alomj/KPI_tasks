# Task 4 (Stream/AsyncIterator/Alternative) -- Ongoing processing of large data sets that do not fit in memory
import asyncio
import aiofiles

input_file_path = "text.txt"

async def async_text_processor(file_path, chunk_size=10):

    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
        while chunk := await file.read(chunk_size):
            await asyncio.sleep(0.1)
            yield chunk.upper()
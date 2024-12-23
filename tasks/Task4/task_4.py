# Task 4 (Stream/AsyncIterator/Alternative) -- Ongoing processing of large data sets that do not fit in memory
import asyncio
import aiofiles



async def async_text_processor(file_path, chunk_size=25):

    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
        while chunk := await file.read(chunk_size):
            await asyncio.sleep(0.1)
            yield chunk.upper()

async def main():
    input_file_path = "text.txt"

    print(f"Read and processing file: {input_file_path}")
    print("\n Processed text (chunk by chunk):")

    async for processed_chunk in async_text_processor(input_file_path, chunk_size=25):
        print(f"[CHUNK]: {processed_chunk}")

if __name__ == "__main__":
    import aiofiles
    asyncio.run(main())
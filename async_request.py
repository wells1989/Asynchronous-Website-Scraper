import aiohttp
import asyncio
import time

async def fetch_page(session, url):
    page_state = time.time()
    async with asyncio.timeout(10):
        async with session.get(url) as response:
                print(f'page took {time.time() - page_state}')
                return response.status
   


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)

        return await grouped_tasks # yields from grouped_tasks, allowing suspension while waiting, returning when all tasks are finished

        
loop = asyncio.get_event_loop()
urls = ['https://google.com' for i in range(10)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))

print(f'all took {time.time() - start}')
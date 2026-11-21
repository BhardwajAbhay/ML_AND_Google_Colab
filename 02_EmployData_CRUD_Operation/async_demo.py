import asyncio;
from timeit import default_timer as timer;

async def run_task(name, seconds):
    print(f'{name} start at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at: {timer()}')

async def main():
   start = timer()
   await asyncio.gather(
       run_task('Task1', 2),
       run_task('Task2', 1),
       run_task('Task3', 3)
   )
   print(f'\nTotal time taken: {timer() - start:.2f} s')

asyncio.run(main())

# async : means do the task parellel to each other, if first task take the time of complete then second task is start and first task also move in the background
# await : it tell the other task to start, means: first task is taking the time start the second task 
import time;
from timeit import default_timer as timer;

def run_task(name, seconds):
    print(f'{name} start at: {timer()}')
    time.sleep(seconds)
    print(f'{name} completed at: {timer()}')


start = timer()
run_task('Task1', 2)
run_task('Task2', 1)
run_task('Task3', 3)

print(f'\nTotal time taken: {timer() - start:.2f} s')
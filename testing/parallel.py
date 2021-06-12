import os
import time
import threading
import multiprocessing

def crunch_numbers():
    """ Do some computations """
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    x = 0
    while x < 10000000:
        x += 1

if __name__ == '__main__':
    NUM_WORKERS = 6
            
     
    start_time = time.time()
    processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(6)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    
    print("Parallel time=", end_time - start_time)
    

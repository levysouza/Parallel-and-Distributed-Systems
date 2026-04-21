import multiprocessing
from multiprocessing import Process
from multiprocessing import Value

shared_counter = Value('i', 0)
workers = 8
iterations = 10_000
process = []

def worker(n):
    print("Starting Worker #"+str(n))
    for _ in range(iterations):
        shared_counter.value += 1

if __name__ == "__main__":

    multiprocessing.set_start_method(method='fork', force=True)
    
    for w in range(workers):
        p = Process(target=worker, args=(w,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print()
    print("Expected Value = " +str(workers * iterations ))
    print("Shared Counter = " +str(shared_counter.value))
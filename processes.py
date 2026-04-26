from multiprocessing import Process, Queue

data = [10, 20, 30, 40, 50]
processes = []

def square(number, q):
    r = number * number
    q.put(r)

if __name__ == "__main__":
    q = Queue()
    
    for d in data:
        p = Process(target=square, args=(d,q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    print("input data = "+str(data))
    print("output data = "+str([q.get() for _ in data]))
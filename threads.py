import threading

data = [10, 20, 30, 40, 50]
result = []
threads = []

def square(number):
    r = number * number
    result.append(r)

if __name__ == "__main__":
    
    for d in data:
        t = threading.Thread(target=square, args=(d,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print()
    print("input data = "+str(data))
    print("output data = "+str(result))
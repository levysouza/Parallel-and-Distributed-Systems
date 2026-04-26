from multiprocessing import Pool

data = [10, 20, 30, 40, 50]

def square(number):
    return number * number

if __name__ == "__main__":
    
    with Pool(processes=2) as p:
        
        result = p.map(func=square, iterable=data)
    
        print("input data = "+str(data))
        print("output data = "+str(result))